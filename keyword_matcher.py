def match_keywords(resume_text, job_desc):
    resume_words = set(resume_text.lower().split())
    jd_words = set(job_desc.lower().split())

    matched = list(resume_words & jd_words)
    missing = list(jd_words - resume_words)
    score = round(len(matched) / len(jd_words) * 100, 2) if jd_words else 0

    return score, matched, missing
