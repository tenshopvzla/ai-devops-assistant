# create pytest tests for fibonacci endpoint
from pathlib import Path
import sys

import pytest
from fastapi.testclient import TestClient

# Ensure imports work even when pytest is invoked outside the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from main import app

client = TestClient(app)


@pytest.mark.parametrize("input, expected", [
    (0, []),                                        
    (1, [0]),
    (2, [0, 1]),    
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test_fibonacci_endpoint(input, expected):
    response = client.get(f"/fibonacci/{input}")
    assert response.status_code == 200
    assert response.json() == {"fibonacci_sequence": expected}                  

@pytest.mark.parametrize("input", [-1, -5, -10])                                
def test_fibonacci_endpoint_invalid_input(input):
    response = client.get(f"/fibonacci/{input}")
    assert response.status_code == 400
    assert "number must be greater than or equal to 0" in response.json()["detail"]             





                                                                                                                                                    