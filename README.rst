|License| |Docs| |Contact| |Site|

Chess Bead Game
=================

Description
----------------

Package for the both chess and Chinese poetry game. The rules of the game involve chess moves from games in pgn format. The board for the game is a Chinese poem of the Tang era, in which the line is equal to 7 characters (the last, 8th vertical is most often punctuation marks). When a piece makes a move, the characters on the board change places. The character on which the piece was is moved to the place of the character to which the move was made.


.. figure:: https://github.com/nevmenandr/chess_bead/raw/main/example/game21_poem130.gif
    :scale: 40 %
    :align: center
    :alt: How the game works.
    


You can get the result texts and visualize it with the package.

You can use custom game in PGN format. 

Inspired by Das Glasperlenspiel by Hermann Hesse.


Quick start
----------------

.. code:: python

    import chess_bead as cb
    
    g = cb.Game()                       # use random chess game from the example PGN 
                                        # file included in the package
    verses = g.start_game()             # get all the permutations in the poem
    v = cb.Viz(verses, g.author, g.title)    # prepare visualization
    v.gif()                             # make the GIF animation with the name 
                                        #'game.gif' in the working directory
    del v                               # clean up the tmp dir


Installation
----------------

The tool could be installed with pip

::

    pip3 install chess_bead

Examples and Docs
-------------------

You can explore the `brief examples <https://github.com/nevmenandr/chess_bead/blob/main/example/Example.ipynb>`_  that could give you a clue. For the deep sinking read the `documentation <https://chess-bead.readthedocs.io/en/latest/>`_.


External resources
----------------------
 
* The poems are taken from the collection `selected from this repository <https://github.com/snowtraces/poetry-source>`_.
* The package uses cwTeXFangSong font licensed with SIL Open Font License (Version 1.1), `see here <https://github.com/l10n-tw/cwtex-q-fonts>`_ .
* `Compiled TTFs <https://github.com/l10n-tw/cwtex-q-fonts-TTFs>`_ .


.. |License| image:: https://img.shields.io/badge/license-GPL-blue.svg
    :target:  https://opensource.org/licenses/GPL-3.0
.. |Docs| image:: https://readthedocs.org/projects/numeral-system-py/badge/?version=latest&style=flat
    :target:  https://chess-bead.readthedocs.io/en/latest/
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
    :target:  https://t.me/nevmenandr
.. |Site| image:: https://img.shields.io/badge/site-nevmenandr-yellowgreen.svg
    :target:  http://nevmenandr.net/bo.php


