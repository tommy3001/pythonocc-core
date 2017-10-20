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
                        'core_visualization_overpaint_viewer.py'
                        ]

    # remove examples to excludes
    for test_name in tests_to_exclude:
        test_fullpath = os.path.join('..', 'examples', test_name)
        if test_fullpath in all_examples_file_names:
            all_examples_file_names.remove(test_fullpath)
    # returns the list of tests
    return all_examples_file_names

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
    print("running %s ..." % example_name, end="")
    try:
        out = subprocess.check_output([sys.executable, example_name],
                                      stderr=subprocess.STDOUT,
                                      universal_newlines=True)
        print("[passed]")
    except subprocess.CalledProcessError as cpe:
        print("%s" % cpe.output)
        print("[failed]")

def export_example_to_rst(example_name):
    """ create a filename with the extension .rst
    """
    rst_filename = os.path.splitext(example_name)[0] + '.rst'
    rst_file = open(rst_filename, "w")
    ## write title. The title is infered from the example name
    example_title = example_name
    rst_file.write("%s\n" % example_name)
    rst_file.write("============\n\n")
    ## write abstract
    rst_file.write("Abstract\n---\n\n")
    ## launch
    rst_file.write("Howto launch the example ::\n\n")
    rst_file.write("  $ python %s\n" % example_name)
    ## output
    #rst_file.write()
    ## code
    rst_file.write("Code\n\n")
    example_content = open(example_name, "r").readlines()
    for line_of_code in example_content:
        rst_file.write("  %s" % line_of_code)
    rst_file.close()

#assert get_example_category("core_visualization_overpaint_viewer.py") == "visualization"

#examples = get_all_available_examples()
#print(examples)
run_example('core_helloworld.py')
export_example_to_rst('core_helloworld.py')