from apps.API_VK.command.CommonCommand import CommonCommand
from apps.service.views import get_issues_text


class Issues(CommonCommand):
    def __init__(self):
        names = ["ишюс", "ишьюс", "иши"]
        help_text = "Ишьюс - список проблем"
        super().__init__(names, help_text)

    def start(self):
        features = get_issues_text()
        return features
