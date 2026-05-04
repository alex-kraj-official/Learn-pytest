import pytest
import others.asd as asd

test_data = [
    (1, 1, 4),  # Test case 1: Square
    (2, 4, 12),  # Test case 2: Standard rectangle
    (0, 5, 10),  # Test case 3: Edge case with zero
    (2.5, 2.0, 9.0),  # Test case 4: Floating point numbers
]


@pytest.mark.parametrize(
    "width, length, expected",
    test_data,
    ids=[f"width: {w}, length: {l}" for w, l, _ in test_data],
)
def test_perimeter(width, length, expected):
    """Test rectangle perimeter."""
    r = asd.Rectangle(width, length)
    assert r.perimeter() == expected
