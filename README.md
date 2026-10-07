# hex2binndec

A tiny Python CLI that converts hexadecimal values to binary and decimal.

## Usage

```bash
python3 main.py
```

Type one hex value per line (no `0x` prefix):

```
E8
BIN: 1110 1000
DEC:  232
```

The binary output is grouped into 4-bit nibbles, one per hex digit.

Input ends on EOF (`Ctrl+D`) or an empty line. You can also pipe a file:

```bash
python3 main.py < input.txt
```

## Limitations

- Input is not validated: a non-hex character (e.g. `G`, or a `0x` prefix) raises `ValueError` and the program exits.
- Processing stops at the first blank line.

## Requirements

Python 3.6+ (uses f-strings). No external packages.
