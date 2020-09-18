import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='ping')
    async def ping(self, ctx):
        await ctx.send('Pong! {0} ms'.format(round(
            self.bot.latency, 1)))

    #remove this function if you disabled custom help from bot.py
    @commands.command(name="help")
    async def help(self, ctx):
        help = ""
        help += "**__Add your helper text__**\n"

        embed = discord.Embed(title="List of commands", color=0x1FEAEA)
        embed.description = help

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utilities(bot))