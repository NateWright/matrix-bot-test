import niobot


class MyFunModule(niobot.Module):  # subclassing niobot.Module is mandatory for auto-detection.
    def __init__(self, bot):
        self.bot = bot  # bot is the NioBot instance you made in main.py!

    @niobot.command()
    async def hello(self, ctx):
        # print(ctx.room.display_name)
        print(ctx.room.group_name_structure()[1])
        await self.bot.send_message(ctx.event.sender, "Hello %s!" % ctx.event.sender)
        await ctx.respond("Hello %s!" % ctx.event.sender)

    @niobot.command(name="ss")
    async def create_secret_santa(self, ctx):
        print(ctx.room.group_name_structure()[1])