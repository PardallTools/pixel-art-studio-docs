Shortcuts
=========================================

Pixel Art Studio's shortcuts live **inside the tool you have armed**. They are not registered in Blender's keymap, they only answer while a Pixel Art Studio tool is active.

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
     - no key, click the button

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
     - :kbd:`Shift+X`
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

Mouse
-----

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Mouse
   * - **Paint, draw the shape, drag out the selection**
     - Left click and drag
   * - **Temporary eyedropper** (from any paint tool)
     - :kbd:`Alt` + left click
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
---------------------

Pixel Art Studio does not have bindable and configurable shortcuts. Shortcuts are handled inside the add-on's own modal operators, which is what keeps them out of Blender's way.

Everything can be quickly accessed with :kbd:`F`, to open the tools and settings popup over the viewports (again, just make sure a tool is armed first by clicking its button, then the :kbd:`F` shortcut works):

.. image:: _static/images/activate-tools-popup.gif