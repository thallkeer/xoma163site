import random
import re
import threading

import pytz


def get_random_item_from_list(my_list, arg=None):
    rand_int = random.randint(0, len(my_list) - 1)
    if arg:
        msg = f"{arg}, ты {my_list[rand_int].lower()}"
    else:
        msg = my_list[rand_int]
    return msg


'''
DEPRECATED
'''


# Вероятность события в процентах
def random_probability(probability):
    if 1 > probability > 99:
        raise RuntimeError("Вероятность события должна быть от 1 до 99")
    rand_int = random.randint(1, 100)
    if rand_int <= probability:
        return True
    else:
        return False


def random_event(events, weights):
    # В принципе это необязательно
    if sum(weights) != 100:
        raise RuntimeError("Сумма вероятности событий должна равняться 100")
    return random.choices(events, weights=weights)


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def check_user_group(user, role):
    group = user.groups.filter(name=role)
    return group.exists()


def get_user_groups(user):
    groups = user.groups.all().values()
    return [group['name'] for group in groups]


def _send_messages_thread(vk_bot, users, message):
    for user in users:
        vk_bot.parse_and_send_msgs(user.user_id, message)


def send_messages(vk_bot, users, message):
    thread = threading.Thread(target=_send_messages_thread, args=(vk_bot, users, message,))
    thread.start()


def remove_tz(datetime):
    return datetime.replace(tzinfo=None)


def localize_datetime(datetime, tz):
    tz_obj = pytz.timezone(tz)
    return pytz.utc.localize(datetime, is_dst=None).astimezone(tz_obj)


def normalize_datetime(datetime, tz):
    tz_obj = pytz.timezone(tz)
    localized_time = tz_obj.localize(datetime, is_dst=None)

    tz_utc = pytz.timezone("UTC")
    return pytz.utc.normalize(localized_time, is_dst=None).astimezone(tz_utc)  # .replace(tzinfo=None)


def get_one_chat_with_user(chat_name, user_id):
    from apps.API_VK.models import VkChat
    chats = VkChat.objects.filter(name__icontains=chat_name)
    if len(chats) == 0:
        raise RuntimeError("Не нашёл такого чата")

    chats_with_user = []
    for chat in chats:
        user_contains = chat.vkuser_set.filter(user_id=user_id)
        if user_contains:
            chats_with_user.append(chat)

    if len(chats_with_user) == 0:
        raise RuntimeError("Не нашёл доступного чата с пользователем в этом чате")
    elif len(chats_with_user) > 1:
        chats_str = '\n'.join(chats_with_user)
        raise RuntimeError("Нашёл несколько чатов. Уточните какой:\n"
                           f"{chats_str}")

    elif len(chats_with_user) == 1:
        return chats_with_user[0]
