FAQ
=========================================

Is Pixel Art Studio a standalone application?
----------------------------------------------

No, it's a Blender add-on (plugin / addon). You use it inside Blender, on your own projects.

Does it require external dependencies?
--------------------------------------

No, it's made 100% with Python using only Blender's APIs, a native Blender add-on. It also works offline: the palette library (500 Lospec palettes) ships inside the add-on.

Which Blender versions does it work with?
-----------------------------------------

Blender 3.6 through 5.x. There are two zips with the same add-on inside: the classic one works on every supported version, and the extension one needs Blender 4.2 or newer. See :doc:`installation`.

Does it have shortcuts / keymaps? Can I customize them?
-------------------------------------------------------

Yes, every shortcut can be rebound, and they only work while a Pixel Art Studio tool is armed (the activator, the hover eyedropper and the tools popup's :kbd:`D` work without). Choose how they live with Blender's, the first time you click a tool: ``Alongside Blender`` (default, Blender's shortcuts keep working while you paint) or ``Pixel Art Studio Only`` (Aseprite style single keys). See :doc:`shortcuts`.

Can I draw, paint, edit and select pixel art in the 3D viewport?
----------------------------------------------------------------

Yes, on the model in the 3D Viewport, both in Edit and Object modes. You can alternate between Pixel Art Studio's tools and Blender's own on the fly (press :kbd:`;`). In Edit Mode, faces you hide are left alone by every tool, which is a handy way to protect a part of the model while you paint next to it.

Can I draw, paint, edit and select pixel art in Blender's Image Editor?
-----------------------------------------------------------------------

Yes, and at the same time as in 3D: the ``Pixel Art Studio`` workspace has the Image Editor on the left and the 3D Viewport on the right, a stroke in one shows up in the other, and the colors and the tool are shared.

My model already has UVs and a texture. What do I need to set up?
------------------------------------------------------------------

Nothing: select the model, click a tool and paint. The first stroke turns the texture into a canvas with layers. Painting works from your UVs and the texture's own texels, it never needs a pixel density, ``Setup Viewport`` or density zones (those are for UV unwrapping with Pixel Art Studio). See :ref:`just-paint`.

My model has no texture. What's the quickest setup?
---------------------------------------------------

The big ``Setup`` button (or a click on the model with any tool): ``Quick Setup`` shows the pixel sizes on the model, live, then ``Create Texture`` makes the texture, its material and new pixel perfect UVs in one click. See :doc:`quick-setup`.

Can I change the pixel size after painting?
-------------------------------------------

Yes. ``Try Pixel Densities`` (``Pixel Density`` panel) shows other pixel sizes on the model with your own texture, and ``Apply New Density`` keeps your painting, scaled to the new pixel size (or carried onto new UVs). One :kbd:`Ctrl+Z` takes it back. See :ref:`quick-setup-try`.

.. _faq-custom-shader-and-material:

My model has a custom shader and custom material, can I use Pixel Art Studio to paint it?
-----------------------------------------------------------------------------------------

Yes. The first stroke turns the color texture your material already uses into a canvas and **leaves your shader as it is**: only that texture's ``Image Texture`` nodes are set to ``Closest``, so the pixels stay crisp (unless you picked ``Linear`` for it, see :doc:`texture-filtering`), and normal maps and roughness maps are left alone. A mesh with several color textures can paint each of them (``Paint On``). See :ref:`automatic-canvas`.

When you export to glTF, your material keeps its shader and its lighting too, and only gets the crisp pixels and the hard edged transparency (see :doc:`game-engines`).

Can the texture be smooth (Linear) instead of crisp?
----------------------------------------------------

Yes. ``Filtering``, under ``Paint On`` in ``Setup``: ``Closest`` (the pixel art look), ``Linear`` or ``N64 (3 Point)``. **Seam Padding** keeps the UV seams from showing a step at every face, and the game engines get the texture ``Linear`` with mipmaps. See :doc:`texture-filtering`.

Is there undo and redo support?
-------------------------------

Yes, strokes are steps in Blender's own undo history: you undo and redo normally with :kbd:`Ctrl+Z` and :kbd:`Ctrl+Shift+Z`.

Can I send my model to Godot, Unity or Unreal Engine?
-----------------------------------------------------

Yes. Integrate the .blend with the engine once, and **every save updates the model in the engine**, unlit and with crisp pixels. For any other engine, the ``Generic Exporter`` writes GLB, glTF or FBX into a folder on every save, and your own ``File > Export > glTF 2.0`` comes out as pixel art too. See :doc:`game-engines` and :doc:`tutorial-game-engines`.

Do I have to unwrap the UVs myself?
-----------------------------------

No. ``Quick Unwrap Model`` (``UV`` panel) unwraps the whole model for pixel art in one click, from any mode: every face gets the same pixel size, packed on whole texels. Prefer your own UV layout? Keep it, and ``Apply Texel Density`` puts it on the pixel size you picked. See :doc:`uv-tools`, :doc:`pixel-density` and :doc:`tutorial-uvs-without-the-uv-editor`.

Can one model have pixels of different sizes?
---------------------------------------------

Yes, with ``Density Zones``: a character's head drawn at twice the density of the legs, for example, which means smaller and more pixels for the head. The pixels stay uniform inside each zone. See :doc:`density-zones` and :doc:`tutorial-multiple-pixel-sizes`.

Can several faces show the same pixels?
---------------------------------------

Yes, ``Stack UVs`` puts the selected faces on one UV spot (the staves of a barrel, the sides of a cylinder): paint one and all of them show it, and every later unwrap keeps them stacked. See :doc:`uv-tools`.

Can several objects share one texture?
--------------------------------------

Yes. **Painting**: every visible object that uses the active object's texture takes the brush where you point at it, so a model made of many parts (a rig, a vehicle) paints as one (see :ref:`several-parts`). **Unwrapping**: select them in Object Mode and click ``Quick Unwrap Model``, every mesh using the same texture is laid out on it together, at one pixel size and with no part on top of another.

Can I keep painting in Aseprite or Photoshop?
---------------------------------------------

Yes. Turn on ``Watch for external file changes`` (``Others`` panel), save the texture in your other app, and Pixel Art Studio asks where the changes go (a new layer on top, for example). See :ref:`external-changes`.

Where are my pixels saved?
--------------------------

The canvas is a normal Blender image, packed inside the .blend together with your layers every time you save. A canvas that came from a texture file (a model you painted on) is also written back to that file, in its own format. It renders and exports like any other texture. See :ref:`canvas-saving`.
