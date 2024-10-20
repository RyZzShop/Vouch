import discord
from discord.ext import commands

TOKEN = 'Ur Token Bot'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command(name='vouch')
async def vouch(ctx, user: discord.Member):
    await ctx.send(f'{ctx.author.mention} a recommandé {user.mention}!')

bot.run(TOKEN)
