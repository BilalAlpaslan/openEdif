import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("openedif/main.py", base=base)]

options = {
    "build_exe": {
        "packages": ["tkinter"],
        # "include_files": ["openedif/"],
        "path": sys.path + ["openedif/"]
    },
}

cx_Freeze.setup(
    name="Openedif",
    options=options,
    version="0.01",
    description="OPENEDIF ::Angular Velocity Calculator for Electronic Differential",
    executables=executables
)
