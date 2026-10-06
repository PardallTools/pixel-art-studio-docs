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

    * Hold :kbd:`Ctrl+Shift` and click to draw a straight line from the last stroke (draw connecting lines and polygons). Hold :kbd:`Ctrl+Shift+Alt` for angled lines (straight, 45 degrees and isometric).
    * ``Pixel Perfect`` (:kbd:`P`) is turned off for brushes bigger than 12px, where it makes no difference.

  * **Custom brushes**: made in the Image Editor from a selection, saved in the .blend file, marked as asset (to share in the Asset Browser) or saved in the add-on preferences (to use in all .blend files).
  * **Eraser** (:kbd:`E`): erases to transparent, with opacity control. It has the brush's line shortcuts (:kbd:`Ctrl+Shift` and :kbd:`Ctrl+Shift+Alt`) and its own Bleed setting.
  * **Adjustable opacity, applied stroke-relative**: like `Aseprite <https://www.aseprite.org/>`_, dragging over the same texels twice inside one stroke applies the opacity **once**.
  * **Line** (:kbd:`L`): pixel perfect stair steps. :kbd:`Shift` snaps the angle: straight, 45 degrees, and the 2:1 / 1:2 isometric angles.
  * **Rectangle** (:kbd:`U`) and **Ellipse** (:kbd:`O`): outlined (stamped with the current brush) or filled, :kbd:`Shift` constrains to a square or a circle (the preview is the final pixels). Fill with the primary color, or with the secondary color plus an outline in the primary color.
  * **Path and Polygon** (:kbd:`C`): bezier tool with smoothed and hard corners, allowing to draw pixel art curves and polygons, including filled polygons (hold and drag the mouse to draw smooth, click and release to draw hard corners, :kbd:`Enter` to confirm the path).
  * **Bucket fill** (:kbd:`G`), two modes:

    * ``Fill by Pixels``: flood fill the active layer or the active selection with an adjustable **tolerance**. When ``Contiguous`` is off it is a global/selection color replace. It also fills enclosed shapes split across many UV islands (ex: a shape drawn on a cylinder cap made of triangles).
    * ``Fill by Selected Faces``: fills the whole UV area of the selected faces, including half pixels (or every face if nothing is selected).
    * :kbd:`Ctrl+G` toggles between the two modes.

  * **Blur** (:kbd:`H`): box blur, pixel aware (it never makes sub-pixels). The ``Scramble`` mode shifts pixels around instead of changing their colors.
  * **Gradient** (:kbd:`D`): two color gradient, ``Linear`` or ``Radial``, with **ordered dithering** (``Bayer 2x2``, ``4x4``, ``8x8``) or ``Smooth`` (fills selection or whole canvas). Hold :kbd:`Shift` for straight gradients, in steps of 45 degrees.
  * **Shading** (:kbd:`S`): lightens or darkens the pixels you paint over, with simple shading, hue shifting or walking along a color ramp. Hold :kbd:`Ctrl` to swap lighten and darken for one stroke.
  * **Spray Can** (:kbd:`Shift+B`): sprays pixels around the cursor. ``Spray Width`` sets the spray area and ``Spray Speed`` how many dots it sprays while you move. Each dot is stamped with the current brush.
  * **Text** (:kbd:`T`): types text with pixel fonts (9 fonts included), bold, italic and outline.
  * **Bleed (UV dilation)**: the brush, eraser, line, bucket fill and gradient can paint past the edges of the UV islands, so no gaps show on the model. ``0.5`` paints the half covered pixels along a UV edge, ``1`` and ``2`` paint whole rings of pixels around the islands.
  * **Fill and dithering patterns** for all drawing tools (brush, shapes, eraser, bucket fill, etc), inspired by Graphics Gale. Fill a pattern with 2 colors, or with the primary color plus transparency. Save your own patterns in the add-on preferences (to use in all .blend files) or as assets.
  * **Brushes and Patterns** section: galleries to pick the brush shape and the pattern.
  * **Eyedropper** (:kbd:`I`), hold :kbd:`Alt` and click with any tool, or **Eyedropper on Hover** (:kbd:`Alt+Shift+X`, no click needed). It picks colors from any object and from any area of the viewport, and shows the color being picked next to the cursor.
  * **Move** (:kbd:`V`): drags a layer or a selection around.
  
    * ``Auto Select Layer``: auto selects the layer at click position.

  * **Tablet pressure**: pressure toggles for ``Size`` and ``Opacity``.
  * **Tool cursor**: the active tool's icon is shown at the mouse position, so you know which tool is active without looking at the toolbar.
  * **Pixel grid** overlay in the Image Editor and in 3D Viewport overlayed on top of the model (color and thickness configurable).
  * **Tiled Mode** (Image Editor): shows the texture repeated around itself, and what you paint past an edge comes back at the opposite edge. Use it to paint seamless textures. Repeat on both axes, only X or only Y.
  * **Mirror and symmetry drawing**: ``Horizontal``, ``Vertical``, ``45`` and ``135`` (they can be combined for multi-axis symmetry). In the 3D Viewport the symmetry has 4 modes: aligned with the view, aligned with the object, aligned with the view at the 3D cursor, and aligned with the object at the 3D cursor. Brushes, bucket fill, gradients and selections are mirrored.

