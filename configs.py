CATEGORIES={
    'Президент':'president',
    'Происшествия':'incidents',
    'Политика':'policy',
    'Общество':'obshestvo',
    'Экономика':'economy',
    'Мысли вслух':'misli',
    'Спорт':'sport',
    'Культура':'culture'
}



def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v