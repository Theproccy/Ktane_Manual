"""A script to build all of the executables in one place."""

import PyInstaller.__main__

FILE_NAME_LIST = [["Keep_Typing_And_Nobody_Explodes.py", "--console", "--clean", "--onefile"],
                  ["Knobs.py", "--console", "--clean", "--onefile"],
                  [r"Symbols/Symbols_Labeler.py", "--windowed", "--clean", "--onefile"]]  # ,"--distpath .\dist\Symbols"

for i in range(len(FILE_NAME_LIST)):
    temp = FILE_NAME_LIST[i]
    print(temp)
    PyInstaller.__main__.run(temp)
