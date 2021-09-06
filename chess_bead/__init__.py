#!/usr/bin/env python3

"""
Package for the both Chinese poetry and chess game. The rules of the game
involve chess moves from games in pgn format. The board for the game is
a Chinese poem of the Tang era, in which the line is equal to 7 characters
(the last, 8th vertical is most often punctuation marks). When a piece
makes a move, the characters on the board change places. The character
on which the piece stood is moved to the place of the character to which
the move was made.

"""

__version__ = "1.0.2"

import copy
import json
import os
import random
import shutil
import tempfile

import chess.pgn
import imageio  # type: ignore
from PIL import Image, ImageDraw, ImageFont  # type: ignore


BASE_DIR = os.path.dirname(__file__)
POEMS_FILE = os.path.join(BASE_DIR, "poems.json")
VERT = {chr(x): x - 97 for x in range(97, 105)}
HORIS = {str(x): 8 - x for x in range(1, 9)}
COLOR = {"red": (255, 0, 0), "bl": (0, 0, 0), "gr": (192, 192, 192)}
POS = (35, 45)


def num_format(num):
    """
    The function formatting the number in the filename
    """
    num = str(num)
    lnum = len(num)
    return "{}{}".format("0" * (4 - lnum), num)


def title_format(title):
    """
    The method formatting the title
    """
    if len(title) > 15:
        string = "{}...".format(title[:15])
    else:
        string = title
    return string


def d_text(canv, hor, vert, cell, fnt, color):
    """
    The method writes a character on the canv
    """
    pos = (15 + (vert * 73), (hor + 1) * 85)
    canv.text(pos, cell, font=fnt, fill=COLOR[color])
    return canv


class Move:
    """
    Data type of the move in the game. It keeps the "board" and the
    cells of the move
    """

    def __init__(self, lines, hor1, vert1, hor2, vert2):
        self.lines = lines
        self.hor1 = hor1
        self.vert1 = vert1
        self.hor2 = hor2
        self.vert2 = vert2


class Game:
    """
    Main class that forms all the states of the "board". You can set
    the poem number from the collection, location of the PGN file and
    the number of the game in the PGN file.
    """

    def __init__(self, poem_num=None, pgn_file=None, chess_game=None):

        with open(POEMS_FILE, encoding="utf-8") as f_j:
            self.poems = json.load(f_j)

        self.poem_num = poem_num
        self.pgn_file = pgn_file
        self.chess_game = chess_game

        if not self.poem_num:
            self.poem = self.poems[random.randint(0, len(self.poems))]
        else:
            self.poem = self.poems[self.poem_num]

        self.load_game()

        self.author = self.poem["author"]
        self.title = self.poem["title"]
        self.lines = []
        for line in self.poem["lines"]:
            self.lines.append(list(line))

    def load_game(self):
        """
        The method loads the game from PGN file. By default it uses
        the file example.pgn
        """
        if not self.pgn_file:
            self.pgn_file = os.path.join(BASE_DIR, "example.pgn")
        with open(self.pgn_file) as f_p:
            game_iter = True
            games = []
            while game_iter:
                game_iter = chess.pgn.read_game(f_p)
                games.append(game_iter)
        if not self.chess_game:
            self.game = random.choice(games)
        else:
            self.game = games[self.chess_game]

        self.event = self.game.headers["Event"]
        self.date = self.game.headers["Date"]
        self.white = self.game.headers["White"]
        self.black = self.game.headers["Black"]
        self.result = self.game.headers["Result"]

    def start_game(self):
        """
        The method generates all the permutations in the poem
        """
        new_lines = copy.deepcopy(self.lines)
        board = Move(new_lines, 8, 8, 8, 8)
        steps = [board]
        for move in self.game.mainline_moves():
            move_s = str(move)
            hm1 = HORIS[move_s[1]]
            vm1 = VERT[move_s[0]]
            hm2 = HORIS[move_s[3]]
            vm2 = VERT[move_s[2]]
            self.lines[hm1][vm1], self.lines[hm2][vm2] = (
                self.lines[hm2][vm2],
                self.lines[hm1][vm1],
            )
            new_lines = copy.deepcopy(self.lines)
            board = Move(new_lines, hm1, vm1, hm2, vm2)
            steps.append(board)
        return steps


class Viz:
    """
    Visualization class, you can create a series of the separate PNG files
    one-by-move and the animated GIF file of rhe whole game. You can set
    an output paths, the duration of the animation and the color coding
    of a move. You have to call del methode for clean up the tmp dir.
    """

    def __init__(
        self,
        steps,
        author,
        title,
        output_path=None,
        gif_path=None,
        gif_filename=None,
        duration=2,
        color=True,
    ):
        self.steps = steps
        self.author = author
        self.title = title
        self.output_path = output_path
        self.duration = duration
        self.font_file = os.path.join(BASE_DIR, "cwfs.ttf")
        self.color = color
        if not self.output_path:
            self.path = tempfile.mkdtemp()  # TemporaryDirectory().name
        else:
            self.path = output_path
        if not gif_path:
            self.gif_path = "."
        else:
            self.gif_path = gif_path
        if not gif_filename:
            self.gif_filename = "game.gif"
        else:
            self.gif_filename = gif_filename

    def png_output(self, step, num):
        """
        The main method for generating PNG file one by one move
        """
        b_c = COLOR["bl"]
        img = Image.new("RGB", (600, 800), color=(255, 255, 255))
        canv = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(self.font_file, 30)
        canv.text(POS, self.author, font=fnt, fill=b_c)
        canv.text(POS, title_format(self.title), font=fnt, fill=b_c)
        fnt = ImageFont.truetype(self.font_file, 80)
        for i, line in enumerate(step.lines):
            for i_i, cell in enumerate(line):
                if self.color:
                    if (i, i_i) == (step.hor1, step.vert1):
                        canv = d_text(canv, i, i_i, cell, fnt, "gr")
                    elif (i, i_i) == (step.hor2, step.vert2):
                        canv = d_text(canv, i, i_i, cell, fnt, "red")
                    else:
                        canv = d_text(canv, i, i_i, cell, fnt, "bl")
                else:
                    canv = d_text(canv, i, i_i, cell, fnt, "bl")
        img.save(os.path.join(self.path, "{}.png".format(num)))

    def png(self, step, num):
        """
        wrap for the png_output method
        """
        self.png_output(step, num_format(num))

    def gif(self):
        """
        This method is for generating gif files. It also call the PNG
        files generation
        """

        for num, step in enumerate(self.steps):
            self.png(step, num)
        images = []
        for filename in sorted(os.listdir(self.path)):
            if not filename.endswith(".png"):
                continue
            images.append(imageio.imread(os.path.join(self.path, filename)))
        imageio.mimsave(
            os.path.join(self.gif_path, self.gif_filename),
            images,
            format="GIF",
            duration=self.duration,
        )

    def __del__(self):
        if not self.output_path:
            shutil.rmtree(self.path)
