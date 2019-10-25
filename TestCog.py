import discord
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Test cog loaded!")

    @commands.command()
    async def CogTest(self, ctx):
        """Sends a test message"""
        await ctx.send("The test cog is working!")

def setup(bot):
    bot.add_cog(TestCog(bot))