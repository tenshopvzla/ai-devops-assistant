import time

from app.services.system_service import SystemService
from app.services.time_service import TimeService


class StatusService:
    """Business logic for health and service status responses."""

    def __init__(self) -> None:
        self._start_time = time.monotonic()

    def get_status(self) -> dict[str, object]:
        uptime_seconds = time.monotonic() - self._start_time
        return {
            "status": "API running correctly",
            "server_time": TimeService.get_current_time_iso(),
            "python_version": SystemService.get_python_version(),
            "uptime_seconds": uptime_seconds,
        }
