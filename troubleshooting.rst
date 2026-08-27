Troubleshooting
=========================================

When I paint with the brush or eraser, sometimes existing colors or pixels are not painted at the cursor's position
---------------------------------------

* This is probably because you are using the tool with ``Pixel Perfect`` mode enabled, which causes the brush to try to draw smoothed, pixel perfect lines and shapes. Disable it and try again.
* If you are painting on the 3D Viewport, it could also mean the texture density is not set up correctly or that the UVs are distorted.

When I paint or select, nothing happens
---------------------------------------

* Make sure you don't have an active selection somewhere. Press :kbd:`Alt+A` to deselect everything or click ``Deselect`` in the toolbar.

.. image:: _static/images/trouble-deselect.png

* Make sure you are not trying to paint on a locked or invisible layer.

.. image:: _static/images/trouble-layers.png

* Make sure the model and texture that you are trying to paint, are set up with a Pixel Art Studio canvas, click ``Make Canvas`` (if available) or ``Setup Pixel Art Canvas`` in the toolbar to do so.

.. image:: _static/images/trouble-makecanvas.png
