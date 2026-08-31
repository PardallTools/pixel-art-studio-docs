Shortcuts
=========================================

Pixel Art Studio's shortcuts live **inside the tool you have armed**. They are not registered in Blender's keymap, they only answer while a Pixel Art Studio tool is active. To customize shortcuts, see :ref:`bindable-shortcuts`.

.. warning::
    **The first tool has to be activated by clicking its button** in the sidebar. Until you click one of the tool buttons (like the ``Brush``), there is no Pixel Art Studio tool listening and Blender keeps catching every key. After you manually activate a tool, all shortcuts below work.
  
.. warning::
    **To get Blender's shortcuts back, you have to manually deactivate the tool.** Click the armed tool's button again to de-activate it (or press :kbd:`ESC` over the viewport). While a tool is armed it owns the keys below, so for example, Blender's :kbd:`G` and :kbd:`B` does not work.

.. image:: _static/images/activate-shortcuts.gif

.. note::
    On macOS every :kbd:`Ctrl` shortcut below maps to :kbd:`Cmd`.

Tools
-----

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Keybinding
   * - **Brush**
     - :kbd:`B`
   * - **Eraser**
     - :kbd:`E`
   * - **Line**
     - :kbd:`L`
   * - **Rectangle**
     - :kbd:`U`
   * - **Ellipse**
     - :kbd:`O`
   * - **Path and Polygon** (bezier curve tool)
     - :kbd:`C`
   * - **Bucket fill**
     - :kbd:`G`
   * - **Gradient**
     - :kbd:`D`
   * - **Blur**
     - :kbd:`H`
   * - **Eyedropper**
     - :kbd:`I`
   * - **Move**
     - :kbd:`V`
   * - **Marquee select**
     - :kbd:`M`
   * - **Ellipse select**
     - :kbd:`Shift+M`
   * - **Lasso select**
     - :kbd:`Q`
   * - **Magic Wand**
     - :kbd:`W`

Pressing the key of the tool currently in use, de-activates it, the same as clicking its button again.

Brush and colors
----------------

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Keybinding
   * - **Increase brush size**
     - :kbd:`]`
   * - **Decrease brush size**
     - :kbd:`[`
   * - **Swap primary and secondary color**
     - :kbd:`X`
   * - **Walk to the next swatch**
     - :kbd:`Ctrl+Shift+X`
   * - **Pixel Perfect on / off**
     - :kbd:`P`

Selection
---------

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Keybinding
   * - **Select all**
     - :kbd:`Ctrl+A`
   * - **Deselect**
     - :kbd:`Alt+A`
   * - **Invert selection**
     - :kbd:`Ctrl+I`
   * - **Add to the selection**
     - :kbd:`Shift` while dragging
   * - **Remove from the selection**
     - :kbd:`Alt` while dragging
   * - **Duplicate the selection**
     - :kbd:`Ctrl` while dragging
   * - **Copy the selected pixels**
     - :kbd:`Ctrl+C`
   * - **Cut the selected pixels**
     - :kbd:`Ctrl+X`
   * - **Paste**
     - :kbd:`Ctrl+V`
   * - **Delete the selected pixels** (or the whole layer when nothing is selected)
     - :kbd:`Backspace` or :kbd:`Delete`

Paste writes into whatever layer is **active**, which is how you move pixels from one layer to another: select on one layer, cut, pick another layer, paste.

View and canvas
---------------

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Keybinding
   * - **Pixel grid overlay on / off**
     - :kbd:`\\` or :kbd:`Shift+3`
   * - **Floating tools and settings popup on the viewports**
     - :kbd:`F`
   * - **Undo**
     - :kbd:`Ctrl+Z`
   * - **Redo**
     - :kbd:`Ctrl+Shift+Z` or :kbd:`Ctrl+Y`
   * - **Cancel the stroke you are drawing, then de-activate the tool**
     - :kbd:`ESC`

Path and Polygon tool
-----------

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Keybinding
   * - **Start a new path**
     - Left click
   * - **Add a new hard corner to the path**
     - Left click and release
   * - **Add a new smooth corner to the path**
     - Left click, hold and drag the mouse
   * - **Close polygon**
     - Left click and release at the first point
   * - **Close the path at the current point**
     - :kbd:`Enter`
   * - **Cancel and clear the path**
     - :kbd:`Backspace`

Mouse
-----

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Mouse
   * - **Paint, draw the shape, drag out the selection**
     - Left click and drag
   * - **Temporary eyedropper / color picker** (from any paint tool)
     - :kbd:`Shift+X` + left click (Blender's default)
   * - **Move the selected pixels**
     - Drag from inside the selection
   * - **Duplicate the selected pixels instead of moving them**
     - :kbd:`Ctrl` + drag from inside the selection
   * - **Constrain**: 45 degrees for the line, square for the rectangle, circle for the ellipse
     - :kbd:`Shift` while dragging
   * - **Drag a symmetry ruler** (Image Editor)
     - Left click and drag the ruler
   * - **Remove a swatch**
     - :kbd:`Ctrl` + click the swatch
   * - **Orbit, pan and zoom the viewport**
     - Middle mouse and the wheel, as always

.. _bindable-shortcuts:

Custom shortcuts and quick access
--------------------------------------------

It's possible to customize every single shortcut used by Pixel Art Studio in :menuselection:`Edit --> Preferences --> Add-ons --> Pixel Art Studio --> Preferences --> Shortcuts`:

.. image:: _static/images/settings-shortcuts.png

Tools and settings popup
----------------------------------------------

Everything can be quickly accessed with :kbd:`F`, to open the tools and settings popup over the viewports, at mouse position (again, just make sure a tool is armed first by clicking its button, then the :kbd:`F` shortcut works):

.. image:: _static/images/activate-tools-popup.gif