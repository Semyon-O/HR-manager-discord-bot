import discord
from discord.ext.commands import Bot
from Config.config import TOKEN
import Functionality.manage as manager
from discord_components import DiscordComponents, Button, ButtonStyle
import Functionality.report as report
import Functionality.settings as setting


bot = Bot(command_prefix='/', intents=discord.Intents.all())


# events
@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('We have logged in {0.guilds} as {0.user}'.format(bot))


@bot.event
async def on_button_click(ctx):
    data_setting = setting.get_data()
    if ctx.component.label == data_setting["settings_buttons_greetings"]["label_hr"]:
        await manager.on_button_hr(ctx)

    if ctx.component.label == data_setting["settings_buttons_greetings"]["label_report"]:
        await report.on_button_report(ctx)



# commands from modules
bot.add_command(manager.create_hr_channel)
bot.add_command(manager.make_greetings_button)
bot.add_command(report.create_report_channel)
bot.add_command(manager.create_archive_channel)

bot.run(TOKEN)
