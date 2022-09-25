import disnake
from disnake.ext import commands
from utils.dropdown import DropdownView

class QueueCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(type(self).__name__ + " loaded")
	
	@commands.slash_command()
	async def autocomplete1(inter: disnake.CommandInteraction, language: str):
		await inter.response.send_message("hi1")

	@commands.slash_command()
	async def colour(inter: disnake.CommandInteraction):
		"""Sends a message with our dropdown containing colours"""

    	# Create the view containing our dropdown
		options = [
			{
				"label": "Milenian",
				"description": "Mid / Top",
				"emoji": '<:gold:1020060594688245801>'
			},
			{
				"label": "Bronze",
				"description": "Fill",
				"emoji": '<:platinum:1020060661243449354>'
			},
			{
				"label": "Paulinho",
				"description": "Jungle / Support",
				"emoji": '<:diamond:1020060692285501460>'
			}
		]
		view = DropdownView(options, "Granda cena")

    	# Sending a message containing our view
		await inter.response.send_message("Pick your favourite colour:", view=view)

	@commands.command()
	async def command(self, ctx):
		print("hi")
