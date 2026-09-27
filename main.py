from __future__ import annotations

import argparse
from pathlib import Path

from src.audio_player import AudioPlayer
from src.config import load_settings
from src.lyric_engine import LyricEngine
from src.song_manager import SongManager
from src.terminal_ui import TerminalUI


ROOT = Path(__file__).parent


def play_song(index: int, manager: SongManager, ui: TerminalUI, settings: dict) -> None:
    song = manager.songs[index]
    ui.clear()
    ui.intro(song)

    audio = AudioPlayer(enabled=settings["audio"].get("enabled", False))
    audio_path = ROOT / song.audio if song.audio else None
    audio_started = audio.play(audio_path, volume=settings["audio"].get("volume", 0.8))

    try:
        LyricEngine(ui=ui, settings=settings).play(song, audio_started=audio_started)
    finally:
        audio.stop()

    ui.ending(song)


def run_demo(manager: SongManager, ui: TerminalUI, settings: dict) -> None:
    if not manager.songs:
        ui.error("No songs found in the songs folder.")
        return
    play_song(0, manager, ui, settings)


def main() -> None:
    parser = argparse.ArgumentParser(description="Terminal lyrics animation player.")
    parser.add_argument("--demo", action="store_true", help="Play the first available song immediately.")
    args = parser.parse_args()

    settings = load_settings(ROOT / "config" / "settings.json")
    ui = TerminalUI(settings=settings)
    manager = SongManager(ROOT / "songs")
    manager.load()

    if args.demo:
        run_demo(manager, ui, settings)
        return

    while True:
        choice = ui.main_menu(manager.songs)
        if choice is None:
            ui.goodbye()
            return
        play_song(choice, manager, ui, settings)
        ui.wait_for_key("Press Enter to return to the library...")


if __name__ == "__main__":
    main()
