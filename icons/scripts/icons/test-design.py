#!/usr/bin/env python3
"""Design regressions discovered by the native per-icon visual audit.

Requires the pinned authoring dependencies, not needed by consumers.
"""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
import draw as art
art.register_full_catalog()

ROOT=Path(__file__).resolve().parents[2]
def layers(name,style='duotone'):
    p=ROOT/'icons'/((name+'.svg') if style=='duotone' else f'styles/{style}/{name}.svg')
    return [(art.path(n.get('d')),float(n.get('opacity','1'))) for n in ET.parse(p).getroot()]
def ink(name,style='solid'):return art.union(*(p for p,a in layers(name,style)))

class DesignRegressionTests(unittest.TestCase):
    def test_badge_family_has_one_symmetric_seal_and_clear_interior_marks(self):
        reference=art.DRAWINGS['badge'][0]
        for name,(body,detail,*_) in art.DRAWINGS.items():
            if name != 'badge' and not name.startswith('badge-'): continue
            self.assertLess(art.op(body,reference,art.po.PathOp.XOR).area,.01,name)
            self.assertLess(art.op(body,art.mirror(body),art.po.PathOp.XOR).area,.01,name)
            # Reserve at least half a unit between mark and inside contour.
            self.assertLess(art.op(detail,art.stroke(body,2.25),art.po.PathOp.INTERSECTION).area,.01,name)

    def test_currency_and_help_marks_clear_their_circular_borders(self):
        for name in ('dollar','euro','pound','circle-help'):
            body,detail,*_=art.DRAWINGS[name]
            self.assertLess(art.op(detail,art.stroke(body,2.25),art.po.PathOp.INTERSECTION).area,.01,name)

    def test_solid_ribbons_and_both_barrier_stripes_remain_visible(self):
        for name,points in [('gift',[(8,11),(5,9)]),('construction',[(5.5,7.5),(10.5,7.5)])]:
            for point in points:self.assertFalse(ink(name).contains(point),(name,point))

    def test_sofa_stroke_has_open_armrests(self):
        for point in [(3,9),(13,9)]:
            self.assertFalse(ink('sofa','stroke').contains(point),point)

    def test_recipe_check_accepts_identical_closed_contours_in_different_order(self):
        # Actual Linux/x86 output of the recipe that blocked the release. The
        # native ordering is derived from it so redrawing film cannot stale it.
        linux=(ROOT/'tests/fixtures/film-linux.svg').read_text()
        first=linux.split('d="',1)[1].split('"',1)[0]
        contours=[c+'Z' for c in first.split('Z') if c]
        native=linux.replace(first,''.join(reversed(contours)),1)
        self.assertNotEqual(native,linux)
        self.assertEqual(art.svg_comparison_key(native),art.svg_comparison_key(linux))
        # Geometry, winding, missing parts, opacity and layer order still matter.
        for changed in [linux.replace('13.375','13.4',1),
                        linux.replace('opacity="0.24"','opacity="0.25"'),
                        linux.replace('M5.675 13.375V2.625H10.325V13.375Z',''),
                        linux.replace('M5.675 13.375V2.625H10.325V13.375Z',
                                      'M5.675 13.375H10.325V2.625H5.675Z')]:
            self.assertNotEqual(art.svg_comparison_key(native),art.svg_comparison_key(changed))
        rows=linux.splitlines()
        rows[1],rows[2]=rows[2],rows[1]
        self.assertNotEqual(art.svg_comparison_key(native),art.svg_comparison_key('\n'.join(rows)+'\n'))

    def test_arrow_shafts_touch_their_heads(self):
        for direction in ['left','right','up','down','up-left','up-right','down-left','down-right']:
            name='arrow-'+direction
            b,d,*_=art.DRAWINGS[name]
            self.assertGreater(art.op(b,d,art.po.PathOp.INTERSECTION).area,.4,name)
            for style in ['duotone','solid','stroke']:
                self.assertEqual(len(art.components(ink(name,style))),1,(name,style))

    def test_redo_and_left_rotation_are_mirrored_not_rotated(self):
        for left,right in [('undo','redo'),('rotate-left','rotate-right')]:
            for style in ['duotone','solid','stroke']:
                diff=art.op(art.mirror(ink(left,style)),ink(right,style),art.po.PathOp.XOR)
                self.assertLess(diff.area,.015,(left,right,style))

    def test_rotation_arc_survives_without_a_faded_segment(self):
        # Previously a valid nonempty SVG lost almost its entire rotation arc.
        # The arc is now uniformly opaque, rather than a secondary tone.
        for name in ['refresh','reset','rotate-left','rotate-right']:
            source=layers(name)
            self.assertTrue(all(a==1 for p,a in source),name)
            shape=art.union(*(p for p,a in source))
            self.assertGreater(shape.area,25,name)
            self.assertGreater(shape.bounds[3]-shape.bounds[1],9,name)

    def test_linear_symbols_never_split_a_continuous_mark_into_tones(self):
        for name,(body,detail,outlined,*_) in art.DRAWINGS.items():
            if not outlined and name not in art.DUOTONE_GLYPHS:
                self.assertTrue(all(a==1 for p,a in layers(name)),name)
        # These examples define the public design rule, independently of the
        # recipe's outline flag or exception classification.
        for name in ['arrow-up','chevron-down','chevrons-right','minus','plus',
                     'close','check','hash','menu','wifi','bluetooth','paperclip']:
            self.assertTrue(all(a==1 for p,a in layers(name)),name)

    def test_surface_depth_remains_in_pencil_trash_and_layers(self):
        for name in ['pencil','trash','layers']:
            alpha={a for p,a in layers(name)}
            self.assertIn(1,alpha,name)
            self.assertTrue(any(0<a<1 for a in alpha),name)

    def test_monochrome_donut_keeps_its_sector_dividers(self):
        self.assertTrue(all(a==1 for p,a in layers('chart-donut')))
        shape=ink('chart-donut','duotone')
        for gap in [(8,3),(13,8),(8,8)]:
            self.assertFalse(shape.contains(gap),gap)
        for segment in [(5,4),(12,5),(8,13)]:
            self.assertTrue(shape.contains(segment),segment)

    def test_downward_trend_arrowhead_clears_the_baseline(self):
        # Removing opacity must not merge the down-arrow into the chart axis.
        for style in ['duotone','solid','stroke']:
            shape=ink('trending-down',style)
            self.assertFalse(shape.contains((12,12.7)),style)
            self.assertTrue(shape.contains((12,11.5)),style)
            self.assertTrue(shape.contains((12,14)),style)

    def test_structural_solid_connections_do_not_turn_into_cutout_fragments(self):
        for name in ['lock','trophy','network','workflow','watch','calendar','cpu','bug','signpost','syringe']:
            components=art.components(ink(name))
            self.assertEqual(len(components),1,(name,[p.area for p in components]))

    def test_counters_remain_open(self):
        for style in ['duotone','solid','stroke']:
            for name,point in [('settings',(8,8)),('chart-donut',(8,8)),('scissors',(4,4))]:
                self.assertFalse(ink(name,style).contains(point),(name,style))

    def test_solid_identifying_details_survive_structural_classification(self):
        for name,point in [('hourglass',(8,4.7)),('bed',(8,10)),('printer',(8,12)),('lungs',(5.5,8.5))]:
            self.assertFalse(ink(name).contains(point),name)
        # Overlapping cards have filled faces, with clearance around the rear.
        for name,point in [('copy',(9,9)),('folders',(8,10)),('airplay',(8,12))]:
            self.assertTrue(ink(name).contains(point),name)

    def test_rotational_families_are_symmetric(self):
        for name,angle in [('settings',45),('snowflake',60)]:
            shape=ink(name,'stroke')
            diff=art.op(shape,art.transform(shape,angle),art.po.PathOp.XOR)
            self.assertLess(diff.area,.08,name)

    def test_default_layers_do_not_compound_alpha(self):
        for name in art.DRAWINGS:
            source=layers(name)
            for i,(a,alpha) in enumerate(source):
                for b,beta in source[i+1:]:
                    overlap=art.op(a,b,art.po.PathOp.INTERSECTION).area
                    self.assertLess(overlap,.02,(name,overlap))

    def test_user_badges_have_clearance(self):
        for name in ('user-plus','user-check','user-x'):
            badge=art.DRAWINGS[name][1]
            for style in ('duotone','solid','stroke'):
                drawing=ink(name,style)
                person=art.op(drawing,badge,art.po.PathOp.DIFFERENCE)
                gap_zone=art.op(art.union(badge,art.stroke(badge,1.6)),badge,art.po.PathOp.DIFFERENCE)
                self.assertLess(art.op(person,gap_zone,art.po.PathOp.INTERSECTION).area,.02,(name,style))

    def test_solid_battery_charge_is_positive_ink(self):
        window=art.rr(3,6,8,4,.5)
        areas=[art.op(ink(name),window,art.po.PathOp.INTERSECTION).area
               for name in ('battery-empty','battery-low','battery-full')]
        self.assertLess(areas[0],.02)
        self.assertGreater(areas[1],5)
        self.assertGreater(areas[2],areas[1]*3)

    def test_non_special_default_compositions_preserve_ink(self):
        special={'airplay','user-plus','user-check','user-x','chart-donut','camera-off','microphone-off','bell-off','cloud-off','bluetooth-off','wifi-off','eye-off','ear-off'}
        for name,(body,detail,outlined,*_) in art.DRAWINGS.items():
            if name in special:continue
            # Explicit surface occlusion changes the intended ink, but must
            # still survive serialization without missing or added geometry.
            override=art.STYLE_OVERRIDES.get(name,{}).get('duotone')
            expected=(art.union(*(p for p,a in override)) if override is not None
                      else art.union(body,detail,art.stroke(body,1.25) if outlined else art.po.Path()))
            actual=ink(name,'duotone')
            self.assertLess(abs(expected.area-actual.area),.04,name)

    def test_airplay_foreground_is_separate_from_screen_in_every_style(self):
        # The lower bezel used to cross the casting triangle in default and
        # Stroke. Preserve an actual transparent gap, including in dark tint.
        for style in ('duotone','solid','stroke'):
            self.assertEqual(len(art.components(ink('airplay',style))),2,style)

if __name__=='__main__':unittest.main()
