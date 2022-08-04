from discord.ext import commands
import discord
from discord.ext import commands
from Functionality.settings import save, get_data
from discord_components import DiscordComponents, Button, ButtonStyle
import Functionality.settings as setting

@commands.command()
async def create_report_channel(ctx, name="Report"):
    guild = ctx.guild
    channel = await guild.create_category(name=name)
    data_settings = get_data()
    data_settings["settings_channel"]["channel_report_name"] = str(channel)
    save(data_settings)
    await ctx.send("Report channel made")


async def on_button_report(ctx):
    guild = ctx.guild
    author = ctx.author
    channel = ctx.channel
    data_setting = setting.get_data()
    cat = discord.utils.get(ctx.guild.categories, name=str(data_setting["settings_channel"]["channel_report_name"]))

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
    }

    text_channel = await guild.create_text_channel(name=str(author), category=cat, overwrites=overwrites)
    await ctx.send("Чат с руководством создан")
    print("Report channel made")