def get_admin_keyboard():
    return {
        "one_time": False,
        "buttons": [
            [
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"1\"}",
                        "label": "Погода"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Помощь"
                    },
                    "color": "primary"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Синички 0"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Синички 20"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Синички 100"
                    },
                    "color": "primary"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Старт"
                    },
                    "color": "positive"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Стоп"
                    },
                    "color": "negative"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Старт синички"
                    },
                    "color": "positive"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Стоп синички"
                    },
                    "color": "negative"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": "Расписание"
                    },
                    "color": "primary"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": "Скрыть"
                    },
                    "color": "secondary"
                }
            ],
        ]
    }


def get_default_keyboard():
    return {
        "one_time": False,
        "buttons": [
            [
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"1\"}",
                        "label": "Погода"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Помощь"
                    },
                    "color": "primary"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"1\"}",
                        "label": "Синички 0"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Синички 20"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        # "payload": "{\"button\": \"2\"}",
                        "label": "Синички 100"
                    },
                    "color": "primary"
                }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": "Скрыть"
                    },
                    "color": "secondary"
                }
            ],
        ]
    }


def get_help_text():
    return \
        "̲С̲т̲р̲и̲м - ссылка на стрим\n" \
        "̲Г̲д̲е N(N - имя человека) - информация о чекточках\n" \
        "̲С̲и̲н̲и̲ч̲к̲и [N[,M]](N - количество кадров в гифке, 20 дефолт, M - качество(0 или 1), 0 дефолт) - ссылка, снапшот и гифка\n" \
        "̲Р̲е̲г - регистрация для участия в петровиче дня\n" \
        "̲П̲е̲т̲р̲о̲в̲и̲ч̲ ̲д̲н̲я - мини-игра, определяющая кто Петрович Дня\n" \
        "̲С̲т̲а̲т̲а - статистика по Петровичам\n" \
        "̲Д̲а̲н̲е̲т - бот вернёт да или нет. Можно просто \"?\" или в конце указать \"?\"\n" \
        "̲Р̲а̲н̲д̲о̲м N[,M] (N,M - от и до) - рандомное число в заданном диапазоне\n" \
        "̲П̲о̲г̲о̲д̲а [N] (N - название города(Самара, Питер, Сызрань, Прибой)) - погода в городе\n" \
        "̲О̲б̲о̲с̲р̲а̲т̲ь [N] - рандомное оскорбление. N - что/кто либо\n" \
        "̲П̲о̲м̲х̲в̲а̲л̲и̲т̲ь [N] - рандомная похвала. N - что/кто либо\n" \
        "̲Ц̲и̲т̲а̲т̲а + пересылаемое сообщение - сохраняет в цитатник сообщение(я)\n" \
        "̲Ц̲и̲т̲а̲т̲ы [N[,M]]- просмотр сохранённых цитат. Возможные комбинации - N - номер страницы, N - фраза для поиска, N - фраза для поиска, M - номер страницы\n" \
        "Клава/скрыть - показывает/убирает клавиатуру\n" \
        "̲П̲о̲м̲о̲щ̲ь - помощь\n" \
        "\n-- команды для группы 6221 --\n" \
        "̲Р̲а̲с̲п̲и̲с̲а̲н̲и̲е - картинка с расписанием\n" \
        "̲У̲ч̲е̲б̲н̲о̲е - ссылка на папку с учебным материалом\n" \
        "̲Л̲е̲к̲ц̲и̲и - ссылка на папку с моими лекциями\n" \
        "̲Н̲е̲д̲е̲л̲я - номер текущей учебной недели\n" \
        "\n--для администраторов--\n" \
        "̲У̲п̲р̲а̲в̲л̲е̲н̲и̲е (N,M) - N - chat_id, M - сообщение [Только для администраторов]\n" \
        "̲С̲т̲р̲и̲м [N] (N - ссылка на стрим) \n" \
        "̲С̲т̲а̲р̲т/̲С̲т̲о̲п [N]- возобновляет/продолжает работу бота. С параметром можно отключить нужный модуль\n" \
        "Бан/Разбан N - N - пользователь \n"


