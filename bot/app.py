async def on_startup(dp):
    from utils.notify_admins import on_startup_notify

    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands

    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    allowed_updates = ['message', 'chat_member', 'my_chat_member', 'callback_query']

    executor.start_polling(
        dp, on_startup=on_startup, allowed_updates=allowed_updates,
    )
