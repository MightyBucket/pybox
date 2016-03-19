#!/usr/bin/env python3

import tkinter as tk
import plexer as pl
from Aria import AriaIO
from tkinter.font import Font
## required:
root = tk.Tk()

def key(event):
    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
        loopAndParse()
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    root.wm_title(msg)

def loopAndParse():
    pl.parseIntoTokens(AriaIO(root).getFull())
    for i in range(0,len(pl.tokens[0])):
        if pl.tokens[3][i] == "STRING":
            print("coloring")
            AriaIO(root).colorize(pl.tokens[1][i],pl.tokens[2][i])

def zeb_demo():
    AriaIO(root).pack(expand=1, fill="both")
    root.bind_all('<Key>', key)
    root.mainloop()

if __name__ == "__main__":
    zeb_demo()