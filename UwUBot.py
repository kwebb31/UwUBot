import os
import discord
import random
import giphy_client
from giphy_client.rest import ApiException
from discord.ext import commands
from ast import alias
from keep_alive import keep_alive
import asyncio
from discord.utils import get

my_secret = os.environ['UwUBotSecret;)']
giphy_token = "JWhCzqqAx9PDRUaAnh71KaiJ5npZAlsW"
api_instance = giphy_client.DefaultApi()

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

friendList = []

lifespells = [
  "flowerweaver", "plantweaver", "treeweaver", "flowerbringer", "lifebringer",
  "liebringer", "lifegiver", "flowergiver", "lifebreather", "flowerbreather",
  "lofeweaver", "lufeweaver", "lifegripper", "loveweaver", "wifeleaver"
]


@bot.event
async def on_ready():
  await print('UwU')
  await print(bot.user)  #tells us that our bot is online

@bot.event  #responding to messages
async def on_message(message):
  message.content = (
    message.content.lower()
  )  #makes all messages lowercase, from the bot's perspective
  if '!random' in message.content or '!roll' in message.content:
    if message.author == bot.user:

      try:
        # Get the value of n from the user's message
        n = int(message.content.split()[2])
      except:
        # If n is not provided or not an integer, send an error message
        await message.channel.send(
          ' Gimme a number for your roll. None of these fancy decimal numbers either, a whole number.'
        )
        return
    else:

      try:
        # Get the value of n from the user's message
        n = int(message.content.split()[1])
      except:
        # If n is not provided or not an integer, send an error message
        await message.channel.send(
          ' Gimme a number for your roll. None of these fancy decimal numbers either, a whole number.'
        )
        return

    # Generate a random number between 1 and n
    random_num = random.randint(1, n)
    high = n * .75
    low = n * .25
    if random_num == 1:
      await message.channel.send(f"a {random_num}... oof,  a crit fail. UwU")
    elif random_num == n:
      await message.channel.send(f"a nat {random_num}!!!! Perfection. UwU ")
    elif random_num >= high:
      await message.channel.send(
        f" {random_num} of {n} - That's a pretty good roll! UwU")
    elif random_num < low:
      await message.channel.send(
        f" {random_num} of {n} - Dang, reroll maybe? UwU")
    # Send the random number to the user
    else:
      await message.channel.send(f'{random_num} of {n}, uwu')

  if message.author == bot.user:  #to not respond to bots
    return

  if "owo" in message.content:
    await message.channel.send("uwu")  #response

  if "uwu" in message.content:
    await message.channel.send("owo")

  if (message.channel.id == "1053580723338096651"):
    await message.add_reaction("<:eggplant:1085108171263188992>")

  if "sex" in message.content:
    await message.channel.send("merky sex joke ily. uwu")

  if message.content.lower() in lifespells:
    await message.channel.send(
      "https://cdn.discordapp.com/attachments/1044326072201781383/1092938797483827321/IMG_3854.png"
    )

  if message.content.lower().startswith("sigma"):
    await message.channel.send("Sigma ballz gottem")

  if message.content.lower().startswith("ligma"):
    await message.channel.send("ligma balls")

  if "cat" in message.content:
    await message.channel.send("A cat. UwU " + message.author.mention)
    await message.channel.send(await search_gifs("cat"))

  if "69" in message.content:
    await message.channel.send("nice :3 uwu")
    await message.channel.send(await search_gifs("nice"))

  if "kitten" in message.content.lower() or "kitty" in message.content.lower():
    await message.channel.send("A baby cat. UwU " + message.author.mention)
    await message.channel.send(await search_gifs("kitten"))

  if "pussy" in message.content.lower() or "bussy" in message.content.lower():
    await message.channel.send("Pop that pussy/bussy bitch " +
                               message.author.mention)
    await message.channel.send(await search_gifs("bussy"))

  if "bongo" in message.content.lower() or "bongocat" in message.content.lower(
  ):
    await message.channel.send("Slap Slap Slap" + message.author.mention)
    await message.channel.send(await search_gifs("bongocat"))

  if message.content.lower().startswith("!wiki"):
    wiki_for = "_".join(message.content.split()[1:])
    await message.channel.send(f"https://en.wikipedia.org/wiki/{wiki_for}")

  await bot.process_commands(message)


#@bot.command()
##async def tts(ctx, *, message):
#  voice_channel = ctx.author.voice.channel
#  voice_client = get(bot.voice_clients, guild=ctx.guild)

#  if voice_client and voice_client.is_connected():
#    await voice_client.move_to(voice_channel)
#  else:
#    voice_client = await voice_channel.connect()

#  source = discord.PCMVolumeTransformer(
#    discord.FFmpegPCMAudio(source=f"tts.mp3?text={message}&lang=en"))
#  voice_client.play(source)
 # while voice_client.is_playing():
#    await asyncio.sleep(1)
#  voice_client.stop()
#  await voice_client.disconnect()


