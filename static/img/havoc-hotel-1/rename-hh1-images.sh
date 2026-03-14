#!/bin/zsh
set -euo pipefail

cd /Users/adampugh/GitHub/TeraCreators-Help/static/img/havoc-hotel-1

rename_file() {
  local old_name="$1"
  local new_name="$2"

  if [[ ! -f "$old_name" ]]; then
    echo "SKIP: file not found: $old_name"
    return
  fi

  if [[ -f "$new_name" ]]; then
    echo "SKIP: target already exists: $new_name"
    return
  fi

  mv "$old_name" "$new_name"
  echo "RENAMED: $old_name -> $new_name"
}

rename_file "21_1_1_IMG_20250719_092853.jpg.dztS0GeOGZ.jpg" "hh1-lobby-stats-escapes-shortest-time.jpg"
rename_file "18_1_1_IMG_7378.jpg.BaHlGgQnyI.jpg" "hh1-lobby-stats-start-screen.jpg"
rename_file "27_1_1_IMG_0952.jpg.iwg-ysigS3.jpg" "hh1-leaderboard-and-guests-0-of-14.jpg"
rename_file "65_1_1_4b17e9ff-c4f5-4508-b860-5e606f93adf7.png.ANFuSNCYXn.jpg" "hh1-guests-13-of-14-stage-18.jpg"
rename_file "77_1_1_Fortnite_3_16_2025_7_42_55_PM.png.h0xHK49b7Y.png" "hh1-old-leaderboard-board.png"

echo
echo "Final files:"
ls -1
