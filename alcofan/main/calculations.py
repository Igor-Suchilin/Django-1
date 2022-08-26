'''Производит необходимые вычисления для сайта'''

from datetime import date

# вычилсяется количество дней от заданной даты до сегодня

start_date = date(2022, 9, 24)
now = date.today()
delta = start_date - now


# формируется правильное окончание (день, дня, дней)

words = ['день', 'дня', 'дней']
deys_left = ['остался', 'осталось']

def day_s(delta):
    if all((delta % 10 == 1, delta % 100 != 11)):
        return words[0], deys_left[0]
    elif all((2 <= delta % 10 <= 4, any((delta % 100 < 10, delta % 100 >= 20)))):
        return words[1], deys_left[1]
    return words[2], deys_left[1]
