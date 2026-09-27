# 🎤 PyLyrics

**PyLyrics** is a beautiful terminal-based lyrics animation player built with Python. It loads lyric timelines from **JSON** or **LRC** files, renders synchronized lyrics with **Rich**, and can optionally play matching audio files with **pygame**.

Perfect for terminal lyric demos, karaoke-style experiments, Sinhala/Singlish lyric displays, and fun animated text reels.

---

## ✨ Features

- 🎶 Animated lyric playback in the terminal
- 📚 Automatic song library from the `songs/` folder
- 📝 Supports custom `.json` song files
- ⏱️ Supports `.lrc` timestamp lyric files
- 🌈 Rich-powered neon terminal panels and colors
- 🖊️ Multiple lyric animation styles
- 🔊 Optional audio playback with pygame
- 📊 Optional playback progress bar
- 🇱🇰 Sinhala/Singlish terminal launcher scripts for Windows
- 🧪 Small unit test suite for timestamp parsing

---

## 📁 Project Structure

```text
Python-Lyrics/
├── config/
│   └── settings.json          # Display, animation, and audio settings
├── songs/
│   ├── demo_original.json     # Demo song timeline
│   └── bowitiya_mal.json      # Example Singlish lyric timeline
├── src/
│   ├── animation_engine.py    # Typewriter, word, reveal, fade animations
│   ├── audio_player.py        # Optional pygame audio playback
│   ├── config.py              # Settings loader and defaults
│   ├── lrc_parser.py          # LRC file parser
│   ├── lyric_engine.py        # Playback timing and lyric rendering
│   ├── models.py              # Song and lyric data models
│   ├── song_manager.py        # Loads songs from the songs folder
│   ├── terminal_ui.py         # Rich terminal interface
│   └── timing_engine.py       # Timestamp parsing and timeline helpers
├── tests/
│   └── test_timing_engine.py  # Unit tests
├── main.py                    # Main interactive app
├── song.py                    # Simple reel-style lyric printer
├── requirements.txt           # Python dependencies
├── run_bowitiya.cmd           # Windows UTF-8 launcher
├── run_sinhala.cmd            # Windows Sinhala mode launcher
└── run_singlish.cmd           # Windows Singlish mode launcher
```

---

## 🧰 Requirements

- Python 3.10 or newer recommended
- Windows Terminal, VS Code Terminal, PowerShell, or another UTF-8 capable terminal
- A Sinhala-capable font if displaying Sinhala text

Python packages:

```text
rich>=13.7.0
pygame>=2.5.2
```

> `pygame` is only needed when audio playback is enabled. Lyrics animation still works with audio turned off.

---

## 🚀 Installation

Open a terminal in the project folder:

