import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
from app import greet


def test_greet():
    assert greet("World") == "Hello, World!"


def test_farewell():
    from app import farewell
    assert farewell("World") == "Goodbye, World!"
