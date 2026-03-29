import sys
from units import units

def main():
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Usage: <format> <value> <unit> <target_unit>")
        sys.exit(1)

    if len(sys.argv) == 4:
        unit_to = sys.argv[3].lower()
        try:
            value = float(sys.argv[1])
        except ValueError:
            print("Value must be a number.")
            sys.exit(2)
        unit_from = sys.argv[2].lower()
        converted_value = convert(value, unit_to, unit_from)
        print(f"{value} {unit_from} is equal to {converted_value} {unit_to}")

    elif len(sys.argv) == 5:
        format = sys.argv[1].lower()
        unit_to = sys.argv[4].lower()
        try:
            value = float(sys.argv[2])
        except ValueError:
            print("Value must be a number.")
            sys.exit(2)
        unit_from = sys.argv[3].lower()
        converted_value = convert(value, unit_to, unit_from)
        if format == '-e':
            print(f"{value:.2e} {unit_from} is equal to {converted_value:.2e} {unit_to}")
        elif format == '-10x':
            print(f"{tenx_format(value)} {unit_from} is equal to {tenx_format(converted_value)} {unit_to}")
        else:
            sys.exit(1)
            print('Invalid format. Use -e for scientific notation or -10x for 10-based notation.')

def convert(value, unit_to, unit_from='m'):
    for category in units:
        if unit_from in units[category] and unit_to in units[category]:
            return value * (units[category][unit_from] / units[category][unit_to])
    raise ValueError(f"Conversion from {unit_from} to {unit_to} is not supported.")

def tenx_format(value):
    exponent = 0
    if value >= 10:
        while value >= 10:
            value /= 10
            exponent += 1
    elif value < 1:
        while value < 1:
            value *= 10
            exponent -= 1
    return f"{value:.2f} x 10^{exponent}"
    



if __name__ == "__main__":
    main()