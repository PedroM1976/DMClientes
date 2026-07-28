from pathlib import Path
import json

folder = Path("dados/importados")
allowed = {".xlsx", ".xls", ".csv"}
files = []
for p in sorted(folder.iterdir(), key=lambda x: x.name.lower()):
    if p.is_file() and p.suffix.lower() in allowed and p.name.lower() != "manifest.json":
        files.append({
            "name": p.name,
            "path": str(p).replace("\\", "/"),
            "label": p.stem
        })

(folder / "manifest.json").write_text(
    json.dumps({"files": files}, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"Manifesto atualizado com {len(files)} ficheiro(s).")
