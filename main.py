import random

word_ukr = ['дедлайн', 'меню', 'лайк', 'ксерокс', 'барбершоп', 'топлес', 'планшет', 'шлагбаум', 'фотографія',
            'куки', 'портфоліо', 'лінк', 'кавер', 'селфі', 'віп-зона', 'попкорн', 'баг', 'рекрутер', 'руфер', 'гімн',
            'пазли', 'дауншифтинґ', 'скріншот', 'чизкейк', 'шарити', 'пікнік', 'гаджет', 'пост', 'шопінг', 'відео',
            'фідбек', 'рюкзак', 'армія', 'бюстгалтер', 'краудфандинґ', 'спіч', 'акаунт', 'челендж', 'івент', 'магазин',
            'булінг', 'графіті', 'аватар', 'лайфхак', 'смайл', 'брелок', 'клавіатура', 'юзер', 'тротуар', 'хайп',
            'браузер', 'абітуріє́нт', 'русифікація', 'фактор', 'аеродром', 'корпоратив', 'абсурд', 'пилосос', 'фільтр',
            'флешмоб', 'абзац', 'дах', 'тренінг', 'абсолютно', 'копія', 'контент', 'аплікація', 'хештег', 'фон',
            'блог', 'вау', 'фонтан', 'каліграфія', 'гелікоптер', 'бюджет', 'інтернет', 'фрик', 'шукати', 'мастрід',
            'прокрастинація', 'буккросинг', 'чипси', 'цвях', 'будувати', 'хейтер', 'лоукост', 'спойлер', 'моментально',
            'фарба', 'тінейджер', 'шлях', 'альтернатива', 'геній', 'уніформа', 'плаґін', 'парасолька', 'беквокал',
            'бібліотека', 'музика', 'юрист', 'дефект', 'стартап', 'швидкий', 'пательня', 'штопор', 'комікс',
            'автомобіль', 'форум', 'бутерброд', 'спікер', 'флірт', 'гарантія', 'аналіз', 'сайт', 'файл', 'прапор',
            'ліхтар', 'блокнот', 'аеропорт', 'дирижабль', 'хендмейд', 'футбол', 'шахта', 'результат', 'проблема',
            'рейтинг', 'принтер', 'аутсорсинґ', 'прикольний', 'банкомат', 'фільм']
author = input("Назвіть Ваше ім'я\n>>> ")


def word_function():
    player_answer = 2
    word = random.choice(word_ukr)
    new_word = '▮' * len(word)
    while player_answer:
        print(f'Є слово {new_word}, {author}. Вгадай.')
        massage_words = input(">>> ")
        massage_words = massage_words.lower()
        #  print(word)
        if massage_words == word:
            player_answer = 0
        else:
            if len(massage_words) > 1:
                print(f'По одній букві будь ласка')
                player_answer = 1
            elif massage_words in word:
                if word.count(massage_words) < 2:
                    w = word.find(massage_words)
                    new_word2 = new_word[:w]
                    new_word3 = new_word[w + 1:]
                    new_word = new_word2 + massage_words + new_word3
                else:
                    word_copy = word
                    alphab = []
                    while word_copy.count(massage_words):
                        w = word_copy.find(massage_words)
                        w = str(w)
                        alphab.append(w)
                        word_copy = word_copy.replace(massage_words, '5', 1)
                    for i in alphab:
                        i = int(i)
                        new_word2 = new_word[:i]
                        new_word3 = new_word[i + 1:]
                        new_word = new_word2 + massage_words + new_word3
            if new_word == word:
                player_answer = 0
            else:
                player_answer = 1
    print(f'Так це {word}')
    ans = input('Спробуєш ще раз? y/else\n>>> ').lower()
    if ans == 'y':
        word_function()
    else:
        print(f'Дякую за гру, {author}!')


word_function()
