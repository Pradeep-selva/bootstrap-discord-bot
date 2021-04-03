# to install all dependencies, run -- pip3 install -r requirements.txt
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# getting discord token from .env
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# setting a bot prefix, to get the default discord.py help command, remove second argument
bot = commands.Bot(command_prefix='+', help_command=None)

# loading all cogs
if __name__ == '__main__':
   for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}') 

# setting bot activity and presence and logging connection.
@bot.event
async def on_ready():
    activity = discord.Game(name="+help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'{bot.user.name} has connected to Discord!')

# running the bot
bot.run(token, bot=True, reconnect=True)