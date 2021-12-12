# import asyncio
# import requests
# import json
import os
# import re
# import random
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import keep_alive

# # grabbing the config file
# with open('config.json') as config_file:
#     secrets = json.load(config_file)

# grabbing keys
token = os.getenv("bot_token")

# intents so bot can see members from DMs
intents = discord.Intents(messages=True,
                          reactions=True,
                          members=True,
                          guilds=True,
                          presences=True)

# bot info
bot = commands.Bot(command_prefix='!',
                   description='Bot to help to stuff and test things.',
                   case_insensitive=True,
                   intents=intents)
slash = SlashCommand(bot, sync_commands=True)

# gathering the commands
cogs = [
    'cogs.chat', 'cogs.games'
    # , 'cogs.reactions'
]

# id's for testing server
# target_server_id = 704139386501201942
# target_channel_id = 725386567740555416
# target_role_id = 760186396555739197


# limiting the eval command to just the bot owner
@bot.command(name='eval', hidden=True)
@commands.is_owner()
async def _eval(ctx, *, code):
    await ctx.send(eval(code))


@_eval.error
async def eval_error(error, ctx):
    if isinstance(error, commands.MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(
            ctx.message.author)
        await ctx.send(ctx.message.channel, text)


@bot.event
async def on_member_join(member):
    rules = bot.get_channel(794619790861664267)
    await member.send("Welcome, Comrade {}!".format(member.name))
    await member.send(
        "Please check out the {} before heading to the dank meme stash.".
        format(rules.mention))


@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    nn = str('Comrade ' + member.display_name)

    if payload.channel_id == 794619790861664267 and payload.message_id == 794619965788913675:
        # rules reaction role
        if str(payload.emoji) == '🆗':
            role = discord.utils.get(payload.member.guild.roles,
                                     name="Comrade")
            await payload.member.add_roles(role)
            await payload.member.edit(nick=nn)
        # power club reaction role
        elif str(payload.emoji) == '🏋️':
            role = discord.utils.get(payload.member.guild.roles,
                                     name="Power Club")
            await payload.member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    # name = str(member.name)
    nn = str(member.display_name).removeprefix('Comrade ')
    if payload.channel_id == 794619790861664267 and payload.message_id == 794619965788913675:
        # rules reaction role
        if str(payload.emoji) == '🆗':
            role = discord.utils.get(guild.roles, name="Comrade")
            await member.remove_roles(role)
            await member.edit(nick=nn)
        # power club reaction role
        elif str(payload.emoji) == '🏋️':
            role = discord.utils.get(guild.roles, name="Power Club")
            await member.remove_roles(role)


# slash command that DMs the sender
@slash.slash(
    name='direct_message',
    description='Initiates a DM with the user.',
    guild_ids=[704139386501201942]
)
async def _dm(ctx):
    await ctx.author.send("Hey, what do you need?")
    await ctx.send("Sliding into those DMs 😏.")

# @bot.event
# @commands.has_any_role('Rear Admiral', 'Comrade')
# async def on_message(message):
#     mention = f'<@!{bot.user.id}>'
#     replies = [
#         "Yes?"
#         , "My lord?"
#         , "What is it?"
#         , "Yes my lord!"
#         , "Oh, what?"
#         , "Y-huh?"
#         , "Now what?"
#         , "More work?"
#         , "Leave me alone!"
#         , "I don't want to do this!"
#         , "Your command?"
#         , "Your orders?"
#         , "Yes, sire?"
#         , "At your service."
#         , "Your Eminence?"
#         , "Exalted one?"
#         , "My sovereign?"
#         , "Your wish?"
#         , "Ready to serve, my lord."
#         , "Your majesty?"
#         , "At your service."
#         , "Sire?"
#         , "What ho!"
#         , "Give me a quest!"
#         , "What do you want?"
#         , "Ach?"
#         , "Aye laddy."
#         , "Who summoned me?"
#         , "Do you need assistance?"
#         , "Your request?"
#     ]
#     if mention in message.content:
#         # await message.channel.send("Who summoned me?")
#         await message.channel.send(random.choice(replies))
#         await message.add_reaction("🥒")


# bot start up event
@bot.event
async def on_ready():
    print("The bot is ready!")
    print(f'Logged in as: {bot.user.name} - {bot.user.id}')
    print(f'Discord version is: {discord.__version__}')
    print('------------------------------------------------------')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="you"))
    for cog in cogs:
        bot.load_extension(cog)
        print(f'{cog} is ready.')
    return


# run the Flask script to keep bot online
keep_alive.keep_alive()

# run bot
bot.run(token)
