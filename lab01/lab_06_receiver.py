def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_arrow(ArrowNames.WEST)
        basic.clear_screen()
    elif receivedNumber == 2:
        basic.show_arrow(ArrowNames.EAST)
        basic.clear_screen()
    elif receivedNumber == 3:
        basic.show_icon(IconNames.TARGET)
        basic.clear_screen()
    else:
        pass
radio.on_received_number(on_received_number)

radio.set_group(136)