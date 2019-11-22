from apps.API_VK.command.CommonCommand import CommonCommand


class get_user_by_id(CommonCommand):
    def __init__(self):
        names = ["get_user_by_id"]
        super().__init__(names, for_admin=True, check_args=True)

    def start(self):
        self.vk_bot.get_user_by_id(self.vk_event.args[0], self.vk_event.chat_id)
        self.vk_bot.send_message(self.vk_event.chat_id, 'done')
