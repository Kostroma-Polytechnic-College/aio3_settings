"""Модуль с клавиатурами для команды start"""
from aiogram.types import BotCommand

COMMANDS = [
    BotCommand(command='start', description='Сброс состояний'),
    BotCommand(command='settings', description='Настройки пользователя'),
]
