import sys
from nubia import Nubia, Options
import commands

if __name__ == "__main__":
    shell = Nubia(
        name="nubia_example",
        command_pkgs=commands,
        options=Options(persistent_history=False),
    )
    sys.exit(shell.run())
