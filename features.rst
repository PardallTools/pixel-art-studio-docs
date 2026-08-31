Features
=========================================

Pixel Art Studio is a Blender add-on (plugin) for **pixel perfect pixel art texture painting**. It supports drawing and painting **pixel art inside Blender**, in the 3D Viewport on top of the model (in Object and Edit modes) and in 2D in the Image Editor. It has tools for drawing and painting (including colors, palettes, layers, pressure sensitivity, bucket fill, gradients), selecting and moving pixels, and quickly setting up the model and the viewport for pixel art. The plugin also helps with setting up and managing multiple texture densities per mesh, allowing for **uniform pixel sizes across the whole mesh or per face pixel size variation**.

Not only it has tools with pixel line handling algorithms, it solves one of the biggest pain points when doing Pixel Art with Blender: pixel size stays consistent regardless of zoom level. One texel stays always one texel, which means always one pixel at the size of the texel defined by you in the whole mesh or per face.

.. video:: _static/videos/pixelartstudio-blender-features.mp4
  :width: 100%

.. _features-details:

Pixel Art Studio features in details
------------------------------------

Every drawing, selection and layer tool works in the **3D Viewport and in the Image Editor**, in **perspective and orthographic** views, so you can move the camera around freely while painting.

* **Drawing and painting tools**

  * All tools are directly inspired by `Aseprite <https://www.aseprite.org/>`_, so you are going to feel right at home.
  * All tools have **pixel perfect line handling** algorithms (with the brush and line tool, it removes the doubled L corners, with the ellipse, it creates pixel perfect circles and ellipses).  
  * **Brush** (:kbd:`B`): freehand painting as a ``Circle`` or ``Square`` brush, free size selection as well presets for ``1 2 3 4``, :kbd:`[` :kbd:`]` to increase/decrease the size on the viewport.
  * **Eraser** (:kbd:`E`): erases to transparent, with opacity control.
  * **Adjustable opacity, applied stroke-relative**: like `Aseprite <https://www.aseprite.org/>`_, dragging over the same texels twice inside one stroke applies the opacity **once**.
  * **Line** (:kbd:`L`): pixel perfect stair steps. :kbd:`Shift` snaps to 45 degrees.
  * **Rectangle** (:kbd:`U`) and **Ellipse** (:kbd:`O`): outlined (stamped with the current brush) or filled, :kbd:`Shift` constrains to a square or a circle (the preview is the final pixels).
  * **Path and Polygon** (:kbd:`C`): bezier tool with smoothed and hard corners, allowing to draw pixel art curves and polygons, including filled polygons (hold and drag the mouse to draw smooth, click and release to draw hard corners, :kbd:`Enter` to confirm the path).
  * **Bucket fill** (:kbd:`G`), two modes:

    * ``Fill by Pixels``: flood fill the active layer or the active selection with an adjustable **tolerance**. When ``Contiguous`` is off it is a global/selection color replace.
    * ``Mesh Faces``: fills the UV area of the selected faces (or every face if nothing is selected).

  * **Blur** (:kbd:`H`): box blur, pixel aware (it never makes sub-pixels).
  * **Gradient** (:kbd:`D`): two color gradient, ``Linear`` or ``Radial``, with **ordered dithering** (``Bayer 2x2``, ``4x4``, ``8x8``) or ``Smooth`` (fills selection or whole canvas).
  * **Eyedropper** (:kbd:`I`) and :kbd:`Alt+click`.
  * **Move** (:kbd:`V`): drags a layer or a selection around.
  
    * ``Auto Select Layer``: auto selects the layer at click position.

  * **Tablet pressure**: pressure toggles for ``Size`` and ``Opacity``.
  * **Pixel grid** overlay in the Image Editor and in 3D Viewport overlayed on top of the model (color and thickness configurable).
  * **Mirror and symmetry drawing**: ``Horizontal``, ``Vertical``, ``45`` and ``135`` (they can be combined for multi-axis symmetry).

