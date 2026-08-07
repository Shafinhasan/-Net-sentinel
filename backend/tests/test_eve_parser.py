from pathlib import Path

from app.services.eve_parser import EveAlertParser, severity_label


FIXTURE = Path(__file__).parent / "fixtures" / "eve.json"


def test_severity_labels() -> None:
    assert severity_label(1) == "high"
    assert severity_label(2) == "medium"
    assert severity_label(3) == "low"
    assert severity_label(None) == "unknown"


def test_parser_returns_only_alert_events() -> None:
    alerts, malformed = EveAlertParser(FIXTURE).read_alerts(limit=50)

    assert len(alerts) == 2
    assert malformed == 1
    assert alerts[0].signature_id == 1000001


def test_parser_filters_by_severity() -> None:
    alerts, malformed = EveAlertParser(FIXTURE).read_alerts(
        limit=50,
        severity="high",
    )

    assert len(alerts) == 1
    assert malformed == 1
    assert alerts[0].severity_label == "high"


def test_missing_file_returns_empty_result(tmp_path: Path) -> None:
    alerts, malformed = EveAlertParser(tmp_path / "missing.json").read_alerts()

    assert alerts == []
    assert malformed == 0
