from apps.API_VK.command.CommonCommand import CommonCommand


class Bye(CommonCommand):
    def __init__(self):
        names = ["пока", "бай", "bb", "бай-бай", "байбай", "бб", "досвидос", "до встречи", "бывай", 'пока-пока']
        super().__init__(names)

    def start(self):
        return "Пока(("
