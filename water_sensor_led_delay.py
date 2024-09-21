# connect the two pins in the sensor to the two on the amplifier
# on amplifier to pico, connect the Vcc to the Vbus, Gnd to Gnd, AO to GP26, and DO to Gnd
import machine
import utime

led_green = machine.Pin(1, machine.Pin.OUT)
led_red = machine.Pin(14, machine.Pin.OUT)
adc = machine.ADC(26)
conversion_factor = 100 / (65535)

while True:
    moisture = 130 - (adc.read_u16() * conversion_factor)
    print("Moisture: ", round(moisture, 1), "% - ", utime.localtime())
    
    if moisture >= 70 :
        led_red.value(1)
        led_green.value(0)
        utime.sleep(30)
    elif moisture < 70 :
        led_green.value(1)
        led_red.value(0)
        utime.sleep_ms(5000)
        led_green.value(0)
        utime.sleep_ms(115000)