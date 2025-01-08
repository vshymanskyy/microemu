# microemu

A simple MicroPython emulator.
It monkey-patches `Python 3` default environment, adding `MicroPython`-specific functionality:

- `micropython`
  - const, viper, native
- `time`
  - ticks_us, ticks_ms, ticks_diff, ticks_add
  - sleep_ms, sleep_us
- `asyncio`
  - sleep_ms
- `machine`
  - Pin, ADC, reset, freq
- `gc`
  - mem_alloc, mem_free
- `network` (empty for now)

## Installing

```sh
pip3 install -U microemu
```

## Usage

```sh
# Run script
microemu examples/script.py arg1 arg2

# Run REPL
microemu
```
