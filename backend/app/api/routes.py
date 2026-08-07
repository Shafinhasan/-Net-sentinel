from fastapi import APIRouter, Query

from app.core.config import get_settings
from app.models import AlertListResponse, HealthResponse, SeverityLabel
from app.services.eve_parser import EveAlertParser

router = APIRouter()
settings = get_settings()


@router.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
        eve_file=str(settings.eve_file),
        eve_file_exists=settings.eve_file.is_file(),
    )


@router.get(
    "/api/v1/alerts",
    response_model=AlertListResponse,
    tags=["alerts"],
)
def list_alerts(
    limit: int = Query(default=50, ge=1, le=500),
    severity: SeverityLabel | None = Query(default=None),
) -> AlertListResponse:
    parser = EveAlertParser(settings.eve_file)
    alerts, malformed_lines = parser.read_alerts(
        limit=limit,
        severity=severity,
    )

    return AlertListResponse(
        source=str(settings.eve_file),
        source_exists=settings.eve_file.is_file(),
        count=len(alerts),
        malformed_lines=malformed_lines,
        items=alerts,
    )
