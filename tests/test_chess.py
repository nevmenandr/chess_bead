#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from unittest import TestCase
from chess_bead import Game
from chess_bead import Viz

class GameTestCase(TestCase):
    
    def test_verse_lines(self):
        
        g = Game()
        lines_length = len(g.lines)
        self.assertEqual(lines_length, 8)
        
    def test_attributes(self):
        
        g = Game(chess_game=21, poem_num=130)
        self.assertEqual(g.author, '王建')
        self.assertEqual(g.event, 'wcc')
        self.assertEqual(g.date, '1957.??.??')
        self.assertEqual(g.result, '1/2-1/2')
        
    def test_start_game(self):
        g = Game(chess_game=21, poem_num=130)
        l = g.start_game()
        self.assertEqual(l[13].hor1, 4)
        self.assertEqual(l[20].lines[3][4], '燒')

    def test_png(self):
        g = Game(chess_game=21, poem_num=130)
        l = g.start_game()
        v = Viz(l, g.author, g.title)
        v.png(l[3], 3)
        path = v.path
        t = os.path.exists(os.path.join(path, '0003.png'))
        self.assertEqual(t, True)
    
    def test_gif(self):
        g = Game(chess_game=21, poem_num=130)
        l = g.start_game()
        v = Viz(l, g.author, g.title)
        v.gif()
        gf = os.path.exists('game.gif')
        self.assertEqual(gf, True)
        
        