# to install all dependencies, run -- pip3 install -r requirements.txt
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# getting discord token from .env
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# to intialise a new cog, add a string to the array in the form -- 'cogs.<file_name_without_extension>'
intial_extensions = ['cogs.utilities']

# setting a bot prefix, to get the default discord.py help command, remove second argument
bot = commands.Bot(command_prefix='+', help_command=None)

# loading all cogs
if __name__ == '__main__':
    for extension in intial_extensions:
        print(f"{extension[5:]}.py loaded")
        bot.load_extension(extension)

# setting bot activity and presence and logging connection.
@bot.event
async def on_ready():
    activity = discord.Game(name="+help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'{bot.user.name} has connected to Discord!')

# running the bot
bot.run(token, bot=True, reconnect=True)