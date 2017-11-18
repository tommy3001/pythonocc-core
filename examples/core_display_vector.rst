core_display_vector.py
======================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_vector.py

------


Screenshots
^^^^^^^^^^^


------

Code
^^^^


.. code-block:: python

  from OCC.gp import gp_Pnt, gp_Vec
  from OCC.Display.SimpleGui import init_display
  
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  display.DisplayVector(gp_Vec(100, 100, 100), gp_Pnt())
  
  start_display()
