import os
import time
import grpc

import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from langchain_file import get_completion
from text2image import create_photo

import src.protos.protobuf_pb2 as pb2
import src.protos.protobuf_pb2_grpc as pb2_grpc


# Токен Telegram бота
BOT_TOKEN = os.environ['BOT_TOKEN']

# Создание экземпляра бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
user_states = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardRemove(selective=False)
    await message.answer(f"Привет, {message.from_user.first_name}! Я бот new_pizza_product :) "
                         f"Здесь ты можешь описать продукт, которого ещё нет в ассортименте DoDoPizza."
                         f" А я подберу ингредиенты и сгенерирую изображение нового продукта.",
                         reply_markup=markup)
    user_states[message.chat.id] = "description"
    await message.answer("Введи описание продукта:")

@dp.message_handler()
async def receive_question(message: types.Message):
    user_states[message.chat.id] = "waiting"
    await message.answer("Твой вопрос был отправлен. Ожидай ответа!")

    # Здесь отправляем запрос через gRPC API и получаем image + text
    text = get_completion(f"Представь что клиент пришёл в пиццерию и хочет попробовать новое блюдо."
                                f" Опиши блюдо в пиццерии который соответствует описанию клиента: {message.text}"
                                f" Дай этому блюду креативное название и красивое краткое описание.")
    promt_for_image = get_completion(f"По данному описанию ниже сгенерируй промт на английском языке для text2image модели,"
                                     f" чтобы получилась реалистичная фотография блюда: {text}")

    image_url = create_photo(promt_for_image)
    img_data = requests.get(image_url[0]).content
    await bot.send_photo(message.chat.id, img_data, caption=text)

    user_states[message.chat.id] = "description"
    await bot.send_message(message.chat.id, "Введи описание продукта снова:")


@dp.message_handler()
async def prepare_message(message: types.Message):
       channel = grpc.aio.insecure_channel(os.environ["SERVICE_HOST"]+":"+os.environ["SERVICE_PORT"])
       stub = message_pb2_grpc.ServiceStub(channel)
       await message.answer("Твой вопрос был отправлен. Ожидай ответа!")
       request = message_pb2.Message(
           sender="bot",
           recipient=message.from_user.first_name,
           content=message.text,
           timestamp=time.time(),
       )
       response = await stub.PrepareMessage(request)
       promt_for_image = get_completion(f"По данному описанию ниже сгенерируй промт на английском языке для text2image модели,"
                                     f" чтобы получилась реалистичная фотография блюда: {text}")
       image_url = create_photo(promt_for_image)
       img_data = requests.get(image_url[0]).content
       await bot.send_photo(message.chat.id, img_data, caption=text)
       await bot.send_message(message.chat.id, "Введи описание продукта снова:")
       print(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
