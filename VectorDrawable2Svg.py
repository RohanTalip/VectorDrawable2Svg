"""
VectorDrawable2Svg
This script convert your VectorDrawable to a Svg
Author: Alessandro Lucchet

Usage: drop one or more vector drawable onto this script to convert them to svg format
"""

from xml.dom.minidom import *
import sys


# extracts all paths inside vd_container and add them into svg_container
def convert_paths(vd_container, svg_container, svg_xml):
    vd_paths = vd_container.getElementsByTagName('path')
    for vd_path in vd_paths:
        # only iterate in the first level
        if vd_path.parentNode == vd_container:
            svg_path = svg_xml.createElement('path')
            svg_path.attributes['d'] = vd_path.attributes[
                'android:pathData'].value
            if vd_path.hasAttribute('android:fillColor'):
                svg_path.attributes['fill'] = vd_path.attributes[
                    'android:fillColor'].value
            else:
                svg_path.attributes['fill'] = 'none'
            if vd_path.hasAttribute('android:strokeLineJoin'):
                svg_path.attributes['stroke-linejoin'] = vd_path.attributes[
                    'android:strokeLineJoin'].value
            if vd_path.hasAttribute('android:strokeLineCap'):
                svg_path.attributes['stroke-linecap'] = vd_path.attributes[
                    'android:strokeLineCap'].value
            if vd_path.hasAttribute('android:strokeMiterLimit'):
                svg_path.attributes['stroke-miterlimit'] = vd_path.attributes[
                    'android:strokeMiterLimit'].value
            if vd_path.hasAttribute('android:strokeWidth'):
                svg_path.attributes['stroke-width'] = vd_path.attributes[
                    'android:strokeWidth'].value
            if vd_path.hasAttribute('android:strokeColor'):
                svg_path.attributes['stroke'] = vd_path.attributes[
                    'android:strokeColor'].value
            svg_container.appendChild(svg_path)


# define the function which converts a vector drawable to a svg
def convert_vector_drawable(vd_file_path):

    # create svg xml
    svg_xml = Document()
    svg_node = svg_xml.createElement('svg')
    svg_xml.appendChild(svg_node)

    # open vector drawable
    vd_xml = parse(vd_file_path)
    vd_node = vd_xml.getElementsByTagName('vector')[0]

    # setup basic svg info
    svg_node.attributes['xmlns'] = 'http://www.w3.org/2000/svg'
    svg_node.attributes['width'] = vd_node.attributes[
        'android:viewportWidth'].value
    svg_node.attributes['height'] = vd_node.attributes[
        'android:viewportHeight'].value
    svg_node.attributes['viewBox'] = '0 0 {} {}'.format(
        vd_node.attributes['android:viewportWidth'].value,
        vd_node.attributes['android:viewportHeight'].value)

    # iterate through all groups
    vd_groups = vd_xml.getElementsByTagName('group')
    for vd_group in vd_groups:

        # create the group
        svg_group = svg_xml.createElement('g')

        # setup attributes of the group
        if vd_group.hasAttribute('android:translateX'):
            svg_group.attributes['transform'] = 'translate({},{})'.format(
                vd_group.attributes['android:translateX'].value,
                vd_group.attributes['android:translateY'].value)

        # iterate through all paths inside the group
        convert_paths(vd_group, svg_group, svg_xml)

        # append the group to the svg node
        svg_node.appendChild(svg_group)

    # iterate through all svg-level paths
    convert_paths(vd_node, svg_node, svg_xml)

    # write xml to file
    svg_xml.writexml(
        open(vd_file_path + '.svg', 'w'), indent="", addindent="  ", newl='\n')


# script begin
if len(sys.argv) > 1:
    iter_args = iter(sys.argv)
    next(iter_args)  #skip the first entry (it's the name of the script)
    for arg in iter_args:
        convert_vector_drawable(arg)
else:
    print("You have to pass me something")
    sys.exit()
