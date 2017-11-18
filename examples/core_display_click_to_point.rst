core_display_click_to_point.py
==============================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_click_to_point.py

------


Screenshots
^^^^^^^^^^^


------

Code
^^^^


.. code-block:: python

  import sys
  
  from OCC.Display.SimpleGui import init_display
  from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
  from OCC.Quantity import Quantity_NOC_ALICEBLUE, Quantity_NOC_ANTIQUEWHITE
  from OCC.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Pln
  
  display, start_display, add_menu, add_function_to_menu = init_display()
  display.set_raytracing_mode()
  my_box = BRepPrimAPI_MakeBox(10., 20., 30.).Shape()
  display.DisplayShape(my_box, update=True)
  start_display()
