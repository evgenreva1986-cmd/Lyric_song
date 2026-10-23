# Lyric Song Synchronizer

A dynamic Python script designed to play an MP3 audio file while accurately synchronizing and scrolling the song lyrics inside the terminal or console.

## 🚀 Features

- **Audio Playback:** Smooth MP3 streaming directly from the console.
- **Dynamic Subtitles:** Time-aligned lyrics scrolling automatically in sync with the current timestamp of the song.
- **Configurable Assets:** Easily customizable by swapping the audio track or editing the external `lyrics.txt` file.

## 🎬 Preview

Here is how it works in action:

![Application Preview](preview.gif)

*(Note: If the GIF isn't loading, make sure to add your own `preview.gif` file to the root repository folder!)*

## 🛠️ Prerequisites & Installation

To run this script locally, make sure you have Python installed, along with the audio processing libraries used in the code.

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate to the directory:**
   ```bash
   cd Lyric_song
   ```
3. **Install dependencies:**  
   *(Depending on which audio framework you used in `Lyrics_song_test.py`, install the matching package, for example `pygame` or `playsound`)*:
   ```bash
   pip install pygame
   ```

## ⚙️ How to Run

Simply launch the main Python script from your terminal:

```bash
python Lyrics_song_test.py
```

## 📂 Project Assets

- `Lyrics_song_test.py` — The core logic managing playback clock cycles and console stdout updates.
- `falling down.mp3` — Default audio track.
- `lyrics.txt` — Timed script file containing the structured text lines.
