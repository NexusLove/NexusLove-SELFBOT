import discord
from discord.ext import commands as NexusLove

class activities(NexusLove.Cog):
    def __init__(self, NexusLove):
        self.NexusLove = NexusLove


    @NexusLove.command()
    async def stream(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Streaming: {content}`')
            await self.NexusLove.change_presence(activity=discord.Streaming(name=content, url="https://www.twitch.tv/NexusLove"))
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @NexusLove.command()
    async def play(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Playing: {content}`')
            await self.NexusLove.change_presence(activity=discord.Game(content))
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @NexusLove.command()
    async def watch(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Watching: {content}`')
            await self.NexusLove.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= content))
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @NexusLove.command()
    async def listen(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Listening: {content}`')
            await self.NexusLove.change_presence(type=discord.Activity.Type.listening, name = content)
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

def setup(NexusLove):
    NexusLove.add_cog(activities(NexusLove))