* **Pixel selection**

  * **Marquee** (:kbd:`M`), **Ellipse** (:kbd:`Shift+M`), **Lasso** (:kbd:`K`) and **Magic Wand** (:kbd:`W`, settings: ``Tolerance`` and ``Contiguous``) (while a selection is active, tools affect only the selected pixels).

    * :kbd:`Shift` adds to selection, :kbd:`Alt` removes from selection (with any of the drag tools). The cursor shows ``+`` or ``-``.
    * :kbd:`Ctrl+A` selects all, :kbd:`Alt+A` deselects, :kbd:`Ctrl+I` inverts.
    * **Select by Topology** (:kbd:`Ctrl+Shift+T`, 3D Viewport only): selects the whole shape of the faces, including the half pixels along diagonal UV edges, so you can paint and fill them.

  * **Drag and move selections**: directly in the texture in the Image Editor and on the model in 3D, across the faces. :kbd:`Ctrl` while dragging duplicates the selection instead of moving it.
  * **Transform** (:kbd:`Ctrl+T`): scale, rotate and skew a selection or a whole layer, in the Image Editor and on the model in 3D. :kbd:`Enter` confirms, :kbd:`Esc` cancels.
  * **Flip** selections horizontally (:kbd:`Shift+H`) and vertically (:kbd:`Shift+V`).
  * **Copy, cut and paste across layers** (:kbd:`Ctrl+C` / :kbd:`Ctrl+X` / :kbd:`Ctrl+V`), and paste as a new layer (:kbd:`Ctrl+Shift+V`).
  * **Selecting in 3D is per texel**: it uses a depth buffer, which causes selection to affect only the texels you are truly selecting.

* **Colors, swatches and palettes**

  * **Colors and Palettes** section with Blender's color wheel inside the panel (it follows Blender's ``Color Picker Type`` preference). Hide the wheel in the add-on preferences.
  * **Primary and secondary color**: :kbd:`X` (or the swap button) to alternate between 2 colors and :kbd:`Alt+X` to walk swatches from your palette.
  * **Custom palettes** by adding swatches (add colors clicking the ``+`` and remove with :kbd:`Ctrl+click`) or by **importing PNG palettes** (for example, palettes from **Lospec**).
  * **Lospec palette library**: 500 palettes bundled with the add-on.

* **Layers and Groups**

  * **Layers** like in painting programs: add, remove, duplicate, move up and down, merge down and merge selected, lock, visibility, opacity.
  * **Groups**: group and ungroup layers, group opacity and visibility (affects all layers inside the group).
  * **Blending modes**: the 19 blending modes from Aseprite, for layers and groups.
  * **Adjustments** (non-destructive, stackable, per layer or group): brightness and contrast, hue and saturation, color curves.
  * **Layer masks and clipping masks**, like Photoshop and Krita.
  * **Import PNG as layer**, **export layer as PNG**, and **paste an image** copied from another program as a new layer.
  * Shortcuts for layer and group operations, like Photoshop.

* **Pixel size and pixel density (texel density)**

  * **One-click pixel size setup**: this solves one of the biggest pain points of doing pixel art in Blender, it makes pixels uniform across the model or per face (see ``Density Zones`` below). 
  * **Density presets**: ``Low Density`` (chunky pixels), ``Medium Density`` (default), ``High Density``, ``Very High Density`` and ``Custom``. Save your own presets.
  * ``Apply Texel Density``: scales the UVs of the selected objects so every texel is the same size, then snaps them to the texel grid.
  * ``Detect Texel Density``: detects the pixel size of the model.

    * **Auto pixel size detection for pre-existing textured models**

* **Viewport and scene setup**

  * ``Setup Viewport``: one click button to setup Blender's grid and snapping so that **one grid square is exactly one texel** at the current density / current pixel size.
  * ``Setup Pixel Art Canvas``: the wizard to create the texture, with a dimensions for the current texture density.
  * **Pixel Art workspace**: ``Image Editor`` on the left and the ``3D Viewport`` on the right. 

