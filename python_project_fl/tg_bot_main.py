import random
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

# бот имеет название HealthyFood, скриншоты бота расположены в папке screen_bot
BOT_TOKEN = '6060272283:AAEtMLolsgpH1O7ipN5DEfbae678RyGxZF4'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
conn = sqlite3.connect('db/tg_food.db', check_same_thread=False)
cursor = conn.cursor()


# создание кнопок и стартовые фразы
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["info", "breakfast","lunch", "dinner", "count"]
    keyboard.add(*buttons)
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    await message.answer(f"Добро пожаловать, {user_full_name}", reply_markup=keyboard)


# вызыв текста из texts/information.txt при нажатии кнопки info
@dp.message_handler(Text(equals="info"))
async def infornation(message: types.Message):
    f_information = open('texts/information.txt', 'r', encoding='utf-8')
    await message.reply(f_information.read())
    f_information.close()

# работа с кнопкой breakfast
@dp.message_handler(Text(equals="breakfast"))
async def product_range_breakfast(message: types.Message):

    records = conn.cursor().execute("""SELECT * FROM food_breakfast""").fetchall()
    randomiser = len(records)

    # m - случайный id
    m = random.randint(1, randomiser)

    # Определение названия блюда под id = m
    name_food = conn.cursor().execute(f"""SELECT name FROM food_breakfast
            WHERE id='{m}' """).fetchall()

    # Определение ингридиентов под id = m
    about_food = conn.cursor().execute(f"""SELECT about FROM food_breakfast
            WHERE id='{m}' """).fetchall()

    # Вывод названия случайного блюда
    for elem_name in name_food:
        await message.answer(*elem_name)

    # Вывод рецепта случайного блюда
    for elem_about in about_food:
        await message.answer(*elem_about)


# работа с кнопкой lunch
@dp.message_handler(Text(equals="lunch"))
async def product_range_breakfast(message: types.Message):

    records = conn.cursor().execute("""SELECT * FROM food_lunch""").fetchall()
    randomiser = len(records)

    # m - случайный id
    m = random.randint(1, randomiser)

    # Определение названия блюда под id = m
    name_food = conn.cursor().execute(f"""SELECT name FROM food_lunch
            WHERE id='{m}' """).fetchall()

    # Определение ингридиентов под id = m
    about_food = conn.cursor().execute(f"""SELECT about FROM food_lunch
            WHERE id='{m}' """).fetchall()

    # Вывод названия случайного блюда
    for elem_name in name_food:
        await message.answer(*elem_name)

    # Вывод рецепта случайного блюда
    for elem_about in about_food:
        await message.answer(*elem_about)

# работа с кнопкой dinner
@dp.message_handler(Text(equals="dinner"))
async def product_range_breakfast(message: types.Message):

    records = conn.cursor().execute("""SELECT * FROM food_dinner""").fetchall()
    randomiser = len(records)

    # m - случайный id
    m = random.randint(1, randomiser)

    # Определение названия блюда под id = m
    name_food = conn.cursor().execute(f"""SELECT name FROM food_dinner
            WHERE id='{m}' """).fetchall()

    # Определение ингридиентов под id = m
    about_food = conn.cursor().execute(f"""SELECT about FROM food_dinner
            WHERE id='{m}' """).fetchall()

    # Вывод названия случайного блюда
    for elem_name in name_food:
        await message.answer(*elem_name)

    # Вывод рецепта случайного блюда
    for elem_about in about_food:
        await message.answer(*elem_about)


# вызыв текста из texts/count.txt при нажатии кнопки info
@dp.message_handler(Text(equals="count"))
async def infornation(message: types.Message):
    f_count = open('texts/count.txt', 'r', encoding='utf-8')
    await message.reply(f_count.read())
    f_count.close()


if __name__ == '__main__':
    executor.start_polling(dp)
