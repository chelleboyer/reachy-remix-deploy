---
title: Reachy Mini Remix
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

# Reachy Mini Remix

**Motion builder for Reachy Mini robots**

A kid-friendly Gradio interface for building and executing dance sequences using the Reachy Mini SDK's recorded moves library. Perfect for learning choreography and creative expression!

## Features

### Easy Block Building
Tap move buttons to add them to your sequence. Each move is represented by a fun emoji that makes it easy to see what Reachy Mini will do!

### 18 Dance Moves
Access the Reachy Mini SDK dance library!

### Instant Playback
Watch Reachy Mini perform your choreography with smooth transitions. The app handles all motion execution through the SDK.

### Beautiful Themes
Choose from TTKBootstrap-inspired themes to customize your building experience.

## How to Use

1. **Start the Daemon** - Ensure `reachy-mini-daemon` is running on your robot
2. **Open Dashboard** - Navigate to `http://localhost:8000` (or your robot's IP)
3. **Launch App** - Click "Run" on the Reachy Mini Remix card
4. **Open UI** - Click the gear button to open the Gradio interface
5. **Build Your Dance** - Tap move buttons to add them to your sequence
6. **Hit Play!** - Press the play button and watch Reachy perform your creation
7. **Edit & Refine** - Use Undo to remove the last move, or Clear to start fresh

### Requirements

- Reachy Mini robot (hardware or simulation)
- Python 3.11+
- reachy-mini SDK 1.1.2+
- gradio 4.0.0+

## Contributing

Created by Michelle Boyer as part of the Reachy Mini App Suite.

## License

MIT License - See LICENSE file for details

## Links

- [Pollen Robotics](https://www.pollen-robotics.com/)
- [Reachy Mini Documentation](https://docs.pollen-robotics.com/)
- [Browse More Apps](https://huggingface.co/spaces/pollen-robotics/Reachy_Mini_Apps)
