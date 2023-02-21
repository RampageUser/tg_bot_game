from config_bot.config import make_bot
from aiogram import Bot, Dispatcher
from aiogram.filters import Text, CommandStart
from aiogram.types import Message,KeyboardButton, ReplyKeyboardMarkup
from database_sqlite.database import *
from logic_game.logic import *

# Создание базы данных
create_tabler()

# Подкидывание токена
tg_bot = make_bot('./config_bot/.env')
TOKEN: str = tg_bot.token

# Регистрация бота
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

# Кнопки
button1: KeyboardButton = KeyboardButton(text='Камень')
button2: KeyboardButton = KeyboardButton(text='Ножницы')
button3: KeyboardButton = KeyboardButton(text='Бумага')
button4: KeyboardButton = KeyboardButton(text='Статистика')
button5: KeyboardButton = KeyboardButton(text='Помощь')
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button1, button2, button3],
                                                              [button4, button5]], resize_keyboard=True, one_time_keyboard=True)

# /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    random_option: str = spin_random_wheel()
    add_player(id=message.from_user.id, first_name=message.from_user.first_name, last_name=message.from_user.last_name,
               random_option=random_option)
    await message.answer('Я бот для игры в\n"Камень Ножницы Бумага".\n'
                         'Давай поиграем!', reply_markup=keyboard)

# /help
@dp.message(Text(text = ['Помощь','/help', 'help'], ignore_case=True))
async def process_help_command(message: Message):
    await message.answer('Ты можешь использовать кнопки,\n'
                         'или вводить все с клавиатуры.', reply_markup=keyboard)

# Обработка пользовательских вариантов
@dp.message(Text(text=['Камень', 'Ножницы', 'Бумага'], ignore_case=True))
async def process_player_option(message: Message):
    random_option: str = show_random_option(id=message.from_user.id)
    compare: bool | None = compare_option(player=message.text, random_option=random_option)
    if compare == True:
        change_win(id=message.from_user.id)
        change_games(id=message.from_user.id)
        option: str = spin_random_wheel()
        change_random_option(id=message.from_user.id, random_option=option)
        await message.answer(f'Ты выйграл!\nБот выбрал: {random_option}', reply_markup=keyboard)
    elif compare == False:
        change_games(id=message.from_user.id)
        option: str = spin_random_wheel()
        change_random_option(id=message.from_user.id, random_option=option)
        await message.answer(f'Ты проиграл!\nБот выбрал: {random_option}', reply_markup=keyboard)
    elif compare == None:
        change_games(id=message.from_user.id)
        option: str = spin_random_wheel()
        change_random_option(id=message.from_user.id, random_option=option)
        await message.answer(f'Ничья!\nБот выбрал: {random_option}', reply_markup=keyboard)

# Показ статистики
@dp.message(Text(text='Статистика', ignore_case=True))
async def process_statistic(message: Message):
    win: int = show_win(id=message.from_user.id)
    games: int = show_games(id=message.from_user.id)
    await message.answer(f'Количество побед: {win}\nКоличество игр: {games}', reply_markup=keyboard)

if __name__ == "__main__":
    dp.run_polling(bot)