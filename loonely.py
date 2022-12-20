from typing import Optional
import disnake
from disnake.ext import commands
from disnake import TextInputStyle

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

class MyModal(disnake.ui.Modal): 
    def __init__(self):
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
            title="Регистрация города",
            custom_id="1",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=0x2F3136) 
        embed.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar) 
        embed.set_footer(text=f"<@{inter.author.id}>", icon_url="https://cdn.discordapp.com/attachments/1011917849050218566/1051534757038657536/882601305871360040.png") 

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            ) 
        
        message = await bot.get_channel(1012089401792270439).send(disnake.utils.get(inter.author.guild.roles, id = 1011771434185535518 ).mention, embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❌')

        embed8 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394> Вы подали заявку на регистрацию города, администрация рассмотрит её в течении 24 часов.**')
        embed8.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
        embed8.set_footer(text=f"Благодарим вас за развитие системы городов <3", icon_url="https://media.discordapp.net/attachments/1051517961086713888/1053690918663884850/121212.png?width=671&height=671")
        
        await inter.author.send(embed=embed8)
        await inter.response.edit_message() 

        payload = await bot.wait_for('raw_reaction_add')
        if str(payload.emoji) == '✅':
            embed9 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394> Ваша заявка на регистрацию города была одобрена, в скором времени с вами свяжется наш администратор.**')
            embed9.set_footer(text=f"Регистрация города была одобрена {payload.member.name}#{payload.member.tag}", icon_url=payload.member.avatar)
            embed9.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
            await inter.author.send(embed=embed9)
            
            await message.delete()
        
        elif str(payload.emoji) == '❌':
            embed10 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394> Ваша заявка на регистрацию города была отклонена! \n\n<a:99_emb:1053692928515641394> Ознакомтесь с правилами в канале <#1011768730105155685>**')
            embed10.set_footer(text=f"Регистрация города была отклонена {payload.member.name}#{payload.member.tag}", icon_url=payload.member.avatar)
            embed10.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
            await inter.author.send(embed=embed10)
            
            await message.delete()

class Confirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)

        @disnake.ui.button(label="Регистрация города", style=disnake.ButtonStyle.blurple) 
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=MyModal())

@bot.command()
@commands.has_any_role(1011771434185535518)  
async def goroda(inter: disnake.AppCmdInter):
    embed13 = disnake.Embed(color=0x2F3136, description=f'**<:99_emb_tochka:1053706410803859527>  Правила регистрации города:** \n\n<a:99_emb:1053692928515641394>  Присутствие строения для путеводителя, пример: воздушный шар, дерижабль, корабль, поезд на станции метро города, катер, яхта. \n\n<a:99_emb:1053692928515641394>  В городе проживают более 6 человек, при этом имеют прописку в паспорте о городе в котором проживают. \n\n<a:99_emb:1053692928515641394>  Город не является приватным или закрытым для посещения, регистрации подлежат только открытые для посещения города, присутствие чёрного списка разрешено.')
    embed13.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
    await bot.get_channel(1011768730105155685).send(embed=embed13)  
    view = Confirm()

    await inter.send(view=view) 

class TwoModal(disnake.ui.Modal): 
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Ваш игровой никнейм",
                custom_id="Ваш игровой никнейм",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Ваш возраст",
                custom_id="Ваш возраст",
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
            title="Заявка на сервер", 
            custom_id="1",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar) 
        embed.set_footer(text=f"<@{inter.author.id}>", icon_url="https://cdn.discordapp.com/attachments/1011917849050218566/1051534757038657536/882601305871360040.png") 

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            ) 
        
        message = await bot.get_channel(1011912836672401468).send(disnake.utils.get(inter.author.guild.roles, id = 1011771434185535518 ).mention, embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❌')
        
        embed6 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394>   Вы заполнили заявку для игры на Loonely, ожидайте проверки, администраторы ответят на неё в течении 8 часов.**')
        embed6.set_footer(text=f"Спасибо что выбираете именно нас <3", icon_url="https://media.discordapp.net/attachments/1051517961086713888/1053690918663884850/121212.png?width=671&height=671")
        embed6.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
        await inter.author.send(embed=embed6)
        await inter.response.edit_message() 

        role2 = disnake.utils.get(inter.author.guild.roles, id = 1012095311537262613)
        await inter.author.remove_roles(role2)

        role = disnake.utils.get(inter.author.guild.roles, id = 1051506901344604231) 
        await inter.author.add_roles(role) 

        payload = await bot.wait_for('raw_reaction_add')
        if str(payload.emoji) == '✅':
            role2 = disnake.utils.get(inter.author.guild.roles, id = 1012095465031999498)
            await inter.author.add_roles(role2)

            role = disnake.utils.get(inter.author.guild.roles, id = 1051506901344604231)
            await inter.author.remove_roles(role)

            nick_for_whitelist = inter.text_values['Ваш игровой никнейм']
            embed5 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394>   Ваша заявка на сервер Loonely была рассмотрена и одобрена администрацией сервера. \n\n<a:99_emb:1053692928515641394>   На данный момент сервер запущен, но зайти на него вы не сможете, он находиться в ожидании выхода новой версии 1.20, вместе с её выпуском сервер начнёт свой запуск. \n\n<#1011768168198455446> — помощник по дискорду \n<#1011767237453041744> — помощник по игре \n\n<a:99_emb:1053692928515641394>   Айпи: loonely.ru \n<a:99_emb:1053692928515641394>   Ник: {nick_for_whitelist}**')
            embed5.set_footer(text=f"Ваша заявка была одобрена {payload.member.name}#{payload.member.tag}", icon_url=payload.member.avatar)
            embed5.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
            await inter.author.send(embed=embed5)
           
            # await bot.get_channel(1012073619846864957).send(f'twl add {nick_for_whitelist} permanent')
            await bot.get_channel(1053035725047738419).send(f'{nick_for_whitelist} — <@{inter.author.id}>')
            await bot.get_channel(1012082840604778576).send(f'К нам присоеденился новый игрок, встречайте — <@{inter.author.id}>')
            await message.delete()

            user = disnake.utils.get(message.guild.members, id=payload.user_id)
            embed2 = disnake.Embed(color=0x2F3136, description=f'Принял игрока <@{inter.author.id}> в белый список проекта.')
            embed2.set_author(name=f"{user}",icon_url=payload.member.avatar)
            await bot.get_channel(1053674899585110057).send(embed=embed2)

        elif str(payload.emoji) == '❌':
            role3 = disnake.utils.get(inter.author.guild.roles, id = 1039219828558409799)
            await inter.author.add_roles(role3)

            role = disnake.utils.get(inter.author.guild.roles, id = 1051506901344604231)
            await inter.author.remove_roles(role)

            user = disnake.utils.get(message.guild.members, id=payload.user_id)
            embed4 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394>   Ваша заявка на сервер Loonely была отклонена. \n\n<a:99_emb:1053692928515641394>   Подробная информация в канале <#1039253387889365002>**')
            embed4.set_footer(text=f"Ваша заявка была отклонена {payload.member.name}#{payload.member.tag}", icon_url=payload.member.avatar)
            embed4.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
            await inter.author.send(embed=embed4)
            
            nick_for_whitelist = inter.text_values['Ваш игровой никнейм']
            await message.delete()

            user = disnake.utils.get(message.guild.members, id=payload.user_id)
            embed3 = disnake.Embed(color=0x2F3136, description=f'Отклонил заявку <@{inter.author.id}> для игры на сервере.')
            embed3.set_author(name=f"{user}",icon_url=payload.member.avatar)
            await bot.get_channel(1053301779380572162).send(embed=embed3) 
            await bot.get_channel(1053301779380572162).send(embed=embed)

class TwoConfirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)
        
        @disnake.ui.button(label="Заявка на сервер", style=disnake.ButtonStyle.blurple)
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=TwoModal()) 

