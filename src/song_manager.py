from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.lrc_parser import load_lrc
from src.models import LyricLine, Song
from src.timing_engine import parse_timestamp


class SongManager:
    def __init__(self, songs_dir: Path) -> None:
        self.songs_dir = songs_dir
        self.songs: list[Song] = []

    def load(self) -> None:
        self.songs_dir.mkdir(parents=True, exist_ok=True)
        songs: list[Song] = []

        for path in sorted(self.songs_dir.glob("*.json")):
            songs.append(self._load_json_song(path))

        for path in sorted(self.songs_dir.glob("*.lrc")):
            songs.append(load_lrc(path))

        self.songs = songs

    def _load_json_song(self, path: Path) -> Song:
        with path.open("r", encoding="utf-8") as file:
            data: dict[str, Any] = json.load(file)

        lyrics: list[LyricLine] = []
        for item in data.get("lyrics", []):
            lyrics.append(
                LyricLine(
                    text=str(item["text"]),
                    start=parse_timestamp(item.get("time", item.get("start", 0))),
                    duration=float(item.get("duration", 2.5)),
                    animation=str(item.get("animation", "typewriter")),
                    color=str(item.get("color", "bright_cyan")),
                    typing_speed=(
                        float(item["typing_speed"])
                        if item.get("typing_speed") is not None
                        else None
                    ),
                )
            )

        lyrics.sort(key=lambda line: line.start)
        return Song(
            title=str(data.get("title", path.stem)),
            artist=str(data.get("artist", "Unknown Artist")),
            audio=data.get("audio"),
            source_path=str(path),
            lyrics=lyrics,
        )
