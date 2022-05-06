import time
import discord
import requests
import os
import random
from discord.ext import commands

# Importing the newly installed library.
from discord_slash import cog_ext, SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash import SlashCommand, SlashContext, ComponentContext
from discord_slash.utils.manage_components import create_actionrow, create_button, ButtonStyle, wait_for_component
from discord_slash.model import ButtonStyle
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix="!", help_command=None,
                   intents=discord.Intents.all())
# Declares slash commands through the bot.
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

icons = os.listdir("icons")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("0 Messages"))
    print('We have logged in as {0.user}'.format(bot))

# Put your server ID in this array.


async def sendEmbed(ctx, speaker, text):
    #speaker_file = f'{str(speaker)}.png'
    #file = discord.File(f'icons/{speaker_file}')
    #color = random.randint(0, 0xffffff)
    #print(color)
    embed = discord.Embed(title=str(speaker),
                          description=text)
    #0xFF5733
    embed.set_thumbnail(url='https://bit.ly/2SBWMs3')
    #embed.colour = color
    await ctx.send(embed=embed)
    # embed.set_image(url="attachment://katta.jpg")

    # embed.set_author(name=ctx.author.display_name,
    #                  icon_url=ctx.author.avatar_url)
    # embed.set_thumbnail(url=f'attachment://{speaker_file}')
    # await ctx.send(embed=embed, file=file)


async def speak(ctx, speaker, text):
    await ctx.defer()
    print(f'{speaker}: {text}')

    response = requests.post('https://mumble.stream/speak',
                             json={'speaker': speaker,
                                   'text': text},
                             headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
    filename = f'{speaker}.wav'
    with open(filename, mode='bx') as f:
        f.write(response.content)

    vc = bot.voice_clients[0]

    # play wav file through FFmpeg
    vc.play(discord.FFmpegPCMAudio(
        executable="C:/ffmpeg/ffmpeg.exe", source=filename))
    try:
        await sendEmbed(ctx, speaker, text)
    except:
        await ctx.send(f'{str(speaker).capitalize()}: {text}', hidden=True)

    # wait until bot is no longer playing file
    while vc.is_playing():
        time.sleep(.1)

    # delete file from directory
    os.remove(filename)


# https://discordpy.readthedocs.io/en/rewrite/api.html#discord.ActivityType
# @bot.event
# async def on_message(message):
# print(message.content)

'''
.env
'''
bot.load_extension("cog")
bot.run(os.getenv('TOKEN'))

