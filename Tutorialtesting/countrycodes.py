def get_CountryCodes(code=None):

    country_dict = {
        'US': {
            'name': 'United States of America'
        },
        'DN': {
            'name': 'Denmark'
        },
        'KE': {
            'name': 'Kenya'
        },
        'TZ': {
            'name': 'Tanzania'
        },
        'UG': {
            'name': 'Uganda'
        },
        'UK': {
            'name': 'United Kingdom'
        },
        'EN': {
            'name': 'England'
        },
    }
    if type(code) != str:
        raise TypeError('Code must be a string')
    elif len(code) != 2:
        raise ValueError('country code must be two characters long')

    if code in country_dict:
        return True, country_dict[code]
    else:
        return False, None
print(get_CountryCodes('TZ'))