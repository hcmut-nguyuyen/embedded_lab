radio.set_group(136)

def on_forever():
    radio.send_number(input.temperature())
    basic.pause(1000)
basic.forever(on_forever)
