import discord

def syntaxHighlight(string, type):
    temp = f"```{type}\n{string}```"
    return temp


def embedColor(string, type, titleName):
    temp = f"```{type}\n{string}```"
    ret = discord.Embed(color=discord.Colour.random(),title=titleName)
    ret.add_field(name="----------------",value=temp)
    return ret
