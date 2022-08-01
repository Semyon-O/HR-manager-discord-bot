import discord
from Config.config import TOKEN
from Functionality.manage import Manager


class Components(Manager):
    async def on_ready(self):
        print("succesful")


bot = Components(command_prefix='/')

bot.run(TOKEN)
