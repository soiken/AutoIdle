# IdleRPG Discord Bot
The IdleRPG Discord Bot is a simple bot built using the discord.py library, designed to automate some of the commands in the IdleRPG game. The bot can automatically send commands to the IdleRPG bot in a specific Discord channel, at specified intervals.

## Features
The bot has the following features:

- Automatically send the following commands to the IdleRPG bot:
  - date
  - fe
  - pray
  - daily
  - xp
- Specify the interval at which to send the commands.
- Ability to manually start and stop the automatic command sending.
- Automatically respond to messages from the IdleRPG bot:
  - If the bot is on cooldown for a command, wait until the cooldown is over and resend the command.
  - If the bot is on an adventure, wait until the adventure is over and automatically start a new adventure.
  - Automatically level up when enough XP is earned.

## Getting Started
To get started with the IdleRPG Discord Bot, follow these steps:

1. Clone this repository to your local machine:

`git clone https://github.com/your-username/idlerpg-discord-bot.git`

2. Install the required dependencies using pip:

`pip install -r requirements.txt`

3. Create a new Discord bot account and invite it to your Discord server. Refer to the official Discord documentation for instructions on how to do this.

4. Copy the bot token from the Discord Developer Portal and set it as the TOKEN environment variable in a .env file:

`TOKEN=<your-bot-token>`

5. Start the bot by running the main.py file:

`python main.py`

6. The bot is now ready to use. Type $autorun in any channel the bot has access to, and it will automatically start sending commands to the IdleRPG bot at specified intervals.

## Usage

To use the IdleRPG Discord Bot, follow these steps:

1. Type $autorun in any channel the bot has access to. The bot will automatically start sending commands to the IdleRPG bot at specified intervals.
2. To stop the automatic command sending, type $autostop.
3. The bot will automatically respond to messages from the IdleRPG bot, including waiting for cooldowns and starting new adventures.

## Acknowledgements

This bot is built using the discord.py library. Thank you to the developers of discord.py for creating such a useful library.
