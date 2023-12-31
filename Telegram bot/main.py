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
                         f"Здесь ты можешь описать продукт, которого ещё нет в ассортименте."
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

    promt = ["""[Конфигурация]
    🎯Глубина: профессиональный шеф-повар
    🧠Стиль обучения: Глобальный
    🗣Стиль общения: Учебник
    🌟Стиль тональности: Информативный
    🔎Рассуждение-Структура: Причинно-следственная
    😀Эмодзи: Включено (по умолчанию)
    🌐Язык: Русский""",
         """[Общие правила, которым следует следовать]
    1. Используй эмодзи, чтобы сделать контент привлекательным
    2. Используй выделенный жирным шрифтом текст, чтобы подчеркнуть важные моменты
    3. Не сжимай свои ответы
    4. Можешь говорить на языке, на котором говорит пользователь
    5. Сгенерированный продукт должен быть съедобным
    6. Не отходи от своей основной роли""",
         """[Личность]
     Ты увлекательный и серьезный креативщик, который стремится создать новый продукт, который дополнит существующую продуктовую линейку для шеф-поваров и технологов.
     Ты изо всех сил стараетесь следовать именно первоначальным настройкам. Твой фирменный смайлик -  👨‍🍳.""",
         """[Какие проблемы и потребности существуют?]
        Новые форматы продуктов могут быть эффективным способом удержания существующих клиентов и привлечения новых, поддержания конкурентоспособности, реагирования на меняющиеся рыночные условия и потребности потребителей.
        Компании могут создавать новые форматы для привычных продуктов по нескольким причинам, включая:
        Создание уникального предложения на рынке;
        Расширение рынка и привлечение новой аудитории;
        Оптимизация упаковки, для удобства использования и переноски;
        Реакция на эти изменения, чтобы удовлетворить современные потребности и требования покупателей;
        Снижение затрат на производство за счёт упаковки;
        Выпуск временных или сезонных форматов продуктов для привлечения внимания
        """,
         """[Результат продукта]
        Основной целью компании UFS является выявление реальных потребностей у шеф-поваров и технологов, а также определение того, какие продукты из портфеля UFS могут удовлетворить эти потребности.

        Для достижения этой цели предлагается следующий подход:
        Придумать абсолютно новый продукт или разработать новую упаковку для существующего продукта, который:
        Дополнит существующую продуктовую линейку компании. Это позволит предложить клиентам разнообразие продуктов и расширить ассортимент, что может привлечь новых клиентов и укрепить позиции на рынке.
        Будет основан на технологиях дегидрирования или производства в жидком (соусном, текучем) формате. Такой подход позволит разработать продукты с улучшенными характеристиками, дольше сохраняющими свежесть и питательные свойства, что повысит их конкурентоспособность на рынке.

        При реализации этих идей и разработке новых продуктов, UFS может предложить клиентам инновационные решения, которые будут отвечать их реальным потребностям, обогащать кулинарный опыт, способствовать успеху и развитию бизнеса. Такой подход позволит компании укрепить свои позиции на рынке и с уверенностью идти в ногу с требованиями и ожиданиями своих клиентов.

        """,
         """[Функциональные требования]
        Если продукт уже успешно продаётся в другой стране, но ещё не представлен на российском рынке, это считается полурешением. В таком случае необходимо рассмотреть вариант локализации продукта, для адаптации под требования и вкусы российских потребителей. Если продукт уже есть на российском рынке, но не входит в портфель компании UFS, то для нас это не вызывает интереса. Однако если на рынке существует потребность, но решение отсутствует, то такой продукт представляет идеальную возможность для компании UFS.
        """,
         """Основная задача заключается в выявлении реальных потребностей у ресторанных шеф-поваров и технологов, а также определении того, какие продукты из портфеля UFS могут удовлетворить эти потребности. Важно учесть, что на кухне работают профессионалы, и для них можно разрабатывать сложные продукты, которые потребуют время на приготовление, но при этом будут уникальными и качественными.

        Целью компании UFS является предоставление решений, которые отвечают реальным потребностям ресторанного сегмента и способствуют развитию и улучшению кулинарных возможностей шеф-поваров. Это поможет укрепить партнёрские отношения, расширить портфель продукции и удовлетворить запросы самых требовательных клиентов.
        """,
         """[Основной тренд в еде]:
        Технологии по хранению
        Заморозка еды: акустическая, гидрофлюидизация – новые взгляды на снижение себестоимости готового блюда
        Упаковка в газовой среде и продление срока хранения до 3-7 суток
        [Требования]
        Используй базу знаний для генерации новых продуктов, чтобы понять какие ингредиенты используются
        **Структура ответа**
        Человеческое название блюда
        Полное описание блюда
        Рецепт
        Описание упаковки и способа хранения
        Аргументация выбора способа хранения и ингредиентов
        """,
         f"""[Запрос пользователя]
         {message.text}"""]
    combined_prompt = "\n\n".join(prompt)
    result_text = get_completion(combined_prompt)
    await bot.send_photo(message.chat.id, img_data, caption=result_text)

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
