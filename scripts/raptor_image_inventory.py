from pathlib import Path
import csv

RAW_DIR = Path("/Users/adampugh/GitHub/TeraCreators-Help/static/img/raptor/_raw")
OUTPUT_CSV = Path("/Users/adampugh/GitHub/TeraCreators-Help/scripts/raptor-image-map.csv")

rows = []

for file_path in sorted(RAW_DIR.rglob("*")):
    if file_path.is_file():
        rows.append({
            "source_path": str(file_path),
            "source_name": file_path.name,
            "suggested_folder": "",
            "new_name": "",
            "notes": "",
        })

with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["source_path", "source_name", "suggested_folder", "new_name", "notes"]
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote: {OUTPUT_CSV}")
print("Open the CSV and fill in suggested_folder and new_name.")