def get_insults():
    return ["Алик", "Алкаш", "алконавт", "Аллаяр", "Альтернативно одаренный", "Амаус", "Аморал",
            "аморальный", "Антихрист", "Аптряй", "Архаровец", "Аспид", "Ащеул", "Баба", "Баба ветрогонка",
            "Бабашкин", "Бабинский", "Бабуин", "Баклан", "Балабол", "Баламошка", "Баламут", "Балахвостъ",
            "Балахрыска", "Балбес", "Балда", "Балдабей", "Баляба", "Бандит", "Банный лист", "Баран",
            "Бармаглот", "Барнабаш", "Барыга", "Басалай", "Басурманин", "Башибузук", "Без царя в голове",
            "Бездарь", "Бездельник", "Безмозглая курица", "Безобразник", "Безпелюха", "Безсоромна баба",
            "Белебеня", "Бесстыдник", "Бестия", "Бестолочь", "Бесшабашный", "Бзыря", "Блаженный", "Блудоумъ",
            "Блудяшка", "Бобыня", "Божевольный", "Божедурье", "Болван", "Болдырь", "Болтун", "Боров",
            "Босяк", "Ботаник", "Брандахлыст", "Бредкий", "Брехло", "Брехун", "Брыдлый", "Буня", "Буслай",
            "Быдло", "Бычара", "Бычьё", "Бяка", "В попу укушенный", "Валандай", "Вася  Бардуль", "Вахлай",
            "Ведьма", "Веред", "Верзила", "Вертопрахъ", "Вертухай", "Вешалка", "Визгопряха", "Висельник",
            "Вобла сушеная ", "Волк позорный", "Волки позорные", "Волочайка", "Волчара", "Волчья сыть",
            "Вонючка", "Ворона ловить", "Ворюга", "Вошь на гребешке", "Вшивота", "Вымесок", "выпивоха",
            "Выпороток", "Выродок", "Вяжихвостка", "Гадина", "Гамадрил", "Гамыра", "Гандон", "Гвозди",
            "Геморрой", "Гиена кладбищенская", "Глазопялка", "Глиста", "Глиста ходячая", "Глуподырый",
            "Гнида", "Гноище", "Гнус", "Гнусь", "Говна лопата", "Говно", "Говноед", "Голиаф",
            "Голова садовая", "Головешка с мозгами", "Головка от патефона", "Головорез", "Голь перекатная",
            "Гомик", "Гондурас", "Гонщик", "Гопник", "Гопота", "Горилла", "Горлопан", "Грабастикъ",
            "Грубиян", "Грымза", "Губошлёп", "Гузыня", "Гульня", "Гусыня", "Гусь", "Дармоед", "Дать в репу",
            "Даун", "Дебил", "Дегенерат", "Декадент", "Демон", "Дерево", "Держиморда", "Дерьмо", "Дистрофик",
            "Дитка", "Долбень", "Долботряс", "Дрищь", "Дрянь", "Дуб", "Дубина", "Дубина стоеросовая",
            "Дуботолкъ", "Дундук", "Дунька", "Дупель", "Дурак", "Дуралей", "дурачок", "Дурбалай",
            "Дурбецелло", "Дурень", "Дурилка", "Дурка", "Дуропляс", "Дурошлеп", "Дурында", "Душман",
            "Душной козел", "Дятел", "Егоза", "Едрён батон", "Ёжкин", "Ёкарный бабай", "Елдыга", "Ёлупень",
            "Ёнда", "Ёра", "Ерондер пуп", "Еропка", "Ерохвостъ", "Ерпыль", "Ершится", "Етишкин дух", "Жаба",
            "Жадина", "Желчный", "Жердяй", "Жертва аборта", "Живоглот", "Живодристик", "Жиздоръ", "Жила",
            "Жиртрест", "Жлоб", "Жмот", "Жополиз", "Жук", "Жук навозный", "Жулик", "Жупел", "забулдыга",
            "Загузастка", "Задница", "Задор", "Задрот", "Задрыга", "Залупа", "заморыш", "Замухрышка",
            "зануда", "Заовинник", "Зараза", "засранец", "Засыха", "Затетёха", "Захухря", "заячий хвост",
            "Звери", "Зверь", "Злодей", "Злотвор", "Злыдень", "Змеиная рвота", "Змея", "зубоскал",
            "Ибтую мэмэ", "Идиот", "Изверг", "Извращенец", "Изувер", "Имбецил", "Индюк", "Ирод", "Иуда",
            "Ишак", "Кабан", "Каботин", "Кабыздох", "Каин", "Какашка", "Каланча", "Каналья", "Каракатица",
            "Карга", "Кацап", "Кащей", "Квазимодо", "Кикимора", "Киселяй", "Клоп", "Клубничка", "Клуша",
            "Клюшка", "Кляузник", "Кобель", "Кобыла", "Козёл", "Козлодой", "Козлодорасина", "Козья морда",
            "Козявка", "Колдырь", "Колобродъ", "Коломесъ", "Колотовка", "Колупай", "Конь педальный",
            "Копрофаг", "Копрофил", "Корова", "Королобый", "Корявый", "Косорукий", "Костеря", "Кочерыжка",
            "Кошёлка", "Кощей", "Кракозяблик", "Краля", "Крамольник", "Кретин", "Кривляка", "Криволапый",
            "Кровопийца", "Кровосос", "Кропотъ", "Крохобор", "Крыса", "Кугут", "Куёлда", "Курва", "Куркуль",
            "Курощупъ", "Кучка на ровном месте", "Кю", "Лапотник", "лахудра", "Ледаша детина", "Лежака",
            "Леший", "Липовый диплом", "Лободырный", "ложкомойка", "лопух", "лох", "Лох,лохушка", "Лоха",
            "Лоший", "Лудъ", "Любомудръ", "Лябзя", "Лярва", "Макака", "Малахольный", "Мамошка", "Мандавошка",
            "Мандуда", "Маракуша", "Маромойка", "Мартышка", "Массаракш", "Мастдай однобитный", "Межеумокъ",
            "Мент", "Мерзавец", "Мерзопакость", "Метёлка", "Михрютка", "Младоуменъ суще", "Мозгляк",
            "Мокрица", "Мокрощёлка", "Моль", "Монстр", "Морда", "Мордоворот", "Мордофиля", "Моркотникъ",
            "Москолудъ", "Моська", "Мочалка", "Мразь", "Мракобес", "Мудак", "Мурло", "мусор", "Муфлон",
            "Мухоблудъ", "Мымра", "Наглец", "Назойливая муха", "Напыщенный индюк", "Насупа", "Насупоня",
            "Нахал", "Невегласъ", "Невежа", "Невежда", "Негодяй", "Негораздокъ", "Недоносок", "Недотёпа",
            "Недотепа", "Недотыкомка", "Недоумок", "Неповоротень", "Непотопляемый", "Несмыселъ", "Нетопырь",
            "Нефырь", "Нехристь", "Нечисть", "Ничтожество", "Обалдуй", "Обдувало", "Обезьяна", "облезлый",
            "Обломъ", "Облудъ", "Оболдуй", "Оболтус", "Обормот", "Образина", "Овца", "Оглоед", "Огуряла",
            "Одоробло", "Озорник", "Окаёмъ", "Окаянный", "Околотень", "Олень", "Олигофрен", "Олух",
            "Олух царя небесного", "омерзительный", "Опущ", "Орангутан", "Осёл", "Осиновый лист",
            "Остолбень", "Остолоп", "Отморозок", "Отстой", "Отымалка", "Охальникъ", "Охламон", "Очкарик",
            "Павлин", "Пакостник", "паразит", "Паршивец", "паскуда", "Пеньтюхъ", "Пердимонокль", "Пердун",
            "пересмешник", "Пес", "петух", "Пехтюкъ", "Печегнётъ", "Печная ездова", "пигалица", "Пидор",
            "Пижон", "Плеха", "Поганец", "Поганка", "Погань", "Подлец", "подонок", "пожиратель гравия",
            "Позорный", "попа", "Попа с ручкой", "Попрешница", "Потаскуха", "Потатуй", "Похабникъ",
            "Пресноплюй", "придурок", "Приставучий репей", "пройдоха", "Проказник", "проныра", "пропойца",
            "простак", "простофиля", "Профура", "профурсетка", "прохвост", "прохиндей", "Прошмандовка",
            "прощелыга", "Псоватый", "Пустобрёхъ", "Пустошный", "Пыня", "Пьявка", "пьянь ", "Пятигузъ",
            "Развисляй", "разгильдяй", "Разделать под орех", "раздолбай", "Раззява", "разиня", "Разлямзя",
            "размазня", "Разноголовый", "Разтетёха", "Растопча", "растыка", "растяпа", "Расшивоха",
            "Расщеколда", "Рахубникъ", "Рвань", "Рогоносец", "рожа", "рохля", "рыло", "Рюма", "сатрап",
            "Свербигузка", "Свинья", "Сволочь", "Сдёргоумка", "Сексот", "Секушка", "Сиволапъ", "Сивый мерин",
            "Скапыжный", "Скаредъ", "Сквернавецъ", "Скоблёное рыло", "Скряга", "смерд", "Сняголовь",
            "Солдафон", "Стеллерова газель", "Стерва", "Стервец", "Стиляга", "Страмецъ", "Страхолюдъ",
            "Стукач", "Суемудръ", "сукин сын", "Супостат", "Сыч", "Та ещё жучка", "Тартыга", "Тварь",
            "Телеухъ", "тетёха", "Тетёшка", "Титёшница", "тля", "Толоконный лобъ", "тормоз", "трепло",
            "Трупёрда", "Трутень", "трынделка", "Трясся", "Туесъ", "Тупица", "тупой", "Тьмонеистовый",
            "Тюрюхайло", "тюфяк", "Ублюдок", "Убожество", "Угланъ", "Удод", "Упырь", "Урка", "Урод", "Урюк",
            "Урюпа", "Ушлёпок", "Фетюк", "Фигляр", "Филькина грамота", "Фифа", "Фофан", "Фраер", "Фуфло",
            "Фуфлыга", "хабалка", "Хабалъ", "халдей", "Халтома", "Халявщик", "Хам", "Хана", "Хандрыга",
            "ханыга", "хапуга", "Харя", "Хмырь", "Хмыстень", "Хобяка", "ходячее кладбище бифштексов",
            "холера", "холуй", "Хорёк ", "Хохрикъ", "Хуже горькой редьки", "Цуцик", "Чёрт",
            "Чёртъ верёвочный", "Чувырла", "Чужеядъ", "Чучело", "Шаврикъ", "Шалава", "шалопут", "Шалопутъ",
            "Шантрапа", "Шаромыжник", "Шваль", "Шевяк", "шельма", "Шибздик", "Шизик", "Шинора", "Шкура",
            "Шлында", "Шлюха", "Шмакодявка", "Шмара", "Шмаровоз", "Шпана", "Шпынь голова", "Шут гороховый",
            "Шушера", "Щаул", "Щегол", "Щенок", "Юродивый", "Я", "Ябеда", "Язва", "Яйцеголовый",
            "Яйцекладущий сын замороженного пня", "Японский городовой", "Ятидрёный хряп",
            "Ублюдок, мать твою, а ну иди сюда говно собачье, решил ко мне лезть? Ты, засранец вонючий, мать твою, а? Ну иди сюда, попробуй меня трахнуть, я тебя сам трахну ублюдок, онанист чертов, будь ты проклят, иди идиот, трахать тебя и всю семью, говно собачье, жлоб вонючий, дерьмо, сука, падла, иди сюда, мерзавец, негодяй, гад, иди сюда ты - говно, ЖОПА"]


