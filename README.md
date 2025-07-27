# quackdoor

Honk Honk!

Quackdoor is python code that will generate a duckyscript that will execute arbitrary python code on the target machine (macos). Best used to create payloads for flipper zero's BadUSB app.

Limitations & Considerations:
- Target system must have python3 installed
- All local python code must be in one file ([eggsecutor.py](https://github.com/mah5057/quackdoor/blob/main/quackdoor/eggsecutor/eggsecutor.py)) as when base64 encoding the eggsecutor, other local modules will not be compiled. External libraries are OK as they will be installed globally on the target system as part of the payload.
- Any credz in the eggsecutor will be recoverable on target system (hatch adds a directive to remove zsh history, but that's probably not enough)
- Assumes zsh on target shell
- Assumes standard macos filesystem conventions (e.g. - zsh history is saved at ~/.zsh_history, etc.)

Usage:
- `git clone git@github.com:mah5057/quackdoor.git`
- `cd quackdoor`
- Write your python payload at `quackdoor/eggsecutor/eggsecutor.py` (skip this step for hello world)
- `make hatch`
- The duckyscript to execute your eggsecutor code will now be in the `quackdoor/hatchery/` directory
- Upload the output duckyscript payload to flipper zero as a payload for the BadUSB app

⚠️ Disclaimer:
This software is provided under the MIT License and is intended for educational and authorized testing purposes only. The author is not responsible for any misuse, damage, or legal consequences resulting from the use of this code.

