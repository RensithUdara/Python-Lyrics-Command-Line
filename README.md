# PyLyrics

PyLyrics is a terminal-based lyrics animation player for Python. It loads songs from JSON or LRC files, renders synchronized lyrics with Rich, and can optionally start audio playback when a matching audio file exists.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`pygame` is only needed for audio playback. The lyrics animation still works if audio playback is disabled in `config/settings.json`.

## Run

```powershell
python main.py
```

For a quick non-interactive demo:

```powershell
python main.py --demo
```

## Add Songs

Add JSON files to `songs/`:

```json
{
  "title": "My Song",
  "artist": "Me",
  "audio": "audio/my_song.mp3",
  "lyrics": [
    {
      "time": "00:00.00",
      "text": "First line",
      "duration": 2.0,
      "animation": "typewriter",
      "color": "cyan"
    }
  ]
}
```

You can also drop `.lrc` files in `songs/`. They will appear in the song library automatically.

Use lyrics you wrote or have permission to use.
