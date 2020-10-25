"""
comparison operators

if temperature is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold
"""


def run_operators(temp):
    if temp > 30:
        print('it''s a hot day')
    elif temp < 10:
        print('it''s a cold day')
    else:
        print('it''s neither hot nor cold')


if __name__ == '__main__':
    run_operators(30)
