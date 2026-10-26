from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_links


@pytest.fixture()
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(check_links, "ROOT", tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "Guide.md").write_text("x", encoding="utf-8")
    return tmp_path


def _check(repo: Path, body: str) -> list[str]:
    doc = repo / "README.md"
    doc.write_text(body, encoding="utf-8")
    return check_links.check_document(doc)


def test_existing_link_passes(repo: Path) -> None:
    assert _check(repo, "[g](docs/Guide.md)") == []


def test_missing_link_is_reported(repo: Path) -> None:
    assert len(_check(repo, "[g](docs/Nope.md)")) == 1


def test_link_with_wrong_case_is_reported(repo: Path) -> None:
    # Windows resolves this; GitHub (case-sensitive) renders a 404.
    assert len(_check(repo, "[g](docs/guide.md)")) == 1


def test_link_with_wrong_case_is_reported(repo: Path) -> None:
    # Windows resolves this; GitHub (case-sensitive) renders a 404.
    assert len(_check(repo, "[g](docs/guide.md)")) == 1
