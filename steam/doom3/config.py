import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil
import logging

root = tk.Tk()
root.withdraw()

logging.basicConfig(
     level=logging.INFO,
     format="[%(levelname)s] %(asctime)s - %(message)s",
     datefmt="%H:%M:%S"
)

logger = logging.getLogger(__name__)

DOOM3BFGBASE="C:/Program Files (x86)/Steam/steamapps/common/DOOM 3 BFG Edition/base/"
AUTOEXECCFG="autoexec.cfg"
folder_path = filedialog.askdirectory(title="Choose Folder:", initialdir=DOOM3BFGBASE)

if folder_path:
    try:
        with open(Path(AUTOEXECCFG), "rb") as src, open( Path(folder_path + "/" + AUTOEXECCFG), "xb") as dst:
            shutil.copyfileobj(src, dst)
            logger.info("Successfully wrote " + AUTOEXECCFG + " to " + folder_path)
    except FileExistsError:
            logger.error(AUTOEXECCFG + " already exists at " + folder_path)