from aiogram.dispatcher.filters.state import State, StatesGroup


class ChangeGroup(StatesGroup):
    change_photo = State()
    change_description = State()
    change_tittle = State()
    chat_id = State()
    message_id = State()