```powershell
cd L:\Python-Lyrics
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## ▶️ How To Run

### 🎼 Interactive Song Library

```powershell
python main.py
```

This opens the song library. Type a song number to play it, or type `Q` to quit.

### ⚡ Quick Demo

```powershell
python main.py --demo
```

This plays the first available song in the `songs/` folder immediately.

### 📱 Reel-Style Terminal Lyrics

```powershell
python main.py --reel
```

or:

```powershell
python song.py
```

### 🪟 Windows Launchers

If Sinhala or special characters look broken in Command Prompt, use the included `.cmd` launchers. They switch the terminal to UTF-8 before running the script.

```cmd
run_bowitiya.cmd
run_sinhala.cmd
run_singlish.cmd
```

---

## ⚙️ Configuration

Settings live in:

```text
config/settings.json
```

Current example:

```json
{
  "display": {
    "theme": "neon",
    "clear_screen": true,
    "panel_width": 74,
    "alignment": "left",
    "show_progress": true
  },
  "animation": {
    "default_style": "typewriter",
    "typing_speed": 0.035,
    "word_speed": 0.18,
    "frame_delay": 0.06,
    "intro_seconds": 1.2,
    "ending_seconds": 1.4
  },
  "audio": {
    "enabled": false,
    "volume": 0.8
  }
}
```

### 🖥️ Display Options

| Setting | Description |
| --- | --- |
| `theme` | Display theme name. Current project uses a neon-style terminal look. |
| `clear_screen` | Clears the terminal between animation frames. |
| `panel_width` | Width of the lyric display panel. |
| `alignment` | Lyric alignment. Use `left` or `center`. |
| `show_progress` | Shows or hides the playback progress bar. |

### 🎞️ Animation Options

| Setting | Description |
| --- | --- |
| `default_style` | Fallback animation style when a lyric line does not define one. |
| `typing_speed` | Delay between characters for typewriter animation. |
| `word_speed` | Delay between words for word-by-word animation. |
| `frame_delay` | Delay between frames for reveal/fade animations. |
| `intro_seconds` | Length of the intro/loading screen. |
| `ending_seconds` | Delay before the ending screen appears. |

### 🔊 Audio Options

| Setting | Description |
| --- | --- |
| `enabled` | Set to `true` to enable audio playback. |
| `volume` | Audio volume from `0.0` to `1.0`. |

---

## 🎨 Animation Styles

Use these names in song JSON files:

| Style | Aliases | Effect |
| --- | --- | --- |
| `typewriter` | Any unknown style falls back to this | Reveals text character by character |
| `word` | `word_by_word` | Reveals one word at a time |
| `center_reveal` | `center`, `reveal` | Expands text outward from the center |
| `fade` | `pulse` | Shows dim, bright, then colored text |
| `instant` | `none` | Displays the full lyric line immediately |

---

## 📝 Add Your Own Songs

Add song files to:

```text
songs/
```

PyLyrics automatically loads:

- `.json` files
- `.lrc` files

### 🎵 JSON Song Format

Create a file such as:

```text
songs/my_song.json
```

Example:

```json
{
  "title": "My Song",
  "artist": "My Artist",
  "audio": "audio/my_song.mp3",
  "lyrics": [
    {
      "time": "00:00.00",
      "text": "First lyric line",
      "duration": 2.5,
      "animation": "typewriter",
      "color": "bright_cyan"
    },
    {
      "time": "00:03.00",
      "text": "Second lyric line",
      "duration": 2.8,
      "animation": "word",
      "color": "bright_magenta"
    }
  ]
}
```

### 🧾 JSON Fields

| Field | Required | Description |
| --- | --- | --- |
| `title` | No | Song title. Defaults to the file name. |
| `artist` | No | Artist name. Defaults to `Unknown Artist`. |
| `audio` | No | Relative path to an audio file. Use `null` for timer-only playback. |
| `lyrics` | Yes | List of timed lyric lines. |
| `time` | Yes | Start time, such as `00:12.50`, `01:05.00`, or `12`. |
| `text` | Yes | Lyric text to display. |
| `duration` | No | Display duration in seconds. Defaults to `2.5`. |
| `animation` | No | Animation style. Defaults to `typewriter`. |
| `color` | No | Rich color name. Defaults to `bright_cyan`. |
| `typing_speed` | No | Per-line typewriter speed override. |

### ⏱️ Timestamp Examples

```text
12          # 12 seconds
00:12.50    # 12.5 seconds
01:02.500   # 1 minute, 2.5 seconds
```

### 🎼 LRC Song Format

You can also add `.lrc` files:

```lrc
[ti:My LRC Song]
[ar:My Artist]
[00:00.00]First lyric line
[00:03.00]Second lyric line
[00:06.50]Third lyric line
```

For LRC files, PyLyrics calculates each line duration from the next timestamp.

---

## 🔊 Enable Audio Playback

1. Put your audio file somewhere inside the project, for example:

```text
audio/my_song.mp3
```

2. Reference it from the song JSON:

```json
"audio": "audio/my_song.mp3"
```

3. Enable audio in `config/settings.json`:

```json
"audio": {
  "enabled": true,
  "volume": 0.8
}
```

When audio is unavailable, disabled, or the file path does not exist, PyLyrics automatically uses timer-based lyric sync.

---

## 🌈 Useful Rich Colors

Try these color names in song JSON files:

```text
bright_cyan
bright_magenta
bright_yellow
bright_white
cyan
green
white
yellow
red
blue
magenta
```

---

## 🇱🇰 Sinhala Text Tips

For the best Sinhala display:

- Use **Windows Terminal** or **VS Code Terminal**
- Set the terminal font to **Nirmala UI**, **Iskoola Pota**, or another Sinhala-capable font
- Use UTF-8 mode
- On Windows Command Prompt, run one of the included `.cmd` files

The launcher scripts already run:

```cmd
chcp 65001
set PYTHONUTF8=1
```

---

## 🧪 Run Tests

Run the unit tests with:

```powershell
python -m unittest
```

Current tests check timestamp parsing behavior in `src/timing_engine.py`.

---

## 🛠️ Troubleshooting

### Lyrics show, but audio does not play

- Make sure `audio.enabled` is `true`
- Check that the audio path exists
- Install pygame with `pip install pygame`
- Try a common audio format such as `.mp3` or `.wav`

### Sinhala text looks broken

- Use Windows Terminal or VS Code Terminal
- Choose a Sinhala-capable font
- Run `run_sinhala.cmd` or `run_singlish.cmd`

### Song does not appear in the library

- Make sure the file is inside `songs/`
- Use `.json` or `.lrc`
- Check that JSON syntax is valid
- Restart `python main.py`

### Animation feels too fast or slow

Edit:

```text
config/settings.json
```

Tune:

- `typing_speed`
- `word_speed`
- `frame_delay`
- individual lyric `duration`

---

## 📌 Example Commands

```powershell
# Open the full interactive app
python main.py

# Play first available song
python main.py --demo

# Run simple reel mode
python main.py --reel

# Run tests
python -m unittest
```

---

## ❤️ Notes

Use lyrics you wrote yourself or have permission to use. For copyrighted songs, keep your local files private unless you have the right to share them.

Have fun making your terminal sing. 🎶
