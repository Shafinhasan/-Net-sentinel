import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api.routes import router
from app.core.config import get_settings

settings = get_settings()

logging.basicConfig(
    level=settings.log_level.upper(),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Defensive API for reading and presenting Suricata EVE alerts "
        "inside the NetSentinel laboratory."
    ),
)

app.include_router(router)

_dashboard_file = Path(__file__).parent / "web" / "dashboard.html"


@app.get("/", include_in_schema=False)
def dashboard() -> HTMLResponse:
    return HTMLResponse(_dashboard_file.read_text(encoding="utf-8"))
