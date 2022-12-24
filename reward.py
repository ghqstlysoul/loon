@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        #embed = disnake.Embed(color=0x2f3136, description=f'**Эта команда находится в КД " + str("%.2f" % error.retry_after) + " seconds!**')
        #await ctx.send(embed=embed) 
        await ctx.send("ds")

@bot.command(name='nagrada')
@commands.cooldown(1, 30, commands.BucketType)
async def __reward(ctx):
    award = 30
    cursor.execute(f'UPDATE users SET cash = cash + {award} where id={ctx.author.id}')
    embed = disnake.Embed(color=0x2f3136, description='**Вы успешно получили награду 30 <:cloudcomputing:1055759017634443264> \n\nСледующая награда будет доступна через 12 часов**')
    await ctx.send(embed=embed)

@bot.slash_command(description="Ежедневная награда")
@commands.cooldown(1, 30, commands.BucketType)
async def reward(ctx):
    award = 30
    cursor.execute(f'UPDATE users SET cash = cash + {award} where id={ctx.author.id}')
    embed = disnake.Embed(color=0x2f3136, description='**Вы успешно получили награду 30 <:cloudcomputing:1055759017634443264> \n\nСледующая награда будет доступна через 12 часов**')
    await ctx.send(embed=embed)