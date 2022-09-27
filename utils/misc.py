import disnake
from disnake.utils import get

def getRoles(n):
    out = []
    c = 0
    for i in reversed(bin(n).replace("0b", "")):
        if int(i):
            out.append(2**c)
        c+=1
    return out

class BoardEmbed(disnake.Embed):
    def __init__(self, queue, bot, **options):
        super().__init__(title="", color=disnake.Colour.red(), **options)
        queueAux = {}
        guild = get(bot.guilds, id = bot.guildId)
        for member in guild.members:
            if member.id in queue:
                rank = "unranked"
                for roleS in member.roles:
                    if roleS.name.lower() in bot.ranks:
                        rank = roleS.name.lower()
                        break
                queueAux[bot.ranks[rank] + member.display_name] = "".join(f"{bot.roles[bot.rolesB[role]]}" for role in getRoles(queue[member.id]))
        list = ""
        for player, roles in queueAux.items():
            list += f"{player}: {roles}\n"
        if list == "":
            self.title = "Queue"
            self.set_image(url="https://media0.giphy.com/media/5x89XRx3sBZFC/giphy.gif?cid=ecf05e47xlqx0lew41cbk40i5tarivqozmlpa6ip4yjeuxou&rid=giphy.gif")
        else:
            self.add_field(name="Queue", value=list)
        
        self.set_footer(text=f"{len(queue)}/10 Players")


                

    
    