* **UV tools for pixel art**

  * **Pixel Art Unwrap**: lays each face flat in its own plane, with its exact shape and pixel density, and packs the islands on the texture. Options:

    * ``Margin (px)``: whole pixels between islands.
    * ``Avoid Shearing and Diagonal Pixels``: faces keep their exact shape. Turn it off to put every corner on a pixel corner (no partial pixels, but faces that are not rectangles bend a little).
    * ``Snap Corners Within``: faces that are already almost on the pixel grid are snapped onto it.
    * ``Keep Pinned UVs``: pinned UVs stay where they are, the other faces are packed around them.
    * ``Keep Density Zones`` and ``Keep Pixel Aspect``: each face uses the density and the pixel aspect of its zone.
    * ``Joined Faces Layout``: ``Unfold``, ``Relax`` (for curved surfaces), ``Project`` or ``Auto``.

  * **Quick Unwrap Model**: unwraps the whole model from any mode (Object, Edit, Sculpt, Paint) and goes back to the mode and selection you had.
  * **Share UVs**: stacks the selected faces on the same UV spot, so they paint the same pixels (ex: paint the 8 sides of a cylinder only once). The last selected face is the source. ``Match Size`` also resizes the other faces to the source's size.
  * **Keep Together (Join)**: neighbouring faces stay connected as one UV island when you unwrap (ex: a character's face or the front of a vehicle), instead of each face becoming its own island. Each joined group can be unwrapped with ``Relax``, ``Keep Aspect`` or ``Keep Shape`` (keeps the island exactly as drawn, only scaled to the pixel density).
  * **Select Linked UV Faces**: selects every face shared or joined with the selected faces.
  * **Flip Islands H** (:kbd:`Shift+F`) and **Flip Islands V** (:kbd:`Shift+V` in the UV Editor): flips UV islands in place.
  * **Shared Faces** and **Joined Faces** lists: every group has a name and a color. Click a group to select it, and the group is highlighted in the 3D Viewport and in the UV Editor.

* **Density Zones** (*optional, advanced*, multiple pixel sizes per model):

  * Assign and manage **texel density values per face**, for **uniform pixel size across the whole mesh or different pixel sizes per face** (a character's head drawn at twice the density of the legs, for example, which means smaller and more pixels for the head).
  * ``Detect Density Zones`` measures the model island by island and **clusters** them into zones automatically.
  * Build zones **from selected faces**, with custom names and densities.
  * ``Apply to Faces``: select faces and give them the zone picked in the list, while you are still creating the model, to test different pixel sizes. It scales their UV islands to the zone's density.
  * **Pixel aspect**: each zone also has a pixel aspect (pixels taller than wide, or the opposite, common in PS1 models). ``Detect Density Zones`` measures it, ``Measure Aspect`` measures it for zones you made by hand, and you can edit it below the list.
  * ``Grid Follows the Face``: while you paint in the 3D Viewport, **Blender's grid is resized and re-pointed on the fly** at the density of the face under the cursor, **to keep one grid square at the size of one pixel for that specific face**.

* **Game engine integration**

  * **Godot, Unity and Unreal Engine**: link a game project once, and every time you save in Blender the models and textures are exported into it. The game project gets pixel art materials automatically (unlit, nearest filtering, no blur).
  * **Auto-export to glTF (GLB) or FBX on save**, into any folder you pick.
  * **Unlit pixel art glTF**: every glTF export out of Blender, also a normal File > Export, writes the texture as unlit pixel art with nearest filtering. Turn it off with ``Unlit Pixel Art in glTF``.

* **Extras and Blender integration**

  * No external dependencies, it's made 100% in Python with Blender's APIs.
  * **Activate and deactivate** Pixel Art Studio with :kbd:`Esc` :kbd:`Esc` or a custom key (default :kbd:`;`).
  * Undo history (you can undo and redo everything alongside Blender).
  * **Tools and settings popup**: press :kbd:`F` over either editor for a floating panel with the tools and their settings.
  * Painting on the model works in **Object and in Edit mode**, and you can alternate between Pixel Art Studio's tools and Blender's own tools on the fly.
  * The canvas is a normal Blender image: it's packed into the .blend, and it renders and exports like any other texture.
  * Customizable shortcuts and keymaps: see :doc:`shortcuts`.

.. note::
    Pixel Art Studio is compatible with **Blender 3.6, Blender 4.0+ through Blender 5.1**. But the **officially supported version is Blender 5.1**.
