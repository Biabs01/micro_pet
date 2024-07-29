def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . # . .
        . . . . .
        . . . # .
        . # # . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        . . # . .
        . . . . .
        """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    basic.show_leds("""
        . . . . .
        . # . # .
        # # . # #
        . . . . .
        . # # # .
        """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . # . # .
        . # # # .
        . # # # .
        . . # . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(500)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . #
        . . . . .
        . # . . .
        . . # # .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_string("Oi!")
    basic.pause(1000)
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        . # # # .
        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . . # #
        # # . # #
        . . . . .
        # . . . .
        . # # # .
        """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    basic.show_leds("""
        . # . # .
        . . . . .
        # # # # #
        # . . . #
        . # # # .
        """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_forever():
    basic.pause(input.running_time())
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        # # . # #
        . . . . .
        . # # # .
        . . . . .
        """)
basic.forever(on_forever)
