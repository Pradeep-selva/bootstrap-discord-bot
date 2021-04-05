import os
import sys
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(prog='bootstrap-discord-bot', 
                                     description='An opinionated cli-tool to bootstrap a discord.py bot') 
  
    parser.add_argument('--cogs', action='store_true', help='bootstrap a discord.py bot code with cogs') 
    parser.add_argument('--nocogs', action='store_true', help="bootstrap a discord.py bot code without cogs") 
    parser.add_argument('--makecog', nargs=2, help='create a new cog in an existing project, enter: cog name, file name')
  
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.cogs:
        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/requirements.py'), 'r') as f:
            with open('requirements.txt', 'w') as w:
                w.write(f.read())

        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/env.py'), 'r') as f:
            with open('.env', 'w') as w:
                w.write(f.read())

        with open('.gitignore', 'w') as w:
            w.write(".env")

        os.mkdir('cogs')

        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/bot_with_cogs.py'), 'r') as f:
            with open('bot.py', 'w') as w:
                w.write(f.read())

        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/sample_cog.py'), 'r') as f:
            with open('./cogs/utilities.py', 'w') as w:
                w.write(f.read())

        print('\33[34m' + '-- YOUR FOLDER TREE --' + '\x1b[0m')

        print("\t-->cogs\n\t\t-->utilities.py\n\t-->bot.py\n\t-->.env\n\t-->requirements.txt\n\t-->.gitignore\n")
        print('\x1b[6;30;42m' + 'Successfully bootstrapped your bot with cogs!' + '\x1b[0m')

        print('\33[43m' + 'RUN: pip3 install -r requirements.txt' + '\x1b[0m')

        print("\n========================================================================")
        print("Star the repo: https://github.com/Pradeep-selva/create-discord-bot")
        print("========================================================================")

    elif args.nocogs:
        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/requirements.py'), 'r') as f:
            with open('requirements.txt', 'w') as w:
                w.write(f.read())

        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/env.py'), 'r') as f:
            with open('.env', 'w') as w:
                w.write(f.read())

        with open('.gitignore', 'w') as w:
            w.write(".env")

        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/bot_without_cogs.py'), 'r') as f:
            with open('bot.py', 'w') as w:
                w.write(f.read())
        
        print('\33[34m' + '-- YOUR FOLDER TREE --' + '\x1b[0m')
        
        print("\t-->bot.py\n\t-->.env\n\t-->requirements.txt\n\t-->.gitignore\n")
        print('\x1b[6;30;42m' + 'Successfully bootstrapped your bot without cogs!' + '\x1b[0m')

        print('\33[43m' + 'RUN: pip3 install -r requirements.txt' + '\x1b[0m')

        print("\n========================================================================")
        print("Star the repo: https://github.com/Pradeep-selva/create-discord-bot")
        print("========================================================================")

    elif args.makecog:
        cog_name = args.makecog[0]
        file_name = args.makecog[1]

        content = f"""import discord
from discord.ext import commands

class {cog_name}(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog({cog_name}(bot))"""
        
        if os.path.isdir("cogs"):
            with open(f'cogs/{file_name}.py', 'w') as w:
                w.write(content)
            print(f"{file_name}.py with cog {cog_name} created successfully in cogs/{file_name}.py!")
        else:
            print("Please initialise a project by running: bootstrap-discord-bot --cogs, to use this command.")


        

        

