import json
import logging
from pathlib import Path
from typing import Any

from app.models import AlertRecord, SeverityLabel

logger = logging.getLogger(__name__)


def severity_label(value: int | None) -> SeverityLabel:
    """Translate Suricata severity numbers into analyst-friendly labels."""
    return {
        1: "high",
        2: "medium",
        3: "low",
    }.get(value, "unknown")


class EveAlertParser:
    """Read Suricata EVE JSON line-by-line without loading the full file."""

    def __init__(self, eve_file: Path) -> None:
        self.eve_file = eve_file

    def read_alerts(
        self,
        *,
        limit: int = 50,
        severity: SeverityLabel | None = None,
    ) -> tuple[list[AlertRecord], int]:
        if not self.eve_file.is_file():
            return [], 0

        alerts: list[AlertRecord] = []
        malformed_lines = 0

        try:
            with self.eve_file.open("r", encoding="utf-8") as handle:
                for line_number, line in enumerate(handle, start=1):
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        event: dict[str, Any] = json.loads(line)
                    except json.JSONDecodeError:
                        malformed_lines += 1
                        logger.warning(
                            "Skipped malformed EVE JSON line %s",
                            line_number,
                        )
                        continue

                    if event.get("event_type") != "alert":
                        continue

                    alert_data = event.get("alert") or {}
                    numeric_severity = alert_data.get("severity")
                    label = severity_label(numeric_severity)

                    if severity is not None and label != severity:
                        continue

                    http_data = event.get("http") or {}
                    alerts.append(
                        AlertRecord(
                            timestamp=str(event.get("timestamp", "")),
                            flow_id=event.get("flow_id"),
                            src_ip=event.get("src_ip"),
                            src_port=event.get("src_port"),
                            dest_ip=event.get("dest_ip"),
                            dest_port=event.get("dest_port"),
                            protocol=event.get("proto"),
                            app_proto=event.get("app_proto"),
                            signature_id=int(alert_data.get("signature_id", 0)),
                            signature=str(
                                alert_data.get("signature", "Unknown signature")
                            ),
                            category=alert_data.get("category"),
                            severity=numeric_severity,
                            severity_label=label,
                            action=alert_data.get("action"),
                            http_hostname=http_data.get("hostname"),
                            http_url=http_data.get("url"),
                        )
                    )

                    if len(alerts) >= limit:
                        break
        except OSError as exc:
            logger.error("Could not read EVE file %s: %s", self.eve_file, exc)
            return [], malformed_lines

        return alerts, malformed_lines
