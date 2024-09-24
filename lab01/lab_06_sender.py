def on_gesture_tilt_left():
    radio.send_number(1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_shake():
    radio.send_number(3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    radio.send_number(2)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

radio.set_group(136)