from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher # ловит events
from aiogram.utils import executor
import requests, os


bot = Bot(token = os.getenv("TOKEN"))
dp = Dispatcher(bot)

# обозначение декоратора (слушает приход новых сообщений)
@dp.message_handler()
async def echo_send(message : types.Message):
	# подождать до свободного места в потоке для исполнения
	# await message.answer(message.text)
	# ждёт и отправляет ответом
	await message.reply(message.text)
	# выслать ответ пользователю в лс (если бот добавлен в группу)
	# await bot.send_message(message.from_user.id, message.text)

# запуск бота
#   skip_updates = True для игнорирования сообщений, 
# прищедщих во время оффлайна бота
executor.start_polling(dp, skip_updates = True)