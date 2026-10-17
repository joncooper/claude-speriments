#!/bin/bash
PYCDC=/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/tools/pycdc/build/pycdc
SRC=/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/oracle/out/stockpyc
DST=/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/oracle/out/decompiled
ok=0; warn=0; fail=0
while IFS= read -r pyc; do
  rel="${pyc#$SRC/}"; py="$DST/${rel%.pyc}.py"
  mkdir -p "$(dirname "$py")"
  if timeout 30 "$PYCDC" "$pyc" > "$py" 2>/dev/null; then
    if grep -q 'WARNING: Decompyle incomplete\|Unsupported opcode' "$py"; then warn=$((warn+1)); else ok=$((ok+1)); fi
  else fail=$((fail+1)); fi
done < <(find "$SRC/dropbox" "$SRC/apex" -name '*.pyc')
echo "decompiled: clean=$ok partial=$warn failed=$fail"
