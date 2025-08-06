import argparse
from quackdoor.payload import read_payload
from quackdoor.encoder import encode_payload, build_python_exec_command
from quackdoor.builder import build_ducky_script


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate DuckyScript payload from Python"
    )
    parser.add_argument("input", help="Path to the python script to inject")
    parser.add_argument("-o", "--output", default="payload.txt", help="Output file")
    parser.add_argument("-p", "--pip-time", default="")
    parser.add_argument(
        "-r",
        "--requirements",
        nargs="*",
        default=[],
        help="Time to wait for pip if using dependencies",
    )
    args = parser.parse_args()

    raw = read_payload(args.input)
    encoded = encode_payload(raw)
    exec_cmd = build_python_exec_command(encoded)
    ducky_script = build_ducky_script(
        exec_cmd, pip_time=args.pip_time, requirements=args.requirements
    )

    with open(args.output, "w") as f:
        f.write(ducky_script)

    print(f"[+] DuckyScript written to {args.output}")


if __name__ == "__main__":
    main()
