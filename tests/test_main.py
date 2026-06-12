import subprocess

def test_run_main():
    result = subprocess.run(
        ["python", "src/main.py"],
        capture_output=True,
        text=True
    )
    assert "DevOps Playground is alive" in result.stdout
