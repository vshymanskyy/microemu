# microemu

A simple MicroPython emulator.
It monkey-patches `Python 3` default environment, adding `MicroPython`-specific functionality:

- `micropython`
  - const
- `time`
  - ticks_us
  - ticks_ms
  - ticks_diff
  - ticks_add
  - sleep_ms
  - sleep_us (dummy)
- `asyncio`
  - sleep_ms
- `machine`
  - Pin
  - ADC
  - reset
  - freq
- `network` (dummy)

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
