import discord
from discord.ext import commands

class CNRCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CNR cog loaded!")

    @commands.command()
    async def vore(self, ctx, user: discord.Member):
        """Vores a given user."""
        await ctx.send("Sorry {}, but you just got vored".format(user.name))

def setup(bot):
    bot.add_cog(CNRCog(bot))
