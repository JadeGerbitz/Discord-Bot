import discord
from discord.ext import commands

import asyncio
import os

ffmpeg_options = {'options': '-vn'}

music = []
dir = "././Music"

for filename in os.listdir(dir):
    if(filename.endswith(".wav") or filename.endswith(".mp3")):
        music.append(dir + "/" + filename)
    if(os.path.isdir(dir + "/" + filename)):
        for file in os.listdir(dir + "/" + filename):
            if(file.endswith(".wav") or file.endswith(".mp3")):
                music.append(dir + "/" + filename + "/" + file)

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music cog loaded!")

    @commands.command()
    async def join(self, ctx):
        """Joins a voice channel"""
        channel = ctx.author.voice.channel

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        def find(query):
            for song in music:
                if(query == (song.split("/")[-1][:-4])):
                    query = song
                    return query
            return "NF"

        query = find(query)

        if(query != "NF"):
            if(ctx.voice_client.is_playing()):
                ctx.voice_client.stop()
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

            await ctx.send('Now playing: {}'.format(query.split("/")[-1][:-4]))
        else:
            await ctx.send("Song not found.")

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")


def setup(bot):
    bot.add_cog(MusicCog(bot))
