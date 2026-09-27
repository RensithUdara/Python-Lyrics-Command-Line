from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_SETTINGS: dict[str, Any] = {
    "display": {
        "theme": "neon",
        "clear_screen": True,
        "panel_width": 74,
        "show_progress": True,
    },
    "animation": {
        "default_style": "typewriter",
        "typing_speed": 0.035,
        "word_speed": 0.18,
        "frame_delay": 0.06,
        "intro_seconds": 1.2,
        "ending_seconds": 1.4,
    },
    "audio": {
        "enabled": False,
        "volume": 0.8,
    },
}


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_settings(path: Path) -> dict[str, Any]:
    if not path.exists():
        return DEFAULT_SETTINGS
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return deep_merge(DEFAULT_SETTINGS, data)
