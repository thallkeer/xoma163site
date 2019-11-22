from apps.API_VK.command.CommonCommand import CommonCommand
from xoma163site.wsgi import cameraHandler


class Start(CommonCommand):
    def __init__(self):
        names = ["старт"]
        super().__init__(names, for_admin=True)

    def start(self):
        if self.vk_event.args[0] == "синички":
            if not cameraHandler.is_active():
                cameraHandler.resume()
                self.vk_bot.send_message(self.vk_event.chat_id, "Стартуем синичек!")
            else:
                self.vk_bot.send_message(self.vk_event.chat_id, "Синички уже стартовали!")
                return
        else:
            self.vk_bot.BOT_CAN_WORK = True
            self.vk_bot.send_message(self.vk_event.chat_id, "Стартуем!")
