import discord
from discord.ext import commands
import asyncio
import random

client = discord.Client()


class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # command that DMs the sender
    @commands.command(
        pass_context=True,
        name='direct_message',
        description='Initiates a DM with the user.',
        help='Initiates a DM with the user.',
        aliases=['dm'],
        usage=''
    )
    async def direct_message(self, ctx):
        await ctx.author.send("Hey, what do you need?")

    # command that replies with the cucumber emoji
    @commands.command(
        pass_context=True,
        name='pickle_me',
        description='Replies with a pickle.',
        help='Replies with a pickle.',
        aliases=['pickle'],
        usage=''
    )
    async def pickle_me(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.message.channel.send("You require a pickle?")
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.message.channel.send("🥒")
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.message.channel.send("There you are.")

    # @client.event
    # @commands.has_any_role('Rear Admiral', 'Comrade')
    # async def on_message(self, message):
    #     mention = f'<@!{client.user.id}>'
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
    #         , "Don't force me to run you through!"
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


def setup(bot):
    bot.add_cog(Chat(bot))