@bot.command(aliases=["fucker"])
async def overwatch(ctx, hero):
  await ctx.send(f"I fucking hate {hero} Overwatch. They suck.")


@bot.command(aliases=['test2', 'testing'])  #other names for the command
async def test(ctx):  #test is the command name
  await ctx.send("This is a tts message", tts=True)
  #response to the command


@bot.command(aliases=['add'])
async def push(ctx, name):
  friendList.append(name)
  await ctx.send(f"Adding {name} to the current queue.", tts=True)


@bot.command(aliases=['remove', 'dequeue'])
async def delete(ctx, name):
  try:
    friendList.remove(name)
    await ctx.send(f"{name} was removed.")
  except:
    await ctx.send(f"{name} was not found in the current queue list.")


@bot.command(aliases=['ready'])
async def pop(ctx):
  new = friendList[0]
  await ctx.send(f"It's {new}'s turn to play!", tts=True)

  friendList.pop(0)


@bot.command(aliases=['queue', 'list'])
async def print(ctx):
  counter = 0
  for item in friendList:
    counter += 1
    await ctx.send(f'{counter}. {item}')


@bot.command()
async def cleared(ctx):
  friendList.cleared()
  await ctx.send("The queue has been cleared.")


@bot.command(aliases=['8ball'])
async def ball(
  ctx
):  #can't really put numbers in the command name so we have 8ball as an alias instead
  ballresponses = [
    'Without a doubt. UwU', 'Outlook good. UwU',
    'Better not tell you now. UwU', 'Cannot predict now. UwU',
    'My reply is no. UwU', 'Signs point to yes. UwU', 'Surely! UwU',
    'Outlook not so good. UwU', "uwu you little shit. UwU"
  ]
  z = random.choice(ballresponses)  #choose yes or no, randomly
  await ctx.send(z)  #send either yes or no


#@bot.command(aliases = ['!generate', '!playlist'])
#async def g(ctx):
#    playlist = myMenu()
#    await ctx.send(playlist) #send either yes or no
@bot.command(aliases=["gif", "giphy"])
async def myGif(ctx, query):
  await ctx.send(await search_gifs(query))


async def search_gifs(query):
  try:
    response = api_instance.gifs_search_get(giphy_token,
                                            query,
                                            limit=100,
                                            rating='r')
    lst = list(response.data)
    gif = random.choices(lst)

    return gif[0].url

  except ApiException as e:
    return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e


from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False
        self.is_paused = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            #try to connect to voice channel if you are not already connected
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                #in case we fail to connect
                if self.vc == None:
                    await ctx.send("Could not connect to the voice channel")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @bot.command(name="play", aliases=["p","playing"], help="Plays a selected song from youtube")
    async def play(self, ctx, *args):
        query = " ".join(args)
        voice_client = get(bot.voice_clients, guild=ctx.guild)
   # if voice_client and voice_client.is_connected():
  #    await voice_client.move_to(voice_channel)
  #  else:
  #    voice_client = await voice_channel.connect()
  #    voice_channel = ctx.author.voice.channel
  #  if voice_channel is None:
            #you need to be connected so that the bot knows where to go
   #         await ctx.send("Connect to a voice channel!")
       # elif self.is_paused:
       #     self.vc.resume()
       # else:
       #     song = self.search_yt(query)
       #     if type(song) == type(True):
       #         await ctx.send("Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
        #    else:
        #        await ctx.send("Song added to the queue")
        #        self.music_queue.append([song, voice_channel])
                
       #         if self.is_playing == False:
       #             await self.play_music(ctx)

    @commands.command(name="pause", help="Pauses the current song being played")
    async def pause(self, ctx, *args):
      if self.is_playing:
		     self.is_playing = False
		     self.is_paused = True
		     self.vc.pause()
      elif self.is_paused:
		     self.is_paused = False
		     self.is_playing = True
		     self.vc.resume()

    @bot.command(name = "resume", aliases=["r"], help="Resumes playing with the discord bot")
    async def resume(self, ctx, *args):
        if self.is_paused:
		        self.is_paused = False
		        self.is_playing = True
		        self.vc.resume()

    @bot.command(name="skip", aliases=["s"], help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music(ctx)


#    @bot.command(name="queue", aliases=["q"], help="Displays the current songs in queue")
#    async def queue(self, ctx):
#       retval = ""
#       for i in range(0, len(self.music_queue)):
            # display a max of 5 songs in the current queue
#            if (i > 4): break
#            retval += self.music_queue[i][0]['title'] + "\n"

#        if retval != "":
#            await ctx.send(retval)
#        else:
#            await ctx.send("No music in queue")

    @bot.command(name="clear", aliases=["c", "bin"], help="Stops the music and clears the queue")
    async def clear(self, ctx):
        if self.vc != None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await ctx.send("Music queue cleared")

    @commands.command(name="leave", aliases=["disconnect", "l", "d"], help="Kick the bot from VC")
    async def dc(self, ctx):
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()

keep_alive()
sneakret = os.environ['UwUBotSecret;)']
bot.run(sneakret)
client.run(sneakret)
