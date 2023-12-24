from aiogram import Dispatcher,Bot,executor
from aiogram.types import Message
from buttons import butons_for_news, btn_link
from configs import get_value
from parsing import news_pars

TOKEN='Your telegram bot token'

bot = Bot(TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message:Message):
    await message.answer('Добро пожаловать в Новостной Бот')
    await show_category_news(message)


async def show_category_news(message:Message):
    await message.answer('Выберите категорию',reply_markup=butons_for_news())



@dp.message_handler(content_types=['text'])
async def get_news_by_category(message:Message):
    chat_id=message.chat.id
    message_id=message.message_id
    category=message.text
    await  bot.delete_message(chat_id,message_id)
    news=news_pars(get_value(category))
    for n in news[::-1]:
        image=n.get('image')
        title=n.get('title')
        description=n.get('description')
        timeof=n.get('timeof')
        link=n.get('link')
        await message.answer_photo(photo=image,parse_mode='HTML',caption=f'''
<b>Время и дата 🕒:</b> {timeof}


<b>Заголовок:</b> {title}


<b>Описание:</b> {description}
''',reply_markup=btn_link(link))
















executor.start_polling(dp)
