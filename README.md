# Clap-to-Rickroll

An automated audio-detection script for Linux that triggers a browser-based prank via microphone input.

## Features

* **Double Clap Detection**: Uses signal processing to identify sharp acoustic peaks.
* **Auto-Volume**: Forces system audio to 100% using ALSA.
* **Rickroll Loop**: Spawns multiple browser tabs with the legendary anthem.
* **Smart Filtering**: Analyzes sound sharpness to reduce false positives from background noise.

## Dependencies

**System (Fedora/Linux):**

```bash
sudo dnf install portaudio-devel alsa-lib-devel

```

**Python:**

```bash
pip install sounddevice numpy pyalsaaudio

```

## Setup

1. Run the script: `python index.py`
2. Perform two sharp claps within **0.15s - 0.8s**.
3. The system will maximize volume and open the YouTube links.

## Configuration

* `ST`: Adjust sharpness sensitivity (lower = more sensitive).
* `DELAY_M/F`: Set the required speed of your claps.
* `COOLDOWN`: Prevents a single loud noise from being counted twice.

---

*Created for fun and local testing.*
