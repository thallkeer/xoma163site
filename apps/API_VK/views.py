import datetime
import json

from django.http import HttpResponse

from apps.API_VK.models import VkChatId, TrustIMEI, Log
from xoma163site.wsgi import vkbot


def where_is_me(request):
    log = Log.objects.create()
    tries = 0
    response_data = []
    while log.success is not True and tries < 10:
        try:
            event = request.GET.get('where', None)
            log.event = event
            imei = request.GET.get('imei', None)
            log.imei = imei
            author = check_imei(imei)
            log.author = author
            if author is None:
                log.msg = "Wrong IMEI"
                log.save()
                return HttpResponse(json.dumps({'success': True, 'error': 'Wrong IMEI'}, ensure_ascii=False),
                                    content_type="application/json")

            dictionary_on = {'home': 'дома', 'work': 'на работе'}
            dictionary_from = {'home': 'из дома', 'work': 'с работы'}

            today = datetime.datetime.now()
            today_logs = Log.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day,
                                            author=author)
            count_work = 0
            count_home = 0
            # ToDo: Тяжелая операция для базы
            for today_log in today_logs:
                if today_log.event == 'work':
                    count_work += 1
                if today_log.event == 'home':
                    count_home += 1

            msg = None
            if event == 'work':
                if count_work % 2 == 0:
                    msg = "Я %s." % (dictionary_on[event])
                else:
                    msg = "Выдвигаюсь %s." % (dictionary_from[event])
            elif event == 'home':
                if count_home % 2 == 0:
                    msg = "Выдвигаюсь %s." % (dictionary_from[event])
                else:
                    msg = "Я %s." % (dictionary_on[event])
            if msg is None:
                log.msg = "Wrong event(?)"
                log.save()
                return HttpResponse(json.dumps({'success': True, 'error': 'Wrong IMEI'}, ensure_ascii=False),
                                    content_type="application/json")

            log.msg = msg
            msg += "\n%s" % author
            chats = VkChatId.objects.filter(is_active=True)

            for chat in chats:
                vkbot.send_message(chat.chat_id, msg)

            response_data = {'success': True, 'msg': msg}
            log.success = True

        except Exception as e:
            response_data = {'success': False, 'exeption': str(e)}
            log.msg = str(e)
        tries += 1
        response_data['tries'] = tries

    log.save()
    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json")


def check_imei(imei):
    imeis = TrustIMEI.objects.filter(is_active=True)
    for item in imeis:
        if imei == item.imei:
            return item
    return None
