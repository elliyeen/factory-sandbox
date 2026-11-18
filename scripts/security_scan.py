"""Deterministic synthetic security scan: fails if the fixture marker or a hardcoded secret pattern appears."""
import pathlib, re, sys
MARKERS = [re.compile(r"INSECURE_FIXTURE_DO_NOT_SHIP"), re.compile(r"(?i)api[_-]?key\s*=\s*['\"][A-Za-z0-9]{16,}")]
bad = []
for p in pathlib.Path(".").rglob("*"):
    if p.is_file() and ".git" not in p.parts and p.name != "security_scan.py" and p.suffix in {".py", ".md", ".html", ".yml", ".txt"}:
        t = p.read_text(errors="ignore")
        bad += [f"{p}: {m.pattern}" for m in MARKERS if m.search(t)]
print("\n".join(bad) or "security scan clean")
sys.exit(1 if bad else 0)
