class FibonacciService:
    """Business logic for generating Fibonacci sequences."""

    @staticmethod
    def generate_sequence(number: int) -> list[int]:
        if number < 0:
            raise ValueError("number must be greater than or equal to 0")

        sequence: list[int] = []
        a, b = 0, 1
        for _ in range(number):
            sequence.append(a)
            a, b = b, a + b
        return sequence
