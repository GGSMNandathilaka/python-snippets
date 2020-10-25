"""
====================================
==========WEIGHT-CONVERTER==========
====================================
"""


def convert_weight(weight, unit):
    multiplier = 0
    unit_text = ''
    if unit.upper() == 'L':
        multiplier = 0.45
        unit_text = 'kilos'
    elif unit.upper() == 'K':
        multiplier = 2.20
        unit_text = 'pounds'
    else:
        print('invalid unit')

    tot_weight = multiplier * float(weight)
    print(f'You are {tot_weight} {unit_text}')


if __name__ == '__main__':
    weight = input('Weight: ')
    unit = input('Enter unit (L/K): ')
    convert_weight(weight, unit)
