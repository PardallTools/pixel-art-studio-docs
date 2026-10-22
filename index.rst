.. Pixel Art Studio Documentation documentation master file, created by
   sphinx-quickstart on Thu Jul  9 16:12:13 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pixel Art Studio Documentation
=========================================

Pixel Art Studio is a Blender add-on (plugin) for pixel perfect pixel art texture painting. It supports drawing and painting pixel art inside Blender, in the 3D Viewport on top of the model (in Object and Edit modes) and in 2D in the Image Editor. It has tools for drawing and painting (including colors, palettes, layers, pressure sensitivity, bucket fill, gradients), selecting and moving pixels, and quickly setting up the model and the viewport for pixel art. **A model that already has UVs and a texture is painted right away**, nothing to set up: click a tool and paint. For a model with no texture, **Quick Setup** shows the pixel sizes live on the model, then makes the texture at the size it needs. **Don't worry about UVs anymore**: one click unwraps the whole model for pixel art (texel density, pixel sizes and no stretched pixels), so you can close Blender's UV Editor and use just the 3D Viewport. Stack faces on the same pixels or join as a single UV island, **without ever moving or scaling a UV island by hand**. The plugin also helps with setting up and managing multiple texture densities per mesh, allowing for uniform pixel sizes across the whole mesh or per face pixel size variation.

And this is not a filter or composer to "PIXELATE" the scene or the model, this is **true pixel art drawing and texturing!**

Not only it has tools with pixel line handling algorithms, it solves one of the biggest pain points when doing Pixel Art with Blender: pixel size stays consistent regardless of zoom level. One texel stays always one texel, which means always one pixel at the size of the texel defined by you in the whole mesh or per face.

Summary of features:

- **Open your model and paint**: a model with UVs and a texture needs no setup, click a tool and paint. Models made of several objects on one texture paint as one.
- **Quick Setup**: see the pixel size on the model before choosing it, then make the texture, the material and the UVs in one click. ``Try Pixel Densities`` changes the pixel size of a model you already painted, keeping the painting.
- **Pixel perfect drawing and painting pixel art tools**: brush / pencil, eraser, line, rectangle, ellipse, bucket fill (by pixels, by selected faces, by color, with bleed), blur, scramble, gradient (with dithering options), opacity, eyedropper, text tool, path, bézier curve, filled polygons, shading, pixel spray, pressure sensitivity.

   - All tools have pixel perfect line handling algorithms.
   - Custom brushes.
   - **Fill and dither patterns** on every drawing tool (dithers, checker, lines, diagonals, grid, or your own pattern cut from a selection).
   - **Noise and Color Jitter**, for hand placed looking texture (grime, grass, rust, wood grain) that never shifts when you paint over it again.
   - **Shading tool**: lighten and darken what is already painted, with hue shifting or stepping along your own palette ramp.

- Pixel **selections**: rectangle, ellipse, lasso, magic wand, invert selection.

   - The selection tools work on the 2D and 3D viewports, and you can drag selected pixels across the faces of the model.
   - Selections can be made by topology, which selects and fills half-pixels (sub texels) in diagonals.
   - **Transform** (scale, rotate, skew) in 2D and on the model, with pixel art rotation algorithms that never invent new colors.

- 2D and 3D viewport **pixel grid overlay**.
- **Mirror and symmetry drawing** on the 2D and 3D viewports.
- **Tiled Mode** in the Image Editor, to paint seamless textures and see them repeat as you draw.
- **Color swatches and color palettes** (and a palette library with 500 predefined palettes).
- **Layers** and layer management with locking, grouping, merging, visibility toggling and blending modes similar to painting programs.

  - Non-destructible **adjustments** (brightness and contrast, color curves and HSL), stackable, per layer.
  - **Clipping layers and transparency masks** like Photoshop and Krita.
  - Export layers, groups or the whole texture as PNG and paste or import images as layers.
  - **Texture Dilation**: the colors of the art grown into the transparent texels around it, so no seam shows at the edges of the UV islands.

- One-click pixel size and **pixel density** setup with predefined presets, as well texel density detection for existing meshes (you can have chunky pixels and fine, detailed pixels).
- One-click setup buttons to **setup the viewport for pixel art** (grid size and snapping adjusted to the pixel size) and to UV unwrap the model for instant pixel art painting.
- **UV tools made for pixel art**: ``Pixel Art Unwrap`` and ``Quick Unwrap Model`` (the whole model, from any mode, in one click), with the same pixel size on every face, tilted or flat.

   - ``Stack UVs``: paint one face and see it on all of them (barrel staves, cylinder sides, crate planks).
   - ``Keep UVs Together (Join)``: curved parts stay one clean island. For organic models, join their faces and tweak the ``Unwrap Options`` if needed.
   - Several meshes on the same texture are unwrapped together, in one packed layout with no overlaps.

- **Density Zones** (*optional*): assign and manage texel density values per face, allowing for **uniform pixel size across the whole mesh or different pixel sizes per face**.

   - Different density zones **automatically resizes Blender's grid on the fly**, when you hover different faces of the model, in the 3D viewport.

- **Game engine integration** with **Godot, Unity and Unreal Engine**: paint in Blender, save, and the model shows up in the engine as pixel art (unlit, crisp pixels, no blur), with no export dialogs.

   - **Auto export** to GLB, glTF or FBX into any folder on every save, for any other engine or tool.
   - Every glTF export you make yourself comes out as unlit pixel art too.

- **Two shortcut modes**: alongside Blender's own shortcuts (default), or Pixel Art Studio's only while a tool is active (like Aseprite). Customizable shortcuts for EVERYTHING.

See :ref:`features-details` for detailed information about each feature.
 
.. video:: _static/videos/v2/pixel-art-studio-features.mp4
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
   :caption: Getting Started

   features
   installation
   quickstart-tutorial
   interface

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Tutorials

   tutorial-first-model
   tutorial-existing-model
   tutorial-uvs-without-the-uv-editor
   tutorial-multiple-pixel-sizes
   tutorial-how-to-blockout-colors
   tutorial-game-engines

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Manual

   setup-and-canvas
   quick-setup
   pixel-density
   uv-tools
   density-zones
   painting-tools
   brushes-and-patterns
   colors-and-palettes
   selection-and-transform
   layers
   symmetry-tiled-mode-and-grid
   game-engines
   preferences
   shortcuts

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Support

   faq
   troubleshooting
   support
   license
   about
