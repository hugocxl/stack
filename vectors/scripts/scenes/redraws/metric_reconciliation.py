from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, rule, standing_notebook

DESCRIPTION = "An open reconciliation ledger shows two equal totals side by side with a check badge beside them."


def draw(s):
    p = standing_notebook(s, 109, 86)
    chart_line(s, p, [(55, 71), (55, 10)], EDGE)
    for x, amounts in ((10, (17, 11, 14)), (63, (11, 14, 17))):
        rule(s, p, x, 66, 30, EDGE)
        for i, amount in enumerate(amounts):
            z = 51 - 10*i
            rule(s, p, x, z, 11, DETAIL)
            rule(s, p, x + 35 - amount, z, amount, DETAIL)
        rule(s, p, x, 23, 35, EDGE)
        rule(s, p, x + 11, 15, 24, EDGE)
    badge(s, "check", *p(115, 16), 13)
