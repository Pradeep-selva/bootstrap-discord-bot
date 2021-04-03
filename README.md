<h1 align="center">Bootstrap Discord Bot</h1>

<h2 align="center">An opinionated cli-tool to bootstrap your discord bot code!</h2>

## Demo

<div align="center">
    <img src="./screenshots/demo.gif" alt="demo" width="600"/>
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

## Usage

- Install using

```
pip install bootstrap-discord-bot
```

- cd into your bot directory

- Run `bootstrap-discord-bot -h` to get help

![img](./screenshots/help.png)
<br/>
<br/>
<br/>

- Run `bootstrap-discord-bot --cogs` to initialise a discord bot with cogs.

![img](./screenshots/cogs.png)
<br/>
<br/>
<br/>

- Run `boostrap-discord-bot --nocogs` to initialise a discord bot without cogs.

![img](./screenshots/nocogs.png)

## Built using

- Python
- Discord.py
- argparse
- setuptools
