import discord
from discord.ext import commands


class Manager(commands.Bot):

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))