@bot.command()
@commands.has_any_role(1011771434185535518)  
async def tigr(inter: disnake.AppCmdInter):
    embed12 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394> Подавайте заявку для игры, кликнув на кнопку ниже.**')
    embed12.set_image(url="https://i.pinimg.com/originals/cd/0a/c5/cd0ac53c65a93a2ccfabb720e1dcb0fe.gif")
    await bot.get_channel(1039227111862444063).send(embed=embed12)  
    view = TwoConfirm()

    await inter.send(view=view)

class ThreeModal(disnake.ui.Modal): 
    def __init__(self):
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
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Описание ситуации",
                custom_id="Описание ситуации",
                style=TextInputStyle.paragraph,
                max_length=1024,
            ),
        ]
        super().__init__(
            title="Заявление в суд", 
            custom_id="1",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=0x2F3136) 
        embed.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar) 

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            ) 
        
        await bot.get_channel(1011769083282341908).send(embed=embed)

        embed11 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394>   Вы направили заявление в суд, оно отобразиться в канале <#1011769083282341908> и с ним обязательно ознакомиться судья нашего сервера.**')
        embed11.set_footer(text=f"Спасибо что помогаете делать сервер лучше <3", icon_url="https://media.discordapp.net/attachments/1051517961086713888/1053690918663884850/121212.png?width=671&height=671")
        embed11.set_image(url="https://media.discordapp.net/attachments/774042908718399509/830486108978544680/1111.png")
        await inter.author.send(embed=embed11)
        await inter.response.edit_message() 

class ThreeConfirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)

        @disnake.ui.button(label="Заявление в суд", style=disnake.ButtonStyle.blurple) 
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=ThreeModal())

@bot.command()
@commands.has_any_role(1011771434185535518)  
async def sud(inter: disnake.AppCmdInter):
    view = ThreeConfirm()

    await inter.send(view=view)

class FourModal(disnake.ui.Modal): 
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Никнейм выдачи",
                custom_id="Никнейм выдачи",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Количество валюты",
                custom_id="Количество валюты",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(
            title="Выдача валюты", 
            custom_id="1",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):        
        money = inter.text_values['Количество валюты']
        nick = inter.text_values['Никнейм выдачи']
        await bot.get_channel(1012073619846864957).send(f'cmi money give {nick} {money}')
        embed15 = disnake.Embed(color=0x2F3136, description=f'**<a:99_emb:1053692928515641394> Выдал {money} <:1_diamond_ore:1050438673935634543>  игроку "{nick}" на электронный баланс.**')
        embed15.set_author(name=f"{inter.author.name}#{inter.author.tag}",icon_url=inter.author.avatar)
        await bot.get_channel(1011917849050218566).send(embed=embed15)
        await inter.response.edit_message() 

class FourConfirm(disnake.ui.View):

        def __init__(self):
            super().__init__(timeout=0)

        @disnake.ui.button(label="Выдача валюты", style=disnake.ButtonStyle.blurple) 
        async def confirm(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
            await inter.response.send_modal(modal=FourModal())

@bot.command()
@commands.has_any_role(1011771434185535518)  
async def give(inter: disnake.AppCmdInter):
    view = FourConfirm()

    await inter.send(view=view)    

#bot.run("MTAzOTUwMzg3NDEzMTc3NTU0OA.G1PW7g.IA7h0oKQvVz-08MduGnnsT74f9bDZ2mckt1ovQ") #Loonely
bot.run("MTA0NzQ4MzIzMjE5MjU3NzYxNw.GYmNWO.AjuxA6XtVm_t1PtOgGRb6OXozFGsHHw0R04kqY") #LoonelyAuth