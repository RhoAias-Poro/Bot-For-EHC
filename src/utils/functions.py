import discord

def syntaxHighlight(string, type):
    temp = f"```{type}\n{string}```"
    return temp


def embedColor(string, type, titleName):
<<<<<<< HEAD
    temp = str("```") + type + "\n" + string + str("```")
    embed = discord.Embed(color=discord.Color.random(), title="")
    embed.add_field(name=titleName, value=temp)
    return embed
=======
    temp = f"```{type}\n{string}```"
    ret = discord.Embed(color=discord.Colour.random(),title=titleName)
    ret.add_field(name="----------------",value=temp)
    return ret
>>>>>>> updateProject
