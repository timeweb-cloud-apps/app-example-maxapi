import asyncio
import logging
import os

from maxapi import Bot, Dispatcher
from maxapi.types import BotStarted, Command, MessageCreated

dp = Dispatcher()

HELP_TEXT = (
    "/start — приветствие\n"
    "/help — список команд\n"
    "/ping — проверка связи\n"
    "Любой другой текст я повторю."
)


@dp.bot_started()
async def bot_started(event: BotStarted) -> None:
    await event.bot.send_message(
        chat_id=event.chat_id,
        text="Привет! Я бот на maxapi, запущенный в Timeweb Cloud Apps.\nКоманды: /help",
    )


@dp.message_created(Command("start"))
async def start(event: MessageCreated) -> None:
    await event.message.answer("Привет! Я бот на maxapi, запущенный в Timeweb Cloud Apps.\nКоманды: /help")


@dp.message_created(Command("help"))
async def help_command(event: MessageCreated) -> None:
    await event.message.answer(HELP_TEXT)


@dp.message_created(Command("ping"))
async def ping(event: MessageCreated) -> None:
    await event.message.answer("pong")


@dp.message_created()
async def echo(event: MessageCreated) -> None:
    text = event.message.body.text if event.message.body else None
    if text:
        await event.message.answer(text)


async def main() -> None:
    bot = Bot(token=os.environ["BOT_TOKEN"])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
