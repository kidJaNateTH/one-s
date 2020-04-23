import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix = '1!')

@client.event
async def on_ready():
    print("bot ready")
    #await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("1!help"))
    await client.change_presence(activity=discord.Streaming(name="1!help", url="https://www.twitch.tv/kidjanateth"))


@client.command()
async def ping(ctx):
    await ctx.send('Pong! XD')

@client.command()
async def say(ctx, *,msg):
    await ctx.message.delete()
    await ctx.send("{}" .format(msg))

@client.command()
async def plus(ctx , a: int ,b: int):
    await ctx.send(a , " + " , b , " = " , a+b)

@client.command(pass_context=True)
async def verify(ctx,age: int):
    
    if age <= 12 and age >= 1:
        await ctx.send("nope kid")
    if age >= 13 and age <= 100:
        await ctx.send("yes you passed")
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Player")
        await ctx.message.author.add_roles(role)
    if age >= 100:
        await ctx.send("are you human?")
    if age <= 0:
        await ctx.send("Are you Sperm?")

@verify.error
async def verify_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```1!verify age```')

client.run('NjkzNjcxOTkzODY1OTI4NzI2.XqBR5w.plP1meKY7DWw0heDEZ5zMvfRCgk')
