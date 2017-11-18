core_display_overlayered_lines.py
=================================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_overlayered_lines.py

------


Screenshots
^^^^^^^^^^^


  .. image:: images/screenshots/capture-core_display_overlayered_lines-1-1510986913.jpeg

------

Code
^^^^


.. code-block:: python

  import sys
  import random
  from math import pi
  
  from OCC.Display.SimpleGui import init_display
  from OCC.Addons import LineItem
  from OCC.Quantity import Quantity_Color
  
  # load the bottle
  from core_classic_occ_bottle import bottle
  
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  number_of_lines = 1000
  
  def draw_random_overlayered_lines(event=None):
      # random line parameters
      window_width = 1024
      window_height = 768
      for i in range(number_of_lines):
          x1 = random.randint(1, window_width)
          x2 = random.randint(1, window_width)
          y1 = random.randint(1, window_height)
          y2 = random.randint(1, window_height)
          line_width = random.uniform(0., 10)
          line_transp = random.random()
          line_type = random.randint(0, 10)
          line_color = Quantity_Color(random.random(), random.random(), random.random(), 1)
          # register line
          a_line = LineItem(x1, y1, x2, y2, display.GetOverLayer(),
                            line_type, line_width, line_transp, line_color)
          display.register_overlay_item(a_line)
  
  if __name__ == '__main__':
      ais_bottle = display.DisplayShape(bottle, update=True)
      add_menu('draw lines')
      add_function_to_menu('draw lines', draw_random_overlayered_lines)
      start_display()
