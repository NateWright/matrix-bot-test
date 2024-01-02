import niobot
import logging
import config

logging.basicConfig(level=logging.INFO, filename="bot.log")

bot = niobot.NioBot(
    homeserver=config.HOMESERVER,
    user_id=config.USER_ID,
    device_id='bot-test',
    store_path='./store',
    command_prefix="!",
    owner_id="@nate-wright:matrix.nwright.tech"
)
# We also want to load `fun.py`'s commands before starting:
bot.mount_module("fun")

@bot.on_event("ready")
async def on_ready(_):
    # That first argument is needed as the first result of the sync loop is passed to ready. Without it, this event
    # will fail to fire, and will cause a potentially catasrophic failure.
    print("Bot is ready!")


@bot.command()
async def ping(ctx):  # can be invoked with "!ping"
    await ctx.reply("Pong!")

bot.run(password=config.PASSWORD)