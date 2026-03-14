from pathlib import Path
import shutil
import sys

RAW_ROOT = Path("/Users/adampugh/GitHub/TeraCreators-Help/static/img/raptor/_raw")
DEST_ROOT = Path("/Users/adampugh/GitHub/TeraCreators-Help/static/img/raptor")

# Best-effort mapping based on the filenames/folders you showed and the guide topics.
# Format:
# "source relative path from _raw": ("destination subfolder", "new clean filename", "note")
#
# Folders available:
# passes, eggs, menus, events, codes, misc
MAPPINGS = {
    # Strongest candidates from the guide topics
    "zeldris25.5.1996/12_1_1_Fortnite_04.03.2026_0_12_53.png.MqDd7ys4E8.png": (
        "passes",
        "raptor-passes-screen-01.png",
        "Likely pass/unlock screen",
    ),
    "zeldris25.5.1996/11_1_1_Fortnite_04.03.2026_0_36_32.png.VenDBi6evC.png": (
        "eggs",
        "raptor-egg-room-20-location-01.png",
        "Likely egg pickup or egg-progress-related screenshot",
    ),
    "thefortniteempire/573_1_1_Screenshot_2025-08-09_000644.png.GTigtOyH-z.png": (
        "codes",
        "raptor-codes-screen-01.png",
        "Likely codes/community reference screenshot",
    ),
    "sirjameskronodagger/450_1_1_20250815_205149.jpg.9cnaY9zYJc.jpg": (
        "events",
        "raptor-loyal-raptor-event-01.jpg",
        "Likely event screenshot",
    ),

    # Good candidates for menus / upgrades / rewards
    "kainesius/350_1_1_IMG_5819.jpg.hfrS725Fvp.jpg": (
        "menus",
        "raptor-upgrades-screen-01.jpg",
        "Likely upgrade screen",
    ),
    "kainesius/351_1_1_IMG_5818.jpg.a2AfAn_tmX.jpg": (
        "menus",
        "raptor-daily-rewards-screen-01.jpg",
        "Likely daily rewards or related progression menu",
    ),
    "marmite_fhh/348_1_1_IMG_2437.jpg.By5usDg1xb.jpg": (
        "menus",
        "raptor-daily-chest-screen-01.jpg",
        "Likely chest or reward-related screenshot",
    ),
    "diva.bae/236_1_1_20251010_142100.jpg.MkFSzRmfpG.jpg": (
        "menus",
        "raptor-egg-upgrades-screen-01.jpg",
        "Likely upgrade or menu screenshot",
    ),
    "koolhix/404_1_1_rn_image_picker_lib_temp_7d9aaefb-4389-46d5-806c-80dd2ad271cd.jpg.V89qeNJ5Q1.jpg": (
        "menus",
        "raptor-progress-menu-01.jpg",
        "Likely progress/menu screenshot",
    ),

    # Egg / run / room related
    "jecorona95/198_1_1_rn_image_picker_lib_temp_6f39bab7-e2e8-49f8-8b31-7e68d5519bb9.jpg.slATHzmEzL.jpg": (
        "eggs",
        "raptor-egg-hud-01.jpg",
        "Likely egg HUD or run screenshot",
    ),
    "jecorona95/269_1_1_rn_image_picker_lib_temp_51be3c91-8193-4e6b-aaa7-af5a2a9aad95.jpg.aXFDnyQNBD.jpg": (
        "eggs",
        "raptor-egg-recovery-room-20-01.jpg",
        "Likely room 20 / egg recovery-related screenshot",
    ),
    "nuny4_/367_1_1_IMG_6960.png.80d2JU-kuY.jpg": (
        "eggs",
        "raptor-egg-run-01.jpg",
        "Likely in-run egg screenshot",
    ),
    "lunaxlama/35_1_1_PXL_20260216_231831885.jpg.zsKBNYOB0G.jpg": (
        "eggs",
        "raptor-egg-milestones-01.jpg",
        "Likely milestone or progress image",
    ),
    "stardustgrove/481_1_1_image.png.VFVVbZ85-e.png": (
        "eggs",
        "raptor-room-20-egg-area-01.png",
        "Likely room 20 egg area",
    ),
    "teensee/215_1_1_image.png.aF_bbFLN_z.png": (
        "eggs",
        "raptor-egg-progress-screen-01.png",
        "Likely egg progress screenshot",
    ),
    "mojer_tribalgod/207_1_1_image-20.png.FLnTtssPgd.png": (
        "eggs",
        "raptor-egg-collection-screen-01.png",
        "Likely egg collection/progress screenshot",
    ),

    # Misc community screenshots that may still be useful
    "avi2425/390_1_1_image.png.bk1K_sZzEY.png": (
        "misc",
        "raptor-community-screenshot-01.png",
        "General screenshot",
    ),
    "caboose2236./336_1_1_13b89264-0497-4458-bdbf-a679fa8ed740.png.5fEYDTXihb.png": (
        "misc",
        "raptor-community-screenshot-02.png",
        "General screenshot",
    ),
    "darky3d/292_1_1_image.png.UgltdYo4N-.png": (
        "misc",
        "raptor-community-screenshot-03.png",
        "General screenshot",
    ),
    "darky3d/292_2_1_image.png.oUYYcB-4uq.png": (
        "misc",
        "raptor-community-screenshot-04.png",
        "General screenshot",
    ),
    "darky3d/292_3_1_image.png.SPZ0j90N8p.png": (
        "misc",
        "raptor-community-screenshot-05.png",
        "General screenshot",
    ),
    "paulypanda92/430_1_1_image.png.-zIoPGvaC0.png": (
        "misc",
        "raptor-community-screenshot-06.png",
        "General screenshot",
    ),
    "titts_nay/157_1_1_IMG_5424.jpg.MsoE8hAUnr.jpg": (
        "misc",
        "raptor-community-photo-01.jpg",
        "General photo",
    ),

    # Probably not directly needed in docs, but keep them organized
    "lyjahboostin/106_1_1_image0.gif.fgzGxzsQ70.gif": (
        "misc",
        "raptor-community-animation-01.gif",
        "Animated image",
    ),
}

