import discord


def syntaxHighlight(string, type):
    temp = str("```") + type + "\n" + string + str("```")
    return temp


def embedColor(string, type, titleName):
    temp = str("```") + type + "\n" + string + str("```")
    embed = discord.Embed(color=discord.Color.random(), title=titleName)
    embed.add_field(name=titleName, value=temp)
    return embed
