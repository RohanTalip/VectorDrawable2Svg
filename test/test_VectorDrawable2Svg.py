
from unittest import TestCase

from drawable2svg.VectorDrawable2Svg import convert_vector_drawable_stream


class VectorDrawable2SvgTestCase(TestCase):

    def test_convert_xml_stream_to_svg(self):

        with open('data/ic_launcher.xml', 'rb') as icon_xml:
            with open('data/colors.xml', 'rb') as colors_xml:
                svg = convert_vector_drawable_stream(icon_xml, colors_xml)

        self.assertTrue('<svg' in svg)
        self.assertTrue('</svg>' in svg)