def get_praises():
    return ["аплодирую вам стоя", "Ас",
            "Без тебя мы бы не справились", "Безукоризненно", "Безукоризненное исполнение", "безупречно", "Бесподобно",
            "Бесценно", "бис", "Благодарю", "Благодарю вас", "Благодарю за супер-работу", "блеск!", "Блестяще",
            "Блистательно", "богатая фантазия", "боец", "Божественно", "Браво", "быстрый", "В самое яблочко",
            "в яблочко!", "вау!", "вдумчиво", "вежливый",
            "Великолепная работа", "великолепно", "Верно", "видно,что выполено со всей душой", "внимательный",
            "Волшебно", "Восхитительно", "вот видишь,как,оказывается,все легко,ведь все получилось!",
            "вот так всегда делай", "вот это да!", "вот это постарался", "Впечатляюще", "впечетляет",
            "все лучше и лучше с каждым днем", " легенда", "чудо",
            "всегда удивляешь меня", "гений",
            "единственный в своем роде",
            "Высшая оценка", "Высший класс", "Гениально", "гениально!", "глубокий",
            "Гораздо лучше", "Грандиозно", "да", "гений!", "просто сокрвище!", "даже не вериться",
            "даже я так не смогла бы", "держи кофету", "доброкачественно", "добросовестно", "добрый", "дружелюбный",
            "душевный", "Еще одно чудо", "замечательно", "звездочка", "Здорово", "Значительный вклад", "золото",
            "золотые руки", "и как тебе только это удается", "талант!",
            "почему скрывал свой талант??", "Идеально", "Изумительно", "именно", "Именно тот билет", "Интересно",
            "Исключительно", "искренний", "Кажется, это заставит нас сверкать",
            "Как вам только удалось сделать так хорошо", "как всегда, идеально)", "как оригинально",
            "Как раз то, что доктор прописал", "Как раз то, что мы хотели",
            "Какой трудолюбивый", "Класс", "Классически", "Классно", "Колоссально", "Кошачий восторг", "красиво",
            "красиво сделанно", "красивый", "Круто", "кто бы мог подумать!", "легендарно", "ловкий",
            "луч света в темном царстве", "лучик", "лучше всех", "лучше некуда", "мастер", "Мировой класс",
            "мне безумно нравится", "мне нравиться", "Мне очень нравится", "Мне это нравится", "многогранный",
            "Мое восхищение", "Мое признание", "Мое уважение", "Мои поздравления", "молодец",
            "молодец, возми с полки пирожок!", "молодчик", "молодчинка", "на +", "наблюдательный", "надо же!",
            "Намного лучше", "Настоящая поэзия", "настоящий", "Настоящий класс", "настоящий помощник", "находчивый",
            "Не вздумай когда-нибудь покидать нас", "не к чему придраться", "не может быть!", "не такой(ая) как все",
            "Не хватает слов для благодарности", "Невероятно", "невообразимый", "Необыкновенно", "необычно",
            "неожиданно", "неординарный ребенок", "Неотразимо", "Непостижимо", "Непревзойденно", "Нереально",
            "Несравненно", "неужели это сам сделал/придумал?", "Обалденно",
            "обожаю", "Огромная работа", "Огромное спасибо", "одаренный ребенок",
            "один из лучших", "Оригинально", "Ослепительно", "осмысленный", "особенный", "ответственный", "открытый",
            "Отличная работа", "отлично", "Отлично поработали", "Очень значительно", "Очень искусно", "очень необычно",
            "Очень признательна вам", "Очень профессионально", "Очень удачно", "Очень хорошо получилось",
            "Ошеломительно", "Первоклассная работа", "Первоклассно", "первоклассный", "Первый класс",
            "пожипаю тебе руку", "Поздравления", "понимающий", "поработал на славу", "Поразили цель", "поразительно",
            "поразительный", "Потрясающе", "потрясающе!", "Правильно", "Превосходно", "прекланяюсь перед тобой",
            "прекрасно", "Прелестно", "Приятная работа", "Просто звезда", "Просто супер!", "Профессионально",
            "Профессионально, как всегда", "Прямое попадание", "птица высокого полета", "путный", "Работа -го класса",
            "работоспособный", "развитый", "рассудительный", "результат меня поразил", "результат на лицо",
            "с такими темпами будешь неузнаваем", "Самый надежный", "самый ответственный", "светишь ярче солнца",
            "светлая голова", "светлый", "сильный", "сказочно", "Славно", "славный", "Совершенно", "Совершенство",
            "Сокровище", "сообразительный", "спасибо", "спасибо тебе!", "Спасибо!", "способный",
            "сразу видно - человек работал!", "стоило попробовать", "стоило только попробовать!",
            "стремящийся к знаниям", "Супер!", "так держать", "такого еще никогда не видела!, в первый раз такое вижу",
            "талант не скроешь", "талантище", "Талантливо", "талантливый", "тебя ждет великое будущее", "То, что нужно",
            "То, что требовалось", "тобой можно гордиться", "толковый", "тонкочувствующий",
            "Трудно поверить", "трудолюбивый", " всегда делаешь конфетку", " лучший", " лучший в этом деле",
            " очень вырос", " очень успешен в этом", " просто мастер", " профи в своем деле",
            " служишь всем примером", " хорошо потрудился", " чудесен", "у меня бы не получилось",
            "У тебя получается это лучше всех", "у тебя талант", "уважаю", "Ударная работа", "Удивительно", "умница",
            "умный", "умный, умнющий", "уму не постижимо", "Уникально", "усердный", "Фантастика", "хвалю",
            "Хорошая работа", "хорошо", "Хорошо иметь вас в команде", "Хорошо поработали", "хорошо сделанно",
            "Хорошо сделано", "Целый отряд чемпионов", "чем дальше, тем лучше", "Чистенько", "чисто", "Чистое золото",
            "чистый", "Что бы мы без вас делали", "Что бы мы делали без вас", "Чувствуется разница", "Чудеса!",
            "Чудесно", "Чудно", "чудный", "Чудо", "Шикарно", "энергичный", "Это великолепно", "это стоило того",
            "Это так здорово — работать с вами", "Это так значительно", "Это хорошо смотрится", "Эффектно",
            "в тебе и не сомневался", "горжусь тобой", "знал, что сможешь!", "могу гордиться тобой",
            "очень ценю вашу работу", "поражен", "я признательна тебе",
            "я ценю твой труд", "Я ценю это", "Вау!"]


def get_bad_words():
    return ['еба', 'ебa', 'eба', 'eбa', 'ёба', 'ёбa', 'пидор', 'пидoр', 'пидоp', 'пидop', 'пидар', 'пидaр',
            'пидаp', 'пидap', "пидр", "пидp", 'гандон', 'годнон', 'хуй', 'пизд', 'бля', 'шлюха', 'мудак',
            'говно', 'моча', 'залупа', 'гей', 'сука', 'дурак', 'говно', 'жопа', 'ублюдок', 'мудак']


def get_bad_answers():
    return ['как же вы меня затрахали...', 'ты обижаешь бота?', 'тебе заняться нечем?', '...',
            'о боже', 'тебе не стыдно?', 'зачем ты так?']


def get_sorry_phrases():
    return ["лан", "нет", "окей", "ничего страшного", "Бот любит тебя", "я подумаю", "ой всё",
            "ну а чё ты :(", "всё хорошо", "каво", "сь", '...', 'оке','ладно, но больше так не делай']
