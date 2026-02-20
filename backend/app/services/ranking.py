import re
from typing import Set


# -----------------------------------
# Text Normalization
# -----------------------------------
def normalize_text(text: str) -> str:
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


# -----------------------------------
# Convert comma string → set
# -----------------------------------
def parse_skill_string(skill_string: str) -> Set[str]:
    if not skill_string:
        return set()
    return set(s.strip().lower() for s in skill_string.split(",") if s.strip())


# -----------------------------------
# Percentage match score
# -----------------------------------
def section_score(required_set: Set[str], resume_words: Set[str]) -> float:
    if not required_set:
        return 0.0

    matched = required_set.intersection(resume_words)
    return (len(matched) / len(required_set)) * 100


# -----------------------------------
# Hybrid ATS Ranking Logic
# -----------------------------------
def hybrid_rank(job, resume_text: str):

    resume_text = normalize_text(resume_text)
    resume_words = set(resume_text.split())

    must_have = parse_skill_string(job.must_have)
    good_to_have = parse_skill_string(job.good_to_have)

    # -------------------------------
    # 1️⃣ Skill Score (Must-Have)
    # -------------------------------
    skill_score = section_score(must_have, resume_words)

    # -------------------------------
    # 2️⃣ Tools Score (Good-To-Have)
    # -------------------------------
    tools_score = section_score(good_to_have, resume_words)

    # -------------------------------
    # 3️⃣ Project Depth Score
    # Skill mentioned ≥2 times = strong signal
    # -------------------------------
    combined_skills = must_have.union(good_to_have)

    project_hits = 0
    for skill in combined_skills:
        if resume_text.count(skill) >= 2:
            project_hits += 1

    if combined_skills:
        project_score = (project_hits / len(combined_skills)) * 100
    else:
        project_score = 0.0

    # -------------------------------
    # 4️⃣ Weighted Final Score
    # -------------------------------
    final_score = (
        0.4 * skill_score +
        0.4 * project_score +
        0.2 * tools_score
    )

    # -------------------------------
    # 5️⃣ Must-Have Enforcement
    # If any mandatory skill missing → penalize
    # -------------------------------
    missing_must_have = [
        skill for skill in must_have if skill not in resume_words
    ]

    if missing_must_have:
        final_score *= 0.5

    # -------------------------------
    # Return Structured Breakdown
    # -------------------------------
    return {
        "skill_score": round(skill_score, 2),
        "project_score": round(project_score, 2),
        "tools_score": round(tools_score, 2),
        "final_score": round(final_score, 2)
    }
