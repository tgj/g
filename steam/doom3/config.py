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

DOOM3BFGBASE="%USERPROFILE%/Saved Games/id Software/DOOM 3 BFG/base"
AUTOEXEC="autoexec"
CFG=".cfg"
BFG="_bfg"
folder_path = filedialog.askdirectory(title="Choose Folder:", initialdir=DOOM3BFGBASE)

if folder_path:
    try:
        with open(Path(AUTOEXEC+BFG+CFG if "BFG" in folder_path else AUTOEXEC+CFG), "rb") as src, open( Path(folder_path + "/" + AUTOEXEC+CFG), "xb") as dst:
            shutil.copyfileobj(src, dst)
            logger.info("Successfully wrote " + AUTOEXEC+CFG + " to " + folder_path)
    except FileExistsError:
            logger.error(AUTOEXEC+CFG + " already exists at " + folder_path)