def ensure_dest_folders():
    for folder in ["passes", "eggs", "menus", "events", "codes", "misc"]:
        (DEST_ROOT / folder).mkdir(parents=True, exist_ok=True)

def copy_mapped_files():
    copied = 0
    missing = []
    skipped_existing = []

    for rel_path, (subfolder, new_name, note) in MAPPINGS.items():
        source = RAW_ROOT / rel_path
        dest = DEST_ROOT / subfolder / new_name

        if not source.exists():
            missing.append(rel_path)
            continue

        if dest.exists():
            skipped_existing.append(str(dest))
            continue

        shutil.copy2(source, dest)
        copied += 1
        print(f"Copied: {source} -> {dest}  [{note}]")

    return copied, missing, skipped_existing

def copy_unmapped_to_misc():
    """
    Optional fallback:
    Any file not explicitly mapped gets copied into misc/unmapped-XX.ext
    so nothing is lost.
    """
    mapped_sources = {RAW_ROOT / rel_path for rel_path in MAPPINGS.keys()}
    unmapped = []

    counter = 1
    for file_path in sorted(RAW_ROOT.rglob("*")):
        if not file_path.is_file():
            continue
        if file_path in mapped_sources:
            continue

        ext = file_path.suffix.lower()
        if not ext:
            ext = ".bin"

        dest = DEST_ROOT / "misc" / f"raptor-unmapped-{counter:02d}{ext}"
        while dest.exists():
            counter += 1
            dest = DEST_ROOT / "misc" / f"raptor-unmapped-{counter:02d}{ext}"

        shutil.copy2(file_path, dest)
        unmapped.append((str(file_path), str(dest)))
        counter += 1

    return unmapped

def main():
    if not RAW_ROOT.exists():
        print(f"ERROR: RAW_ROOT does not exist: {RAW_ROOT}")
        sys.exit(1)

    ensure_dest_folders()

    copied, missing, skipped_existing = copy_mapped_files()
    unmapped = copy_unmapped_to_misc()

    print("\n--- Summary ---")
    print(f"Mapped files copied: {copied}")
    print(f"Unmapped files copied to misc: {len(unmapped)}")
    print(f"Missing mapped sources: {len(missing)}")
    print(f"Skipped because destination existed: {len(skipped_existing)}")

    if missing:
        print("\nMissing mapped source files:")
        for item in missing:
            print(f"- {item}")

    if skipped_existing:
        print("\nSkipped existing destination files:")
        for item in skipped_existing:
            print(f"- {item}")

    if unmapped:
        print("\nUnmapped files copied to misc:")
        for src, dest in unmapped:
            print(f"- {src} -> {dest}")

if __name__ == "__main__":
    main()
