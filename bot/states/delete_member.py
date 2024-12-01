from aiogram.dispatcher.filters.state import State, StatesGroup


class DeleteMember(StatesGroup):
    tg_user_id = State()
    message_id = State()
    chat_id = State()
