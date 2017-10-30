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

__doc__ = """ This script creates an rst file per each example
of the /examples folder. The rst consist of:
* one or more screenshots
* the python code of the example
"""
# look for all example names
import os
import glob
import sys
import subprocess

os.environ["PYTHONOCC_OFFSCREEN_RENDERER"] = "1"
os.environ["PYTHONOCC_OFFSCREEN_RENDERER_DUMP_IMAGE"] = "1"
os.environ["PYTHONOCC_OFFSCREEN_RENDERER_DUMP_IMAGE_PATH"] = os.path.join("images", "screenshots")

def get_screenshots_for_example(example_name):
    """ look into the screenshots folder, and returns
    file names
    """
    all_screenshots = glob.glob(os.path.join('images', 'screenshots', 'capture-core_*.jpeg'))
    #print(all_screenshots)
    base_name = os.path.splitext(example_name)[0]
    r = []
    for screenshot_name in all_screenshots:
        if base_name in screenshot_name:
            r.append(screenshot_name)
    return r

def get_all_available_examples():
    all_examples_file_names = glob.glob(os.path.join('.', 'core_*.py'))
    # some tests have to be excluded from the automatic
    # run. For instance, qt based examples
    tests_to_exclude = ['core_display_signal_slots.py',
                        'core_font_3d_console.py',
                        'core_display_overlayered_image.py',
                        'core_display_overlayered_lines.py',
                        'core_display_overlayered_text.py',
                        'core_display_raytracing.py',
                        'core_visualization_overpaint_viewer.py',
                        'core_display_click_to_point.py'
                        ]

    # remove examples to excludes
    for test_name in tests_to_exclude:
        test_fullpath = os.path.join('..', 'examples', test_name)
        if test_fullpath in all_examples_file_names:
            all_examples_file_names.remove(test_fullpath)
    # only store basenames
    all_examples_basenames = map(os.path.basename, all_examples_file_names)
    # returns the list of tests
    return all_examples_basenames

def get_example_category(example_name):
    """
    Returns display, or topology etc. that is to say the
    second term pf the name
    """
    return example_name.split("_")[1]

def run_example(example_name):
    """
    Execute the test from a subprocess, call all functions if any,
    get the screenshots generated from the offscreen renderer.
    """
    try:
        out = subprocess.check_output([sys.executable, example_name],
                                      stderr=subprocess.STDOUT,
                                      universal_newlines=True)
        print("%s [passed]" % example_name)
    except subprocess.CalledProcessError as cpe:
        print("%s" % cpe.output)
        print("%s [passed]" % example_name)

def export_example_to_rst(example_name):
    """ create a filename with the extension .rst
    """
    rst_filename = os.path.splitext(example_name)[0] + '.rst'
    rst_file = open(rst_filename, "w")
    ## write title. The title is infered from the example name
    example_title = example_name
    rst_file.write("%s\n" % example_name)
    st = ''.join(["=" for i in range(len(example_name))])
    rst_file.write("%s\n\n" % st)
    ## write abstract
    rst_file.write("Abstract\n^^^^^^^^\n\n")
    rst_file.write("to do\n\n")
    rst_file.write("------\n\n")
    ## launch
    rst_file.write("Launch the example\n^^^^^^^^^^^^^^^^^^\n\n")
    rst_file.write("  $ python %s\n\n" % example_name)
    rst_file.write("------\n\n")
    ## screenshots
    rst_file.write("\nScreenshots\n^^^^^^^^^^^\n\n\n")
    for image_file in get_screenshots_for_example(example_name):
        #print(image_file)
        rst_file.write("  .. image:: images/screenshots/%s\n\n" % os.path.basename(image_file))
    rst_file.write("------\n")
    ## code
    rst_file.write("\nCode\n^^^^\n\n")
    rst_file.write("\n.. code-block:: python\n\n")
    example_content = open(example_name, "r").readlines()
    for line_of_code in example_content[17:]:
        rst_file.write("  %s" % line_of_code)
    rst_file.close()

all_examples_basenames = get_all_available_examples()
for example_basename in all_examples_basenames:
    run_example(example_basename)
    export_example_to_rst(example_basename)
