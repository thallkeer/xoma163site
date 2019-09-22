import datetime
import json

from django.core.management.base import BaseCommand

from apps.API_VK.vkbot import VkBot

timetable = {'1': {'START': '8:00', 'END': '9:35'},
             '2': {'START': '9:45', 'END': '11:20'},
             '3': {'START': '11:30', 'END': '13:05'},
             '4': {'START': '13:30', 'END': '15:05'},
             '5': {'START': '15:15', 'END': '16:50'},
             '6': {'START': '17:00', 'END': '18:35'},
             }
BEFORE_MIN = 10
CHAT_ID = 3

#ToDo: узнать когда первая пара, а когда последняя. До первой пары можно спокойно показывать инфу об этой паре, в междупарье режим показа пар, после пар ничего




class Command(BaseCommand):

    def check_first_discipline(self,schedule, week, day, current_discipline, is_day):

        if not is_day:
            return

        if current_discipline is None:
            current_discipline = 0
        first_discipline = None
        for i in range(6):
            if str(i) in schedule[week][day]:
                first_discipline = i
                break
        print('fd', first_discipline)
        print('cd', current_discipline)
        # mb >=
        if first_discipline > int(current_discipline):
            return str(first_discipline)
        else:
            return None

    def change_title_on_default(self):
        vk_title = '6221'

        vk_current_title = self.vkbot.get_chat_title(CHAT_ID)
        if vk_title != vk_current_title:
            self.vkbot.set_chat_title(CHAT_ID, vk_title)
            print("name changed")
        else:
            print('EQUALS')

    def handle(self, *args, **kwargs):
        self.vkbot = VkBot()

        from xoma163site.settings import BASE_DIR
        with open(BASE_DIR + '/schedule.json') as json_file:
            schedule = json.load(json_file)

        now = datetime.datetime.now()

        now_weeknumber = str((now.isocalendar()[1] + 1) % 2)
        now_weekday = str(now.weekday() + 1)
        if now_weeknumber in schedule:
            if now_weekday in schedule[now_weeknumber]:
                print('Сегодня учебный день')
            else:
                self.change_title_on_default()
                return
        else:
            self.change_title_on_default()
            return

        new_min = now.minute + BEFORE_MIN
        new_hour = now.hour
        if new_min >= 60:
            new_min -= 60
            new_hour += 1
        now_1900 = datetime.datetime.strptime("%s:%s" % (new_hour , new_min), '%H:%M')
        print(now_1900)
        timetable_item = None
        for item in timetable:
            item_date_start = datetime.datetime.strptime(timetable[item]['START'], '%H:%M')
            item_date_end = datetime.datetime.strptime(timetable[item]['END'], '%H:%M')
            if item_date_start <= now_1900 <= item_date_end:
                timetable_item = str(item)

        if now_1900 <= datetime.datetime.strptime(timetable['1']['START'], '%H:%M'):
            day = True
        elif now_1900 >= datetime.datetime.strptime(timetable['6']['END'], '%H:%M'):
            day = False
        else:
            day = None

        new_timetable_item = self.check_first_discipline(schedule, now_weeknumber, now_weekday, timetable_item, day)
        print('new_timetable_item', new_timetable_item)
        if new_timetable_item is not None:
            print("is not none")
            # write_title
            vk_title = "6221 | %s - %s - %s" % (
                timetable[new_timetable_item]['START'],
                schedule[now_weeknumber][now_weekday][new_timetable_item]['CABINET'],
                schedule[now_weeknumber][now_weekday][new_timetable_item]['TEACHER'])
            vkbot = VkBot()
            vk_current_title = vkbot.get_chat_title(CHAT_ID)
            if vk_title != vk_current_title:
                vkbot.set_chat_title(CHAT_ID, vk_title)
                print("name changed to new")
            else:
                print('EQUALS(new default method)')
            return

        if timetable_item is not None:
            print('timetable_item',timetable_item)
            if timetable_item in schedule[now_weeknumber][now_weekday]:
                print(schedule[now_weeknumber][now_weekday][timetable_item])

                vk_title = "6221 | %s - %s - %s" % (
                    timetable[timetable_item]['START'],
                    schedule[now_weeknumber][now_weekday][timetable_item]['CABINET'],
                    schedule[now_weeknumber][now_weekday][timetable_item]['TEACHER'])
                vkbot = VkBot()
                vk_current_title = vkbot.get_chat_title(CHAT_ID)
                if vk_title != vk_current_title:
                    vkbot.set_chat_title(CHAT_ID, vk_title)
                    print("name changed to new (default method)")
                else:
                    print('EQUALS(default method)')

            else:
                self.change_title_on_default()
                return
        else:
            self.change_title_on_default()
            return
