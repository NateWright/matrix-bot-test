import niobot
import logging
import config

logging.basicConfig(level=logging.DEBUG, filename="bot.log")

bot = niobot.NioBot(
    homeserver=config.HOMESERVER,
    user_id=config.USER_ID,
    device_id=config.DEVICE_ID,
    store_path='./store',
    command_prefix="!bot ",
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
    await ctx.respond("Pong!")

# And while we're at it, we can add an event listener.
# For this example, we'll add an event listener that tells the user if there's a command error.
@bot.on_event("command_error")
async def on_command_error(ctx: niobot.Context, error: Exception):
    """Called when a command raises an exception"""
    # Take a look at the event reference for more information about events.
    # Now, we can send a message to the user.
    await ctx.respond("Error: {}".format(error))

bot.run(access_token=config.ACCESS_TOKEN)