####################################
How to Blockout Colors Quickly
####################################

================================================
Fill by Face Selection in Edit Mode
================================================

.. video:: _static/videos/pixelartstudio-fillfaces.mp4
  :width: 100%

If you want to block out colors quickly, filling big areas of the mesh with a single color, you can use the ``Bucket Fill`` tool with ``Fill by Faces``:

1. Select the ``Bucket Fill`` tool (:kbd:`G`)
2. Untoggle ``Fill by Pixels`` to fill by faces instead of pixels
3. Go to Edit Mode, select the faces you want to fill with a single color

    - Also make sure you are in the correct Pixel Art Studio layer or create a new one

4. Choose a color and fill the faces with a single click with the bucket tool!

================================================
Fill by using Pixel Selection
================================================

.. video:: _static/videos/pixelartstudio-fillselection.mp4
  :width: 100%

You can also fill areas of the mesh with a single color by using the pixel selection tools, using the ``Bucket Fill`` tool and then unchecking ``Contiguous`` and increase the ``Tolerance`` to fill more pixels at once:

1. Make selections with any of the selection tools

    - Hold :kbd:`Shift` to add to the selection

2. Select the ``Bucket Fill`` tool (:kbd:`G`)
3. Untoggle ``Contiguous`` to fill every matching pixel in the selection
4. Increase the ``Tolerance``, so it doesn't filter by the color underneath
5. Choose a color and fill the pixels with a single click with the bucket tool