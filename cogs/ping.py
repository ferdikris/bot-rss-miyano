import discord
from discord.ext import commands
import datetime
import time
from random import choice, randint
class pingtime:
    """Ping, with time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong."""
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t3 = time.perf_counter()
        thedata = ("**Ping.**\nTime: " + str(round((t2-t1)*1000)) + "ms")
        thedata2 = ("**Pong.**\nTime: " + str(round((t3-t2)*1000)) + "ms")
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        color2 = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color2 = int(color2, 16)
        data = discord.Embed(description=thedata, colour=discord.Colour(value=color))
        data2 = discord.Embed(description=thedata2, colour=discord.Colour(value=color2))

        
        await self.bot.say(embed=data)
        await self.bot.say(embed=data2)		

def setup(bot):
    n = pingtime(bot)
    bot.add_cog(n)
