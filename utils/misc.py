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

def getUsers(queue, bot):
    out = {}
    guild = get(bot.guilds, id = bot.guildId)
    for member in guild.members:
        if member.id in queue:
            rank = "unranked"
            for roleS in member.roles:
                if roleS.name.lower() in bot.ranks:
                    rank = roleS.name.lower()
                    break
            out[member.id] = {"name": member.display_name, "rank": bot.ranks[rank], "roles": "".join(f"{bot.roles[bot.rolesB[role]]}" for role in getRoles(queue[member.id]))}

    return out

class BoardEmbed(disnake.Embed):
    def __init__(self, queue, bot, **options):
        super().__init__(title="", color=disnake.Colour.red(), **options)
        queueAux = getUsers(queue, bot)
        list = ""
        for _, player in queueAux.items():
            list += f"{player['rank']+player['name']}: {player['roles']}\n"
        if list == "":
            self.title = "Queue"
            self.set_image(url="https://media0.giphy.com/media/5x89XRx3sBZFC/giphy.gif?cid=ecf05e47xlqx0lew41cbk40i5tarivqozmlpa6ip4yjeuxou&rid=giphy.gif")
        else:
            self.add_field(name="Queue", value=list)
        
        self.set_footer(text=f"{len(queue)}/10 Players")

class BoardEmbed2(disnake.Embed):
    def __init__(self, queue, bot, **options):
        super().__init__(title="", color=disnake.Colour.dark_blue(), **options)

                

    
    


