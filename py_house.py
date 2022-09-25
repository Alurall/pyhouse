import logging
import os
from dotenv import load_dotenv
load_dotenv()
from typing import List
import disnake
from disnake.ext import commands
from database import ClientDB
from cogs.queue import QueueCog

#bot = commands.Bot(command_prefix=commands.when_mentioned)


class PyHouse(commands.Bot):
	def __init__(self, **options):
		super().__init__(commands.when_mentioned, **options)

		logging.basicConfig()
		self.logger = logging.getLogger("py_house")
		self.logger.setLevel(logging.INFO)

		self.logger.info("Loading Cogs...")
		self.add_cog(QueueCog(self))
		

	async def on_ready(self):
		self.logger.info("Connecting to the DB...")
		self.session = ClientDB(os.environ["MONGO_STRING"])
		self.session.connect()
		self.session.printstuff()
	
	@commands.slash_command()
	async def autocomplete1(inter: disnake.CommandInteraction, language: str):
		await inter.response.send_message("hi1")

	
	@commands.command()
	async def command(self, ctx):
		print("hi")

description = "Just a test bot"
intents = disnake.Intents.all()
bot = PyHouse(description=description, intents=intents)
bot.run(os.environ["INHOUSE_BOT_TOKEN"])



# You may even add autocompletion for your commands.
# This requires the type to be a string and for you to not use enumeration.
# Your autocompleter may return either a dict of names to values or a list of names
# but the amount of options cannot be more than 20.

#LANGUAGES = ["Python", "JavaScript", "TypeScript", "Java", "Rust", "Lisp", "Elixir"]
#
#
#async def autocomplete_langs(inter, string: str) -> List[str]:
#    return [lang for lang in LANGUAGES if string.lower() in lang.lower()]
#
#
#@bot.slash_command()
#async def autocomplete(
#    inter: disnake.CommandInteraction,
#    language: str = commands.Param(autocomplete=autocomplete_langs),
#):
#    ...
#
#
## In case you don't want to use Param or need to use self in a cog you may
## create autocomplete options with the decorator @slash_command.autocomplete()
#@bot.slash_command()
#async def languages(inter: disnake.CommandInteraction, language: str):
#    ...
#
#
#@languages.autocomplete("language")
#async def language_autocomp(inter: disnake.CommandInteraction, string: str):
#    string = string.lower()
#    return [lang for lang in LANGUAGES if string in lang.lower()]


