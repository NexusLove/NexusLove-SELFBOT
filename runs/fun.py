import discord, time
from discord.ext import commands as NexusLove

class fun(NexusLove.Cog):
    def __init__(self, NexusLove):
        self.NexusLove = NexusLove


    @NexusLove.command()
    async def danc(self, ctx):
        await ctx.message.delete()
        danc = 'https://images-ext-2.discordapp.net/external/poPP7Gv08VAxIs_v2xQHxcOme1vobWjPZUKg2AaXI4A/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/840794659206987797.gif'
        await ctx.send(danc)

    @NexusLove.command()
    async def hah(self, ctx):
        await ctx.message.delete()
        hah = 'https://images-ext-1.discordapp.net/external/9bXisJjSpCgJ0h7JqkuZQvwhPAoR1T4GvppqRRvF7Vs/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/767782981073895455.png'
        await ctx.send(hah)

    @NexusLove.command()
    async def lonely(self, ctx):
        await ctx.message.delete()
        lonely = 'https://images-ext-1.discordapp.net/external/VhJSrbqpdITpmAJj9uTM2ZhkEYv2r7d1Kx6m6uQRyCY/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/859049848413618186.gif'
        await ctx.send(lonely)

    @NexusLove.command()
    async def ahh(self, ctx):
        await ctx.message.delete()
        ahh = 'https://images-ext-2.discordapp.net/external/Z_w6bKFL5Wxop1bfhTED-ozmy-t3TRwN1CMvg32KkuA/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/755088073884434494.gif'
        await ctx.send(ahh)

    @NexusLove.command()
    async def bbye(self, ctx):
        await ctx.message.delete()
        bbye = 'https://images-ext-1.discordapp.net/external/FbRZdVStEO91EdORLk2M8ZE4o_qhiWVDloqZUH3noK4/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/712388967902740490.gif'
        await ctx.send(bbye)

    @NexusLove.command()
    async def twerk(self, ctx):
        await ctx.message.delete()
        twerk = 'https://images-ext-2.discordapp.net/external/t-YyTGVICEGuAptTeteVLVIPorNmDLizca1GWPKfT1w/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/854605974974627881.gif'
        await ctx.send(twerk)

    @NexusLove.command()
    async def nani(self, ctx):
        await ctx.message.delete()
        nani = 'https://images-ext-1.discordapp.net/external/eUUVCGPbTUmRu_WD7SsTuNUnzDvPZ75sS-7cx5xi5Qg/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/682737787685961832.png'
        nani1 = 'https://images-ext-1.discordapp.net/external/5OVbqNSz2eHVzRecO5cT0T2sb5nrG9OLIR8FLp6qxr8/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/683356400726179876.png'
        nani2 = 'https://images-ext-2.discordapp.net/external/ffQBCA7pQ-NxOKzzMWuLadm8vTtU6blh8LpPz-tHK0M/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/683356144571383810.png'
        await ctx.send(nani)
        time.sleep(0.5)
        await ctx.send(nani1)
        time.sleep(0.5)
        await ctx.send(nani2)

    @NexusLove.command()
    async def love(self, ctx):
        try:
            await ctx.message.edit(content="I")
            await ctx.message.edit(content="I ")
            await ctx.message.edit(content="I L")
            await ctx.message.edit(content="I Lo")
            await ctx.message.edit(content="I Lov")
            await ctx.message.edit(content="I Love")
            await ctx.message.edit(content="I Love ")
            await ctx.message.edit(content="I Love Y")
            await ctx.message.edit(content="I Love Yo")
            await ctx.message.edit(content="I Love You")                                        
            await
ctx.message.edit(content="<3")
        except Exception as e:
            print(f"{e}")

    @NexusLove.command()
    async def sessoo(self, ctx):
        try:
            for i in range(100):
                await ctx.message.edit(content="S")
                time.sleep(1)
                await ctx.message.edit(content="SE")
                time.sleep(1)
                await ctx.message.edit(content="SES")
                time.sleep(1)
                await ctx.message.edit(content="SESS")
                time.sleep(1)
                await ctx.message.edit(content="SESSO")
        except Exception as e:
            print(f"{e}")
    
    @NexusLove.command()
    async def jews(self,ctx):
        await ctx.message.edit(content="🇱 🇴 🇱 🇯 🇪 🇼 🇸")
            
    @NexusLove.command()
    async def cp(self,ctx):
        await ctx.message.edit(content="🇨 🇵❓ ❓ ❔")

def setup(NexusLove):
    NexusLove.add_cog(fun(NexusLove))