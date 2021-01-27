#!/bin/env python3

import curses
import pygame
from PIL import Image, ImageFilter
from texel.texelator import Texelator

FPS = 60
texplaySize = (80, 40)
displaySize = (500, 250)

texelator: Texelator = Texelator()


def main(stdscr):
    curses.initscr()
    stdscr.nodelay(1)

    FramePerSec: pygame.time.Clock = pygame.time.Clock()

    image: Image.Image = Image.open("idle.jpg")
    while True:
        # stdscr.clear()

        # Behavior
        ch = stdscr.getch()
        if ch == ord("q"):
            break
        elif ch == curses.KEY_RIGHT:
            image = Image.open("right.jpg")
        elif ch == curses.KEY_LEFT:
            image = Image.open("left.jpg")
        elif ch == curses.KEY_UP:
            image = Image.open("up.jpg")
        elif ch == curses.KEY_DOWN:
            image = Image.open("down.jpg")

        # Texelate pygame surface
        output = texelator.render(image.filter(
            ImageFilter.CONTOUR), texplaySize[0], texplaySize[1])
        stdscr.addstr(0, 0, output)

        stdscr.refresh()

        FramePerSec.tick(FPS)


curses.wrapper(main)
texelator.saveTileCache()

print("\n\n\n\n")
