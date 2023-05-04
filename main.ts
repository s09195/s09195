input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P14, 1)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P14, 0)
})
let 濕度 = 0
basic.showLeds(`
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    `)
basic.showLeds(`
    . # . # .
    # # # # #
    # # # # #
    . # # # .
    . . # . .
    `)
pins.digitalWritePin(DigitalPin.P14, 0)
basic.forever(function () {
    濕度 = pins.analogReadPin(AnalogPin.P0)
    basic.showNumber(濕度)
    if (濕度 > 700) {
        basic.showIcon(IconNames.Skull)
        pins.digitalWritePin(DigitalPin.P14, 1)
    } else {
        basic.showIcon(IconNames.Happy)
        pins.digitalWritePin(DigitalPin.P14, 0)
    }
    basic.pause(5000)
})
