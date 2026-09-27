from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class LyricLine:
    text: str
    start: float
    duration: float = 2.5
    animation: str = "typewriter"
    color: str = "bright_cyan"
    typing_speed: float | None = None


@dataclass(frozen=True)
class Song:
    title: str
    artist: str = "Unknown Artist"
    audio: str | None = None
    source_path: str | None = None
    lyrics: list[LyricLine] = field(default_factory=list)

    @property
    def duration(self) -> float:
        if not self.lyrics:
            return 0.0
        last = self.lyrics[-1]
        return last.start + last.duration
