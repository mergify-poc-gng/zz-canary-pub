import os
import subprocess


def run(cmd):
    return os.path.basename(cmd)


def unsafe_exec(user_input):
    # command injection: user input flows into a shell
    return subprocess.check_output(user_input, shell=True)


def unsafe_eval(user_input):
    # code injection: user input flows into eval
    return eval(user_input)
