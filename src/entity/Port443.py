import asyncio

import discord
from dotenv import load_dotenv

from src.utils import functions as util

load_dotenv()


class port443:
    ############# set up variable #######################################################
    userLogin = False
    host = "antoineHackerLord.com"
    HTML = '''
    <!DOCTYPE html>
       <html lang="en">
         <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <meta http-equiv="X-UA-Compatible" content="ie=edge">
           <link rel="stylesheet" href="style.css">
           <title>On Includes</title>
         </head>
         <body>
           <script src="script.js"></script>
            <!-- you can open file script.js and style.css -->
           <h1>My Life as Terror</h1>
           <p>The greater the suffer, the greater the piece.</p>
           <br>
           <p> Source: EHC </p>
           <button type="button" onclick="greetings();">Say hello</button>
         </body>
       </html>
    '''
    CSS = '''
    body {
        background-color: lightblue;
        /* NO1} */
          }'''
    JS = '''function detonate()
     {
       alert("Self destructed!");
     }'''
    YOUTUBE = 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6WIULXGR3TSV3HLBRVC==='
    WEBSITE = 'antoineHackerLord.com'
    FINALE = """
    - COMPLETED ATTACKS: 
        +) 29/02/2019: SPREAD OUT CORONA VIRUS
        +) 20/10/2020: HIJACK INTERNATIONAL AIRPLANE IN CHINA
        +) 09/11/2021: BOMB AT EIFEL TOWER IN FRANCE

    - PLANNING ATTACKS: 
        +) 26/11/2022 AT ********* ********* (FOR SECURITY REASON ONLY SHOW THE ENCODED IMAGE)"""
    PASSWORD = 'picoctf'
    user = 'shine102'

    ##################################################################################################
    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send("Enter password: ")

        def check(msg):  # check if the information come from the same person
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            # take user input with 'message' placeholder
            password = await ctx.bot.wait_for('message', check=check, timeout=60.0)
            # after this password is like an object that have lots of attributes, so we need to access the
            # content of it
        except TimeoutError:
            # if over 60 seconds then kick
            await ctx.send(util.syntaxHighlight("You did not enter password on time, automatically exit", "fix"))
            return False

        if password.content == self.PASSWORD:  # same pass
            await ctx.send(util.syntaxHighlight(f"Login to {self.host} through port 443 successfully\n", ""))
            port443.userLogin = True
            return True
        else:
            await ctx.send(embed=util.embedColor("- Wrong password, please try again -", "diff", "ERROR"))
            return False

    async def listAllFile(self, ctx):
        await ctx.send(
            util.syntaxHighlight("1. base.html\n2. script.js\n3. style.css\n4. antoineHackerLordTest.com\n", ""))
        await ctx.send(embed=util.embedColor(
            "To open and see the content of files above, please use command $open", 'diff', 'OPEN COMMAND'))

    async def open(self, ctx, fileName: str):
        if fileName == 'base.html':
            await ctx.send(embed=util.embedColor(self.HTML, "html", "FILE: base.html"))
        elif fileName == 'script.js':
            await ctx.send(embed=util.embedColor(self.JS, "js", "FILE: script.js"))
        elif fileName == 'style.css':
            await ctx.send(embed=util.embedColor(self.CSS, "css", "FILE: style.css"))
            await asyncio.sleep(5)
            string = '''Congrats on finding the nuclear key, you have done well. However, we worry that he would change the attack but still happen at the same location.\nYour final mission is to find the document file containing information about that attack and find the exact name of the place where it takes place.
            '''
            await ctx.send(embed=util.embedColor(string, "", "FINAL MISSION"))
            await asyncio.sleep(3)
            string = "Our spy tells us that maybe it is hidden at the current directory. You should check it.\nRemember that you only have 5 minutes left before Antoine finds out everything. Good luck !\n(P/s: Maybe this could help you: https://devconnected.com/how-to-show-hidden-files-on-linux/. Anyway, the command is: ls -a 😜)"
            await ctx.send(embed=util.embedColor(string, "", "HINT FOR YOU"))

        elif fileName == 'antoineHackerLordTest.txt':
            await ctx.send(embed=util.embedColor("YOU ARE LATE", "", "FILE: antoineHackerLordTest.txt"))
            await ctx.send(util.syntaxHighlight(
                "Oh no, the time is almost up, you must hurry!!!!!",
                ""))
        elif fileName == '.secret.txt':
            await ctx.send(embed=util.embedColor(self.YOUTUBE, "", "FILE: .secret.txt"))
            await ctx.send(
                util.syntaxHighlight("Oh, another encryption. Looks like Base64 but it isn't. Perhaps, Base 64/2=? ",
                                     ""))
        elif fileName == '.nothing_special_here.txt':
            await ctx.send(embed=util.embedColor(self.FINALE, "", "FILE: .nothing_special_here.txt"))
            await ctx.send(file=discord.File('C:\\Users\ADMIN\Pictures\QRCODE.png'))
            await util.syntaxHighlight(
                "The image above is strange, haven't seen it before, you should Google Lens it to see what happen and "
                "remember, double of something is the best 🐧 "
                "Almost end of our mission, please summit the key and location to the website", "")
        else:
            await ctx.send(embed=util.embedColor("- No such file exist - ", "diff", "ERROR"))
        return True

    async def listAllHiddenFile(self, ctx):
        await ctx.send(util.syntaxHighlight(
            "1. base.html\n2. script.js\n3. style.css\n4. antoineHackerLordTest.txt\n5. .secret.txt\n6. .nothing_special_here.txt",
            ""))
