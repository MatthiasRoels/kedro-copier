import ast 


def test_template(copie):
    expected_files = [
        ".gitignore",
        "README.md",
        "pyproject.toml",
        "tox.ini",
    ]
    expected_dirs = [
        "src",
        "src/project_name",
        "src/tests",
    ]

    result = copie.copy(
        extra_answers={
            "project_name": "project-name",
        },
    )

    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_dir.is_dir()

    for path in expected_files:
        assert (result.project_dir / path).is_file()
    for path in expected_dirs:
        assert (result.project_dir / path).is_dir()


def test_local_data_dirs(copie):
    result = copie.copy(
        extra_answers={
            "project_name": "project-name",
            "include_local_data": True,
        },
    )

    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert (result.project_dir / "data").is_dir()

def test_pandera_hooks_included(copie):
    result = copie.copy(
        extra_answers={
            "project_name": "project-name",
            "include_pandera_hooks": True,
        },
    )

    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert (result.project_dir / "src" / "project_name" / "pandera_hooks.py").is_file()


def test_mlflow_hooks_included(copie):
    result = copie.copy(
        extra_answers={
            "project_name": "project-name",
            "include_mlflow_hooks": True,
        },
    )

    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert (result.project_dir / "src" / "project_name" / "mlflow_hooks.py").is_file()

    with open(str(result.project_dir / "src" / "project_name" / "mlflow_hooks.py")) as file:
        ast.parse(file.read())
