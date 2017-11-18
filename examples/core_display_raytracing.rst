core_display_raytracing.py
==========================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_raytracing.py

------


Screenshots
^^^^^^^^^^^


  .. image:: images/screenshots/capture-core_display_raytracing-1-1510987058.jpeg

  .. image:: images/screenshots/capture-core_display_raytracing-2-1510987058.jpeg

  .. image:: images/screenshots/capture-core_display_raytracing-3-1510987058.jpeg

------

Code
^^^^


.. code-block:: python

  import sys
  
  from OCC.Display.SimpleGui import init_display
  from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCone
  from OCC.Graphic3d import Graphic3d_NOM_PLASTIC, Graphic3d_NOM_ALUMINIUM
  from OCC.V3d import V3d_SpotLight, V3d_COMPLETE, V3d_XnegYnegZpos
  from OCC.Quantity import Quantity_NOC_WHITE, Quantity_NOC_CORAL2, Quantity_NOC_BROWN
  from OCC.BRepAlgoAPI import BRepAlgoAPI_Cut
  from OCC.gp import gp_Vec
  
  from core_geometry_utils import translate_shp
  
  # first create geometry
  from core_classic_occ_bottle import bottle
  table = translate_shp(BRepPrimAPI_MakeBox(100, 100, 10).Shape(), gp_Vec(-50, -50, -10))
  glass_out = BRepPrimAPI_MakeCone(7, 9, 25).Shape()
  glass_in = translate_shp(BRepPrimAPI_MakeCone(7, 9, 25).Shape(), gp_Vec(0., 0., 0.2))
  glass = BRepAlgoAPI_Cut(glass_out, glass_in).Shape()
  translated_glass = translate_shp(glass, gp_Vec(-30, -30, 0))
  
  # then inits display
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  # create one spotlight
  spot_light = V3d_SpotLight(display.Viewer_handle, -100, -100, 100,
                             V3d_XnegYnegZpos, Quantity_NOC_WHITE)
  ## display the spotlight in rasterized mode
  spot_light.Display(display.View_handle, V3d_COMPLETE)
  display.View.SetLightOn()
  
  display.DisplayShape(bottle, material=Graphic3d_NOM_ALUMINIUM)
  display.DisplayShape(table, material=Graphic3d_NOM_PLASTIC, color=Quantity_NOC_CORAL2)
  display.DisplayShape(translated_glass,
                       material=Graphic3d_NOM_PLASTIC,
                       color=Quantity_NOC_BROWN,
                       transparency=0.6,
                       update=True)
  
  def raytracing_default_depth(event=None):
      display.SetRaytracingMode()
  
  def raytracing_depth_8(event=None):
      display.SetRaytracingMode(depth=8)
      
  def rasterization(event=None):
      display.SetRasterizationMode()
  
  def exit(event=None):
      sys.exit(0)
  
  if __name__ == '__main__':
      add_menu('raytracing')
      add_function_to_menu('raytracing', rasterization)
      add_function_to_menu('raytracing', raytracing_default_depth)
      add_function_to_menu('raytracing', raytracing_depth_8)
      add_function_to_menu('raytracing', exit)
      start_display()
