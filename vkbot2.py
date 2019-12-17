from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
from colorama import init
from colorama import Fore, Back, Style
import random

# use Colorama to make Termcolor work on Windows too
init()

token = "4ad56051586625cf0560d856d1eecc0867054acc16395ea2ab7099e1b1e9e5240f0ac60c76e75ca919d37"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print( Fore.BLACK )
            print( Back.GREEN )
            print("Сообщение пришло в: "+ str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения: " + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method("messages.send", {"user_id": event.user_id, "message": "Привет!Я ещё бета,погоди пару недель.", "random_id": 0})
