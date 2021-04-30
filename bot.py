import time
import discord
import nacl
import os
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand # Importing the newly installed library.
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv
load_dotenv()
PATH = 'C:/Users/samue/OneDrive/Desktop/DiscordTTS/big-buck-bunny_trailer.webm'

client = commands.Bot(command_prefix="!", help_command=None, intents = discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

guild_ids = [815585085632937984] # Put your server ID in this array.

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
#Ping the bot and receive response time
@slash.slash(name='ping', description='Pong!🏓', guild_ids=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f'Pong! ({client.latency*1000}ms)')

#Join the Voice channel
@slash.slash(name='join', description='Join the authors VC.', guild_ids=guild_ids)
async def join(ctx):
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg.exe", source=PATH))
        
        await ctx.send(hidden=True, content='Command executed!')
    else:
        await ctx.send('The author is not in a voice channel!')
    

#Disconnect Bot from Voice channel
# @slash.slash(name='disconnect', description='Disconnect from the authors VC.', guild_ids=guild_ids)
# async def disconnect(ctx):

#Say text in a custom TTS voice
@slash.slash(name='tts', 
            description='Outputs a TTS message in the voice of the chosen speaker.',
            guild_ids=guild_ids,
            options=[
				create_option(name='category', 
							description='Popular political figures.', 
							option_type=3, 
							required=True,
							choices=[
								create_choice(
                            		name='Politics',
                            		value='politics'
                         		),
								create_choice(
                            		name='Cartoons and Anime',
                            		value='cartoons-and-anime'
                         		),
							]),
                create_option(
                    name='speaker',
                    description='Speaker of text.',
                    option_type=3,
                    required=True,
                    choices=[
						#1
                        create_choice(
                            name='Altman',
                            value='sam-altman'
                        ),
						#2
                  		
						 #3
						create_choice(
                            name='Attenborough',
                            value='david-attenborough'
                         ),
						 #4
						create_choice(
                            name='Ayoade',
                            value='richard-ayoade'
                        ),
						#(5)
						create_choice(
                            name='Barker',
                            value='bob-barker'
                        ),
						#6------------------------------------
						create_choice(
                            name='Bart',
                            value='bart-simpson'
                        ),
						#7
						create_choice(
                            name='Bill',
                            value='bill-clinton'
                        ),
						#8
						create_choice(
                            name='Boss',
                            value='the-boss'
                        ),
						#9
						create_choice(
                            name='Brimley',
                            value='wilford-brimley'
                        ),
						#(10)
						create_choice(
                            name='Broomstick',
                            value='boomstick'
                        ),
						#11------------------------------------
                        create_choice(
                            name='Bush',
                            value='george-w-bush'
                        ),
						#12
                  		create_choice(
                            name='Carter',
                            value='jimmy-carter'
                         ),
						 #13
						create_choice(
                            name='Cooper',
                            value='anderson-cooper'
                         ),
						 #14
						create_choice(
                            name='Cramer',
                            value='jim-cramer'
                        ),
						#(15)
						create_choice(
                            name='Cranston',
                            value='bryan-cranston'
                        ),
						#16------------------------------------
						create_choice(
                            name='cross',
                            value='david-cross'
                        ),
						#17
						create_choice(
                            name='darth',
                            value='darth-vader'
                        ),
						#18
						create_choice(
                            name='Boss',
                            value='the-boss'
                        ),
						#19
						create_choice(
                            name='Brimley',
                            value='wilford-brimley'
                        ),
						#(20)
						create_choice(
                            name='Broomstick',
                            value='boomstick'
                        ),
						#21------------------------------------

                    ]   
                ),
               
                create_option(
                    name='text',
                    description='Enter text here.',
                    option_type=3,
                    required=True
                )
])
async def tts(ctx, speaker,text: str):
    await ctx.send(f'Wow, you actually chose {speaker}? :( \n You wrote: {text}')
    # send text to TTS model
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