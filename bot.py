import discord
from discord.ext import commands
import os
import yt_dlp as youtube_dl
import asyncio
from dotenv.main import load_dotenv
load_dotenv() 

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# BASIC

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def kys(ctx):
    await ctx.send('It\'s really important to understand that words carry immense weight, especially when directed at someone during a difficult time. Telling someone to "kys" (kill yourself) is not only incredibly harmful but also dangerous. It\'s crucial to approach others with kindness and empathy, even when disagreements or frustrations arise. If you\'re feeling overwhelmed or upset, there are better ways to express those feelings without resorting to hurtful language. Consider talking to a friend, family member, or counselor about what\'s bothering you. Remember, everyone is fighting their own battles, and a little compassion can go a long way in making the world a better place for all of us. Let\'s aim to lift each other up rather than tearing each other down.')

@bot.command()
async def echo(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! {latency:.2f}ms')

# MUSIC

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.message.delete()
    else:
        await ctx.send('I am not in a voice channel.')

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'noplaylist': 'True',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'restrictfilenames': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto',
            'source_address': '0.0.0.0'  # Bind to IPv4 since IPv6 addresses cause issues sometimes
        }
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

    # searching the item on youtube
    def search_yt(self, item):
        with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False
        info = ydl.sanitize_info(info)
        url = info['url']
        title = info['title']
        return {
            'title': title,
            'source': url
        }

    @commands.command()
    async def play(self, ctx, *, search: str):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await channel.connect()
            elif ctx.voice_client.channel != channel:
                await ctx.voice_client.move_to(channel)

            ctx.voice_client.stop()

            try:
                info = self.search_yt(search)
                if not info:
                    await ctx.send('Could not find the requested video.')
                    return

                source = await discord.FFmpegOpusAudio.from_probe(info['source'], **self.FFMPEG_OPTIONS)
                ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
                await ctx.send(f'Now playing: {info["title"]}')
            except Exception as e:
                await ctx.send(f'An error occurred: {str(e)}')
                print(f'Error: {str(e)}')
        else:
            await ctx.send('Join a voice channel first.')

async def main():
    await bot.add_cog(Music(bot))
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())