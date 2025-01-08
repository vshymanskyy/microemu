from machine import Pin
import micropython, time

D2 = const(2)

@micropython.viper
def compute(x, y):
    return x * y + 42

led = Pin(D2, Pin.OUT)
led.value(1)
time.sleep_ms(500)
led.value(0)
print('Answer:', compute(1, 0))
