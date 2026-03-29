import pytest
import sys
from main import main, convert

def test_convert():
    assert convert(1, 'km', 'm') == 0.001
    assert convert(1, 'm', 'km') == 1000
    assert convert(1, 'cm', 'm') == 100
    assert convert(1, 'm', 'cm') == 0.01
    assert convert(1, 'mm', 'm') == 1000
    assert convert(1, 'm', 'mm') == 0.001
    assert convert(1, 'ft', 'm') == 3.280839895013123
    assert convert(1, 'm', 'ft') == 0.3048
    assert convert(1, 'yd', 'm') == 1.0936132983377078
    assert convert(1, 'm', 'yd') == 0.9144
    assert convert(1, 'mi', 'm') == 0.0006213711922373339
    assert convert(1, 'm', 'mi') == 1609.344
    assert convert(1, 'kg', 'g') == 0.001
    assert convert(1, 'g', 'kg') == 1000
    assert convert(1, 'mg', 'g') == 1000
    assert convert(1, 'g', 'mg') == 0.001
    assert convert(1, 'oz', 'g') == 0.035273961949580414
    assert convert(1, 'g', 'oz') == 28.349523125
    assert convert(1, 'lb', 'g') == 0.002204622621848776
    assert convert(1, 'g', 'lb') == 453.59237
    assert convert(1, 'ton', 'g') == 1.102311310924388e-06
    assert convert(1, 'g', 'ton') == 907184.74

def test_invalid_conversion():
    with pytest.raises(ValueError):
        convert(1, 'km', 'kg')
    with pytest.raises(ValueError):
        convert(1, 'g', 'm')
    with pytest.raises(ValueError):
        convert(1, 'ft', 'kg')

def test_invalid_format():
    with pytest.raises(SystemExit):
        sys.argv = ['main.py', '-x', '1', 'm', 'km']
        main()

def test_non_numeric_value():
    with pytest.raises(SystemExit):
        sys.argv = ['main.py', 'abc', 'm', 'km']
        main()
