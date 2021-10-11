from config import Config

async def AuthUserCheck(chat_id, user_id):
    # if public
    if 0 in Config.AUTH_IDS:
        return True
    # if userid in config
    elif user_id in Config.AUTH_IDS:
        return True
    # if chatid in config
    elif chat_id in Config.AUTH_IDS:
        return True
    else:
        return False