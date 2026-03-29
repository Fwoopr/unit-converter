# Unit Converter

A command-line unit converter supporting length and mass conversions across SI and imperial units, with optional scientific notation and 10-based output formatting.

---

## Usage
 
```bash
unit-converter <value> <unit_from> <unit_to>
unit-converter <format> <value> <unit_from> <unit_to>
```
 
### Examples
 
```bash
unit-converter 5 km m
# 5.0 km is equal to 5000.0 m
 
unit-converter -e 5 km m
# 5.00e+00 km is equal to 5.00e+03 m
 
unit-converter -10x 0.003 m mm
# 3.00 x 10^-3 m is equal to 3.00 x 10^0 mm
```

### Format Flags
| Flag | Description |
|------|-------------|
| *(none)* | Standard decimal output |
| `-e` | Scientific notation |
| `-10x` | 10-based notation (e.g. `3.00 x 10^3`) |

---

## Supported Units

### Length (base: meter)
SI prefixes from km down to pm, plus imperial units: `in`, `ft`, `yd`, `mi`

### Mass (base: gram)
SI prefixes from kg down to pg, plus imperial units: `oz`, `lb`, `ton`

### Energy (base: joule)
Joule, calories, `kWh` and `eV`

### Frequency (base: Hz)
`Hz` to `GHz`

---

## Installation
 
```bash
pip install .
unit-converter 5 km m
```
 
---
## Project Structure
```
unit-converter/
├── main.py    
├── units.py     
├── test_main.py 
└── README.md
```
 
---
 
## Testing
 
```bash
pytest test_unit_converter.py
```

## How It Works

All units are stored as conversion factors relative to a base unit (meter for length, gram for mass). Converting from `unit_from` to `unit_to` is a single multiplication:

```python
value * (units[unit_from] / units[unit_to])
```

---



## Skills
`Python` `CLI` `sys.argv` `Modular Design`
