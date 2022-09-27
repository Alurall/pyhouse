import disnake
from disnake.ext import commands
from utils.views import View, View2, RoleSelect, Button
from utils.misc import BoardEmbed

class QueueCog(commands.Cog):
	queue = {}
	#	148922387587399680: 10,
	#	339368436624785408: 31,
	#	777198470276317204: 16,
	#}

	def __init__(self, bot):
		self.bot = bot # sets the client variable so we can use it in cogs
		self.reset_state()
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(type(self).__name__ + " loaded")
		await self.draw_board()

	async def draw_board(self):
		board = BoardEmbed(self.queue, self.bot)
		button = Button(self.selector, self.bot)
		channel = self.bot.get_channel(self.bot.queueChannelId)
		if not self.state["tableId"]:
			self.state["tableId"] = await channel.send(embed=board, view=button)
		else:
			await self.state["tableId"].edit(embed=board, view=button)
	
	async def update_response(self, user):
		view = self.selector(user)
		await self.bot.get_eph(user).edit_original_message(view=view)

	def selector(self, user):
		status = self.state["status"]
		if status == 0:
			if user in self.queue:
				return View2(RoleSelect(self, self.bot.roles), self.remove_from_queue)
			else:
				return View(RoleSelect(self, self.bot.roles))
		elif status == 1:
			pass
		else:
			pass
	
	async def remove_from_queue(self, user):
		if self.state["status"] == 0 and user in self.queue:
			self.queue.pop(user)
			await self.draw_board()
			await self.update_response(user)
			
	def reset_state(self):
		self.state = {
			"tableId":   None, # Link to the message
			"status":    0,    # 0 -> waiting for players; 1 -> Selecting players; 2 -> Game in progress
			"cpt1":      None, # User id#
			"cpt2":      None, # User id#
			"team1":     [],   # List of ids#
			"team2":     [],   # List of ids#
			"firstpick": None, # capt id#
			"side":      None, # True or False
		}

	@commands.slash_command()
	async def redraw(self, inter: disnake.CommandInteraction, language: str):
		await self.draw_board()
		await inter.response.send_message("hi1")

