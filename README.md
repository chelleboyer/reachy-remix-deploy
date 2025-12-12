---
title: Reachy Remix
emoji: 🎵
colorFrom: purple
colorTo: blue
sdk: static
pinned: false
short_description: Build dance sequences with tap-to-add blocks!
tags:
 - reachy_mini
 - reachy_mini_python_app
 - dance
 - motion-builder
 - kids
---

# Reachy Remix

**Motion builder for Reachy Mini robots**

A kid-friendly Gradio interface for building and executing dance sequences using the Reachy Mini SDK's recorded moves library. Perfect for learning choreography and creative expression!

## Features

### Easy Block Building
Tap move buttons to add them to your sequence. Each move is represented by a fun emoji that makes it easy to see what Reachy will do!

### 20+ Dance Moves
Access the full Reachy Mini SDK dance library including:
- **yeah_nod** - Enthusiastic head nod
- **no_head** - Head shake
- **spin** - Full body rotation
- **happy_ears** - Antenna celebration
- **sad_head** - Drooping head
- And 15+ more moves from the SDK!

### Instant Playback
Watch Reachy Mini perform your choreography with smooth transitions. The app handles all motion execution through the SDK.

### Beautiful Themes
Choose from 26 TTKBootstrap-inspired themes to customize your building experience.

## How to Use

1. **Start the Daemon** - Ensure `reachy-mini-daemon` is running on your robot
2. **Open Dashboard** - Navigate to `http://localhost:8000` (or your robot's IP)
3. **Launch App** - Click "Run" on the Reachy Remix card
4. **Open UI** - Click the gear button to open the Gradio interface
5. **Build Your Dance** - Tap move buttons to add them to your sequence
6. **Hit Play!** - Press the play button and watch Reachy perform your creation
7. **Edit & Refine** - Use Undo to remove the last move, or Clear to start fresh

## Technical Details

- **Framework**: Gradio 6.0.2
- **Robot SDK**: reachy-mini 1.1.2
- **Architecture**: ReachyMiniApp with Gradio UI
- **Ports**: 
  - Dashboard: 8000
  - FastAPI Settings: 7900
  - Gradio UI: 7901
- **Deployment**: Editable pip install with virtual environment

## Installation

### Quick Start

```bash
cd reachy-remix-deploy

# Create virtual environment
python3 -m venv .venv

# Install package
.venv/bin/pip install -e .

# Start daemon (will auto-discover app)
.venv/bin/reachy-mini-daemon
```

The app will be available in the Reachy Mini Dashboard at `http://localhost:8000`.

### Package Structure

```
reachy-remix-deploy/
├── .venv/                    # Virtual environment
├── reachy_remix/            # Python package
│   ├── __init__.py          # Package exports
│   ├── app.py               # Main app with Gradio UI
│   └── static/              # Static files for settings server
│       └── index.html       # Redirects to Gradio UI
├── pyproject.toml           # Package configuration
└── README.md                # This file
```

### Requirements

- Reachy Mini robot (hardware or simulation)
- Python 3.11+
- reachy-mini SDK 1.1.2+
- gradio 4.0.0+

## Contributing

Created by the Reachy Dev Team as part of the Reachy Mini App Suite.

## License

MIT License - See LICENSE file for details

## Links

- [Pollen Robotics](https://www.pollen-robotics.com/)
- [Reachy Mini Documentation](https://docs.pollen-robotics.com/)
- [Browse More Apps](https://huggingface.co/spaces/pollen-robotics/Reachy_Mini_Apps)
