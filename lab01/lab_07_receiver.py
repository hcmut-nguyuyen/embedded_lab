def on_received_number(receivedNumber):
    global temp
    temp = receivedNumber
radio.on_received_number(on_received_number)

temp = 0
radio.set_group(136)

def on_forever():
    if temp > 40:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.pause(500)
        basic.clear_screen()
        basic.pause(500)
    else:
        basic.clear_screen()
basic.forever(on_forever)
