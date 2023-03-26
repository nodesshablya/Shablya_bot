import discord
from discord.ext import commands
import asyncio


TOKEN = 'MTA4OTIzNDU4Nzc2MDIwMTg2OA.GCo0CE.Na00qY5B1tIaG0xZHKQjF_eqElD1HxxsqlcLqw'


ROLE_ID = 1088818348042752131


intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_member_join(member):

    if member.bot:
        return

    role = member.guild.get_role(ROLE_ID)
    await member.add_roles(role)

    await asyncio.sleep(86400)

    await member.remove_roles(role)


client.run(TOKEN)
