from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_dependency_freshness as fresh
import check_upstream_updates as upstream


@pytest.mark.parametrize(
    "payload",
    ["[]", '"x"', "null", json.dumps({"repo": "r", "branch": "b", "reviewed_date": "d", "reviewed_through": 123})],
)
def test_load_baseline_rejects_malformed_shapes(tmp_path: Path, payload: str) -> None:
    path = tmp_path / "b.json"
    path.write_text(payload, encoding="utf-8")
    with pytest.raises(upstream.UpstreamCheckError):
        upstream.load_baseline(path)


@pytest.mark.parametrize("payload", ["[]", '{"deferrals": []}', '{"deferrals": "x"}', "null"])
def test_load_deferrals_tolerates_malformed_shapes(tmp_path: Path, payload: str) -> None:
    path = tmp_path / "d.json"
    path.write_text(payload, encoding="utf-8")
    assert fresh.load_deferrals(path) == {}


def test_deferral_matches_normalized_package_name(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(fresh, "fetch_pypi_version", lambda name: "2.0")
    pkg = {"name": "Typing_Extensions", "minimum": "1.0", "requirement": "x>=1.0", "source": "r", "hold": ""}
    rows = fresh.collect_status([pkg], {"typing-extensions": ("2.0", "reviewed")})
    assert rows[0]["deferred_reason"] == "reviewed"
    assert not fresh.needs_review(rows[0])
