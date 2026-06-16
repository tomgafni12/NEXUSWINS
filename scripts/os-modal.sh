#!/usr/bin/env bash
# Wrapper for os-modal.py with fallbacks
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$SCRIPT_DIR/os-modal.py"

if command -v python3 >/dev/null 2>&1; then
    if [ -n "${DISPLAY-}" ]; then
        python3 "$PY" --title "NexusWins" --message "This is a primitive OS-style modal. Continue?" --timeout 30
    else
        # Headless: prefer terminal 'loom' modal if available
        if [ -x "$SCRIPT_DIR/os-modal-term.py" ]; then
            python3 "$SCRIPT_DIR/os-modal-term.py" --title "NexusWins" --message "This is a primitive OS-style modal.\nPress Enter to continue or Esc to cancel." --timeout 30
        else
            # Console fallback
            python3 "$PY" --title "NexusWins" --message "This is a primitive OS-style modal. Continue?"
        fi
    fi
else
    echo "This is a primitive OS-style modal. Continue? [y/N]"
    read -r ans
    case "$ans" in
        y|Y) exit 0 ;;
        *) exit 1 ;;
    esac
fi
