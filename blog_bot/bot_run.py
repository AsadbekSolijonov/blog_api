import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from blog_bot.api import get_posts

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6669615336:AAHoZW2A0w93z4Kyxd8WwmwE32jPfXNfiBc"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('posts'))
async def posts_handler(message: Message) -> None:
    try:
        datas = get_posts()
        datas = datas if datas else "Ma'lumot qo'shing"
        await message.answer(f"{datas}")
    except ConnectionError as e:
        await message.answer("Nice Try! ")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
