# tests/test_hello_world.py

def test_example():
    """A simple test to ensure pytest runs correctly."""
    assert 1 + 1 == 2

def test_string():
    """Another basic test for demonstration."""
    assert "hello".upper() == "HELLO"

def test_list_length():
    """Test list length calculation."""
    items = [1, 2, 3]
    assert len(items) == 3
