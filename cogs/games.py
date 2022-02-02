import discord
from discord.ext import commands
import asyncio
import random
import re
import itertools


client = discord.Client()


# noinspection SpellCheckingInspection
class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # command that rolls dice
    @commands.command(
        pass_context=True,
        name='roll',
        help='Rolls a die/dice with modifiers.',
        aliases=['r'],
        description='Rolls a die/dice with modifiers, specified by the user.\n'
                    'Multiple types of dice can be rolled with additional (+NdS) added to middle of the formula.\n'
                    'Advantage/disadvantage only work when rolling 1d20 (other dice and modifiers are accommodated).\n'
                    'Input "!roll char#" to roll a character ability score array with 1) 3d6 straight up, '
                    '2) 4d6 - lowest',
        usage='<NdS(+NdS)±M/char[1/2]> <a/d>'
    )
    async def roll(self, ctx, formula='1d20', adv=''):
        if formula == 'char1':
            for _ in range(0, 6):
                rolls = []
                for _ in range(0, 3):
                    rolls.append(random.randint(1, 6))
                total = sum(rolls)
                async with ctx.typing():
                    await asyncio.sleep(0.5)
                    await ctx.send(f'{ctx.author.mention} rolled {rolls}, for a total of {total}.')
        elif formula == 'char2':
            for _ in range(0, 6):
                rolls = []
                for _ in range(0, 4):
                    rolls.append(random.randint(1, 6))
                rolls.sort(reverse=True)
                rolls.pop()
                total = sum(rolls)
                async with ctx.typing():
                    await asyncio.sleep(0.5)
                    await ctx.send(f'{ctx.author.mention} rolled {rolls}, for a total of {total}.')
        elif re.search(r'^\d+d\d+(?:\+\d+d\d+)*[+|-]?\d*$', formula) is None:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Formula incorrect, please try again using the NdS±M format.")
        else:
            f_dice = re.findall(r'\d+d\d+', formula)
            mod = re.search(r'([+|-]\d+?)$', formula)
            crit = ''
            a = ''
            if mod is None:
                mod = 0
            else:
                mod = mod.group(1)
            dice = []
            for d in f_dice:
                f_die = re.match(r'(\d+)d(\d+)', d)
                dice.append([int(f_die.group(1)), int(f_die.group(2))])
            rolls = []
            total = 0
            for i in dice:
                j = 0
                while j < i[0]:
                    roll = random.randint(1, int(i[1]))
                    rolls.append(roll)
                    if i[0] == 1 and i[1] == 20:
                        if adv == 'a':
                            a = "**advantage** and "
                            a_roll = random.randint(1, int(i[1]))
                            rolls.append(a_roll)
                            if a_roll > roll:
                                total -= roll
                            else:
                                total -= a_roll
                        elif adv == 'd':
                            a = "**disadvantage** and "
                            a_roll = random.randint(1, int(i[1]))
                            rolls.append(a_roll)
                            if a_roll < roll:
                                total -= roll
                            else:
                                total -= a_roll
                        if roll == 1:
                            crit = "miss"
                        elif roll == 20:
                            crit = "hit"
                    j += 1
            total += sum(rolls) + int(mod)
            result = f'{ctx.author.mention} rolled {rolls}, with {a}a modifier of {mod}, for a total of {total}.'
            async with ctx.typing():
                if crit == 'hit':
                    await asyncio.sleep(1)
                    await ctx.send('https://gph.is/g/Z86v0wb')
                    applause = ['https://gph.is/g/a993Kq8', 'http://gph.is/1MNcqXS', 'http://gph.is/2na2PP2']
                    await asyncio.sleep(0.5)
                    if adv == 'd':
                        for i in applause:
                            await ctx.send(i)
                    else:
                        await ctx.send(random.choice(applause))
                elif crit == "miss":
                    await asyncio.sleep(1)
                    await ctx.send('https://gph.is/g/ZWlWypL')
                    await asyncio.sleep(0.5)
                    boo = ['https://gph.is/2In3WtK', 'http://gph.is/148y1Or', 'http://gph.is/13FlHbd',
                           'https://gph.is/2eYZZg2', 'http://gph.is/1UyY5v6',
                           'https://tenor.com/view/takeshi-run-game-fail-slip-gif-16406291',
                           'https://tenor.com/view/stare-laugh-fialed-funny-gif-17007708',
                           'https://tenor.com/view/takeshi-castle-fail-bump-gif-12772898']
                    await ctx.send(random.choice(boo))
                    if adv == 'a':
                        await ctx.send(random.choice(boo))
                        await ctx.send(random.choice(boo))
                await asyncio.sleep(1)
                await ctx.send(result)


  # slash command that rolls dice
  @slash.slash(
      pass_context=True,
      name='roll',
      help='Rolls a die/dice with modifiers.',
      aliases=['r'],
      description='Rolls a die/dice with modifiers, specified by the user.\n'
                  'Multiple types of dice can be rolled with additional (+NdS) added to middle of the formula.\n'
                  'Advantage/disadvantage only work when rolling 1d20 (other dice and modifiers are accommodated).\n'
                  'Input "!roll char#" to roll a character ability score array with 1) 3d6 straight up, '
                  '2) 4d6 - lowest',
      usage='<NdS(+NdS)±M/char[1/2]> <a/d>'
  )
  async def roll(self, ctx, formula='1d20', adv=''):
        if formula == 'char1':
            for _ in range(0, 6):
                rolls = []
                for _ in range(0, 3):
                    rolls.append(random.randint(1, 6))
                total = sum(rolls)
                async with ctx.typing():
                    await asyncio.sleep(0.5)
                    await ctx.send(f'{ctx.author.mention} rolled {rolls}, for a total of {total}.')
        elif formula == 'char2':
            for _ in range(0, 6):
                rolls = []
                for _ in range(0, 4):
                    rolls.append(random.randint(1, 6))
                rolls.sort(reverse=True)
                rolls.pop()
                total = sum(rolls)
                async with ctx.typing():
                    await asyncio.sleep(0.5)
                    await ctx.send(f'{ctx.author.mention} rolled {rolls}, for a total of {total}.')
        elif re.search(r'^\d+d\d+(?:\+\d+d\d+)*[+|-]?\d*$', formula) is None:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Formula incorrect, please try again using the NdS±M format.")
        else:
            f_dice = re.findall(r'\d+d\d+', formula)
            mod = re.search(r'([+|-]\d+?)$', formula)
            crit = ''
            a = ''
            if mod is None:
                mod = 0
            else:
                mod = mod.group(1)
            dice = []
            for d in f_dice:
                f_die = re.match(r'(\d+)d(\d+)', d)
                dice.append([int(f_die.group(1)), int(f_die.group(2))])
            rolls = []
            total = 0
            for i in dice:
                j = 0
                while j < i[0]:
                    roll = random.randint(1, int(i[1]))
                    rolls.append(roll)
                    if i[0] == 1 and i[1] == 20:
                        if adv == 'a':
                            a = "**advantage** and "
                            a_roll = random.randint(1, int(i[1]))
                            rolls.append(a_roll)
                            if a_roll > roll:
                                total -= roll
                            else:
                                total -= a_roll
                        elif adv == 'd':
                            a = "**disadvantage** and "
                            a_roll = random.randint(1, int(i[1]))
                            rolls.append(a_roll)
                            if a_roll < roll:
                                total -= roll
                            else:
                                total -= a_roll
                        if roll == 1:
                            crit = "miss"
                        elif roll == 20:
                            crit = "hit"
                    j += 1
            total += sum(rolls) + int(mod)
            result = f'{ctx.author.mention} rolled {rolls}, with {a}a modifier of {mod}, for a total of {total}.'
            async with ctx.typing():
                if crit == 'hit':
                    await asyncio.sleep(1)
                    await ctx.send('https://gph.is/g/Z86v0wb')
                    applause = ['https://gph.is/g/a993Kq8', 'http://gph.is/1MNcqXS', 'http://gph.is/2na2PP2']
                    await asyncio.sleep(0.5)
                    if adv == 'd':
                        for i in applause:
                            await ctx.send(i)
                    else:
                        await ctx.send(random.choice(applause))
                elif crit == "miss":
                    await asyncio.sleep(1)
                    await ctx.send('https://gph.is/g/ZWlWypL')
                    await asyncio.sleep(0.5)
                    boo = ['https://gph.is/2In3WtK', 'http://gph.is/148y1Or', 'http://gph.is/13FlHbd',
                           'https://gph.is/2eYZZg2', 'http://gph.is/1UyY5v6',
                           'https://tenor.com/view/takeshi-run-game-fail-slip-gif-16406291',
                           'https://tenor.com/view/stare-laugh-fialed-funny-gif-17007708',
                           'https://tenor.com/view/takeshi-castle-fail-bump-gif-12772898']
                    await ctx.send(random.choice(boo))
                    if adv == 'a':
                        await ctx.send(random.choice(boo))
                        await ctx.send(random.choice(boo))
                await asyncio.sleep(1)
                await ctx.send(result)


def setup(bot):
    bot.add_cog(Games(bot))
