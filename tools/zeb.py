
### CREATED BY DARYL CECILE > GITHUB: DARCECTECH
## YOU MAY USE AND AMMEND THE CODE AS LONG AS IT IS MADE EXPLICIT IN NEW ITERATIONS
## IF YOU HAVE ANY SUGGESTIONS, PLEASE LET ME KNOW.
## I AM PLANNING TO CHANGE THE LICENSE TO MIT-LICENSE FOR THIS PROJECT ONCE IT IS COMPLETE

import tkinter as tk
import plexer as pl
from Blitz import BlitzIO
from tkinter.font import Font
## required:
root = tk.Tk()

def zeb_demo():
    sht = BlitzIO(root).pack()
    root.mainloop()

if __name__ == "__main__":
    zeb_demo()