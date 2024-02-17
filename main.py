from pyrogram import Client as ClientP
import asyncio
import random
import logging
import os


CHAT = -1002015466621
MAIN_MESSAGE = 6

logging.basicConfig(level=logging.INFO,
                    filename='send_message.log',
                    filemode='a',
                    format="%(asctime)s|%(levelname)s|%(message)s",
                    encoding='utf-8')


async def main():
    await app_user.start()
    count = 1
    while True:
        msg = await app_user.send_message(chat_id=CHAT,
                              text='Хочу айфон.',
                              reply_to_message_id=MAIN_MESSAGE)
        logging.info(f'{msg.link} | {msg.id} | Отослал сообщение №{count}')
        count += 1
        time_range = random.randint(58, 63)
        await asyncio.sleep(time_range)
        next_msg = await app_user.get_messages(chat_id=CHAT,
                                            message_ids=msg.id+1)
        if next_msg.from_user is None:
            logging.warning(f'Спустя минуту после отправки {msg.link} | {msg.id} нет сообщений!')
            await asyncio.sleep(30)
            next_msg = await app_user.get_messages(chat_id=CHAT,
                                            message_ids=msg.id+1)
            if next_msg.from_user is None:
                logging.warning(f'Спустя 30 сек до сих пор нет сообщений!')
                await asyncio.sleep(30)
                next_msg = await app_user.get_messages(chat_id=CHAT,
                                                message_ids=msg.id+1)
                if next_msg.from_user is None:
                    win = await app_user.send_message(chat_id=CHAT,
                              text='УрааААаааААААаАа я победил! Мой прошлый коммент продержался больше 1 минуты последним!',
                              reply_to_message_id=MAIN_MESSAGE)
                    logging.critical(f'ТЫ ВЫИГРАЛ!!!! Ссылка на сообщение (последнее): {msg.link} | {msg.id}\nСсылка на сообщение(победное): {win.link} | {win.id}')
                    break
    await app_user.stop()

if __name__ == '__main__':
    app_user = ClientP(name='Pyrogram_Client', api_id=os.environ['API_ID'], api_hash=os.environ['API_HASH'])
    asyncio.run(main())