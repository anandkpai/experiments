# Whisper Dialogue Toolkit (Local)

This toolkit lets you transcribe an MP3 locally using **faster-whisper** and produce a clean, **dialogue-style transcript** labeled by order:

```
Anand: ...
Anindya: ...
```

It will also generate a **Word (.docx)** file with the same dialogue.

## 1) Install prerequisites

### Windows (recommended via Conda)
1. Install Miniconda if you don't already have it.
2. Open **Anaconda Prompt (Miniconda3)** and create an env:

```bash
conda create -n whisper python=3.10 -y
conda activate whisper
pip install -r requirements.txt
```

> If you have an NVIDIA GPU and CUDA drivers installed, `faster-whisper` will use it automatically. Otherwise it falls back to CPU (slower).

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

> You may also need FFmpeg for MP3 loading:
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt-get update && sudo apt-get install ffmpeg`

## 2) Run the script

Basic usage:

```bash
python transcript_whisper_local.py   --audio "PATH/TO/abcl 27 aug.mp3"   --out_dir "out"   --model medium   --device auto   --gap_threshold 1.2   --chunk_minutes 10   --speaker1 "Anand"   --speaker2 "Anindya"
```

Key options:
- `--model` : `small`, `medium`, or `large-v3` (accuracy↑ => speed↓)
- `--device`: `auto` (GPU if available), `cuda`, or `cpu`
- `--gap_threshold`: seconds of silence to start a **new turn**
- `--chunk_minutes`: split long audio into N-minute chunks for stability
- `--speaker1`, `--speaker2`: names to label by **order of turns**

Outputs (in `--out_dir`):
- `dialogue.txt` : final dialogue transcript
- `dialogue.docx` : Word version
- `chunks/` : per-chunk raw segment text (for incremental review)

## 3) Tips

- If you want **immediate incremental output**, open a second terminal and run `tail -f out/chunks/chunk_*.txt` as the script progresses.
- If you're on CPU, prefer models `small` or `medium`. For best accuracy, use `large-v3` (requires more VRAM/CPU).

## 4) Example (Windows PowerShell)

```powershell
# Adjust the path to your MP3
.un_example.ps1 -AudioPath "C:\Users\you\Downloads\abcl 27 aug.mp3"
```

This will write results into `out\` beside the script.

---

**Speaker labeling logic (by order):**
- The first detected **turn** is labeled **Anand**.
- The second turn is labeled **Anindya**.
- Then it **alternates** for each subsequent turn.
- A "turn" is a consecutive run of whisper segments separated by less than `--gap_threshold` seconds of silence.

You can tweak the silence gap with `--gap_threshold`. For more granular turns, decrease it (e.g., `0.8`). For longer monologues, increase it (e.g., `1.8`).