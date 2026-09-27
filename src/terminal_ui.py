from __future__ import annotations

import time

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from src.models import LyricLine, Song


class TerminalUI:
    def __init__(self, settings: dict) -> None:
        self.settings = settings
        self.console = Console()
        self.panel_width = int(settings["display"]["panel_width"])

    def clear(self) -> None:
        if self.settings["display"].get("clear_screen", True):
            self.console.clear()

    def main_menu(self, songs: list[Song]) -> int | None:
        self.clear()
        self.console.print(
            Panel(
                Align.center("[bold bright_cyan]PYLYRICS[/]\n[magenta]Terminal Lyrics Animation Player[/]"),
                width=self.panel_width,
                border_style="bright_magenta",
            )
        )

        if not songs:
            self.error("No songs found. Add .json or .lrc files to the songs folder.")
            return None

        table = Table(title="Song Library", border_style="cyan", show_lines=False)
        table.add_column("#", justify="right", style="bright_yellow")
        table.add_column("Title", style="bright_white")
        table.add_column("Artist", style="green")
        table.add_column("Source", style="dim")
        for index, song in enumerate(songs, start=1):
            table.add_row(str(index), song.title, song.artist, song.source_path or "")

        self.console.print(table)
        self.console.print("[dim]Type a song number, or Q to quit.[/]")

        while True:
            choice = Prompt.ask("Select")
            if choice.strip().lower() in {"q", "quit", "exit"}:
                return None
            if choice.isdigit() and 1 <= int(choice) <= len(songs):
                return int(choice) - 1
            self.console.print("[red]Please choose a valid song number.[/]")

    def intro(self, song: Song) -> None:
        seconds = float(self.settings["animation"].get("intro_seconds", 1.2))
        frames = [
            "[dim]Loading lyric timeline...[/]",
            "[cyan]Syncing terminal lights...[/]",
            "[bright_magenta]Starting animation...[/]",
        ]
        for frame in frames:
            self.clear()
            self.console.print(
                Panel(
                    Align.center(
                        f"[bright_cyan]NOW PLAYING[/]\n\n[bold white]{song.title}[/]\n[green]{song.artist}[/]\n\n{frame}"
                    ),
                    width=self.panel_width,
                    border_style="bright_cyan",
                )
            )
            time.sleep(seconds / len(frames))

    def render_playback(
        self,
        song: Song,
        line: LyricLine,
        content: str | Text,
        elapsed: float,
        audio_started: bool,
    ) -> None:
        self.clear()
        body = Text()
        body.append("NOW PLAYING\n", style="bright_cyan bold")
        body.append(f"{song.title}\n", style="white bold")
        body.append(f"{song.artist}\n\n", style="green")

        if isinstance(content, Text):
            lyric_text = content
        else:
            lyric_text = Text(content, style=f"{line.color} bold")

        alignment = self.settings["display"].get("alignment", "center")
        align = "left" if alignment == "left" else "center"
        panel = Panel(
            Align(lyric_text, align=align, vertical="middle"),
            width=self.panel_width,
            height=7,
            border_style=line.color,
        )

        self.console.print(Align.center(body))
        self.console.print(panel)

        if self.settings["display"].get("show_progress", True):
            progress = min(1.0, elapsed / max(song.duration, 0.01))
            status = "Audio" if audio_started else "Timer"
            self.console.print(
                Align.center(
                    Text(
                        f"{status} sync  {format_time(elapsed)} / {format_time(song.duration)}",
                        style="dim",
                    )
                )
            )
            self.console.print(ProgressBar(total=1.0, completed=progress, width=50))

    def ending(self, song: Song) -> None:
        time.sleep(float(self.settings["animation"].get("ending_seconds", 1.4)))
        self.clear()
        self.console.print(
            Panel(
                Align.center(f"[bright_magenta]Finished[/]\n\n[white]{song.title}[/]"),
                width=self.panel_width,
                border_style="bright_magenta",
            )
        )

    def wait_for_key(self, message: str) -> None:
        Prompt.ask(message, default="")

    def error(self, message: str) -> None:
        self.console.print(f"[red]{message}[/]")

    def goodbye(self) -> None:
        self.clear()
        self.console.print("[bright_cyan]Goodbye.[/]")


def format_time(seconds: float) -> str:
    seconds = max(0, int(seconds))
    minutes, rest = divmod(seconds, 60)
    return f"{minutes:02d}:{rest:02d}"
