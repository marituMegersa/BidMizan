import pytest

def test_collusion_variance_check():
    prices = [500000.0, 501000.0, 500500.0]
    avg = sum(prices) / len(prices)
    variance = sum((p - avg) ** 2 for p in prices) / len(prices)
    cv = (variance ** 0.5) / avg
    assert cv < 0.05
