core_font_helloworld.py
=======================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_font_helloworld.py

------


Screenshots
^^^^^^^^^^^


  .. image:: images/screenshots/capture-core_font_helloworld-1-1510987126.jpeg

------

Code
^^^^


.. code-block:: python

  from OCC.Display.SimpleGui import init_display
  from OCC.Addons import text_to_brep, Font_FA_Bold
  
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  ## create a basic string
  arialbold_brep_string = text_to_brep("pythonocc rocks !", "Arial", Font_FA_Bold, 12., True)
  
  ## Then display the string
  display.DisplayShape(arialbold_brep_string, update=True)
  
  start_display()
