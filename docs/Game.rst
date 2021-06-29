
.. _Game-chapter:

===========
class Game
===========

This is the main class in the package, it allows to generate permutations of the poem, loads the game from the PGN files and chooses the poem from a collection.


Text collection
----------------

Text collection inside the package contains around 7400 poems of Tang era. All the poems have 8 lines and 7 characters in each line. In addition to it the final character of the line is a punctuation mark. That gives us 8x8 matrix, which is similar to the classical chess board. The game is to consider that these are not hieroglyphs, but the cells of a chessboard. If a piece on the chessboard makes a move, the words of the Chinese poem move with it. After each move, we can again remember that this is not chess, but a text, and try to read and understand it.

The whole list of poems with the author names and the titles `is placed here <https://github.com/nevmenandr/chess_bead/blob/main/chess_bead/poems.json>`_ .


How to make it work
--------------------

.. code:: python

    import chess_bead as cb

You have several options for customizing the game. These options must be used when creating an instance of the class. 

The most simple variant is not to pass any parameters to the class:

.. code:: python

    g = cb.Game()
    
This will cause Python to choose a random poem from the collection and a random chess game. The package provides a small set of chess games in PGN format as an example. But you can find lots of games in this format yourself. Seriously, there are plenty of them (millions and millions). For example `on GitHub <https://github.com/rozim/ChessData>`_ .

Constructor parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

You can choose a particular poem and game from the collection if you know their numbers. Parameters `chess_game` and `poem_num` accept only integers.

.. code:: python

    g = cb.Game(chess_game=15, poem_num=2000)

As it was said before, you can use your own PGN file (don't mix with grafic format PNG). Then you must point to it in  the parameter:

.. code:: python

    g = cb.Game(pgn_file='/path/to/file.pgn')

You can combine these parameters:

.. code:: python

    g = cb.Game(pgn_file='/path/to/file.pgn', chess_game=15, poem_num=2000)

You can use your own chess game but not the Chinese text. These are the conditions of the game.

.. note::

    If you do not specify the number of the game and the poem, Python choose them randomly.


Let the game begin
-------------------

To start the permutations in the poem, you must call the method `start_game`. It has no parameters, but be attentive, you must define a variable to keep the result of the game:

.. code:: python

    verses = g.start_game()

The result is the list of objects. Each object contains the information about the previous move and the current position.

.. code:: python

    >>> verses = g.start_game()
    >>> verses[5]
    <chess_bead.Move object at 0x7f431fc35d60>
    >>> verses[5].lines
    [['一', '片', '非', '煙', '隔', '九', '吟', '，'], ['蓬', '巒', '仙', '仗', '儼', '雲', '細', '。'], ['天', '泉', '水', '暖', '龍', '枝', '旗', '，'], ['露', '畹', '春', '多', '鳳', '舞', '遲', '。'], ['榆', '莢', '桑', '海', '星', '斗', '轉', '，'], ['桂', '花', '尋', '去', '月', '輪', '變', '。'], ['人', '間', '散', '來', '朝', '朝', '移', '，'], ['莫', '遣', '佳', '期', '更', '後', '期', '。']]
    >>> verses[5].hor1
    6

Here you can see the object after the 5th move. This object has an attribute `lines`, which allows you to get an access to the position, and the coordinate attributes, e. g. `hor1` (horisontal coordinate on the board).

.. note::

    With a simple Python code you can make a plain text from it.
    
.. code:: python

    permutated =[]
    for line in l[5].verses:
        permutated.append(''.join(line))
    permutated_text = '\n'.join(permutated)
    print(permutated_text)

Main attributes
----------------

Using the attributes, we can access additional information about the poem and about the game.

author
  Author's of the poem name
title
  Poem's title
event
  Chess event where the game was played.
date
  Chess game's date.
white
  Who played white.
black
  Who played black.
result
  Who won.

.. code:: python

    >>> g.event
    'wcc'
    >>> g.date
    '1957.??.??'
    >>> g.white
    'Botvinnik M'


