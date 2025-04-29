# copier-kedro

[Copier](https://github.com/copier-org/copier) template for Kedro projects.

_As simple as possible. No magic._

## Usage

```
mkdir my-kedro-project && cd my-kedro-project
uvx copier copy --trust gh:MatthiasRoels/kedro-copier.git .
```

✨

(`uvx` is the shorthand for `uv tool run`, see [the uv documentation](https://docs.astral.sh/uv/guides/tools/))

## Features

- [uv] for project management.
- [pytest] for testing.
- [GitHub Actions] for continuous integration and publishing to PyPI.
- [ruff] for style checks and automatic Python code formatting.
- [pre-commit] for optional automation of style checks.

## License

[MIT License](LICENSE)

[uv]: https://github.com/astral-sh/uv
[copier]: https://github.com/copier-org/copier/
[pytest]: https://docs.pytest.org/
[ruff]: https://docs.astral.sh/ruff/
[pre-commit]: https://github.com/pre-commit/pre-commit/
[GitHub Actions]: https://github.com/features/actions/
