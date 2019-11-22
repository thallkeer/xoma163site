from apps.API_VK.command.CommonCommand import CommonCommand
from apps.Statistics.views import get_issues_text


class Issues(CommonCommand):
    def __init__(self):
        names = ["ишюс", "ишьюс", "иши"]
        super().__init__(names)

    def start(self):
        features = get_issues_text()
        self.vk_bot.send_message(self.vk_event.chat_id, features)
