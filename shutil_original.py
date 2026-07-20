import shutil
import os

home = os.path.expanduser("~")
shutil.copy(
    os.path.join(home,"test.txt"),
    os.path.join(home, "01.python","testop.txt"),
)
