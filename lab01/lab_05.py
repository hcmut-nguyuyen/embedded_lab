edge = 0

def on_forever():
    global edge
    edge = input.compass_heading()
    if edge < 45:
        basic.show_arrow(ArrowNames.NORTH)
    else:
        if edge < 135:
            basic.show_arrow(ArrowNames.EAST)
        else:
            if edge < 225:
                basic.show_arrow(ArrowNames.SOUTH)
            else:
                if edge < 315:
                    basic.show_arrow(ArrowNames.WEST)
                else:
                    basic.show_arrow(ArrowNames.NORTH)
basic.forever(on_forever)
