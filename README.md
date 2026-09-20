# Ahmed Open Source Toolkit

A small, dependency-free Python CLI that checks whether a repository has the basic files and automation expected for an open-source project.

## What it checks

- README
- LICENSE
- .gitignore
- tests
- GitHub Actions CI

The tool is intentionally simple so contributors can extend it with more checks.

## Requirements

- Python 3.9+

## Usage

From the repository root:

```bash
python -m oss_toolkit .
```

You can also run the module directly after installing the package:

```bash
oss-check .
```

The command exits with code 0 when all checks pass and code 1 when one or more checks fail.

## Development

```bash
python -m pip install -e .[dev]
pytest
```

## Contributing

Bug reports, feature requests, and pull requests are welcome. See CONTRIBUTING.md for the development workflow.

## License

MIT