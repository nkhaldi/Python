import asyncio
import logging
from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from location import register_location
from user import register_user
from weather import register_weather

logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_user(dp)
    register_weather(dp)
    register_location(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    env = Env()
    env.read_env(".env")

    bot = Bot(token=env.str("BOT_TOKEN"), parse_mode='HTML')
    dp = Dispatcher(bot)

    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
