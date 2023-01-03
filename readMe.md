## Discord Bot for Dice rolling

The bot rolls dices in unique roleplaying-system.

### Installation and running without docker

Copy sample.env to .env and enter your DISCORD_TOKEN.

`python -m venv env`

`env\Scripts\Activate`

`pip install -r requirements.txt`

`cd src && bot.py`

### With docker

Copy sample.env to .env and enter your DISCORD_TOKEN.

`docker-compose up --build -d`

### Mogenius

Enter your DISCORD_TOKEN into mogenius key_vault.

Currently running on it.

### Invite

https://discord.com/api/oauth2/authorize?client_id=1059725786258616350&permissions=2048&scope=bot
