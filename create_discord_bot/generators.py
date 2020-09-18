import os
from pathlib import Path

def gen_commons():
    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/requirements.txt'), 'r') as f:
        with open('requirements.txt', 'w') as w:
            w.write(f.read())

    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/.env'), 'r') as f:
        with open('.env', 'w') as w:
            w.write(f.read())

    with open('.gitignore', 'w') as w:
        w.write(".env")


def gen_cogs():
    os.mkdir('cogs')

    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/bot_with_cogs.py'), 'r') as f:
        with open('bot.py', 'w') as w:
            w.write(f.read())

    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/sample_cog.py'), 'r') as f:
        with open('./cogs/utilities.py', 'w') as w:
            w.write(f.read())


def gen_nocogs():
    with open(os.path.join(Path(__file__).parent.absolute(), 'boilerplates/bot_without_cogs.py'), 'r') as f:
        with open('bot.py', 'w') as w:
            w.write(f.read())