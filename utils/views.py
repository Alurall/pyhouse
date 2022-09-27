import disnake
from disnake.ext import commands

class RoleSelect(disnake.ui.Select):
    def __init__(self, queue, roles):
        self.queue = queue
        option_list = []
        count = 0
        for name, emoji in roles.items():
            option_list.append(
                disnake.SelectOption(
                    label=name,
                    description="",
                    emoji=emoji,
                    value=str(2**count),
                )
            )
            count += 1

        super().__init__(
            placeholder="Select 1 or more roles",
            min_values=1,
            max_values=6,
            options=option_list,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        if len(self.queue.queue) >= 10:
            return
        roles = 0
        if len(self.values) >= 5 or "32" in self.values:
            self.queue.queue[interaction.user.id] = 32
        else:
            for value in self.values:
                roles += int(value)
            self.queue.queue[interaction.user.id] = roles
        await self.queue.draw_board()
        await self.queue.update_response(interaction.user.id)

class Dropdown(disnake.ui.Select):
    def __init__(self, options, placeholder = "", min_values=1, max_values=1):
        # Set the options that will be presented inside the dropdown
        option_list = []
        for option in options:
            print(option)
            option_list.append(
                disnake.SelectOption(
                    label=option["label"],
                    description=option["description"],
                    emoji=option["emoji"]
                )
            )

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            options=option_list,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await self.msg.msg.edit(view=self.msg.msg.view)
        #names = ''
        #for value in self.values:
        #    names += "**"+value+"**" if names == '' else (" and " + "**"+value+"**")
        #await interaction.response.send_message(f"You picked {names}")


class View(disnake.ui.View):
    def __init__(self, item, **options):
        super().__init__(**options)

        # Adds the dropdown to our view object.
        self.add_item(item)

class Button(disnake.ui.View):
    def __init__(self, selector, bot, **options):
        self.selector = selector
        self.bot = bot
        super().__init__(**options)
        
    @disnake.ui.button(label="Click me!", style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("", view=self.selector(interaction.user.id), ephemeral=True)
        if self.bot.get_eph(interaction.user.id):
            await self.bot.get_eph(interaction.user.id).edit_original_message(content="dismiss me", view=None, embed=None)
        self.bot.add_eph(interaction.user.id, interaction)

class View2(disnake.ui.View):
    def __init__(self, item, func, **options):
        self.func = func
        super().__init__(**options)
        self.add_item(item)

    @disnake.ui.button(label="Leave Queue", style=disnake.ButtonStyle.red)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await self.func(interaction.user.id)



