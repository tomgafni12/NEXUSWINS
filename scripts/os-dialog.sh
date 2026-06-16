#!/usr/bin/env bash
# Cross-platform OS-like dialog launcher.
# Tries zenity, yad, kdialog; falls back to Python/tkinter.

DIR="$(cd "$(dirname "$0")" && pwd)"

if command -v zenity >/dev/null 2>&1; then
  zenity --question --title="NexusWins" --text="This is an operating-system style dialog.\nDo you want to continue?" --ok-label="Yes" --cancel-label="No"
  rc=$?
  if [ $rc -eq 0 ]; then
    echo "RESULT=Yes"
    exit 0
  else
    echo "RESULT=No"
    exit 1
  fi
elif command -v yad >/dev/null 2>&1; then
  yad --question --title="NexusWins" --text="This is an operating-system style dialog.\nDo you want to continue?" --button=Yes:0 --button=No:1
  rc=$?
  if [ $rc -eq 0 ]; then
    echo "RESULT=Yes"
    exit 0
  else
    echo "RESULT=No"
    exit 1
  fi
elif command -v kdialog >/dev/null 2>&1; then
  if kdialog --yesno "This is an operating-system style dialog.\nDo you want to continue?"; then
    echo "RESULT=Yes"
    exit 0
  else
    echo "RESULT=No"
    exit 1
  fi
elif command -v python3 >/dev/null 2>&1; then
  if python3 - <<'PY' 2>/dev/null
import tkinter
print('ok')
PY
  then
    python3 "$DIR/os-dialog.py"
    exit $?
  fi
fi

echo "No graphical dialog tool found. Install 'zenity', 'yad', or 'python3-tk' to use this script."
exit 2
