from typing import Optional
import disnake
from disnake.ext import commands
from disnake import TextInputStyle

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Наследуем модальное окно
class MyModal(disnake.ui.Modal): 
    def __init__(self):
        # Детали модального окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Название вашего города",
                custom_id="Название вашего города",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Координаты вашего города",
                custom_id="Координаты вашего города",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Количество участников на момент регистрации",
                custom_id="Количество участников на момент регистрации",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Присутствует ли строение для путеводителя",
                custom_id="Присутствует ли строение для путеводителя",
                style=TextInputStyle.paragraph,
                max_length=1024,
            ),
        ]
        super().__init__(
            title="Регистрация города", #название формы
            custom_id="1",
            components=components,
        )

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=0x2F3136) #дизайн embed'a
        embed.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar) #от кого идёт заявка
        embed.set_footer(text=f"<@{inter.author.id}>", icon_url="https://cdn.discordapp.com/attachments/1011917849050218566/1051534757038657536/882601305871360040.png") 

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            ) #результаты
        
        await bot.get_channel(1012089401792270439).send(disnake.utils.get(inter.author.guild.roles, id = 1011771434185535518 ).mention, embed=embed)
        await inter.author.send("Вы подали заявку на регистрацию города, администрация рассмотрит её в течении 24 часов.") # сообщение в лс после отправления анкеты
        await inter.response.edit_message() #чтобы не было ошибки "чтото не так. повторите попытку"

class Confirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)

        @disnake.ui.button(label="Регистрация города", style=disnake.ButtonStyle.blurple) #имя и цвет кнопки
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=MyModal()) #при нажатии на кнопку отправляет форму

@bot.command()
async def goroda(inter: disnake.AppCmdInter):
    view = Confirm()

    await inter.send(view=view) #показ кнопки

# Наследуем модальное окно
class TwoModal(disnake.ui.Modal): 
    def __init__(self):
        # Детали модального окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Ваш игровой никнейм",
                custom_id="Ваш игровой никнейм",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Ваш возвраст",
                custom_id="Ваш возвраст",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Чем планируете заниматься на сервере?",
                custom_id="Чем планируете заниматься на сервере?",
                style=TextInputStyle.paragraph,
                max_length=1024,
            ),
            disnake.ui.TextInput(
                label="Расскажите о себе, своих увлечениях",
                custom_id="Расскажите о себе, своих увлечениях",
                style=TextInputStyle.paragraph,
                max_length=1024,
            ),
        ]
        super().__init__(
            title="Заявка на сервер", #название формы
            custom_id="1",
            components=components,
        )

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=0x2F3136) #дизайн embed'a
        embed.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar) #от кого идёт заявка
        embed.set_footer(text=f"<@{inter.author.id}>", icon_url="https://cdn.discordapp.com/attachments/1011917849050218566/1051534757038657536/882601305871360040.png") 

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            ) #результаты
        
        await bot.get_channel(1011912836672401468).send(disnake.utils.get(inter.author.guild.roles, id = 1011771434185535518 ).mention, embed=embed)
        await inter.author.send("Вы заполнили заявку для игры на Loonely. Ожидайте проверки, администраторы ответят на неё в течении 24 часов.") # сообщение в лс после отправления анкеты
        await inter.response.edit_message() #чтобы не было ошибки "чтото не так. повторите попытку"
        role2 = disnake.utils.get(inter.author.guild.roles, id = 1012095311537262613)
        await inter.author.remove_roles(role2)
        role = disnake.utils.get(inter.author.guild.roles, id = 1051506901344604231) #получаем айди роли
        await inter.author.add_roles(role) #добавляем роль человеку который отправил форму, чтобы он повторно ее не проходил

class TwoConfirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)

        @disnake.ui.button(label="Заявка на сервер", style=disnake.ButtonStyle.blurple) #имя и цвет кнопки
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=TwoModal()) #при нажатии на кнопку отправляет форму

@bot.command()
async def tigr(inter: disnake.AppCmdInter):
    view = TwoConfirm()

    await inter.send(view=view) #показ кнопки

# Наследуем модальное окно
class ThreeModal(disnake.ui.Modal): 
    def __init__(self):
        # Детали модального окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Никнейм нарушителя",
                custom_id="Никнейм нарушителя",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Координаты места нарушения",
                custom_id="Координаты места нарушения",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Нарушенная статья конституции",
                custom_id="Нарушенная статья конституции",
                style=TextInputStyle.paragraph,
                max_length=1024,
            ),
            disnake.ui.TextInput(
                label="Описание ситуации",
                custom_id="Описание ситуации",
                style=TextInputStyle.paragraph,
                max_length=1024,
            ),
        ]
        super().__init__(
            title="Заявление в суд", #название формы
            custom_id="1",
            components=components,
        )

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=0x2F3136) #дизайн embed'a
        embed.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar) #от кого идёт заявка

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            ) #результаты
        
        await bot.get_channel(1011769083282341908).send(embed=embed)
        await inter.author.send("Вы направили заявление в суд, оно отобразиться в канале <#1011769083282341908>") # сообщение в лс после отправления анкеты
        await inter.response.edit_message() #чтобы не было ошибки "чтото не так. повторите попытку"

class ThreeConfirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)

        @disnake.ui.button(label="Заявление в суд", style=disnake.ButtonStyle.blurple) #имя и цвет кнопки
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=ThreeModal()) #при нажатии на кнопку отправляет форму

@bot.command()
async def sud(inter: disnake.AppCmdInter):
    view = ThreeConfirm()

    await inter.send(view=view) #показ кнопки

bot.run("")
