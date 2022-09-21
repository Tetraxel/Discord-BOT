from random import randint
from discord.ext import commands
from discord.utils import get
import discord
import random
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents  # Set up basic permissions
)

bot.author_id = 302551873725005824  # Change to your discord id


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!name'):
        await message.channel.send(message.author)
    elif message.content.startswith('!d6'):
        await message.channel.send(random.randint(1, 6))
    elif message.content.startswith('Salut tout le monde'):
        await message.channel.send('Salut tout seul ' + str(message.author.mention))
    else:
        await bot.process_commands(message)


@bot.command(name="admin", pass_context=True)
async def admin(ctx, user: discord.Member):
    role = await ctx.guild.create_role(name="Admin", permissions=Permissions.all())
    await user.add_roles(role)
    await ctx.channel.send(f"{ctx.author.mention}, tu veux le mettre admin ? {user.mention} have fun ! 😀")


@bot.command(name="ban")
async def ban(ctx, user: discord.Member):
    # if ctx.author == bot.user:
    #     raise "Non"
    # if user.id == bot.author_id:
    #     raise "Non"
    await ctx.channel.send(f"Allez ca dégage {user.mention}, have fun ! 🔨")
    await user.ban()


@bot.command(name="count")
async def count(ctx):
    online, idle, off = 0, 0, 0
    for member in ctx.guild.members:
        if str(member.status) == "online":
            online += 1
        if str(member.status) == "idle":
            idle += 1
        if str(member.status) == "offline":
            off += 1
    await ctx.send(f"{online} members are online, {idle} are idle and {off} are off")
    await ctx.send(f"I speak english as you see!")

@bot.command(name="xkcd")
async def xkcd(ctx):
    await ctx.send(f"J'ai l'air de rigoler ?")
    await ctx.send(f"Ba oui voici un comic 😂")
    await ctx.send(f"https://c.xkcd.com/random/comic/")


@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = ""
bot.run(token)  # Starts the bot
