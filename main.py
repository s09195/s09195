def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P14, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P14, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

濕度 = 0
basic.show_leds("""
    . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
""")
basic.show_leds("""
    . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
""")
pins.digital_write_pin(DigitalPin.P14, 0)

def on_forever():
    global 濕度
    濕度 = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(濕度)
    if 濕度 > 700:
        basic.show_icon(IconNames.SKULL)
        pins.digital_write_pin(DigitalPin.P14, 1)
    else:
        basic.show_icon(IconNames.HAPPY)
        pins.digital_write_pin(DigitalPin.P14, 0)
    basic.pause(2000)
basic.forever(on_forever)
