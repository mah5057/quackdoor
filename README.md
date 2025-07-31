# quackdoor

Honk Honk!

Quackdoor is python code that will generate a duckyscript that will execute arbitrary python code on the target machine (macos). Best used to create payloads for flipper zero's BadUSB app.

Limitations & Considerations:
- Target system must have python3 installed
- All local python code must be in one file ([eggsecutor.py](https://github.com/mah5057/quackdoor/blob/main/quackdoor/eggsecutor/eggsecutor.py)) as when base64 encoding the eggsecutor, other local modules will not be compiled. External libraries are OK as they will be installed globally on the target system as part of the payload.
- Any sensitive information written in the eggsecutor may be recoverable on the target system 
- Assumes zsh on target shell
- Assumes standard macos filesystem conventions

Usage:
1. `git clone git@github.com:mah5057/quackdoor.git`
2. `cd quackdoor`
3. Write your python payload at `quackdoor/eggsecutor/eggsecutor.py` (skip this step for hello world)
4. IF you are using external dependencies, list them by name [here](https://github.com/mah5057/quackdoor/blob/main/quackdoor/incubator/hatch.py#L18) and make sure that [PIP_TIME](https://github.com/mah5057/quackdoor/blob/main/quackdoor/incubator/hatch.py#L17) is long enough for `pip install` to finish.
5. `make hatch`
6. The duckyscript to execute your eggsecutor code will now be in the `quackdoor/hatchery/` directory
7. Upload the output duckyscript payload to flipper zero as a payload for the BadUSB app

⚠️ Disclaimer:
This software is provided under the MIT License and is intended for educational and authorized testing purposes only. The author is not responsible for any misuse, damage, or legal consequences resulting from the use of this code.

