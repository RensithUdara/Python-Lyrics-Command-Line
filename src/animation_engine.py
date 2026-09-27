from __future__ import annotations

import time
from collections.abc import Callable

from rich.text import Text

from src.models import LyricLine


RenderFn = Callable[[str | Text, LyricLine], None]


class AnimationEngine:
    def __init__(self, settings: dict) -> None:
        animation = settings["animation"]
        self.default_typing_speed = float(animation["typing_speed"])
        self.word_speed = float(animation["word_speed"])
        self.frame_delay = float(animation["frame_delay"])
        self.default_style = str(animation["default_style"])

    def render(self, line: LyricLine, render_frame: RenderFn) -> None:
        style = (line.animation or self.default_style).lower()
        if style in {"word", "word_by_word"}:
            self._word_by_word(line, render_frame)
        elif style in {"center", "center_reveal", "reveal"}:
            self._center_reveal(line, render_frame)
        elif style in {"fade", "pulse"}:
            self._fade(line, render_frame)
        elif style in {"instant", "none"}:
            render_frame(line.text, line)
        else:
            self._typewriter(line, render_frame)

    def _typewriter(self, line: LyricLine, render_frame: RenderFn) -> None:
        speed = line.typing_speed or self.default_typing_speed
        buffer = ""
        for char in line.text:
            buffer += char
            render_frame(buffer, line)
            time.sleep(speed)

    def _word_by_word(self, line: LyricLine, render_frame: RenderFn) -> None:
        words = line.text.split()
        for index in range(1, len(words) + 1):
            render_frame(" ".join(words[:index]), line)
            time.sleep(self.word_speed)

    def _center_reveal(self, line: LyricLine, render_frame: RenderFn) -> None:
        text = line.text
        middle = len(text) // 2
        for radius in range(1, middle + 2):
            start = max(0, middle - radius)
            end = min(len(text), middle + radius)
            render_frame(text[start:end].center(len(text)), line)
            time.sleep(self.frame_delay)
        render_frame(text, line)

    def _fade(self, line: LyricLine, render_frame: RenderFn) -> None:
        for style in ("dim", "white", line.color):
            render_frame(Text(line.text, style=style), line)
            time.sleep(self.frame_delay * 4)
