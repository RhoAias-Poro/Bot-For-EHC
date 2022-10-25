import os
# @bot.command(name="pussy")
# async def Cat(ctx):
#   api = os.environ['API']
#   # send requests to the api and response now a json
#   response = requests.get(api)
#   image_link = response.json()[0]  # like a list and need to choose index
#   await ctx.send(image_link["url"])  # print the url


# async def five_minutes_images():
#   while True:
#     now = datetime.datetime.now()
#     then = now + datetime.timedelta(minutes=5)
#     wait_time = (then - now).total_seconds()
#     await asyncio.sleep(wait_time)

#     ID = os.environ['channelID']  # return string obj
#     channel = bot.get_channel(int(ID))
#     await Cat(channel)