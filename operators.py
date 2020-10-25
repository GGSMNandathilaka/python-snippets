"""
comparison operators

ex: 1
if temperature is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold

ex. 2
If name is less than 3 characters long -> name must be at least 3 characters
Otherwise if it's more than 50 characters long -> name can be a maximum of 50 characters
Otherwise -> name looks good !
"""


def run_operators_temp(temp):
    if temp > 30:
        print('it''s a hot day')
    elif temp < 10:
        print('it''s a cold day')
    else:
        print('it''s neither hot nor cold')


def run_operators_name(name):
    if len(name) < 3:
        print('Name must be at least 3 characters')
    elif len(name) > 50:
        print('Name can be a maximum of 50 characters')
    else:
        print('Name looks good !')


if __name__ == '__main__':
    # run_operators_temp(30)
    run_operators_name('Shehan Nandathilaka')
