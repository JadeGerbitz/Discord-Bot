import discord
from discord.ext import commands

class CNRCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CNR cog loaded!")

    @commands.command()
    async def findID(self, ctx, user: discord.Member):
        """Vores a given user."""
        print(user.id)

    @commands.command()
    async def emojiAdd(self, ctx):
        """Adds an emoji to a message."""
        msg = await ctx.send("test")
        await msg.add_reaction("\U0001F346")

def setup(bot):
    bot.add_cog(CNRCog(bot))
