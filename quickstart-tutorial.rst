###################
Quickstart Tutorial
###################

This is a how to use / quickstart guide / tutorial to get you started with Pixel Art Studio, a Blender add-on.

**********************
What is Pixel Art Studio?
*************************

See the :doc:`features` page for more details.

**********************
Installation and setup
**********************

See the :doc:`installation` page for more details.

***************************************************
Setup viewport, pixel density, and canvas (texture)
***************************************************

.. _new-project-setup:

1. Setup for new projects (new blend file)
==================================

.. video:: _static/videos/quickstart/quickstart01-setup.mp4
  :width: 100%

1. To start using Pixel Art Studio with a new ``.blend`` file, delete the default cube and make sure you have no object selected.

    - If you already have a model or a blend file where you want to use Pixel Art Studio, keep following along in this section (and skip step 5), make sure you select your existing mesh. Then after done, see the next section :ref:`existing-project-setup`.

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

2. Setup for existing projects and models
================================

2.1. The model is not UV unwrapped and not textured
----------------------------------------------

.. video:: _static/videos/quickstart/quickstart-setup-1-no-uv-no-texture.mp4
  :width: 100%

1. Open the ``.blend`` file, select your mesh, and then follow the same steps listed above in :ref:`new-project-setup`.

    - Follow all the steps (except ``Add 1m Cube``) to setup the viewport, pixel density, and canvas.

2. After follow the steps and creating the canvas and the texture with ``Setup Pixel Art Canvas``, switch to ``Edit Mode``, select all vertices, and then click ``Pixel Art Unwrap``.
3. You can choose another density preset or manually type a new one in ``Texel Density``, and re-run ``Setup Pixel Art Canvas`` and ``Pixel Art Unwrap`` until you are happy with the result.

.. note::
    Pixel Art Studio ``Pixel Art Unwrap`` is basic, mostly aimed at rectangular and cube shapes, as all it does is a per-face planar projection with no island rotation and scaling, adds a texel island margin and then it automatically packs the UV islands.
    
    In most cases, it's recommended that you manually UV Unwrap meshes before texture painting them with Pixel Art Studio. See :ref:`<existing-uv-unwrapped-model>`.

.. _existing-uv-unwrapped-model:

2.2. The model is UV unwrapped and doesn't have a texture
----------------------------------------------

.. video:: _static/videos/quickstart/quickstart-setup-2-uv-no-texture.mp4
  :width: 100%

1. Open the ``.blend`` file, select your mesh, and then follow the same steps listed above in :ref:`new-project-setup`.

    - Follow all the steps (except ``Add 1m Cube``) to setup the viewport, pixel density, and canvas.

2. As soon as you finish setting up the canvas and the texture with ``Setup Pixel Art Canvas``, you are ready to paint.
3. If you are not satisfied with the pixel sizes laid on your UVs, you can change the density and re-run ``Setup Pixel Art Canvas``.

2.3. The model is UV unwrapped and has a texture
----------------------------------------------

1. Open the ``.blend`` file with the model that you want to texture paint with Pixel Art Studio.
2. The first step is detecting the texel density of your existing texture: does it have multiple sizes or a single pixel size?
3. ``Density Zones`` manages meshes with different texel densities per face (multiple pixel sizes in the same mesh). Expand ``Density Zones`` and click ``Detect Density Zones``.

2.3.1. The mesh has just one pixel size (single texel density)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. video:: _static/videos/quickstart/quickstart-setup-3-uv-texture-single-density.mp4
  :width: 100%

1. If just one zone was detected in Density Zones, you can click ``Clear Zones`` to remove it, close the ``Density Zones`` section.
2. Click ``Setup Viewport`` (it automatically detects texel density and sets up the viewport grid, where one grid unit is equal to one pixel size).
3. Click ``Make Canvas``, now Pixel Art Studio is going to work with your existing texture and you are ready to paint.

2.3.2. The mesh has multiple pixel sizes (multiple texel densities)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. video:: _static/videos/quickstart/quickstart-setup-4-uv-texture-many-densities.mp4
  :width: 100%

1. If more than one zone was detect in Density Zones, you are going to have to keep the zones, in order to keep the different pixel sizes. Pixel Art Studio is going to automatically resize and re-point Blender's grid as you hover the mesh's faces with the plugin tools, to keep one grid square at the size of one pixel for that specific face (you don't have to do anything else about it).
2. Click ``Setup Viewport``.
3. Click ``Make Canvas``, now Pixel Art Studio is going to work with your existing texture, with all the different pixel sizes of your mesh and you are ready to paint.
4. See :doc:`density-zones` to learn how to manage and create Density Zones.