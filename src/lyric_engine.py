from __future__ import annotations

import time

from src.animation_engine import AnimationEngine
from src.models import LyricLine, Song
from src.terminal_ui import TerminalUI
from src.timing_engine import Timeline


class LyricEngine:
    def __init__(self, ui: TerminalUI, settings: dict) -> None:
        self.ui = ui
        self.animations = AnimationEngine(settings)

    def play(self, song: Song, audio_started: bool = False) -> None:
        timeline = Timeline()

        for line in song.lyrics:
            timeline.wait_until(line.start)
            line_started = timeline.elapsed

            def render_frame(content: str, lyric_line: LyricLine) -> None:
                self.ui.render_playback(
                    song=song,
                    line=lyric_line,
                    content=content,
                    elapsed=timeline.elapsed,
                    audio_started=audio_started,
                )

            self.animations.render(line, render_frame)

            spent = timeline.elapsed - line_started
            hold = max(0.0, line.duration - spent)
            if hold > 0:
                time.sleep(hold)
