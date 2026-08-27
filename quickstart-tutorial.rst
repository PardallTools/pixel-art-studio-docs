Quickstart Tutorial
=========================================

This is a how to use / quickstart guide / tutorial to get you started with Pixel Art Studio, a Blender add-on.

What is Pixel Art Studio?
----------------------

See the :doc:`features` page for more details.

Installation and setup
----------------------

See the :doc:`installation` page for more details.

Setup viewport, pixel density, and canvas (texture)
---------------------------------------------------

Setup new project (new blend file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. video:: _static/videos/quickstart/quickstart01-setup.mp4
  :width: 100%

1. To start using Pixel Art Studio with a new ``.blend`` file, delete the default cube and make sure you have object selected.

    - If you already have a mesh or a blend file where you want to use Pixel Art Studio, see below :ref:`below <existing-project-setup>`, but the first steps are the same, so keep following along with this section.

2. Expand the sidebar with :kbd:`N` and click ``Pixel Art Studio``.
3. In ``Setup``, choose a Pixel Density Preset or "Custom". The pixel density determines the size of the pixels in the mesh. **Lower density: larger pixels, higher density: smaller pixels** (and thus more details, with the cost of requiring more texture space).
    
    - If you choose "Custom", expand the ``Pixel Density`` section, set the ``Texel Density`` value and press ``Apply Texel Density``.

4. Click ``Setup Viewport`` to match Blender's viewport grid and snapping with the pixel size from the density selected.

    - After clicking ``Setup Viewport``, one grid unit is equal to one pixel.
    - Shading is automatically set to ``Flat > Texture`` (not required, but recommended for pixel art).

5. Click ``Add 1m Cube`` to add a new cube that is one meter in size, adjusted to the grid and texel density: the smaller the density, less pixels fit per meter (the unit of measure for pixel density is ``px/m``).
6. Click ``Setup Pixel Art Canvas``, to create a new texture and automatically assign a material with the texture and no interpolation.

    - You can also check ``Pixel Grid Layer`` to create a new layer containing a generated color grid or a pixel checker texture, so you can visualize each pixel.
7. You are now ready to start painting! Change the view to ``Front Orthographic``, zoom in to see that each grid unit is equal to one pixel in the checker texture.

.. tip::

    If you want bigger or smaller pixels, you can choose another density preset and click ``Setup Pixel Art Canvas`` again or manually type a new ``Texel Density``, click ``Apply Texel Density`` and ``Setup Pixel Art Canvas`` again. Blender's grid follows automatically.

    If ``Setup Viewport`` turns red, click it again to fix the viewport (it does not touch your texture).


.. _existing-project-setup:

Setup existing project and mesh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open the ``.blend`` file with the model that you want to texture paint with Pixel Art Studio. It's recommended that's already UV unwrapped, with non-rotated, non-stretched, non-deformed UVs.

    - Your mesh does not need to have a material or a texture, you can create it from scratch in Pixel Art Studio, but if it's already textured and you want to edit it in Pixel Art Studio, you can also do that.

.. note::
    Pixel Art Studio has an ``Pixel Art Unwrap`` tool, but it's basic, mostly aimed at rectangular shapes.

TODO:
- Click arrow button to show in the image editor or in the 3d viewport