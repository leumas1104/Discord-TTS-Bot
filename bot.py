import time
import discord
import requests
import nacl
import os
from discord.ext import commands
# Importing the newly installed library.
from discord_slash import cog_ext, SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv

load_dotenv()

PATH = 'C:/Users/samue/OneDrive/Desktop/DiscordTTS/big-buck-bunny_trailer.webm'
#speaker_capitalized = None

client = commands.Bot(command_prefix="!", help_command=None,
                      intents=discord.Intents.all())
# Declares slash commands through the client.
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("0 Messages"))
    print('We have logged in as {0.user}'.format(client))

# Put your server ID in this array.
guild_ids = [815585085632937984, 387214698757750784]


'''
Slash commands
'''
# Ping the bot and receive response time


@slash.slash(name='ping', description='🗣 Pong!🏓', guild_ids=guild_ids)
async def _ping(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f'Pong! ({round(client.latency*1000)}ms)')

# Join the Voice channel


@slash.slash(name='join', description='🗣 Join the authors VC.', guild_ids=guild_ids)
async def join(ctx):
    try:
        voice_channel = ctx.author.voice.channel
    except AttributeError:
        await ctx.send(hidden=True, content='**ERROR**: You are not in a voice channel!\nJoin a channel and try again.')
        return

    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice_client == None:
        vc = await voice_channel.connect()
        await ctx.send(hidden=True, content='Connected!')
        print('Connected!')
    else:
        await ctx.send(hidden=True, content='**ERROR**: Already connected to voice client!')
# vc.play(discord.FFmpegPCMAudio(
    #   executable="C:/ffmpeg/ffmpeg.exe", source=PATH))
# Disconnect Bot from Voice channel


@slash.slash(name='leave', description='🗣 Disconnect from the authors VC.', guild_ids=guild_ids)
async def leave(ctx):
    try:
        await client.voice_clients[0].disconnect()
        await ctx.send(hidden=True, content='Disconnected!')
        print('Disconnected!')
    except:
        await ctx.send(hidden=True, content='**ERROR**: Already disconnected!')

    # Say text in a custom TTS voice


@slash.slash(name='tts_politics',
             description='🗣 TTS featuring Political Figures.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Arnold',
                             value='arnold-schwarzenegger'
                         ),
                         # 2
                         create_choice(
                             name='Bill',
                             value='bill-clinton'
                         ),
                         # 3
                         create_choice(
                             name='Bush',
                             value='george-w-bush'
                         ),
                         # 4
                         create_choice(
                             name='Carter',
                             value='jimmy-carter'
                         ),
                         # (5)
                         create_choice(
                             name='Hillary',
                             value='hillary-clinton'
                         ),
                         # 6 -----------------------------------
                         create_choice(
                             name='Mcconnell',
                             value='mitch-mcconnell'
                         ),
                         # 7
                         create_choice(
                             name='Nixon',
                             value='richard-nixon'
                         ),
                         # 8
                         create_choice(
                             name='Obama',
                             value='barack-obama'
                         ),
                         # 9
                         create_choice(
                             name='Palin',
                             value='sarah-palin'
                         ),
                         # (10)
                         create_choice(
                             name='Reagan',
                             value='ronald-reagan'
                         ),
                         # 11 --------------------------------
                         create_choice(
                             name='Shapiro',
                             value='ben-shapiro'
                         ),
                         # 12
                         create_choice(
                             name='Trump',
                             value='donald-trump'
                         ),
                         # 13
                         create_choice(
                             name='Tucker',
                             value='tucker-carlson'
                         ),
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)
    # send text to TTS model


@slash.slash(name='tts_cartoons_anime',
             description='🗣 TTS featuring Cartoon and Anime characters.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Bart',
                             value='bart-simpson'
                         ),
                         # 2
                         create_choice(
                             name='Cartman',
                             value='eric-cartman'
                         ),
                         # 3
                         create_choice(
                             name='Goku',
                             value='goku'
                         ),
                         # 4
                         create_choice(
                             name='Griffin',
                             value='peter-griffin'
                         ),
                         # (5)
                         create_choice(
                             name='Homer',
                             value='homer-simpson'
                         ),
                         # 6 ---------------------------
                         create_choice(
                             name='Krabs',
                             value='mr-krabs'
                         ),
                         # 7
                         create_choice(
                             name='Lisa',
                             value='lisa-simpson'
                         ),
                         # 8
                         create_choice(
                             name='Spongebob',
                             value='spongebob-squarepants'
                         ),
                         # 9
                         create_choice(
                             name='Squidward',
                             value='squidward'
                         ),
                         # (10)
                         create_choice(
                             name='Vegeta',
                             value='vegeta'
                         ),
                         # 11 ---------------------------
                         create_choice(
                             name='Yugi',
                             value='yami-yugi'
                         )
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)
    # send text to TTS model


