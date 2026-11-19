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
AUTOEXEC="autoexec"
CFG=".cfg"
BFG="_bfg"
folder_path = filedialog.askdirectory(title="Choose Folder:", initialdir=DOOM3BFGBASE)

if folder_path:
    autoexec_path = AUTOEXEC+BFG+CFG if "BFG" in folder_path else AUTOEXEC+CFG
    try:
        with open(Path(autoexec_path), "rb") as src, open( Path(folder_path + "/" + AUTOEXEC+CFG), "xb") as dst:
            shutil.copyfileobj(src, dst)
            logger.info("Successfully wrote " + AUTOEXEC+CFG + " to " + folder_path)
    except FileExistsError:
            logger.error(AUTOEXEC+CFG + " already exists at " + folder_path)