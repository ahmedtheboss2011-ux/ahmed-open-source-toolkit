from pathlib import Path

from oss_toolkit.cli import check_repository


def test_repository_checks_pass_for_expected_layout(tmp_path: Path) -> None:
    for path in [
        "README.md",
        "LICENSE",
        ".gitignore",
        "tests",
        ".github/workflows/ci.yml",
    ]:
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("placeholder", encoding="utf-8")

    results = check_repository(tmp_path)
    assert all(ok for _, ok in results)


def test_repository_checks_detect_missing_file(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Demo", encoding="utf-8")

    results = dict(check_repository(tmp_path))
    assert results["README"] is True
    assert results["License"] is False