@slash.slash(name='tts_science_tech',
             description='🗣 TTS featuring Scientist and Technology Dudes.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Altman',
                             value='sam-altman'
                         ),
                         # 2
                         create_choice(
                             name='Attenborough',
                             value='david-attenborough'
                         ),
                         # 3
                         create_choice(
                             name='Degrasse',
                             value='neil-degrasse-tyson'
                         ),
                         # 4
                         create_choice(
                             name='Gates',
                             value='bill-gates'
                         ),
                         # (5)
                         create_choice(
                             name='Graham',
                             value='paul-graham'
                         ),
                         # 6 --------------------------------
                         create_choice(
                             name='Luckey',
                             value='palmer-luckey'
                         ),
                         # 7
                         create_choice(
                             name='Nye',
                             value='bill-nye'
                         ),
                         # 8
                         create_choice(
                             name='Thiel',
                             value='peter-thiel'
                         ),
                         # 9
                         create_choice(
                             name='Zuckerberg',
                             value='mark-zuckerberg'
                         )
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)
    # send text to TTS model


@slash.slash(name='tts_games_fantasy',
             description='🗣 TTS featuring Video Game and Fantasy characters.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Anakin',
                             value='anakin-skywalker'
                         ),
                         # 2
                         create_choice(
                             name='Boss',
                             value='the-boss'
                         ),
                         # 3
                         create_choice(
                             name='Darth',
                             value='darth-vader'
                         ),
                         # 4
                         create_choice(
                             name='Keeper',
                             value='crypt-keeper'
                         ),
                         # (5)
                         create_choice(
                             name='Obi-Wan',
                             value='obi-wan-kenobi'
                         ),
                         # 6 --------------------------
                         create_choice(
                             name='Saruman',
                             value='saruman'
                         ),
                         # 7
                         create_choice(
                             name='Scout',
                             value='scout'
                         ),
                         # 8
                         create_choice(
                             name='Snake',
                             value='solid-snake'
                         ),
                         # 9
                         create_choice(
                             name='Snape',
                             value='severus-snape'
                         ),
                         # 10
                         create_choice(
                             name='Sonic',
                             value='sonic'
                         ),
                         # 11
                         create_choice(
                             name='Trevor',
                             value='trevor-philips',
                         ),
                         # 12
                         create_choice(
                             name='Yoda',
                             value='yoda',
                         )
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)
    # send text to TTS model


@slash.slash(name='tts_memers',
             description='🗣 TTS featuring epic Memers.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Cramer',
                             value='jim-cramer'
                         ),
                         # 2
                         create_choice(
                             name='Phil',
                             value='dr-phil-mcgraw'
                         ),
                         # 3
                         create_choice(
                             name='Rosen',
                             value='michael-rosen'
                         ),
                         # 4
                         create_choice(
                             name='Wiseau',
                             value='tommy-wiseau'
                         )
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)
    # send text to TTS model


@slash.slash(name='tts_celebrities',
             description='🗣 TTS featuring Celebrities.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Ayoade',
                             value='richard-ayoade'
                         ),
                         # 2
                         create_choice(
                             name='Barker',
                             value='bob-barker'
                         ),
                         # 3
                         create_choice(
                             name='Brimley',
                             value='wilford-brimley'
                         ),
                         # 4
                         create_choice(
                             name='Cranston',
                             value='bryan-cranston'
                         ),
                         # (5)
                         create_choice(
                             name='Cross',
                             value='david-cross'
                         ),
                         # 6 ------------------------------------
                         create_choice(
                             name='Deen',
                             value='paula-deen'
                         ),
                         # 7
                         create_choice(
                             name='Dench',
                             value='judi-dench'
                         ),
                         # 8
                         create_choice(
                             name='Devito',
                             value='danny-devito'
                         ),
                         # 9
                         create_choice(
                             name='Ferguson',
                             value='craig-ferguson'
                         ),
                         # (10)
                         create_choice(
                             name='Gottfried',
                             value='gilbert-gottfried'
                         ),
                         # 11 -----------------------------------
                         create_choice(
                             name='Jones',
                             value='james-earl-jones'
                         ),
                         # 12
                         create_choice(
                             name='Lee',
                             value='christopher-lee'
                         ),
                         # 13
                         create_choice(
                             name='Nimoy',
                             value='leonard-nimoy'
                         ),
                         # 14
                         create_choice(
                             name='Rickman',
                             value='alan-rickman'
                         ),
                         # (15)
                         create_choice(
                             name='Rogers',
                             value='fred-rogers'
                         ),
                         # 16 ---------------------------------
                         create_choice(
                             name='Shohreh',
                             value='shohreh-aghdashloo'
                         ),
                         # 17
                         create_choice(
                             name='Simmons',
                             value='j-k-simmons'
                         ),
                         # 18
                         create_choice(
                             name='Takei',
                             value='george-takei'
                         ),
                         # 19
                         create_choice(
                             name='White',
                             value='betty-white'
                         ),
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)
    # send text to TTS model


