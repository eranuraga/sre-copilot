from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"

def load_skill(skill_name: str) -> str:
    skill_path = SKILLS_DIR / f"{skill_name}.md"

    if not skill_path.exists():
        raise FileNotFoundError(f"Skill file not found: {skill_path}")

    return skill_path.read_text(encoding="utf-8").strip()