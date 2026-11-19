from scenes.redraws.on_site_arrival_alert import service_van

DESCRIPTION = "A service van has a tool-compartment latch and a location pin printed on its sliding panel."


def draw(s):
    service_van(s, tracking=True)
