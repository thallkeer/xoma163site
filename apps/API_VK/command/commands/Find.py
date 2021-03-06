import os

from apps.API_VK.command.CommonCommand import CommonCommand
from xoma163site.settings import BASE_DIR


class Find(CommonCommand):
    def __init__(self):
        names = ["поиск", "найди", "найти", "ищи", "искать"]
        help_text = "Поиск  - ищет информацию по картинкам"
        detail_help_text = "Поиск ([N]) - ищет информацию по картинкам, N - поисковый запрос"

        super().__init__(names, help_text, detail_help_text, args=1, api=False)

    def start(self):
        import requests

        query = self.vk_event.original_args
        count = 5

        r = requests.get(
            "https://api.qwant.com/api/search/images",
            params={
                'count': 20,
                'q': query,
                't': 'images',
                'safesearch': 1,
                'locale': 'ru_RU',
                'uiv': 4
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            }
        )
        if r.status_code == 429:
            return "Не так часто"

        response = r.json().get('data').get('result').get('items')
        urls = [r.get('media') for r in response]
        if len(urls) == 0:
            return "Ничего не нашёл"
        attachments = []
        for url in urls:
            path = f"{BASE_DIR}/static/vkapi/{query}.jpg"
            try:
                img = requests.get(url)
                img_file = open(path, "wb")
                img_file.write(img.content)
                img_file.close()

                photo = self.vk_bot.upload_photo(path)
                attachments.append(photo)
            except Exception as e:
                print(str(e))
            finally:
                if os.path.exists(path):
                    os.remove(path)
            if len(attachments) >= count:
                break
        if len(attachments) == 0:
            return "Ничего не нашёл 2"
        return {'msg': '', 'attachments': attachments}
