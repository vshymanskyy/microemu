#!/usr/bin/env python
import time, os, json, sys, asyncio, builtins

class utime:
    @staticmethod
    def ticks_us():
        return int(time.time() * 1000000)

    @staticmethod
    def ticks_ms():
        return int(time.time() * 1000)

    @staticmethod
    def ticks_diff(ticks1, ticks2):
        return ticks1 - ticks2

    @staticmethod
    def ticks_add(ticks1, ticks2):
        return ticks1 + ticks2

    @staticmethod
    def sleep_ms(x):
        time.sleep(x / 1000)

    @staticmethod
    def sleep_us(x):
        raise NotImplementedError()

class uasyncio:
    @staticmethod
    async def sleep_ms(x):
        await asyncio.sleep(x / 1000)

class machine:
    class Pin:
        IN = 0
        OUT = 1
        PULL_UP = 2
        PULL_DOWN = 3

        def __init__(self, pin, mode=IN, pull=None):
            self.pin = pin
            self.mode = mode
            self.pull = pull
            self.state = 0
            print(f"Initialized Pin {pin} with mode {mode}, pull {pull}")

        def value(self, val=None):
            if val is None:
                print(f"Reading value from Pin {self.pin}: {self.state}")
                return self.state
            else:
                print(f"Setting value of Pin {self.pin} to {val}")
                self.state = val

    class ADC:
        def __init__(self, pin):
            self.pin = pin
            print(f"Initialized ADC on Pin {pin}")

        def read(self):
            value = int(time.time() * 1000) % 1024
            print(f"ADC read value from Pin {self.pin}: {value}")
            return value

    @staticmethod
    def reset():
        print("Machine reset.")
        sys.exit(1)

    @staticmethod
    def freq(hz=None):
        if hz:
            print(f"Setting CPU frequency to {hz} Hz.")
        else:
            return 160000000  # Default to 160 MHz for simulation

class network:
    pass

class micropython:
    @staticmethod
    def const(x):
        return x

def _patch(orig, micro):
    for attr in dir(micro):
        if not attr.startswith("_"):
            setattr(orig, attr, getattr(micro, attr))

def inject_shim():
    _patch(time, utime)
    _patch(asyncio, uasyncio)

    sys.modules["utime"] = time
    sys.modules["uos"] = os
    sys.modules["ujson"] = json
    sys.modules["uasyncio"] = asyncio
    sys.modules["machine"] = machine
    sys.modules["network"] = network
    sys.modules["micropython"] = micropython

    builtins.const = micropython.const

def main():
    sys.path.append(os.getcwd())

    inject_shim()

    if len(sys.argv) < 2:
        import code, readline, rlcompleter
        readline.parse_and_bind("tab: complete")
        code.interact("MicroPython emulation")
        sys.exit(0)

    script_name = sys.argv[1]
    script_args = sys.argv[2:]

    # Modify sys.argv to match the target script's expectations
    sys.argv = [script_name] + script_args

    # Load and execute the script
    try:
        import runpy
        runpy.run_path(script_name, run_name="__main__")
    except FileNotFoundError:
        print(f"Error: File '{script_name}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
