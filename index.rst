.. Pixel Art Studio Documentation documentation master file, created by
   sphinx-quickstart on Thu Jul  9 16:12:13 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pixel Art Studio Documentation
=========================================

Pixel Art Studio is a Blender add-on for **pixel perfect pixel art texture painting**. It supports drawing and painting **pixel art inside Blender**, in the 3D Viewport on top of the model (in Object and Edit modes) and in 2D in the Image Editor. It has tools for drawing and painting (including colors, palettes, layers, pressure sensitivity, bucket fill, gradients), selecting and moving pixels, and quickly setting up the model and the viewport for pixel art. The plugin also helps with setting up and managing multiple texture densities per mesh, allowing for **uniform pixel sizes across the whole mesh or per face pixel size variation**.

Not only it has tools with pixel line handling algorithms, it solves one of the biggest pain points when doing Pixel Art with Blender: pixel size stays consistent regardless of zoom level. One texel stays always one texel, which means always one pixel at the size of the texel defined by you in the whole mesh or per face.

Summary of features:

- **Pixel perfect drawing and painting pixel art tools**: brush / pencil, eraser, path and polygon (bezier curve), line, rectangle, ellipse, bucket fill (by pixels, by selected faces, by color), blur, gradient (with dithering options), opacity, color picker, pressure sensitivity.

   - All tools have pixel perfect line handling algorithms.

- Pixel selection: rectangle, ellipse, lasso, magic wand, invert selection.

   - The selection tools work on the 2D and 3D viewports, and you can drag selected pixels across the faces of the model.

- 2D and 3D viewport **pixel grid overlay**.
- **Mirror and symmetry drawing** on the 2D and 3D viewports.
- **Color swatches and color palettes** (and a palette library with more than 500 predefined palettes).
- **Layers** and layer management with locking, grouping, merging and visibility toggling, similar to painting programs.
- One-click pixel size and **pixel density** setup with predefined presets, as well texel density detection for existing meshes (you can have chunky pixels and fine, detailed pixels).
- One-click setup buttons to **setup the viewport for pixel art** (grid size and snapping adjusted to the pixel size) and to UV unwrap the model for instant pixel art painting (*notice: auto UV unwrapping is very basic, for the majority of models you are still going to need to manually unwrap UVs*).
- **Density Zones** (*optional*): assign and manage texel density values per face, allowing for **uniform pixel size across the whole mesh or different pixel sizes per face**.

   - Different density zones **automatically resizes Blender's grid on the fly**, when you hover different faces of the model, in the 3D viewport.

See :ref:`features-details` for detailed information about each feature.
 
.. video:: _static/videos/pixelartstudio-blender-features.mp4
  :width: 100%

Where to get it
----------------

See the :doc:`installation` page.

How to use it
--------------

See the :doc:`quickstart-tutorial` page.

Need help?
----------

See the :doc:`support` page.

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Quickstart
   
   features
   installation

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Tutorials and Guides

   quickstart-tutorial

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Manual

   manual-coming-soon
   shortcuts
   density-zones

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Support
   
   faq
   troubleshooting
   support
   license
   about