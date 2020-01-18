from apps.API_VK.command.CommonCommand import CommonCommand
from apps.API_VK.models import Words


def get_from_db(field_name):
    my_field = {field_name + "__isnull": False, 'type': 'good'}
    try:
        word = getattr(Words.objects.filter(**my_field).order_by('?').first(), field_name).lower()
    except AttributeError:
        word = "Нет такого слова :("
    except Exception as e:
        word = "Нет такого слова :( Ошибочка - {}".format(str(e))
    return word


def add_phrase_before(recipient, word, field_name):
    if field_name[1] == '1':
        return "{}, ты {}".format(recipient, word)
    elif field_name[1] == 'm':
        return "{}, вы {}".format(recipient, word)
    else:
        return "EXCEPTION LOLOLOL"


def check_key(keys, translator):
    for key in keys:
        if key in translator:
            return key
    return False


class Praise(CommonCommand):
    def __init__(self):
        names = ["похвалить", "похвали", "хвалить"]
        help_text = "̲П̲о̲х̲в̲а̲л̲и̲т̲ь [N[,M] - рандомная похвала. N - что-то/род и число, M - род и число"
        super().__init__(names, help_text)

    def start(self):
        translator = {
            'м': 'm1',
            'ж': 'f1',
            'с': 'n1',
            'м1': 'm1',
            'ж1': 'f1',
            'с1': 'n1',
            'мм': 'mm',
            'жм': 'fm'
        }
        if self.vk_event.keys:
            key = check_key(self.vk_event.keys, translator)
            if key:
                translator_key = key
            else:
                msg = "Неверные ключи определения пола и числа. Доступные: {}".format(str(list(translator.keys())))
                return msg
        else:
            if self.vk_event.params_without_keys:
                try:
                    user = self.vk_bot.get_user_by_name([self.vk_event.params_without_keys])
                    if user.gender == '1':
                        translator_key = 'ж1'
                    else:
                        translator_key = 'м1'
                except Exception as e:
                    translator_key = 'м1'
            else:
                translator_key = 'м1'

        if self.vk_event.params_without_keys:
            recipient = self.vk_event.params_without_keys
            if "петрович" in recipient:
                msg = "спс))"
            else:
                word = get_from_db(translator[translator_key])
                msg = add_phrase_before(recipient, word, translator[translator_key])
        else:
            msg = get_from_db(translator[translator_key])
        return msg
