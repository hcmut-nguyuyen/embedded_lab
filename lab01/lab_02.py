basic.show_icon(IconNames.HEART)
basic.pause(2000)

def on_forever():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # . # .
        # . . . #
        . . . . .
        # . . . #
        . # . # .
        """)
    basic.pause(100)
    basic.show_leds("""
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        """)
    basic.pause(100)
basic.forever(on_forever)
