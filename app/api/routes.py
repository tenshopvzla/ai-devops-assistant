from fastapi import APIRouter, HTTPException

from app.services.fibonacci_service import FibonacciService
from app.services.status_service import StatusService
from app.services.system_service import SystemService

router = APIRouter()
status_service = StatusService()


@router.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello AI DevOps Assistant"}


@router.get("/fibonacci/{number}")
def fibonacci(number: int) -> dict[str, list[int]]:
    try:
        sequence = FibonacciService.generate_sequence(number)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {"fibonacci_sequence": sequence}


@router.get("/system_info")
def system_info() -> dict[str, str]:
    return SystemService.get_system_info()


@router.get("/status")
def status() -> dict[str, object]:
    return status_service.get_status()
