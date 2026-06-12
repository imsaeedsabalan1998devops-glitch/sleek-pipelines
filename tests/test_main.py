import subprocess
from src.main import run

def test_placeholder():
    assert True

def test_run_main():
    result = subprocess.run(
        ["python", "src/main.py"],
        capture_output=True,
        text=True
    )
    assert "DevOps Playground is alive" in result.stdout

def test_run_function():
    assert run() == "DevOps Playground is alive 🔥"
