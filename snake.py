import random
import curses

s=curses.initscr()
curses.curs_set(0)
sh,sw =s.getmaxyx()
w=curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(1000)

snkx=sw/4
snky=sh/2
snake=[
    [snky,snkx],
    [snky,snkx-1],
    [snky,snkx-2]
    ]
food=[sh/2,sw/2]
w.addch(food[0],food[1],curses.ACS_PI)

