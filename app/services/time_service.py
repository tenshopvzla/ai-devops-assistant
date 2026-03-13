from datetime import datetime


class TimeService:
    """Provides time-related helpers for API responses."""

    @staticmethod
    def get_current_time_iso() -> str:
        return datetime.now().isoformat()
