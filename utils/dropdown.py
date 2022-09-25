import os

import disnake
from disnake.ext import commands

class Dropdown(disnake.ui.Select):
    def __init__(self, options, placeholder):

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
        #options = [
        #    disnake.SelectOption(
        #        label="Red", description="Your favourite colour is red", emoji="🟥"
        #    ),
        #    disnake.SelectOption(
        #        label="Green", description="Your favourite colour is green", emoji="🟩"
        #    ),
        #    disnake.SelectOption(
        #        label="Blue", description="Your favourite colour is blue", emoji="🟦"
        #    ),
        #]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder=placeholder,
            min_values=1,
            max_values=2,
            options=option_list,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        names = ''
        for value in self.values:
            names += "**"+value+"**" if names == '' else (" and " + "**"+value+"**")
        await interaction.response.send_message(f"You picked {names}")


class DropdownView(disnake.ui.View):
    def __init__(self, options, placeholder):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown(options, placeholder))
