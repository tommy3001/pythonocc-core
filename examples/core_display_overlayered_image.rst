core_display_overlayered_image.py
=================================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_overlayered_image.py

------


Screenshots
^^^^^^^^^^^


  .. image:: images/screenshots/capture-core_display_overlayered_image-1-1510986874.jpeg

------

Code
^^^^


.. code-block:: python

  from math import pi
  
  from OCC.TCollection import TCollection_AsciiString
  from OCC.Addons import TextureItem
  from OCC.Display.SimpleGui import init_display
  
  # load the bottle
  from core_classic_occ_bottle import bottle
  
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  
  def absolute_position(event=None):
      # create a texture
      aTextureItem = TextureItem(TCollection_AsciiString("./images/carre-200.png"),
                                 display.GetView().GetObject(),
                                 display.GetOverLayer())
      aTextureItem.SetAbsolutePosition(50, 50)
      display.register_overlay_item(aTextureItem)
  
  
  def relative_position(event=None):
      # create a texture
      aTextureItem = TextureItem(TCollection_AsciiString("./images/carre-200.png"),
                                 display.GetView().GetObject(),
                                 display.GetOverLayer())
      aTextureItem.SetRelativePosition(30, 60)  # 30% width, 60% width
      display.register_overlay_item(aTextureItem)
  
  if __name__ == "__main__":
      display.DisplayShape(bottle, update=True)
      menu_name = 'overlay images'
      add_menu(menu_name)
      add_function_to_menu(menu_name, absolute_position)
      add_function_to_menu(menu_name, relative_position)
      start_display()