from pathlib import Path
import hashlib

root = Path(__file__).resolve().parent
sumfile = root / "SHA256SUMS.txt"

ok = True
for line in sumfile.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line:
        continue
    digest, filename = line.split("  ", 1)
    path = root / filename
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    status = "OK" if actual == digest else "MISMATCH"
    print(f"{filename}: {status}")
    ok &= actual == digest

raise SystemExit(0 if ok else 1)
