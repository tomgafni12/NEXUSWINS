#!/usr/bin/env python3
"""
Terminal 'loom' modal using curses. Works in headless terminals.
Exit codes: 0=Continue, 1=Cancel, 2=Timeout
"""
import curses
import time
import sys
import argparse

def draw_box(stdscr, y, x, h, w, title, message):
    stdscr.attron(curses.color_pair(1))
    for i in range(h):
        stdscr.addstr(y + i, x, ' ' * w)
    stdscr.attroff(curses.color_pair(1))
    # border
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(y, x, '+' + '-' * (w-2) + '+')
    for i in range(1, h-1):
        stdscr.addstr(y+i, x, '|' + ' ' * (w-2) + '|')
    stdscr.addstr(y+h-1, x, '+' + '-' * (w-2) + '+')
    stdscr.attroff(curses.color_pair(2))
    # title
    if title:
        t = ' ' + title + ' '
        stdscr.addstr(y, x + 2, t, curses.A_BOLD)
    # message
    lines = message.split('\n')
    for idx, line in enumerate(lines[:h-4]):
        stdscr.addstr(y+2+idx, x+2, line[:w-4])
    # buttons
    btn_y = y + h - 2
    cont = '[ Continue ]'
    canc = '[ Cancel ]'
    stdscr.addstr(btn_y, x + w - len(cont) - 4, cont, curses.A_REVERSE)
    stdscr.addstr(btn_y, x + 3, canc)

def run_modal(stdscr, title, message, timeout):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    sh, sw = stdscr.getmaxyx()
    # target size
    tw, th = min(80, sw-4), min(20, sh-4)
    cx = (sw - tw) // 2
    cy = (sh - th) // 2

    frames = 8
    for i in range(1, frames+1):
        frac = i / frames
        w = max(20, int(tw * frac))
        h = max(8, int(th * frac))
        x = (sw - w) // 2
        y = (sh - h) // 2
        stdscr.clear()
        draw_box(stdscr, y, x, h, w, title, message)
        stdscr.refresh()
        time.sleep(0.05)

    start = time.time()
    stdscr.nodelay(False if timeout is None else True)
    while True:
        if timeout is not None:
            elapsed = time.time() - start
            if elapsed >= timeout:
                return 2
            remaining = int(timeout - elapsed)
            info = f'Auto-cancel in {remaining}s'
            stdscr.addstr(cy+th, max(0, cx), info)
        key = stdscr.getch()
        if key in (curses.KEY_ENTER, 10, 13):
            return 0
        if key in (27, ord('q')):
            return 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', default='NexusWins', help='Dialog title')
    parser.add_argument('--message', default='This is a primitive OS-style modal.\nPress Enter to continue or Esc to cancel.', help='Dialog message')
    parser.add_argument('--timeout', type=int, default=None, help='Auto-cancel seconds')
    args = parser.parse_args()

    try:
        code = curses.wrapper(run_modal, args.title, args.message, args.timeout)
    except Exception:
        print(args.message)
        ans = input('Continue? [y/N]: ').strip().lower()
        code = 0 if ans == 'y' else 1

    sys.exit(code)

if __name__ == '__main__':
    main()
