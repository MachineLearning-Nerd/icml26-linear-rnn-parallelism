#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: build_candidate.sh JUDGED_DIR CANDIDATE_DIR ALLOWLIST MANIFEST" >&2
  exit 2
fi

judged_dir=$1
candidate_dir=$2
allowlist=$3
manifest=$4

[[ -d "$judged_dir" ]] || { echo "judged directory missing" >&2; exit 1; }
if [[ -e "$candidate_dir" ]] && [[ -n "$(find "$candidate_dir" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "candidate directory must be empty" >&2
  exit 1
fi

mkdir -p "$candidate_dir"
rsync -a --exclude '.cache' "$judged_dir/" "$candidate_dir/"
chmod -R u+w "$candidate_dir"

cp release/space/README.md "$candidate_dir/README.md"
cp .trackio/logbook/logbook.json "$candidate_dir/logbook.json"
cp .trackio/logbook/pages/index.md "$candidate_dir/pages/index.md"
for page in release-overview current-claim-1 current-claim-2 current-claim-3 current-claim-4 current-claim-5 current-claim-6; do
  mkdir -p "$candidate_dir/pages/$page"
  cp ".trackio/logbook/pages/$page/page.md" "$candidate_dir/pages/$page/page.md"
done

mkdir -p "$candidate_dir/repro/src" "$candidate_dir/evidence" \
  "$candidate_dir/reports/linear-rnn-reproduction/images" "$candidate_dir/notebooks"
cp pyproject.toml uv.lock "$candidate_dir/"
cp repro/src/*.py "$candidate_dir/repro/src/"
for claim_dir in .openresearch/artifacts/claim_*; do
  cp -R "$claim_dir" "$candidate_dir/evidence/"
done
cp -R .openresearch/artifacts/startup "$candidate_dir/evidence/"
cp reports/linear-rnn-reproduction/*.md "$candidate_dir/reports/linear-rnn-reproduction/"
cp reports/linear-rnn-reproduction/images/*.svg "$candidate_dir/reports/linear-rnn-reproduction/images/"
cp notebooks/linear_rnn_reproduction.py "$candidate_dir/notebooks/"

{
  while IFS= read -r candidate_file; do
    relative=${candidate_file#"$candidate_dir/"}
    hash=$(shasum -a 256 "$candidate_file" | cut -d ' ' -f 1)
    printf '%s  %s\n' "$hash" "$relative"
  done < <(find "$candidate_dir" -type f -not -path '*/.cache/*' | LC_ALL=C sort)
} > "$manifest"

{
  while IFS= read -r candidate_file; do
    relative=${candidate_file#"$candidate_dir/"}
    judged_file="$judged_dir/$relative"
    if [[ ! -f "$judged_file" ]] || ! cmp -s "$candidate_file" "$judged_file"; then
      printf '%s\n' "$relative"
    fi
  done < <(find "$candidate_dir" -type f -not -path '*/.cache/*' | LC_ALL=C sort)
} > "$allowlist"
