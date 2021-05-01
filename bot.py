import time
import discord
import nacl
import os
from discord.ext import commands
# Importing the newly installed library.
from discord_slash import cog_ext, SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv
load_dotenv()

PATH = 'C:/Users/samue/OneDrive/Desktop/DiscordTTS/big-buck-bunny_trailer.webm'

client = commands.Bot(command_prefix="!", help_command=None,
                      intents=discord.Intents.all())
# Declares slash commands through the client.
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

guild_ids = [815585085632937984]  # Put your server ID in this array.

vocodesVoices = {
    "altman": "sam-altman",
    "arnold": "arnold-schwarzenegger",
    "attenb": "david-attenborough",
    "ayoade": "richard-ayoade",
    "barker": "bob-barker",
    "bart": "bart-simpson",
    "bill": "bill-clinton",
    "boss": "the-boss",
    "brimley": "wilford-brimley",
    "broomstick": "boomstick",
    "bush": "george-w-bush",
    "carter": "jimmy-carter",
    "cartman": "eric-cartman",
    "cooper": "anderson-cooper",
    "cramer": "jim-cramer",
    "cranston": "bryan-cranston",
    "cross": "david-cross",
    "darth": "darth-vader",
    "deen": "paula-deen",
    "tyson": "neil-degrasse-tyson",
    "dench": "judi-dench",
    "devito": "danny-devito",
    "ferguson": "craig-ferguson",
    "gates": "bill-gates",
    "goku": "goku",
    "gottfried": "gilbert-gottfried",
    "graham": "paul-graham",
    "hillary": "hillary-clinton",
    "homer": "homer-simpson",
    "jones": "james-earl-jones",
    "keeper": "crypt-keeper",
    "king": "larry-king",
    "krabs": "mr-krabs",
    "lee": "christopher-lee",
    "lisa": "lisa-simpson",
    "luckey": "palmer-luckey",
    "mcconnell": "mitch-mcconnell",
    "nimoy": "leonard-nimoy",
    "nixon": "richard-nixon",
    "nye": "bill-nye",
    "obama": "barack-obama",
    "oliver": "john-oliver",
    "palin": "sarah-palin",
    "penguinz0": "moistcr1tikal",
    "griffin": "peter-griffin",
    "phil": "dr-phil-mcgraw",
    "reagan": "ronald-reagan",
    "rickman": "alan-rickman",
    "rogers": "fred-rogers",
    "rosen": "michael-rosen",
    "saruman": "saruman",
    "scout": "scout",
    "shapiro": "ben-shapiro",
    "shohreh": "shohreh-aghdashloo",
    "simmons": "j-k-simmons",
    "snake": "solid-snake",
    "snape": "severus-snape",
    "sonic": "sonic",
    "spongebob": "spongebob-squarepants",
    "squidward": "squidward",
    "stein": "ben-stein",
    "takei": "george-takei",
    "thiel": "peter-thiel",
    "trevor": "trevor-philips",
    "trump": "donald-trump",
    "tucker": "tucker-carlson",
    "tupac": "tupac-shakur",
    "vegeta": "vegeta",
    "white": "betty-white",
    "wiseau": "tommy-wiseau",
    "wizard": "wizard",
    "yugi": "yami-yugi",
    "zuckerberg": "mark-zuckerberg"
}

'''
Slash commands
'''
# Ping the bot and receive response time


@slash.slash(name='ping', description='Pong!🏓', guild_ids=guild_ids)
async def _ping(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f'Pong! ({client.latency*1000}ms)')

# Join the Voice channel


@slash.slash(name='join', description='Join the authors VC.', guild_ids=guild_ids)
async def join(ctx):
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(
            executable="C:/ffmpeg/ffmpeg.exe", source=PATH))

        await ctx.send(hidden=True, content='Command executed!')
    else:
        await ctx.send('The author is not in a voice channel!')


# Disconnect Bot from Voice channel
# @slash.slash(name='disconnect', description='Disconnect from the authors VC.', guild_ids=guild_ids)
# async def disconnect(ctx):

# Say text in a custom TTS voice
@slash.slash(name='tts_politics',
             description='TTS featuring Political Figures.',
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
                             name='tucker',
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
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_cartoons_anime',
             description='TTS featuring Cartoon and Anime characters.',
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
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_science_tech',
             description='TTS featuring Scientist and Technology Dudes.',
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
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_games_fantasy',
             description='TTS featuring Video Game and Fantasy characters.',
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
                             name='Boss',
                             value='the-boss'
                         ),
                         # 2
                         create_choice(
                             name='Darth',
                             value='darth-vader'
                         ),
                         # 3
                         create_choice(
                             name='Keeper',
                             value='crypt-keeper'
                         ),
                         # 4
                         create_choice(
                             name='Saruman',
                             value='saruman'
                         ),
                         # (5)
                         create_choice(
                             name='Scout',
                             value='scout'
                         ),
                         # 6 --------------------------
                         create_choice(
                             name='Snake',
                             value='solid-snake'
                         ),
                         # 7
                         create_choice(
                             name='Snape',
                             value='severus-snape'
                         ),
                         # 8
                         create_choice(
                             name='Sonic',
                             value='sonic'
                         ),
                         # 9
                         create_choice(
                             name='Trevor',
                             value='trevor-philips',
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
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_memers',
             description='TTS featuring epic Memers.',
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
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_celebrities',
             description='TTS featuring Celebrities.',
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
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_news_influence',
             description='TTS featuring News Presenters and Influencers.',
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
    print(f'{str(speaker).capitalize()}: {text}')
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model


@slash.slash(name='tts_music',
             description='TTS featuring Musicians.',
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
    speaker_capitalized = str(speaker).capitalize()
    print(f'\n{speaker_capitalized}: {text}')
    await ctx.send(f'{speaker_capitalized}: {text}', hidden=True)
    # Embed with picture of Speaker
    # await ctx.send(discord.Embed(), hidden=True)
    # send text to TTS model

'''
.env
'''
client.run(os.getenv('TOKEN'))


def getJson(ctx, speaker, text):

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
