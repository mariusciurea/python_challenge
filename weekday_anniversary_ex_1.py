from datetime import date

def get_weekday(n: str, birthday: str) -> date.weekday:
    '''
    birthday: yyyy-mm-dd
    :param n:
    :param birthday:
    :return: date object - weekday anniversary
    '''
    WEEKDAY = {0:'Luni', 1:'Marti', 2:'Miercuri', 3:'Joi',
               4:'Vineri', 5:'Sambata', 6:'Duminica'}
    try:
        years = int(n)
    except ValueError as e:
        print(f'A aparut aceasta eroare: -> {e}. '
              f'Anul trebuie sa fie un numar')
    else:
        current_year = date.today().year
        birthday = f'{current_year + years}{birthday[birthday.find("-")::]}'
        return WEEKDAY[date.fromisoformat(birthday).weekday()]

if __name__ == '__main__':
    n = input('number of years: ')
    birthday = input('your birthday: ')
    day = get_weekday(n, birthday)
    print(day)