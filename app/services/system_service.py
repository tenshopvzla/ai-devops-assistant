import platform

from app.services.time_service import TimeService


class SystemService:
    """Business logic for system/runtime details."""

    @staticmethod
    def get_python_version() -> str:
        return platform.python_version()

    @classmethod
    def get_system_info(cls) -> dict[str, str]:
        return {
            "python_version": cls.get_python_version(),
            "current_time": TimeService.get_current_time_iso(),
        }
