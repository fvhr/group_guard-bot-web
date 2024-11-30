from modules.interaction_api import InteractionBackendAPI


async def get_chat_info(chat_id: str) -> tuple[str, bool]:
    chat_info = await InteractionBackendAPI.get_chat(chat_id)
    description = chat_info['description'] if chat_info['description'] else "Описание отсутствует"
    bot_admin_status = "✅ Бот является администратором" if chat_info[
        'bot_is_admin'] else "❌ Бот не является администратором"
    message_text = (
        f'📋 <b>Информация о группе:</b>\n\n'
        f'🏷 <b>Название:</b> {chat_info["title"]}\n'
        f'📖 <b>Описание:</b> {description}\n'
        f'🔗 <b>Ссылка:</b> <a href="{chat_info["url"]}">Перейти в группу</a>\n'
        f'🖼 <b>Аватар:</b> <a href="{chat_info["avatar_url"]}">Посмотреть</a>\n'
        f'👮‍♂️ <b>Статус бота:</b> {bot_admin_status}'
    )
    admin_rights = (
        '\n\n⚠️ <b>Для корректной работы предоставьте боту права администратора.</b>'
    )
    if chat_info['bot_is_admin']:
        return message_text, True
    return message_text + admin_rights, False
