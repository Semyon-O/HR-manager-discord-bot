import discord
from discord.ext import commands
from Functionality.settings import save, get_data
from discord_components import DiscordComponents, Button, ButtonStyle
import Functionality.settings as setting


@commands.command()
async def create_hr_channel(ctx, name="Заявки"):
    guild = ctx.guild
    channel = await guild.create_category(name=name)
    data_settings = get_data()
    data_settings["settings_channel"]["channel_hr_name"] = str(channel)
    save(data_settings)
    await ctx.send("Channel made")


@commands.command()
async def create_archive_channel(ctx, name="Archive"):
    guild = ctx.guild
    channel = await guild.create_category(name=name)
    data_settings = get_data()
    data_settings["settings_channel"]["archive_channel"] = str(channel)
    save(data_settings)
    await ctx.send("Archive channel made")

@commands.command()
async def make_greetings_button(ctx):
    try:
        embed = discord.Embed(title="Присоединяйся к нам",
                              colour=0x87CEEB)
        embed.add_field(name="Описание", value="Привет. Этот бот поможет тебе связаться с руководством этого сервера "
                                               "если "
                                               "ты хочешь быть частью этой команды или если хочешь подать репорт на "
                                               "перевод",
                        inline=False)
        embed.add_field(name="Подача ""Заявки",
                        value="Все очень просто. Ты нажимаешь на кнопку и в отдельной категории "
                              "создается твой чат с руководством. \n "
                              "Пока ты будешь ждать собеседования с руководством ты увидешь кнопку "
                              "заполнить анкету кандидата. \n "
                              "Нажми на нее и заполни все поля о себе."
                              "Как только ты закончишь собеседование нажми на кнопку 'закрыть' если "
                              "уверен, что у тебя не осталось вопросов.", inline=False)
        embed.add_field(name="Сообщение ошибки",
                        value="Если вас, что-то не устраивает в нашей работе, то нажмите на кнопку ""сообщить об "
                              "ошибке \n "
                              "Для вас будет создан чат, с руководством, где вы сможете рассказать об ошибке",
                        inline=False)
        embed.set_footer(
            text="При первом нажатии кнопки могут не сработать.Если это произойдет,то попробуйте еще раз. Если они все еще не сработали то пишите администрации сервера.")
        await ctx.send(
            embed=embed,
            components=[
                Button(style=ButtonStyle.blue, label=get_data()["settings_buttons_greetings"]["label_hr"]),
                Button(style=ButtonStyle.red, label=get_data()["settings_buttons_greetings"]["label_report"])
            ]
        )
    except:
        print("Ошибка. Кнопка не создалась")

async def on_button_hr(ctx):
    guild = ctx.guild
    author = ctx.author
    channel = ctx.channel
    data_setting = setting.get_data()
    cat = discord.utils.get(ctx.guild.categories, name=str(data_setting["settings_channel"]["channel_hr_name"]))

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
    }

    text_channel = await guild.create_text_channel(name=str(author), category=cat, overwrites=overwrites)
    await ctx.send("Чат с руководством создан")
    print("Hr channel work")
