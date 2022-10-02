from discord.ext import commands
from cogs.match import Match


async def createSession(ctx: commands.Context, interval: int):
    if not Match.instance:
        Match.instance = Match(ctx, interval)
        await Match.instance.run()
        del Match.instance
        Match.instance = None


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='matches')
    async def _matches(self, ctx: commands.Context, interval: int = 60):
        self.bot.loop.create_task(createSession(ctx, interval))

    @commands.command(name="mstop")
    async def _stop(self, ctx: commands.Context):
        if Match.instance:
            await Match.instance.stop()


async def setup(bot):
    await bot.add_cog(Info(bot))
