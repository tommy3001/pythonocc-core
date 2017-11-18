core_display_change_rendering_params.py
=======================================

Abstract
^^^^^^^^

to do

------

Launch the example
^^^^^^^^^^^^^^^^^^

  $ python core_display_change_rendering_params.py

------


Screenshots
^^^^^^^^^^^


  .. image:: images/screenshots/capture-core_display_change_rendering_params-1-1510986825.jpeg

------

Code
^^^^


.. code-block:: python

  import sys
  
  from OCC.Display.SimpleGui import init_display
  from OCC.BRepPrimAPI import (BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus,
                               BRepPrimAPI_MakeCone)
  from OCC.Graphic3d import (Graphic3d_NOM_GLASS, Graphic3d_NOM_COPPER,
                             Graphic3d_NOM_PLASTIC, Graphic3d_NOM_ALUMINIUM,
                             Graphic3d_MaterialAspect, Graphic3d_RM_RAYTRACING)
  from OCC.V3d import V3d_SpotLight, V3d_COMPLETE, V3d_XnegYnegZpos
  from OCC.Quantity import (Quantity_NOC_WHITE, Quantity_NOC_GREEN, Quantity_NOC_INDIANRED,
                           Quantity_NOC_CORAL2, Quantity_NOC_BROWN)
  from OCC.BRepAlgoAPI import BRepAlgoAPI_Cut
  from OCC.gp import gp_Vec
  from core_geometry_utils import translate_shp
  
  # first create geometry
  from core_classic_occ_bottle import bottle
  
  box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
  
  # then inits display
  display, start_display, add_menu, add_function_to_menu = init_display()
  
  # get rendering params
  rendering_params = display.View.ChangeRenderingParams()
  rendering_params.Method = Graphic3d_RM_RAYTRACING
  rendering_params.IsAntialiasingEnabled = True
  rendering_params.IsShadowEnabled = True
  rendering_params.IsReflectionEnabled = True
  rendering_params.RaytracingDepth = 5
  rendering_params.IsTransparentShadowEnabled = True
  display.View.Redraw()
  print(rendering_params)
  # create one spotlight
  print(dir(rendering_params))
  display.DisplayShape(box, update=True)
  print(rendering_params.StereoMode)
  rendering_params.StereoMode = True
  print(rendering_params.StereoMode)
  
  def raytracing(event=None):
      pass#display.SetRaytracingMode()
      
  def rasterization(event=None):
      pass#display.SetRasterizationMode()
  
  def exit(event=None):
      sys.exit(0)
  
  if __name__ == '__main__':
      add_menu('raytracing')
      add_function_to_menu('raytracing', rasterization)
      add_function_to_menu('raytracing', raytracing)
      add_function_to_menu('raytracing', exit)
      start_display()