"""Импорт модулей обработки событий"""
from aiogram import Dispatcher
from . import start, settings


async def include_routers(dp: Dispatcher):
    """Добавить роутеры в диспетчер"""
    dp.include_routers(
        start.router,
        settings.router,
    )
