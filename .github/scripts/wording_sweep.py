"""Remove the last Android-studio phrasing anywhere on the site."""
import pathlib

PAIRS = [
    ("استوديو أندرويد مستقل يبني ألعاب ألغاز صغيرة وتطبيقات", "استوديو برمجيات مستقل يبني ألعاب ألغاز صغيرة وتطبيقات"),
    ("استوديو أندرويد مستقل", "استوديو برمجيات مستقل"),
    ("استوديو أندرويد", "استوديو برمجيات"),
    ("Independent Android studio", "Independent software studio"),
    ("Android studio", "software studio"),
    ("MD Work works without an account. Nothing is locked behind a sign-in, and your notes stay on your device.",
     "‏MD Work يعمل دون تسجيل حساب: لا شيء محجوب خلف تسجيل الدخول، وملاحظاتك تبقى على جهازك."),
]

changed = 0
for path in sorted(pathlib.Path(".").rglob("*.html")):
    if ".git" in path.parts or ".github" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    before = text
    for old, new in PAIRS:
        if old in text:
            text = text.replace(old, new)
    if text != before:
        path.write_text(text, encoding="utf-8")
        changed += 1
        print("updated", path)
print("files changed:", changed)
