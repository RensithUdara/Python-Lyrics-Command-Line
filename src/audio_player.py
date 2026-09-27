from __future__ import annotations

from pathlib import Path


class AudioPlayer:
    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled
        self._pygame = None
        self._playing = False

    def play(self, path: Path | None, volume: float = 0.8) -> bool:
        if not self.enabled or path is None or not path.exists():
            return False

        try:
            import pygame
        except ImportError:
            return False

        pygame.mixer.init()
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))
        pygame.mixer.music.play()
        self._pygame = pygame
        self._playing = True
        return True

    def stop(self) -> None:
        if self._pygame is not None and self._playing:
            self._pygame.mixer.music.stop()
            self._playing = False