* **Pixel selection**

  * **Marquee** (:kbd:`M`), **Ellipse** (:kbd:`Shift+M`), **Lasso** (:kbd:`Q`) and **Magic Wand** (settings: ``Tolerance`` and ``Contiguous``) (while a selection is active, tools affect only the selected pixels).

    * :kbd:`Shift` adds to selection, :kbd:`Alt` removes from selection (with any of the drag tools).

  * **Drag and move selections**: directly in the texture in the Image Editor and on the model in 3D, across the faces. :kbd:`Ctrl` while dragging duplicates the selection instead of moving it.
  * **Copy, cut and paste across layers** (:kbd:`Ctrl+C` / :kbd:`Ctrl+X` / :kbd:`Ctrl+V`).
  * **Selecting in 3D is per texel**: it uses a depth buffer, which causes selection to affect only the texels you are truly selecting.

* **Colors, swatches and palettes**

  * **Primary and secondary color**: :kbd:`X` to alternate between 2 colors and :kbd:`Shift+X` to walk swatches from your palette.
  * **Custom palettes** by adding swatches (add colors clicking the ``+`` and remove with :kbd:`Ctrl+click`) or by **importing PNG palettes** (for example, palettes from **Lospec**).
  * **Lospec palette library**: 500 palettes bundled with the add-on.

* **Layers and Groups**

  * **Layers** like in painting programs: add, remove, duplicate, move up and down, merge down and merge selected, lock, visibility, opacity.
  * **Groups**: group and ungroup layers, group opacity and visibility (affects all layers inside the group).

* **Pixel size and pixel density (texel density)**

  * **One-click pixel size setup**: this solves one of the biggest pain points of doing pixel art in Blender, it makes pixels uniform across the model or per face (see ``Density Zones`` below). 
  * **Density presets**: ``Low Density`` (chunky pixels), ``Medium Density`` (default), ``High Density``, ``Very High Density`` and ``Custom``.
  * ``Apply Texel Density``: scales the UVs of the selected objects so every texel is the same size, then snaps them to the texel grid.
  * ``Detect Texel Density``: detects the pixel size of the model.

    * **Auto pixel size detection for pre-existing textured models**

* **Viewport and scene setup**

  * ``Setup Viewport``: one click button to setup Blender's grid and snapping so that **one grid square is exactly one texel** at the current density / current pixel size.
  * ``Setup Pixel Art Canvas``: the wizard to create the texture, with a dimensions for the current texture density.
  * **Pixel Art workspace**: ``Image Editor`` on the left and the ``3D Viewport`` on the right. 

* **Pixel Art Unwrap**

  * Basic UV unwrap made for pixel art.

  .. note::
      Auto UV unwrapping is very basic. For the majority of models you are still going to need to manually unwrap the UVs, and then use Pixel Art Studio's density tools on top of your own layout.

* **Density Zones** (*optional, advanced*, multiple pixel sizes per model):

  * Assign and manage **texel density values per face**, for **uniform pixel size across the whole mesh or different pixel sizes per face** (a character's head drawn at twice the density of the legs, for example, which means smaller and more pixels for the head).
  * ``Detect Density Zones`` measures the model island by island and **clusters** them into zones automatically.
  * Build zones **from selected faces**, with custom names and densities.
  * ``Grid Follows the Face``: while you paint in the 3D Viewport, **Blender's grid is resized and re-pointed on the fly** at the density of the face under the cursor, **to keep one grid square at the size of one pixel for that specific face**.

* **Extras and Blender integration**

  * No external dependencies, it's made 100% in Python with Blender's APIs.
  * Undo history (you can undo and redo everything alongside Blender).
  * **Tools and settings popup**: press :kbd:`F` over either editor for a floating panel with the tools and their settings.
  * Painting on the model works in **Object and in Edit mode**, and you can alternate between Pixel Art Studio's tools and Blender's own tools on the fly.
  * The canvas is a normal Blender image: it's packed into the .blend, and it renders and exports like any other texture.
  * Customizable shortcuts and keymaps: see :doc:`shortcuts`.

.. note::
    Pixel Art Studio is compatible with **Blender 3.6, Blender 4.0+ through Blender 5.1**. But the **officially supported version is Blender 5.1**.
