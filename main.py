suma = 0
promedio = 0
porcentaje = 0

def on_forever():
    global suma, promedio, porcentaje
    # 1. ALGORITMO BARRENDERO (Filtro por promedio de 10 lecturas)
    suma = 0
    for index in range(10):
        suma += pins.analog_read_pin(AnalogPin.P0)
        basic.pause(20)
    promedio = suma / 10
    # 2. CONVERSIÓN A PORCENTAJE (De 0-1023 a 0%-100%)
    porcentaje = Math.round(promedio / 1023 * 100)
    # 3. REGLA DE SEGURIDAD (Alarma si supera el 30%)
    if porcentaje > 30:
        basic.show_icon(IconNames.NO)
        music.play_tone(523, music.beat(BeatFraction.HALF))
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)