@slash.slash(name='tts_news_influence',
             description='🗣 TTS featuring News Presenters and Influencers.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Spea,ker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Boomstick',
                             value='boomstick'
                         ),
                         # 2
                         create_choice(
                             name='Cooper',
                             value='anderson-cooper'
                         ),
                         # 3
                         create_choice(
                             name='King',
                             value='larry-king'
                         ),
                         # 4
                         create_choice(
                             name='Oliver',
                             value='john-oliver'
                         ),
                         # (5)
                         create_choice(
                             name='Penguinz0',
                             value='moistcr1tikal'
                         ),
                         # 6 --------------------------
                         create_choice(
                             name='Stein',
                             value='ben-stein'
                         ),
                         # 7
                         create_choice(
                             name='Wizard',
                             value='wizard'
                         )
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)

    # send text to TTS model


@slash.slash(name='tts_music',
             description='🗣 TTS featuring Musicians.',
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name='speaker',
                     description='Speaker of text.🔊',
                     option_type=3,
                     required=True,
                     choices=[
                         # 1
                         create_choice(
                             name='Tupac',
                             value='tupac-shakur'
                         )
                     ]
                 ),

                 create_option(
                     name='text',
                     description='Enter text here.',
                     option_type=3,
                     required=True
                 )
             ])
async def tts(ctx, speaker, text: str):
    createEmbed(speaker, text, embed)
    # await ctx.send(discord.Embed(), hidden=True)
    await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)
    speak(speaker, text)


def createEmbed(speaker, text, embed):
    # Embed with picture of Speaker
    # file = discord.File("path/to/my/image.png", filename="image.png")
    embed = discord.Embed()
    # embed.set_image(url="attachment://image.png")
    # await channel.send(file=file, embed=embed)

    # await ctx.send(discord.Embed(), hidden=True)
    pass


def speak(speaker, text):
    print(f'{speaker}: {text}')

    response = requests.post('https://mumble.stream/speak',
                             json={'speaker': speaker,
                                   'text': text},
                             headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
    filename = f'{speaker}.wav'
    with open(filename, mode='bx') as f:
        f.write(response.content)

    vc = client.voice_clients[0]

    # play wav file through FFmpeg
    vc.play(discord.FFmpegPCMAudio(
        executable="C:/ffmpeg/ffmpeg.exe", source=filename))
    # wait until bot is no longer playing file◘
    while vc.is_playing():
        time.sleep(.1)

    # delete file from directory
    os.remove(filename)


# https://discordpy.readthedocs.io/en/rewrite/api.html#discord.ActivityType
# @client.event
# async def on_message(message):
# print(message.content)

'''
.env
'''
client.run(os.getenv('TOKEN'))

# import os
# import requests
# import discord

# TOKEN = 'ODM1ODcxMjU4NDY0ODc4NjI0.YIVvxQ.YGTe114hz4BMkp-4Wq1jNtPNBf4'
# GUILD_ID = '815585085632937984'

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# # @client.event
# # async def on_message(message):
# #     if message.author == client.user:
# #         return

# #     if message.content.startswith('$hello'):
# #         await message.channel.send('Hello!')
# url = "https://discord.com/api/v8/applications/835871258464878624/guilds/815585085632937984/commands"

# joinVoice = {
#     "name": "join",
#     "description": "Join the VC of command author.",
# }

# tts = {
#     "name": "tts",
#     "description": "Say anything in different TTS voices.",
#     "options": [
#         {
#             "name": "person",
#             "description": "The TTS speaker.",
#             "type": 3,
#             "required": True,
#             "choices": [
#                 {
#                     "name": "Samuel",
#                     "value": "person_samuel"
#                 },
#                 {
#                     "name": "Trump",
#                     "value": "person_trump"
#                 },
#                 {
#                     "name": "Daniel",
#                     "value": "person_daniel"
#                 }
#             ]
#         },
#         {
#             "name": "text",
#             "description": "User specified message",
#             "type": 3,
#             "required": True
#         }
#     ]
# }

# # For authorization, you can use either your bot token
# headers = {
#     "Authorization": "Bot ODM1ODcxMjU4NDY0ODc4NjI0.YIVvxQ.YGTe114hz4BMkp-4Wq1jNtPNBf4"
# }

# z = requests.post(url, headers=headers, json=joinVoice)
# r = requests.post(url, headers=headers, json=tts)
# i = requests.get(url, headers=headers)

# print(i.content)

# client.run(TOKEN)
