.. Pixel Art Studio Documentation documentation master file, created by
   sphinx-quickstart on Thu Jul  9 16:12:13 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pixel Art Studio Documentation
=========================================

Pixel Art Studio is a Blender add-on for **pixel perfect pixel art texture painting**. It supports drawing and painting **pixel art inside Blender**, in the 3D Viewport on top of the model (in Object and Edit modes) and in 2D in the Image Editor. It has tools for drawing and painting (including colors, palettes, layers, pressure sensitivity, bucket fill, gradients), selecting and moving pixels, and quickly setting up the model and the viewport for pixel art. The plugin also helps with setting up and managing multiple texture densities per mesh, allowing for **uniform pixel sizes across the whole mesh or per face pixel size variation**.

Not only it has tools with pixel line handling algorithms, it solves one of the biggest pain points when doing Pixel Art with Blender: pixel size stays consistent regardless of zoom level. One texel stays always one texel, which means always one pixel at the size of the texel defined by you in the whole mesh or per face.

Summary of features:

- **Pixel perfect drawing and painting pixel art tools**: brush / pencil, eraser, line, rectangle, ellipse, bucket fill (by pixels, by selected faces, by color), blur, scramble, gradient (with dithering options), shading brush, spray can, text tool, path, bézier curve, filled polygons, opacity, color picker, pressure sensitivity.

   - All tools have pixel perfect line handling algorithms.
   - Custom brushes.
   - **Fill and dithering patterns** for all drawing tools (brush, shapes, eraser, bucket fill, etc), with custom patterns.
   - **Bleed (UV dilation)** for the brush, eraser, line, bucket fill and gradient.
   - Straight, 45 degrees and isometric angled lines.

- Pixel **selections**: rectangle, ellipse, lasso, magic wand, invert selection.

   - The selection tools work on the 2D and 3D viewports, and you can drag selected pixels across the faces of the model.
   - Selections can be made by topology, which selects and fills half-pixels (sub texels) in diagonals.
   - **Transform** layers and selections (scale, rotate, skew) and flip them horizontally and vertically.

- 2D and 3D viewport **pixel grid overlay**.
- **Tiled Mode** in the Image Editor, to paint seamless textures.
- **Mirror and symmetry drawing** on the 2D and 3D viewports.
- **Colors and palettes**: Blender's color wheel inside the panel, color swatches, color palettes (and a palette library with more than 500 predefined palettes), pick colors from any object and any area of the viewport.
- **Layers** and layer management with locking, grouping, merging, visibility toggling and blending modes similar to painting programs.

  - Non-destructible **adjustments** (brightness and contrast, color curves and HSL), stackable, per layer.
  - **Clipping layers and transparency masks** like Photoshop and Krita.
  - Export layers as PNG and paste or import images as layers.

- One-click pixel size and **pixel density** setup with predefined presets, as well texel density detection for existing meshes (you can have chunky pixels and fine, detailed pixels).
- One-click setup buttons to **setup the viewport for pixel art** (grid size and snapping adjusted to the pixel size).
- **UV tools made for pixel art**:

  - **Pixel Art Unwrap**: lays each face flat with its exact shape and pixel density, no stretched pixels. *Quick Unwrap Model* unwraps the whole model from any mode.
  - **Share UVs**: stack faces on the same UV spot, so they paint the same pixels (ex: paint the 8 sides of a cylinder only once).
  - **Keep Together (Join)**: neighbouring faces stay connected as one UV island (ex: a character's face, a vehicle's front).
  - Flip UV islands, keep pinned UVs, and lists to manage the shared and joined faces.

- **Density Zones** (*optional*): assign and manage texel density values per face, allowing for **uniform pixel size across the whole mesh or different pixel sizes per face**.

   - Different density zones **automatically resizes Blender's grid on the fly**, when you hover different faces of the model, in the 3D viewport.
   - Each zone has a pixel aspect (pixels taller than wide or the opposite, common in PS1 models), and Pixel Art Unwrap respects it.
   - Apply Density Zones to Faces while you are still creating the model, to test different pixel sizes.

- **Game engine integration** with **Godot, Unity and Unreal Engine**: models and textures are exported when you save in Blender, and the game project gets pixel art materials automatically.

   - Auto-export to glTF and FBX on save, into any folder.
   - Every glTF export out of Blender writes the texture as unlit pixel art.

- Customizable shortcuts for EVERYTHING.

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
   tutorial-how-to-blockout-colors

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