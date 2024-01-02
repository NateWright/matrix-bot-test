import niobot


class MyFunModule(niobot.Module):  # subclassing niobot.Module is mandatory for auto-detection.
    def __init__(self, bot):
        self.bot = bot  # bot is the NioBot instance you made in main.py!

    @niobot.command()
    async def hello(self, ctx):
        await ctx.reply("Hello %s!" % ctx.event.sender)