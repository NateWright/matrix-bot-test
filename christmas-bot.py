# echo.py
# Example:
# randomuser - "!echo example string"
# echo_bot - "example string"

import simplematrixbotlib as botlib

creds = botlib.Creds("https://matrix.nwright.tech", "natebot", "3X4h5EuphixE@3W", session_stored_file="session.txt")
config = botlib.Config()
config.encryption_enabled = True
config.emoji_verify = True
config.ignore_unverified_devices = False
config.store_path = './crypto_store/'
config.join_on_invite = True
bot = botlib.Bot(creds, config)
PREFIX = '!bot '

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args()[1:])
            )
    elif match.is_not_from_this_bot() and match.prefix() and match.command("start"):

        bot.api.
        [u, b ] = bot.api.room_create(is_direct=True, invite=[message.sender])
        await bot.api.send_text_message(
            u, "Hello, I am a bot. I am here to help you with your Christmas shopping. Type !help for more information."
        )


bot.run()