import pytest
import sys
from main import main, convert

def test_convert():
    # Length conversions
    assert convert(1, 'km', 'm') == 0.001
    assert convert(1, 'm', 'km') == 1000
    assert convert(1, 'hm', 'm') == 0.01
    assert convert(1, 'm', 'hm') == 100.0
    assert convert(1, 'dam', 'm') == 0.1
    assert convert(1, 'm', 'dam') == 10.0
    assert convert(1, 'dm', 'm') == 10.0
    assert convert(1, 'm', 'dm') == 0.1
    assert convert(1, 'cm', 'm') == 100
    assert convert(1, 'm', 'cm') == 0.01
    assert convert(1, 'mm', 'm') == 1000
    assert convert(1, 'm', 'mm') == 0.001
    assert convert(1, 'in', 'm') == 39.37007874015748
    assert convert(1, 'm', 'in') == 0.0254
    assert convert(1, 'ft', 'm') == 3.280839895013123
    assert convert(1, 'm', 'ft') == 0.3048
    assert convert(1, 'yd', 'm') == 1.0936132983377078
    assert convert(1, 'm', 'yd') == 0.9144
    assert convert(1, 'mi', 'm') == 0.0006213711922373339
    assert convert(1, 'm', 'mi') == 1609.344
    
    # Mass conversions
    assert convert(1, 'kg', 'g') == 0.001
    assert convert(1, 'g', 'kg') == 1000
    assert convert(1, 'hg', 'g') == 0.01
    assert convert(1, 'g', 'hg') == 100.0
    assert convert(1, 'dag', 'g') == 0.1
    assert convert(1, 'g', 'dag') == 10.0
    assert convert(1, 'dg', 'g') == 10.0
    assert convert(1, 'g', 'dg') == 0.1
    assert convert(1, 'cg', 'g') == 100.0
    assert convert(1, 'g', 'cg') == 0.01
    assert convert(1, 'mg', 'g') == 1000
    assert convert(1, 'g', 'mg') == 0.001
    assert convert(1, 'oz', 'g') == 0.035273961949580414
    assert convert(1, 'g', 'oz') == 28.349523125
    assert convert(1, 'lb', 'g') == 0.002204622621848776
    assert convert(1, 'g', 'lb') == 453.59237
    assert convert(1, 'ton', 'g') == 1.102311310924388e-06
    assert convert(1, 'g', 'ton') == 907184.74
    
    # Energy conversions
    assert convert(1, 'kJ', 'J') == 0.001
    assert convert(1, 'J', 'kJ') == 1000
    assert convert(1, 'cal', 'J') == 1 / 4.184
    assert convert(1, 'J', 'cal') == 4.184
    assert convert(1, 'kcal', 'J') == 1 / 4184.0
    assert convert(1, 'J', 'kcal') == 4184.0
    assert convert(1, 'kWh', 'J') == 1 / 3600000.0
    assert convert(1, 'J', 'kWh') == 3600000.0
    
    # Frequency conversions
    assert convert(1, 'kHz', 'Hz') == 0.001
    assert convert(1, 'Hz', 'kHz') == 1000
    assert convert(1, 'MHz', 'Hz') == 1e-6
    assert convert(1, 'Hz', 'MHz') == 1e6
    assert convert(1, 'GHz', 'Hz') == 1e-9
    assert convert(1, 'Hz', 'GHz') == 1e9

def test_invalid_conversion():
    # Length to mass conversions should fail
    with pytest.raises(ValueError):
        convert(1, 'km', 'kg')
    with pytest.raises(ValueError):
        convert(1, 'g', 'm')
    with pytest.raises(ValueError):
        convert(1, 'ft', 'kg')
    # Length to energy conversions should fail
    with pytest.raises(ValueError):
        convert(1, 'km', 'J')
    # Mass to frequency conversions should fail
    with pytest.raises(ValueError):
        convert(1, 'g', 'Hz')
    # Energy to frequency conversions should fail
    with pytest.raises(ValueError):
        convert(1, 'J', 'Hz')

def test_invalid_format():
    with pytest.raises(SystemExit):
        sys.argv = ['main.py', '-x', '1', 'm', 'km']
        main()

def test_non_numeric_value():
    with pytest.raises(SystemExit):
        sys.argv = ['main.py', 'abc', 'm', 'km']
        main()
