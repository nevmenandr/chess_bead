
.. _Vis-chapter:

===========
class Vis
===========

You can visualize the game. No matter static or animated image you want, you must generate static PNG files first. Images could be black and white or colored. They are colored by default. You can't customize the colores. Red color encode the cell to, grey color encode the cell from.

Temp directory
----------------

You can generate PNG files in the specific folder or in a temp directoy. By default it is the temp directory.

.. code:: python

    import chess_bead as cb
    g = cb.Game()
    verses = g.start_game()
    v = cb.Viz(verses, g.author, g.title)

.. note::

    All moves and positions (``verses``), author's name (``g.author``) and poem's title (``g.title``) are required.

The path to the temp directory stored in a ``path`` attribute:

.. code:: python

    >>> v.path
    '/tmp/tmpx2uxfbkl'

This directory is not automatically deleted. It must be deleted by deleting the class instance.

.. code:: python

    >>> del v
    >>> v.path
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'v' is not defined
    >>> import os
    >>> os.path.exists('/tmp/tmpx2uxfbkl')
    False



PNG files
------------

You can specify:

**output_path**
  Location where PNG will be generated. Tmp directory by default.
**gif_path**
  Location of the output GIF file. Working directory by default.
**gif_filename**
  Filename of the GIF. ``game.gif`` by default.
**duration**
  Duration of the animation. ``2`` by default. Make sense only for animated images.
**color**
  Color coding of the move. Colored by default.

.. code:: python

    v = cb.Viz(l, g.author, g.title, output_path='.', gif_filename='chess_bead_game.gif')
    v.png(l[20], 20)

Last line generates the PNG image of the single 20th move.

Animation
------------


GIF
~~~~~~~~~~~~~~~~~~~~~~~~~

Very simple code for GIF animation:

.. code:: python
    
    v.gif()


MP4
~~~~~~~~~~~~~~~~~~~~~~~~~

There is no built-in tool for making mp4 from the png files. But you can use ffmpeg.

.. code:: python

    import os
    os.system("ffmpeg -r 2 -f image2 -s 600x800 -i {}/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ./output.mp4".format(v.path))
