import os
import sys
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(prog='bootstrap-discord-bot', 
                                     description='An opinionated cli-tool to bootstrap a discord.py bot') 
  
    parser.add_argument('--cogs', action='store_true', help='bootstrap a discord.py bot code with cogs') 
    parser.add_argument('--nocogs', action='store_true', help="bootstrap a discord.py bot code without cogs") 
  
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/requirements.py'), 'r') as f:
        with open('requirements.txt', 'w') as w:
            w.write(f.read())

    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/env.py'), 'r') as f:
        with open('.env', 'w') as w:
            w.write(f.read())

    with open('.gitignore', 'w') as w:
        w.write(".env")

    if args.cogs:
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

    else:
        with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/bot_without_cogs.py'), 'r') as f:
            with open('bot.py', 'w') as w:
                w.write(f.read())
        
        print('\33[34m' + '-- YOUR FOLDER TREE --' + '\x1b[0m')
        
        print("\t-->bot.py\n\t-->.env\n\t-->requirements.txt\n\t-->.gitignore\n")
        print('\x1b[6;30;42m' + 'Successfully bootstrapped your bot without cogs!' + '\x1b[0m')

    print('\33[43m' + 'RUN: pip3 install -r requirements.txt' + '\x1b[0m')

    print("\n========================================================================")
    print("Check the repo out: https://github.com/Pradeep-selva/create-discord-bot")
    print("========================================================================")
