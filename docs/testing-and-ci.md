# Testing and Continuous Integration

## 1. Unit Testing

The project uses Python's built-in `unittest` framework to test the shared scoring engine.

Run the tests locally:

```bash
python -m unittest discover -v
```

The tests cover:

- Risk classification.
- Low-risk classification.
- Values below, above, and exactly at the threshold.
- Invalid number of features.
- Negative values.
- Non-numerical inputs.
- Boolean inputs.
- NaN and infinite values.

## 2. Code Quality

Ruff is used for automated Python code-quality checks.

Run Ruff locally:

```bash
python -m pip install ruff
python -m ruff check .
```

## 3. Python Syntax Validation

Python compilation is used to check the syntax of the application and test modules:

```bash
python -m compileall -q app.py gui.py streamlit_app.py test_app.py
```

## 4. GitHub Actions Workflow

The CI/CD workflow is defined in:

`.github/workflows/python-ci-cd.yml`

The workflow uses Python 3.12 and runs automated checks on configured branch pushes and pull requests targeting `main` and `dev`.

### Continuous Integration

The test job performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs project dependencies and Ruff.
4. Runs Ruff code-quality checks.
5. Compiles the Python modules.
6. Executes unit tests.

### Application Packaging

On pushes to `main`, the package job creates a ZIP archive containing:

- `app.py`
- `gui.py`
- `streamlit_app.py`
- `requirements.txt`

The archive is uploaded as a GitHub Actions artifact.

### Windows Executable Build

The Windows build job uses PyInstaller to create a standalone executable from `gui.py`.

The executable is uploaded as a GitHub Actions artifact.

### Automated GitHub Releases

When a version tag matching `v*` is pushed, the workflow:

1. Runs the test job.
2. Builds the Windows executable.
3. Downloads the Windows executable artifact.
4. Creates a GitHub Release using the version tag as the release name.
5. Generates release notes automatically and attaches `RiskAssessment.exe` to the release.

The release job runs only after the test and Windows build jobs have completed successfully.

## 5. Workflow Summary

| Job | Purpose |
|---|---|
| `test` | Code quality, syntax validation, and unit tests |
| `package` | ZIP archive of the application |
| `build-windows-exe` | Windows desktop executable |
| `create-release` | Automated GitHub release |

