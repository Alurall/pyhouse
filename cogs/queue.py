import disnake
from disnake.ext import commands
from utils.dropdown import DropdownView

class Confirm(disnake.ui.View):
	def __init__(self, msg):
		super().__init__()
		self.msg = msg

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
	@disnake.ui.button(label="Open", style=disnake.ButtonStyle.gray)
	async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
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
		await interaction.response.send_message("Confirming", view=DropdownView(options, "Granda cena", self.msg, self), ephemeral=True)


class QueueCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(type(self).__name__ + " loaded")
		await self.queue_board()

	async def queue_board(self):
		embed = disnake.Embed(
    		title="",
    		color=disnake.Colour.red(),
		)
		embed.add_field(name="Queue", value="<:roletop:1020061534728241212>\n<:rolejungle:1020061595323355147>\n<:rolemid:1020061701464408104>\n<:rolebot:1020061665657626694>\n<:rolesupport:1020061565011120188>\n<:rolefill:1020061631092379709>", inline=False)

		channel = self.bot.get_channel(self.bot.queue_chid)
		self.msg = await channel.send(embed=embed, view=Confirm(self))
	
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
