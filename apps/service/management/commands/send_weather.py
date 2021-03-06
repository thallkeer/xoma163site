from django.core.management.base import BaseCommand

from apps.API_VK.APIs.yandex_weather import get_weather
from xoma163site.wsgi import vk_bot


class Command(BaseCommand):

    def handle(self, *args, **options):
        chat_ids = options['chat_id'][0].split(',')
        city_name = options['city'][0]
        from apps.service.models import City
        city = City.objects.filter(synonyms__icontains=city_name).first()
        if not city:
            return "Не нашёл город"
        weather = get_weather(city)

        for chat_id in chat_ids:
            vk_bot.send_message(chat_id, weather)

    def add_arguments(self, parser):
        parser.add_argument('chat_id', nargs='+', type=str,
                            help='chat_id')
        parser.add_argument('city', nargs='+', type=str,
                            help='city')
