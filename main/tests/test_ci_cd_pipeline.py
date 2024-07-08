import os
import subprocess
import pytest

def test_ci_cd_workflow():
    try:
        # Replace with the path to your ci-cd.yml file
        workflow_file = 'path/to/ci-cd.yml'

        # Simulate running GitHub Actions workflow
        process = subprocess.run(['github-script-runner', 'run', workflow_file],
                                 capture_output=True, text=True, check=True)

        # Check if the workflow completed successfully
        assert process.returncode == 0, f"GitHub Actions workflow failed with output: {process.stdout}"

    except subprocess.CalledProcessError as exc:
        pytest.fail(f"Error running GitHub Actions workflow: {exc}")

# Optional: Run the test if this script is run directly
if __name__ == "__main__":
    pytest.main()
