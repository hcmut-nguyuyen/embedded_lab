def on_gesture_tilt_left():
    basic.show_number(3)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    basic.show_number(1)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    basic.show_number(2)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_tilt_right():
    basic.show_number(4)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_forever():
    pass
basic.forever(on_forever)
