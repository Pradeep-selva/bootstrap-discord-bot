# to install all dependencies, run -- pip3 install -r requirements.txt
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# getting discord token from .env
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='+')

# to get the default discord.py help command, remove the following line
bot.remove_command('help')

# setting bot activity and presence and logging connection.
@bot.event
async def on_ready():
    activity = discord.Game(name="+help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='ping', help='ping')
async def ping(ctx):
    await ctx.channel.send('Pong! {0} ms'.format(round(bot.latency, 1)))

# running the bot
bot.run(token)