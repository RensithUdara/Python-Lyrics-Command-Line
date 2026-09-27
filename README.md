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

For the simple Instagram-reel-style terminal print:

```powershell
python song.py
```

The reel script defaults to Singlish. You can also run:

```powershell
python song.py --mode sinhala
python song.py --mode both
```

On Windows, use the included CMD launchers if Sinhala text looks broken:

```cmd
run_sinhala.cmd
run_singlish.cmd
```

For Sinhala rendering, use Windows Terminal or VS Code Terminal and set the terminal font to a Sinhala-capable font such as `Nirmala UI` or `Iskoola Pota`. Also make sure the terminal is using UTF-8; the CMD launchers run `chcp 65001` automatically.

or:

```powershell
python main.py --reel
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

Use lyrics you wrote or have permission to use. The included Sinhala/Singlish lyrics are original demo text. Replace them with your own song lines in `song.py` or add a new JSON file in `songs/`.
