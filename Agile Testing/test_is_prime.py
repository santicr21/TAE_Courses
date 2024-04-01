import is_prime
import pytest

@pytest.mark.parametrize("n, expected_result", [
    (1, True),
    (2, True),
    (3, True),
    (4, False),
    (9, False),
    (11, True),
])

def test_number_is_prime(n, expected_result):
    actual_result = is_prime.is_prime(n)
    assert actual_result == expected_result