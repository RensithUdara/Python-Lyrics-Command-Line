from __future__ import annotations

import argparse
import os
import random
import shutil
import sys
import time


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DEEP_RED = "\033[38;5;88m"
SOUL_PURPLE = "\033[38;5;54m"
GOLDEN_WARM = "\033[38;5;136m"
MIST_BLUE = "\033[38;5;24m"
MIST_WHITE = "\033[38;5;251m"
BOLD = "\033[1m"
RESET = "\033[0m"


SONG_LINES = [
    "Bovitiyaa mal sulagee vaenenakeaata",
    "kevita thiyaapan ahakin",
    "kabaragoyin dhaeka niyara udin paena",
    "dhuvalaa vareeng mage malee",
    "",
    "goovindhaa hee kadhu maedhdhen",
    "vahiinnath vagee",
    "goovindhaa ee kadhu maedhdhen",
    "vahiinnath vagee",
    "",
    "gagulaellee pavanaellee hasaraellee piyambannee",
    "akurak ee nodhanim",
    "gagulaellee pavanaellee hasaraellee piyambannee",
    "akurak ee nodhanim",
    "",
    "paensala dhekata kadaagena",
    "madhatiya aeta ekathu karaagena",
    "paaena pothata piriyak naae mata",
    "vaagee eevaa naae mee haritha kalaavata",
    "mii amba gas aththe paehila hodha",
    "maala girav vata ganan hadhanavadha",
    "chakkareeta vadaa dhannava mang",
    "manthare mee kadhu kathaa karana hada",
    "naevgala kandhen ee ehaata",
    "mal pipilaa aethi malina barava",
    "yanna oone dhavasaka balang inna",
    "hath kadhu pisagena ira vadinaa raga",
    "amara ithing mang ennaae heta",
    "vevaela kevitak ven naae thava",
    "baana ekka yaaya puraavata",
    "gopalu rajaa vennam mee yaayata",
    "",
    "goovindhaa hee kadhu maedhdhen",
    "vahiinnath vagee",
    "goovindhaa ee kadhu maedhdhen",
    "vahiinnath vagee",
    "",
    "gagulaellee pavanaellee hasaraellee piyambannee",
    "akurak ee nodhanim",
    "gagulaellee pavanaellee hasaraellee piyambannee",
    "akurak ee nodhanim",
    "",
    "bovitiya mal sulagee vaenenakeaata",
    "kevita thiyaapan ahakin",
    "kabaragoyin dhaeka niyara udin paena",
    "dhuvalaa vareeng mage malee",
    "bovitiyaa mal sulagee vaenenakeaata",
    "kevita thiyaapan ahakin",
    "kabaragoyin dhaeka niyara udin paena",
    "dhuvalaa vareeng mage malee",
]

COLORS = [MIST_WHITE, GOLDEN_WARM, GOLDEN_WARM, SOUL_PURPLE, MIST_BLUE, GOLDEN_WARM]


def terminal_width() -> int:
    return max(50, shutil.get_terminal_size(fallback=(80, 24)).columns)


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def soulful_typing(text: str, color: str, delay: float = 0.05, indent: int = 0) -> None:
    sys.stdout.write(" " * indent)
    sys.stdout.flush()

    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.01))

    print()


def left_typing(text: str, color: str, delay: float, pause: float) -> None:
    indent = 8
    soulful_typing(text, color, delay, indent)
    time.sleep(pause)


def print_intro() -> None:
    clear_screen()
    print()
    soulful_typing("♪ Bovitiyaa Mal ♪", MIST_WHITE, 0.035, 8)
    time.sleep(0.35)
    soulful_typing("Full Singlish Lyrics", GOLDEN_WARM, 0.04, 8)
    time.sleep(0.8)
    print()


def play(mode: str = "singlish") -> None:
    print_intro()
    color_index = 0

    for line in SONG_LINES:
        if not line:
            print()
            time.sleep(0.9)
            continue

        color = COLORS[color_index % len(COLORS)]
        color_index += 1
        delay = 0.035 if len(line) > 34 else 0.048
        pause = 0.95 if line.endswith("vagee") or line.endswith("nodhanim") else 0.55
        left_typing(line, color, delay, pause)
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Print Bovitiyaa Mal full Singlish lyrics.")
    parser.add_argument(
        "--mode",
        choices=("singlish", "sinhala", "both"),
        default="singlish",
        help="Kept for compatibility; this song file uses Singlish lyrics.",
    )
    parser.parse_args()
    play()


if __name__ == "__main__":
    main()
