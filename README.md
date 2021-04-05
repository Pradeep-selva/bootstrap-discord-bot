<h1 align="center">Bootstrap Discord Bot</h1>

<h2 align="center">An opinionated cli-tool to bootstrap\generate your discord bot code!</h2>

## Demo

<div align="center">
    <img src="https://i.ibb.co/ZWdm21b/demo.gif" alt="demo" width="600"/>
</div>
<br/>

[![Downloads](https://pepy.tech/badge/bootstrap-discord-bot)](https://pepy.tech/project/bootstrap-discord-bot)
[![Downloads](https://pepy.tech/badge/bootstrap-discord-bot/month)](https://pepy.tech/project/bootstrap-discord-bot)
[![Downloads](https://pepy.tech/badge/bootstrap-discord-bot/week)](https://pepy.tech/project/bootstrap-discord-bot)

<br/>
<br/>

## Features

- Support for code with/without cogs.
- .env file support for keys and .gitignore to hide it.
- Bot code pre-built with a utility ping function to get you started!
- Setup new cogs using cli.

## Usage

- Install using

```
pip install bootstrap-discord-bot
```

- cd into your bot directory

- Run `bootstrap-discord-bot -h` to get help

<div align="center">
    <img src="https://i.ibb.co/c61P53p/help.png" alt="help" width="800"/>
</div>
<br/>
<br/>
<br/>

- Run `bootstrap-discord-bot --cogs` to initialize a discord bot with cogs.

<div align="center">
    <img src="https://i.ibb.co/DkzZsQv/cogs.png" alt="cogs" width="800"/>
</div>
<br/>
<br/>
<br/>

- Run `boostrap-discord-bot --nocogs` to initialize a discord bot without cogs.

<div align="center">
    <img src="https://i.ibb.co/hCjP76r/nocogs.png" alt="demo" width="800"/>
</div>

- Run `bootstrap-discord-bot --makecog cog_name file_name` to initialize a file in the cogs folder with required cog boilerplate.

## Built using

- Python
- Discord.py
- argparse
- setuptools
