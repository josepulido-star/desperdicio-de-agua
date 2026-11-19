let suma = 0
let promedio = 0
let porcentaje = 0
basic.forever(function () {
    // 1. ALGORITMO BARRENDERO (Filtro por promedio de 10 lecturas)
    suma = 0
    for (let index = 0; index < 10; index++) {
        suma += pins.analogReadPin(AnalogPin.P0)
        basic.pause(20)
    }
    promedio = suma / 10
    // 2. CONVERSIÓN A PORCENTAJE (De 0-1023 a 0%-100%)
    porcentaje = Math.round(promedio / 1023 * 100)
    // 3. REGLA DE SEGURIDAD (Alarma si supera el 30%)
    if (porcentaje > 30) {
        basic.showIcon(IconNames.No)
        music.playTone(523, music.beat(BeatFraction.Half))
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
