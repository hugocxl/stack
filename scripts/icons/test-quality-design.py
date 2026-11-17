#!/usr/bin/env python3
"""Geometry regressions found during the full design-family visual review."""
from pathlib import Path
import string
import unittest
import xml.etree.ElementTree as ET

import draw as art

art.register_full_catalog()
ROOT = Path(__file__).resolve().parents[2]


def ink(name, style='stroke'):
    source = ROOT / 'icons' / 'styles' / style / f'{name}.svg'
    return art.union(*(art.path(node.get('d')) for node in ET.parse(source).getroot()))


class DesignQualityRegressionTests(unittest.TestCase):
    def test_circle_letters_keep_clear_space_inside_the_ring(self):
        # The former Q tail joined the ring; wide letters also crowded it.
        for letter in string.ascii_lowercase:
            name = f'circle-letter-{letter}'
            pieces = sorted(art.components(ink(name)), key=lambda p: p.area, reverse=True)
            self.assertGreaterEqual(len(pieces), 2, name)
            ring, mark = pieces[0], art.union(*pieces[1:])
            clearance = art.op(ring, art.stroke(mark, .8), art.po.PathOp.INTERSECTION)
            self.assertLess(clearance.area, .01, name)

    def test_between_arrows_do_not_join_either_panel(self):
        # Each icon must retain two distinct panels and one distinct arrow.
        for axis in ('horizontal', 'vertical'):
            for position in ('start', 'end'):
                name = f'between-{axis}-{position}'
                for style in ('solid', 'stroke'):
                    self.assertEqual(len(art.components(ink(name, style))), 3, (name, style))

    def test_backup_clock_clears_the_cloud_contour(self):
        # Previously the clock merged into the bottom of the cloud.
        pieces = sorted(art.components(ink('cloud-backup')), key=lambda p: p.area, reverse=True)
        self.assertEqual(len(pieces), 2)
        cloud, clock = pieces
        clearance = art.op(cloud, art.stroke(clock, .8), art.po.PathOp.INTERSECTION)
        self.assertLess(clearance.area, .01)

    def test_cuboid_has_no_rear_edge_through_its_top_face(self):
        shape = ink('cuboid')
        self.assertFalse(shape.contains((6, 4)))
        self.assertTrue(shape.contains((10, 10)))  # The visible vertical edge remains.


if __name__ == '__main__':
    unittest.main()
