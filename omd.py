
def yes_no():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )

    if yes_no():
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'День оказался дождливым. '
        'Утка, довольная своим решением, открыла зонт. '
        'По дороге она встретила друзей гусей-штукатуров. '
        'Пойти утке с гусями? '
    )
    if yes_no():
        print(
            'Гуси рассказали ей о плюсах своей работы. '
            'Теперь утка будет штукатуром. '
        )
    else:
        print(
            'Утка дошла до бара и села за стойку. '
            'Вдруг она увидела, как в бар вошел скелет. '
        )


def step2_no_umbrella():
    print(
        'День оказался дождливым. '
        'Утка, разочарованная своим решением, вернулась домой.'
    )


if __name__ == '__main__':
    step1()
