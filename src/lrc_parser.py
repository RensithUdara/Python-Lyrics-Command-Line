from __future__ import annotations

import re
from pathlib import Path

from src.models import LyricLine, Song
from src.timing_engine import parse_timestamp


LRC_LINE_RE = re.compile(r"(\[(\d{1,2}:\d{2}(?:\.\d{1,3})?)\])+(.+)?")
META_RE = re.compile(r"^\[(ti|ar|al):(.+)\]$", re.IGNORECASE)


def load_lrc(path: Path) -> Song:
    title = path.stem.replace("_", " ").title()
    artist = "Unknown Artist"
    entries: list[tuple[float, str]] = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue

        meta = META_RE.match(line)
        if meta:
            key, value = meta.group(1).lower(), meta.group(2).strip()
            if key == "ti":
                title = value
            elif key == "ar":
                artist = value
            continue

        lyric = LRC_LINE_RE.match(line)
        if not lyric:
            continue

        text = (lyric.group(3) or "").strip()
        for timestamp in re.findall(r"\[(\d{1,2}:\d{2}(?:\.\d{1,3})?)\]", line):
            entries.append((parse_timestamp(timestamp), text))

    entries.sort(key=lambda item: item[0])
    lyrics: list[LyricLine] = []
    for index, (start, text) in enumerate(entries):
        next_start = entries[index + 1][0] if index + 1 < len(entries) else start + 2.8
        lyrics.append(
            LyricLine(
                text=text,
                start=start,
                duration=max(1.0, next_start - start),
                animation="typewriter",
                color="bright_cyan",
            )
        )

    return Song(title=title, artist=artist, source_path=str(path), lyrics=lyrics)
