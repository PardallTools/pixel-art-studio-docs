Features
=========================================

Pixel Art Studio is a Blender add-on (plugin) for **pixel perfect pixel art texture painting**. It supports drawing and painting **pixel art inside Blender**, in the 3D Viewport on top of the model (in Object and Edit modes) and in 2D in the Image Editor. It has tools for drawing and painting (including colors, palettes, layers, pressure sensitivity, bucket fill, gradients), selecting and moving pixels, and quickly setting up the model and the viewport for pixel art. The plugin also helps with setting up and managing multiple texture densities per mesh, allowing for **uniform pixel sizes across the whole mesh or per face pixel size variation**.

Not only it has tools with pixel line handling algorithms, it solves one of the biggest pain points when doing Pixel Art with Blender: pixel size stays consistent regardless of zoom level. One texel stays always one texel, which means always one pixel at the size of the texel defined by you in the whole mesh or per face.

.. video:: _static/videos/v2/pixel-art-studio-features.mp4
  :width: 100%

.. _features-details:

Pixel Art Studio features in details
------------------------------------

Every drawing, selection and layer tool works in the **3D Viewport and in the Image Editor**, in **perspective and orthographic** views, so you can move the camera around freely while painting.

* **Drawing and painting tools**

  * All tools are directly inspired by `Aseprite <https://www.aseprite.org/>`_, so you are going to feel right at home.
  * All tools have **pixel perfect line handling** algorithms (with the brush and line tool, it removes the doubled L corners, with the ellipse, it creates pixel perfect circles and ellipses).
  * **Paint straight on the model**: lines and shapes stay straight across UV seams and around edges, and big brushes wrap over seams and corners **without leaking into other UV islands** or into empty texture space.
  * **Open your model and paint**: a model that already has UVs and a texture needs no setup, the first stroke turns the texture into layers (only the color texture, normal and roughness maps are left alone).
  * **Models made of many objects on one texture** (a rig, a vehicle in parts): every part takes the brush where you point at it, whichever object is selected, and a stroke stays on the part it started on.
  * **Brush** (:kbd:`Shift+Alt+B`): freehand painting as a ``Circle``, ``Square`` or custom brush, free size selection as well presets for ``1 2 3 4``, :kbd:`Alt+[` :kbd:`Alt+]` to increase/decrease the size on the viewport.
  * **Eraser** (:kbd:`Shift+Alt+E`): erases to transparent, with opacity control (it keeps its own size, shape and opacity, apart from the brush's).
  * **Adjustable opacity, applied stroke-relative**: like `Aseprite <https://www.aseprite.org/>`_, dragging over the same texels twice inside one stroke applies the opacity **once**.
  * **Line** (:kbd:`Shift+Alt+L`): pixel perfect stair steps. :kbd:`Shift` snaps to straight lines, 45 degrees and **2:1 isometric** lines.
  * **Lines from the last dab**: :kbd:`Ctrl+Shift+click` draws a straight line from your last dab with the brush or the eraser, and :kbd:`Ctrl+Shift+Alt+click` snaps it to the same perfect angles (a chain of clicks draws a polygon).
  * **Rectangle** (:kbd:`Shift+Alt+U`) and **Ellipse** (:kbd:`Shift+Alt+O`): outlined (stamped with the current brush), filled, or outlined in the primary color and filled with the secondary, :kbd:`Shift` constrains to a square or a circle (the preview is the final pixels).
  * **Path and Polygon** (:kbd:`Shift+Alt+C`): bezier tool with smoothed and hard corners, allowing to draw pixel art curves and polygons, including filled polygons (click and drag to draw a smooth corner, click to draw a hard corner, :kbd:`Enter` to finish the path).
  * **Text**: crisp pixel font text, never antialiased, with bold, italic and outline (nine pixel fonts bundled, plus the fonts installed on your system).
  * **Bucket** (:kbd:`Shift+Alt+F`), two modes:

    * ``Pixel``: flood fill with an adjustable **tolerance**. When ``Contiguous`` is off it is a global/selection color replace. On the model **the fill follows the surface**, so an outline drawn on the model holds the fill even across many UV islands.
    * ``Face``: fills whole faces out to their own edges (the selected faces, or every face if nothing is selected).

  * **Bleed**: covers the half pixels along diagonal UV edges, and pads UV islands against mipmap bleeding (brush, eraser, line, bucket and gradient).
  * **Blur** (:kbd:`Shift+Alt+H`): box blur, pixel aware (it never makes sub-pixels).

    * ``Scramble``: shuffles the texels under the brush, the area gets noisy and **no new color is ever made**.

  * **Shading**: lightens or darkens what is already painted, the way a pixel artist would.

    * ``Simple Shading``, ``Hue Shifting`` (highlights warm up towards yellow, shadows cool down towards blue) and ``Color Replace`` (steps along your own palette ramp).
    * :kbd:`Ctrl` swaps lighten and darken for one stroke.

  * **Pixel Spray**: a pixel art spray can, it stays on the pixel grid and wraps around the model's seams.
  * **Gradient** (:kbd:`Shift+Alt+D`): two color gradient, ``Linear`` or ``Radial``, with **ordered dithering** (``Bayer 2x2``, ``4x4``, ``8x8``) or ``Smooth`` (fills the selection, the whole layer, or everything you see on the model).
  * **Eyedropper** (:kbd:`Shift+Alt+I`) and :kbd:`Alt+click`.

    * :kbd:`Alt+Shift+X`: samples the color under the pointer with no click and no tool armed (hold it and the color follows the pointer).
    * In the 3D Viewport it also samples **reference images**, other objects and the background, and a texture that isn't a canvas yet (it never makes one).
    * The new and the old color are shown right at the cursor while you sample.

  * **Move** (:kbd:`Shift+Alt+V`): drags a layer or a selection around (on the model it's carried across the faces).

    * ``Auto Select Layer``: auto selects the layer at click position.

  * **Tablet pressure**: pressure toggles for ``Size`` and ``Opacity``.
  * **Live brush preview**: the exact dab is drawn under the cursor before you click, on the model and in the Image Editor, with the armed tool's icon right below it.

* **Brushes, patterns and colors**

  * **Custom brushes** from anything you draw, with Aseprite's three alignments, usable on the model, saved in the file, in the preferences (every file) or as assets.
  * **Fill and dither patterns** on every drawing tool: ``Dither 12%``, ``Dither 25%``, ``Checker 50%``, ``Dither 75%``, lines, diagonals and grid, or **your own pattern** cut from a selection.

    * Patterns stay **locked to the pixel grid**: strokes, fills and shapes meet without seams, on the flat texture and across the model's UV seams.
    * ``Transparent``: lays a pattern over art that is already there.

  * **Noise** and **Color Jitter**: hand placed looking texture (grime, grass, rust, wood grain) that never shifts when you paint over the same area again.
  * **Primary and secondary color**: :kbd:`Alt+X` to alternate between 2 colors, and ``Next Swatch`` to walk the swatches of your palette.
  * **Blender's own color picker** inside the panel, and **the hex you pick is exactly the hex painted** (no color management surprises).
  * **Custom palettes** by adding swatches (add colors clicking the ``+`` and remove with :kbd:`Ctrl+click`) or by **importing palette images** (for example, palettes from **Lospec**).
  * **Lospec palette library**: 500 palettes bundled with the add-on, offline, previewed live on your model as you click them.

* **Pixel selection and transform**

  * **Marquee** (:kbd:`Shift+Alt+M`), **Ellipse Select**, **Lasso** (:kbd:`Shift+Alt+K`) and **Magic Wand** (:kbd:`Shift+Alt+W`) (while a selection is active, tools affect only the selected pixels).

    * :kbd:`Shift` adds to selection, :kbd:`Alt` removes from selection (with any of the drag tools).

  * **Selecting in 3D is per texel**: select what you see on the mesh, and it's the same selection in the texture.
  * **Drag and move selections**: directly in the texture in the Image Editor and on the model in 3D, **across the faces like a sticker**, even across separate UV islands. :kbd:`Ctrl` while dragging duplicates the selection, :kbd:`Shift` holds it to one axis.
  * **Transform** (:kbd:`Shift+Alt+T`): scale, rotate, skew and anchor with handles like Aseprite's, in 2D and **on the model**, always landing on whole texels.

    * Three rotation algorithms (``Clean Rotation``, ``Fast Rotation`` and ``RotSprite``), and **none of them invents colors**, so your palette stays clean.

  * **Select by topology**: grabs the half pixels along diagonal UV edges that every other tool leaves behind.
  * **Copy, cut and paste across layers** (:kbd:`Ctrl+Shift+C` / :kbd:`Ctrl+Shift+X` / :kbd:`Ctrl+Shift+V`), and ``Paste as New Layer``.
  * Flip the selection horizontally and vertically.
  * The selection clears itself when you put the tools away (optional).

* **Layers and Groups**

  * **Layers** like in painting programs: add, remove, duplicate, move up and down, merge down and merge selected, lock, visibility, opacity.
  * **Groups**: group and ungroup layers, nested groups, group opacity and visibility (affects all layers inside the group).
  * **19 blend modes** (Aseprite's set), on layers and on groups, with Photoshop style group blending.
  * **Clipping layers and layer masks** like Photoshop and Krita: shade inside a shape, hide without erasing, change your mind later.
  * **Non-destructive adjustments**: ``Brightness/Contrast``, ``Hue/Saturation`` and ``Color Curve``, stackable, on a layer or on a whole group.
  * **Import and export**: export a layer or a group as a cropped PNG, or the whole texture (``Export Texture``, what ``Image > Save As`` writes), import images as layers, and **paste images from any program's clipboard** as a new layer.
  * ``Texture Dilation``: grows the colors of the art into the transparent texels around it, **so UV seams don't bleed the background in** (in a game engine, for example). On a layer, a group or the whole texture, with a live preview.
  * Photoshop and Krita muscle memory in ``Pixel Art Studio Only``: :kbd:`Ctrl+Shift+N`, :kbd:`Ctrl+J`, :kbd:`Ctrl+E`, :kbd:`Ctrl+G`.

* **Pixel size and pixel density (texel density)**

  * **One-click pixel size setup**: this solves one of the biggest pain points of doing pixel art in Blender, it makes pixels uniform across the model or per face (see ``Density Zones`` below).
  * ``Quick Setup``: **see the pixel size on the model before you choose it**. The big ``Setup`` button draws every preset (or your own number) live on the model, with the texture size it needs and a preview of the UVs, then ``Create Texture`` makes the texture, the material and the UVs in one click.
  * ``Try Pixel Densities``: change the pixel size of a model **you already painted**, previewed with your own texture, and ``Apply New Density`` keeps the painting (scaled to the new pixel size, or carried onto new UVs). One :kbd:`Ctrl+Z` takes it back.
  * **Density presets**: ``Low Density, big pixels (16px/m)`` (chunky pixels), ``Medium Density (50px/m)`` (default), ``High Density, small pixels (110px/m)``, ``Very High Density, small pixels (220px/m)`` and ``Custom``.
  * **Your own presets**, saved once and ready in every project.
  * ``Apply Texel Density``: puts the UVs of the selected objects on the pixel size, **island by island, keeping your own UV layout** (no slanted pixels, islands stay where you put them).
  * ``Detect Texel Density``: detects the pixel size of the model.

    * **Auto pixel size detection for pre-existing textured models**

  * **A red button tells you** when the model is off the pixel size you asked for, and a painted texture is always asked about before its pixel size changes (``Keep my painting`` or ``Start with a blank texture``).
  * ``Grow Texture to Fit``: texture too small? The canvas grows to fit the UVs, layers included, as one undo step.

* **Viewport and scene setup**

  * ``Setup Viewport``: one click button to setup Blender's grid and snapping so that **one grid square is exactly one texel** at the current density / current pixel size (plus flat texture shading and colors shown 1:1).
  * ``Setup Pixel Art Canvas``: the wizard to create the texture, its layers and a crisp unlit material, and it tells you **which texture size your model really needs**.
  * ``Remove Unused Textures``: removes the textures a setup made that nothing uses any more (left behind while trying densities).
  * ``Snap Selection to Pixel Grid``: snaps objects or vertices on the pixel grid at any zoom, something Blender's own snapping can't do.
  * **Several textures on one mesh**: ``Paint On`` lists them to select the one to paint on, or let a click on a face switch to its texture.
  * **Pixel Art Studio workspace**: ``Image Editor`` on the left and the ``3D Viewport`` on the right.

* **UV tools**

  * ``Pixel Art Unwrap``: UV unwrap made for pixel art, **the same pixel size on every face**, tilted or flat, packed on whole pixels.
  * ``Quick Unwrap Model``: unwraps the whole model from any mode and puts your mode and selection back, in one undo step. **The eye beside it previews the new UVs on the model** at any pixel size, before anything changes.
  * **Several meshes on one texture** (a character in several parts, for example) are unwrapped as one packed layout with no overlaps.
  * ``Stack UVs``: **paint it once, see it everywhere** (barrel staves, cylinder sides, wheel spokes), and every unwrap keeps them stacked.
  * ``Keep UVs Together (Join)``: curved parts stay one clean island, unfolded flat or relaxed so the stretch is spread thin. Imported models (glTF) whose faces only touch are offered a weld first.

    * ``Keep Shape``: keeps the UV proportions you drew through every unwrap.

  * **Color coded groups** of stacked and joined faces, lit under the mouse in the 3D Viewport and in the UV Editor.
  * Flip UV islands, snap UVs to pixels, keep pinned UVs, and margins measured in pixels.
  * Lists of the stacked and joined groups, with a trash button to remove them all at once.

  .. note::
      Every face gets its own island unless you stack or join faces. For organic models you may still want to unwrap the UVs by hand, and then use Pixel Art Studio's density tools on top of your own layout.

* **Density Zones** (*optional, advanced*, multiple pixel sizes per model):

  * Assign and manage **texel density values per face**, for **uniform pixel size across the whole mesh or different pixel sizes per face** (a character's head drawn at twice the density of the legs, for example, which means smaller and more pixels for the head).
  * ``Detect Density Zones`` measures the model island by island and **clusters** them into zones automatically (PS1 style models included).
  * **Stretched pixels survive a new unwrap**: the pixel aspect of each zone is measured and kept.
  * Build zones **from selected faces**, with custom names and densities.
  * ``Grid Follows the Face``: while you paint in the 3D Viewport, **Blender's grid is resized and re-pointed on the fly** at the density of the face under the cursor, **to keep one grid square at the size of one pixel for that specific face**.

* **Symmetry, Tiled Mode and pixel grid**

  * **Mirror and symmetry drawing**: horizontal, vertical, 45 and -45 degrees (they can be combined for multi-axis symmetry). On the model it works like a Mirror modifier, pixel exact.
  * **Tiled Mode** in the Image Editor: paint seamless textures and see them repeat around the canvas as you draw.
  * **Pixel grid** overlay in the Image Editor and in 3D Viewport overlayed on top of the model, so stretched or half pixels show before you paint (color and thickness configurable).

* **Game engines**

  * **Paint in Blender, press** :kbd:`Ctrl+S` **and see it in Godot, Unity or Unreal Engine**: no export dialogs, no manual reimport.
  * **Pixel art arrives as pixel art**: unlit, nearest filtered, no mipmap blur, hard edged transparency, in every engine. It fixes the classic "black or blurry model" import problem.
  * ``Fix Models in Project``: fixes the models that were already in the project before the integration.
  * **Generic Exporter**: GLB, glTF or FBX into any folder on every save, for any other engine or tool.
  * Any **glTF export you make yourself** comes out as unlit pixel art too.
  * Safe in your project: nothing deleted, your own materials and import settings left alone.

* **Extras and Blender integration**

  * No external dependencies, it's made 100% in Python with Blender's APIs.
  * Undo history (you can undo and redo everything alongside Blender).
  * **Tools popup**: press :kbd:`D` over either editor for a panel with the tools and their settings, right at the pointer, even with no tool armed.
  * Painting on the model works in **Object and in Edit mode**, and you can alternate between Pixel Art Studio's tools and Blender's own tools on the fly. Hide faces in Edit Mode to protect them while you paint next to them.
  * **Paint on the model and on the flat texture at the same time**, side by side, with the same colors and tools in both.
  * The canvas is a normal Blender image: it's packed into the .blend, and it renders and exports like any other texture. A texture that came from a file is written back **in its own format** (PNG, JPEG, TGA, 16 bit PNG and more).
  * **Keep using Aseprite** (or any editor) on the same texture file: Blender asks how to bring the changes into your layers instead of overwriting them (with ``Watch for external file changes`` on).
  * **Two shortcut modes**: ``Alongside Blender`` (default) **keeps Blender's own shortcuts working while you paint**, ``Pixel Art Studio Only`` gives you Aseprite style single keys (asked the first time you click a tool). Every shortcut is customizable, and **one key** (:kbd:`;`) jumps between Pixel Art Studio and Blender: see :doc:`shortcuts`.

.. note::
    Pixel Art Studio works on **Blender 3.6 through 5.x** (the extension version needs Blender 4.2 or newer). See :doc:`installation`.
