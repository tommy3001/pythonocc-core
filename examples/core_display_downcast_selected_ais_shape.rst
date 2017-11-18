core_display_downcast_selected_ais_shape.py
===========================================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_downcast_selected_ais_shape.py

------


Screenshots
^^^^^^^^^^^


------

Code
^^^^


.. code-block:: python

  from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
  from OCC.AIS import AIS_Shape, Handle_AIS_Shape_DownCast, Handle_AIS_InteractiveObject
  from OCC.Display.SimpleGui import init_display
  
  
  def print_xy_click(shp, *kwargs):
      for shape in shp:
          print("Shape selected: ", shape)
      print(kwargs)
  
  
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  box = BRepPrimAPI_MakeBox(100,100,100).Shape()
  anAis = AIS_Shape(box)
  
  ais_context = display.GetContext().GetObject()
  ais_context.SetCurrentObject(anAis.GetHandle())
  ais_context.InitCurrent()
  currentAis = ais_context.Current()
  print(currentAis)
  shape = Handle_AIS_Shape_DownCast(currentAis)
  start_display()
