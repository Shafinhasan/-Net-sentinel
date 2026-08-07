from typing import Literal

from pydantic import BaseModel, Field


SeverityLabel = Literal["high", "medium", "low", "unknown"]


class AlertRecord(BaseModel):
    timestamp: str
    flow_id: int | None = None
    src_ip: str | None = None
    src_port: int | None = None
    dest_ip: str | None = None
    dest_port: int | None = None
    protocol: str | None = None
    app_proto: str | None = None
    signature_id: int
    signature: str
    category: str | None = None
    severity: int | None = None
    severity_label: SeverityLabel
    action: str | None = None
    http_hostname: str | None = None
    http_url: str | None = None


class AlertListResponse(BaseModel):
    source: str
    source_exists: bool
    count: int = Field(ge=0)
    malformed_lines: int = Field(ge=0)
    items: list[AlertRecord]


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    version: str
    eve_file: str
    eve_file_exists: bool
