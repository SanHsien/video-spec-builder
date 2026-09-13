from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_skill_file_structure() -> None:
    skill_path = ROOT / "SKILL.md"
    assert skill_path.is_file()
    content = skill_path.read_text(encoding="utf-8")
    assert len(content) > 1000
    # YAML frontmatter check
    assert content.startswith("---")
    second_dashes = content.find("---", 3)
    assert second_dashes > 3
    frontmatter = content[3:second_dashes]
    assert "name:" in frontmatter or "description:" in frontmatter


def test_required_references_exist_and_not_empty() -> None:
    required = (
        "components-catalog.md",
        "dialogue-style.md",
        "pacing-rules.md",
        "question-bank.md",
        "scene-breakdown.md",
        "spec-rules.md",
        "workflow-0-1.md",
        "workflow-iteration.md",
    )
    for ref in required:
        ref_path = ROOT / "references" / ref
        assert ref_path.is_file(), f"Missing references/{ref}"
        text = ref_path.read_text(encoding="utf-8")
        assert len(text) > 100, f"references/{ref} is too short ({len(text)} bytes)"


def test_spec_template_and_spacex_example() -> None:
    template = (ROOT / "templates" / "video-spec-template.md").read_text(encoding="utf-8")
    assert "video-spec" in template.lower() or "shot" in template.lower()
    assert len(template) > 500

    example = (ROOT / "examples" / "video-spec-spacex.md").read_text(encoding="utf-8")
    assert re.search(r"\d+(\.\d+)?s\s*[–-]\s*\d+(\.\d+)?s", example) or "Scene" in example, "Example must have scenes and timecodes"
    assert len(example) > 1000


def test_spec_mono_theme_integrity() -> None:
    design = (ROOT / "spec-mono" / "design.md").read_text(encoding="utf-8")
    tokens = (ROOT / "spec-mono" / "tokens.css").read_text(encoding="utf-8")
    components = (ROOT / "spec-mono" / "spec-mono-components.md").read_text(encoding="utf-8")

    assert "--color-" in tokens or "--font-" in tokens or "tokens" in tokens.lower()
    assert len(design) > 500
    assert len(components) > 1000


def test_full_code_components_exist() -> None:
    full_code = ROOT / "Full Code"
    assert full_code.is_dir()
    app_jsx = full_code / "app.jsx"
    assert app_jsx.is_file()
    app_content = app_jsx.read_text(encoding="utf-8")
    assert "export default" in app_content or "function" in app_content

    sections = full_code / "sections"
    assert sections.is_dir()
    jsx_files = list(sections.glob("*.jsx"))
    assert len(jsx_files) >= 9, f"Found {len(jsx_files)} section JSX files, expected at least 9"
