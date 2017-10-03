##Copyright 2017 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

import sys
import random
from math import pi

from OCC.Display.SimpleGui import init_display
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Visual3d import Visual3d_Layer, Visual3d_LayerItem
from OCC.V3d import V3d_LayerMgr
from OCC.Aspect import (Aspect_TODT_NORMAL, Aspect_TODT_SUBTITLE,
                        Aspect_TODT_DEKALE, Aspect_TODT_BLEND, Aspect_TODT_DIMENSION)

from OCC.Quantity import (Quantity_Color, Quantity_NOC_BLACK,
                         Quantity_NOC_WHITE, Quantity_NOC_ORANGE)
from OCC.TCollection import TCollection_AsciiString
from OCC.gp import gp_Ax1, gp_Pnt, gp_Dir, gp_Trsf
from OCC.TopLoc import TopLoc_Location
from OCC.Addons import LineItem

display, start_display, add_menu, add_function_to_menu = init_display()
mybox = BRepPrimAPI_MakeBox(10, 10, 10).Shape()

# load the bottle
from core_classic_occ_bottle import bottle


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
    display.DisplayShape(mybox, update = True)
    start_display()
