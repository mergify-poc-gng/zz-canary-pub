import os
import subprocess
import sys


def main():
    # taint source: process argv -> shell command sink
    user_cmd = sys.argv[1]
    subprocess.check_output(user_cmd, shell=True)

    # taint source: stdin -> eval sink
    expr = input("expr: ")
    print(eval(expr))

    # taint source: environment -> os.system sink
    target = os.environ["TARGET"]
    os.system("ping " + target)


if __name__ == "__main__":
    main()
