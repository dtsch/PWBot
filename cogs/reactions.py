import discord
from discord.ext import commands


client = discord.Client()


class Reactions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.event
    async def on_member_join(self, member):
        rules = client.get_channel(794619790861664267)
        await member.send("Welcome, Comrade {}!".format(member.name))
        await member.send("Please check out the {} before heading to the dank meme stash."
                          .format(rules.mention))

    @client.event
    async def on_raw_reaction_add(self, payload):
        guild = client.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if payload.channel_id == 794619790861664267 and payload.message_id == 794619965788913675:
            # rules reaction role
            if str(payload.emoji) == '🆗':
                role = discord.utils.get(payload.member.guild.roles, name="Comrade")
                await payload.member.add_roles(role)
            # power club reaction role
            elif str(payload.emoji) == '🏋️':
                role = discord.utils.get(payload.member.guild.roles, name="Power Club")
                await payload.member.add_roles(role)

    @client.event
    async def on_raw_reaction_remove(self, payload):
        guild = client.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)
        if payload.channel_id == 794619790861664267 and payload.message_id == 794619965788913675:
            # rules reaction role
            if str(payload.emoji) == '🆗':
                role = discord.utils.get(guild.roles, name="Comrade")
                await member.remove_roles(role)
            # power club reaction role
            elif str(payload.emoji) == '🏋️':
                role = discord.utils.get(guild.roles, name="Power Club")
                await member.remove_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
