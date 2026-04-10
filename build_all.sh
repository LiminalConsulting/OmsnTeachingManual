#!/bin/bash
# Build all manuals and exercise books
# Run from repo root: bash build_all.sh
# Optional: bash build_all.sh math   (rebuild one subject only)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD="$SCRIPT_DIR/shared/build.sh"
BUILD_EX="$SCRIPT_DIR/shared/build_exercises.sh"

SUBJECT="${1:-all}"
SUCCESS=0
FAIL=0

run() {
  local dir="$1"
  local script="$2"
  local input="$3"
  local output="$4"
  local lang="${5:-pt-PT}"
  if [ ! -f "$dir/$input" ]; then
    echo "⏭  Skipping $input (not yet created)"
    return 0
  fi
  if (cd "$dir" && bash "$script" "$input" "$output" "$lang"); then
    SUCCESS=$((SUCCESS + 1))
  else
    FAIL=$((FAIL + 1))
  fi
}

build_math() {
  local d="$SCRIPT_DIR/subjects/math"
  run "$d/manual" "$BUILD" MANUAL_FINAL_PRINT.md          MANUAL_FINAL.pdf          pt-PT
  run "$d/manual" "$BUILD" MANUAL_FINAL_EN_PRINT.md       MANUAL_FINAL_EN.pdf       en-US
  run "$d/manual" "$BUILD" MANUAL_FINAL_BILINGUAL_SRC.md  MANUAL_FINAL_BILINGUAL.pdf bilingual
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_PT.md    EXERCISES_FINAL.pdf          pt-PT
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_EN.md    EXERCISES_FINAL_EN.pdf       en-US
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_BILINGUAL.md EXERCISES_FINAL_BILINGUAL.pdf bilingual
}

build_physics() {
  local d="$SCRIPT_DIR/subjects/physics-chemistry"
  run "$d/manual" "$BUILD" MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md    MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf    pt-PT
  run "$d/manual" "$BUILD" MANUAL_FINAL_PHYSICS_CHEMISTRY_EN_PRINT.md MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf en-US
  run "$d/manual" "$BUILD" MANUAL_FINAL_PHYSICS_CHEMISTRY_BILINGUAL_SRC.md MANUAL_FINAL_PHYSICS_CHEMISTRY_BILINGUAL.pdf bilingual
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_PT.md    EXERCISES_FINAL.pdf          pt-PT
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_EN.md    EXERCISES_FINAL_EN.pdf       en-US
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_BILINGUAL.md EXERCISES_FINAL_BILINGUAL.pdf bilingual
}

build_sciences() {
  local d="$SCRIPT_DIR/subjects/sciences"
  run "$d/manual" "$BUILD" MANUAL_FINAL_SCIENCES_PRINT.md    MANUAL_FINAL_SCIENCES.pdf    pt-PT
  run "$d/manual" "$BUILD" MANUAL_FINAL_SCIENCES_EN_PRINT.md MANUAL_FINAL_SCIENCES_EN.pdf en-US
  run "$d/manual" "$BUILD" MANUAL_FINAL_SCIENCES_BILINGUAL_SRC.md MANUAL_FINAL_SCIENCES_BILINGUAL.pdf bilingual
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_PT.md    EXERCISES_FINAL.pdf          pt-PT
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_EN.md    EXERCISES_FINAL_EN.pdf       en-US
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_BILINGUAL.md EXERCISES_FINAL_BILINGUAL.pdf bilingual
}

build_history() {
  local d="$SCRIPT_DIR/subjects/history-geography"
  run "$d/manual" "$BUILD" MANUAL_FINAL_HISTORY_GEOGRAPHY_PRINT.md    MANUAL_FINAL_HISTORY_GEOGRAPHY.pdf    pt-PT
  run "$d/manual" "$BUILD" MANUAL_FINAL_HISTORY_GEOGRAPHY_EN_PRINT.md MANUAL_FINAL_HISTORY_GEOGRAPHY_EN.pdf en-US
  run "$d/manual" "$BUILD" MANUAL_FINAL_HISTORY_GEOGRAPHY_BILINGUAL_SRC.md MANUAL_FINAL_HISTORY_GEOGRAPHY_BILINGUAL.pdf bilingual
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_PT.md    EXERCISES_FINAL.pdf          pt-PT
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_EN.md    EXERCISES_FINAL_EN.pdf       en-US
  run "$d/exercises" "$BUILD_EX" EXERCISES_FINAL_BILINGUAL.md EXERCISES_FINAL_BILINGUAL.pdf bilingual
}

case "$SUBJECT" in
  math)    build_math ;;
  physics) build_physics ;;
  sciences) build_sciences ;;
  history) build_history ;;
  all)
    build_math
    build_physics
    build_sciences
    build_history
    ;;
  *)
    echo "Unknown subject: $SUBJECT. Use: math | physics | sciences | history | all"
    exit 1
    ;;
esac

echo ""
echo "Done: $SUCCESS succeeded, $FAIL failed"
# Allow partial success — bilingual paracol builds may fail until longtable compat is resolved
if [ $SUCCESS -eq 0 ] && [ $FAIL -gt 0 ]; then
  exit 1
fi
