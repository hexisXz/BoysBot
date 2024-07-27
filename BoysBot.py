"""
MADE BY:
          _____                    _____                                            _____                    _____          
         /\    \                  /\    \                 ______                   /\    \                  /\    \         
        /::\____\                /::\    \               |::|   |                 /::\    \                /::\    \        
       /:::/    /               /::::\    \              |::|   |                 \:::\    \              /::::\    \       
      /:::/    /               /::::::\    \             |::|   |                  \:::\    \            /::::::\    \      
     /:::/    /               /:::/\:::\    \            |::|   |                   \:::\    \          /:::/\:::\    \     
    /:::/____/               /:::/__\:::\    \           |::|   |                    \:::\    \        /:::/__\:::\    \    
   /::::\    \              /::::\   \:::\    \          |::|   |                    /::::\    \       \:::\   \:::\    \   
  /::::::\    \   _____    /::::::\   \:::\    \         |::|   |           ____    /::::::\    \    ___\:::\   \:::\    \  
 /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  ______|::|___|___ ____  /\   \  /:::/\:::\    \  /\   \:::\   \:::\    \ 
/:::/  \:::\    /::\____\/:::/__\:::\   \:::\____\|:::::::::::::::::|    |/::\   \/:::/  \:::\____\/::\   \:::\   \:::\____\
\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /|:::::::::::::::::|____|\:::\  /:::/    \::/    /\:::\   \:::\   \::/    /
 \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  ~~~~~~|::|~~~|~~~       \:::\/:::/    / \/____/  \:::\   \:::\   \/____/ 
          \::::::/    /    \:::\   \:::\    \            |::|   |           \::::::/    /            \:::\   \:::\    \     
           \::::/    /      \:::\   \:::\____\           |::|   |            \::::/____/              \:::\   \:::\____\    
           /:::/    /        \:::\   \::/    /           |::|   |             \:::\    \               \:::\  /:::/    /    
          /:::/    /          \:::\   \/____/            |::|   |              \:::\    \               \:::\/:::/    /     
         /:::/    /            \:::\    \                |::|   |               \:::\    \               \::::::/    /      
        /:::/    /              \:::\____\               |::|   |                \:::\____\               \::::/    /       
        \::/    /                \::/    /               |::|___|                 \::/    /                \::/    /        
         \/____/                  \/____/                 ~~                       \/____/                  \/____/         
                                                                                                                            
"""



#imports 
from discord.ext import commands 
import randfacts
import wonderwords
from wonderwords import RandomWord
import logging
import sys
import time
import datetime
import pycord 
import nextcord
import os
from googleapiclient.discovery import build
import requests
from bardapi import Bard
from dotenv import load_dotenv
import random
import asyncio
import youtube_dl
from discord import FFmpegPCMAudio
import json
from nextcord.utils import get
import asyncio
import aiosqlite


# discord bots key
BOT_KEY = ""


#from nextcord.ext import commands

start = datetime.datetime.now()

#put the path to where you have the log.txt if you want logging
logging.basicConfig(filename="", level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

try:
    1/0
except ZeroDivisionError as err:
    logger.error(err)

# guild ID
GUILD_ID = ""

# SERVER OWNERS ID 
USER_ID = ""

intents = nextcord.Intents.all() 

intents.message_content = True

# this is the command to run the bot. feel free to change it if you like
client = commands.Bot(command_prefix='bb:', intents=intents) 

# discord channel
channel = client.get_channel()

user_data = {}

time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}
# Struct:
# {
#    "<author_id>": ["<msg_time>", "<msg_time>", ...],
#    "<author_id>": ["<msg_time>"],
# }



# API KEYS make sure add your google API keys for the WEB search function to work inside of discord
GOOGLE_API_KEY = ''
SEARCH_ENGINE_ID = ''



# DIALOGUE
greetings = ["Hello", "Howdy", "yo", "Bonjour", "wasssup", "Hey there", "Ahoy", "Hola", "Guten tag", "Good day", "'G'day", "hallo", "was good"]

insults = ["Im not insulting you; Im describing you.",
          "You bring everyone so much joy when you leave the room.",
          "I'd explain it to you, but I left my crayons at home.",
          "You're proof that even evolution can go in reverse.",
          "Your secrets are always safe with me. I never even listen when you tell me them.",
          "id give you a nasty look but youve already got one.",
          "Im trying to see things from your perspective, but I cant get my head that far up my ass.",
          "Id agree with you, but then wed both be wrong.",
          "If I wanted to hear from an asshole, Id fart.",
          "You have delusions of adequacy.",
          "Youre like a software update. Whenever I see you, I think, 'Not now.'",
          "Remember when I asked for your opinion? Me neither.",
          "I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.",
          "Somewhere out there is a tree, tirelessly producing oxygen for you. I think you owe it an apology.",
          "If laughter is the best medicine, your face must be curing the world.",
          "Your face makes onions cry.",
          "Youre not stupid; you just have bad luck thinking.",
            "You are proof that even God makes mistakes sometimes.",
            "If ignorance is bliss, you must be the happiest person on the planet.",
            "You are the human version of period cramps.",
            "Im jealous of people who dont know you.",
            "Its impossible to underestimate you.",
            "Id slap you, but that would be animal abuse.",
            "You bring everyone so much joy... when you leave the room.",
            "You're like a cloud. When you disappear, it's a beautiful day.",
            "I'd explain it to you, but your brain would explode.",
            "You are proof that God has a sense of humor.",
            "I'd love to stay and chat, but I'd rather have a tooth pulled.",
            "You must have been born on a highway because thats where most accidents happen.",
            "Your gene pool could use a little chlorine.",
            "You have the perfect face for radio.",
            "You're the reason the gene pool needs a lifeguard.",
            "You're not as dumb as you look. That would be impossible.",
            "I guess you prove that even duct tape can't fix stupid.",
            "Your family tree must be a cactus because everyone on it is a prick.",
            "Youre the reason God created the middle finger.",
            "You're a gray sprinkle on a rainbow cupcake.",
            "Your secrets are always safe with me. I never even listen when you tell me them.",
            "Im not saying I hate you, but I would unplug your life support to charge my phone.",
            "I was going to give you a nasty look, but you already have one.",
            "You are the human equivalent of a participation trophy.",
            "Youre about as useful as a screen door on a submarine.",
            "I'd call you an idiot, but that would be an insult to stupid people.",
            "You're not ugly, you're just... aesthetically challenged.",
            "You are living proof that evolution can go in reverse.",
            "Your only purpose in life is to serve as a warning to others.",
            "Ive seen people like you before, but I had to pay admission.",
            "You're the reason they put instructions on shampoo bottles.",
            "If you were any more inbred, youd be a sandwich.",
            "I thought of you today. It reminded me to take out the trash.",
            "You must have been born on a highway because thats where most accidents happen.",
            "I don't know what your problem is, but I'm guessing it's hard to pronounce.",
            "You're as useless as a knitted condom.",
            "Youre the reason the gene pool needs a lifeguard.",
            "Id agree with you but then wed both be wrong.",
            "I'd like to see things from your point of view, but I can't get my head that far up my ass.",
            "I see youve set aside this special time to humiliate yourself in public.",
            "Your birth certificate is an apology letter from the condom factory.",
            "You are proof that God has a sense of humor.",
            "You're as bright as a black hole, and twice as dense.",
            "You're the result of why condoms should be mandatory.",
            "You must have been born on a highway because thats where most accidents happen.",
            "You're so ugly, you scared the crap out of the toilet.",
            "Your family tree must be a cactus because everybody on it is a prick.",
            "You are proof that even God makes mistakes.",
            "You are like a cloud. When you disappear, its a beautiful day.",
            "I'd slap you, but that would be animal abuse.",
            "You're as useless as a screen door on a submarine.",
            "You are the reason why they put instructions on shampoo.",
            "Youre not stupid; you just have bad luck thinking.",
            "You're like a software update. Whenever I see you, I think, 'Not now.'",
            "I'd love to stay and chat, but I'd rather have a root canal.",
            "I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.",
            "Your brain's so minute, if a hungry cannibal cracked your head open, there wouldn't be enough to cover a small water biscuit.",
            "If you were any more inbred, youd be a sandwich.",
            "I bet your brain feels as good as new, seeing that you never use it.",
            "You bring everyone so much joy, when you leave the room.",
            "Youre the reason God created the middle finger.",
            "If I wanted to kill myself, I'd climb your ego and jump to your IQ.",
            "You must have been born on a highway because thats where most accidents happen.",
            "I would have agreed with you, but then wed both be wrong.",
            "I was going to give you a nasty look, but you already have one.",
            "Your gene pool could use a little chlorine.",
            "You're a gray sprinkle on a rainbow cupcake.",
            "If I had a face like yours, I'd sue my parents.",
            "You're as useless as a knitted condom.",
            "I see youve set aside this special time to humiliate yourself in public.",
            "I'd agree with you but then wed both be wrong.",
            "I guess you prove that even duct tape can't fix stupid.",
            "Your secrets are always safe with me. I never even listen when you tell me them.",
            "Im not saying I hate you, but I would unplug your life support to charge my phone.",
            "You are the human equivalent of a participation trophy.",
            "You're the reason they put instructions on shampoo bottles.",
            "I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.",
            "If I wanted to hear from an asshole, Id fart.",
            "You are proof that even God makes mistakes sometimes."]


# GIFS
susgifs = ["https://tenor.com/view/homelander-firecracker-milk-fire-cracker-the-boys-gif-15981747816355297523", "https://tenor.com/view/marcus-eyebrow-raise-sus-labrats-gif-13364863364524068533",
           "https://tenor.com/view/sus-goofy-ahh-the-rock-sus-gif-26995232", "https://tenor.com/view/hard-nope-gif-20352667"]

GIFS = ["https://tenor.com/view/lamine-yamal-barcelona-gif-11453904374483358390",
       "https://tenor.com/view/kevin-hart-stare-blink-really-you-serious-gif-7356251",
       "https://tenor.com/view/kevin-hart-stare-blink-really-you-serious-gif-7356251",
       "https://tenor.com/view/what-huh-face-shocked-zoom-gif-23833189",
       "https://tenor.com/view/funny-meme-public-weird-gif-11126868111164642824",
       "https://tenor.com/view/when-the-banana-sells-a-million-dollars-gif-11873212726979639512",
       "https://tenor.com/view/aplausos-clapped-leonardo-dicaprio-clap-slow-clap-gif-1724742745274938226",
       "https://tenor.com/view/dwayne-johnson-the-rock-eyebrow-gif-22322634",
       "https://tenor.com/view/tmzka-modric-luka-modric-croatia-croacia-gif-17666515",
       "https://tenor.com/view/mila-stauffer-whatever-eye-roll-gif-13204669",
       "https://tenor.com/view/facepalm-really-stressed-mad-angry-gif-16109475",
       "https://tenor.com/view/the-boys-butcher-gif-5041092981331887802",
       "https://tenor.com/view/black-black-man-african-africa-kid-gif-10379492666684688795",
       "https://tenor.com/view/black-black-hat-gif-23351208",
       "https://tenor.com/view/mouth-open-meme-funny-black-guy-mouth-open-meme-black-guy-mouth-meme-gif-14667232777531175562",
       "https://tenor.com/view/buzz-lightyear-no-sign-of-intelligent-life-dumb-toy-story-gif-11489315",
       "https://tenor.com/view/youstupid-gif-18622374",
       "https://tenor.com/view/anthony-petrocelli-stupid-dumb-fool-silly-gif-16043319",
       "https://tenor.com/view/dumb-more-stupid-gif-8521460407890876856",
       "https://tenor.com/view/ugly-mf-dumb-gif-24537569",
       "https://tenor.com/view/hell-yeah-why-you-so-stupic-so-stupid-why-you-gif-16729742",
       "https://tenor.com/view/stupid-steve-harvey-family-feud-south-africa-s-illy-dumb-gif-20867218",
       "https://tenor.com/view/boothill-stupid-hsr-star-rail-funny-gif-10042719508562238188",
       "https://tenor.com/view/you're-stupid-mehgan-james-basketball-wives-orlando-you're-dumb-you're-an-idiot-gif-6586431651306657706",
       "https://tenor.com/view/nice-opinion-ur-stupid-nice-opinion-too-bad-ur-stupid-donkey-kong-dont-care-didnt-ask-gif-21852707",
       "https://tenor.com/view/s-gif-586832218265368954",
       "https://tenor.com/view/kuroo-tetsurou-haikyuu-anime-laugh-lol-gif-14127137827951654805",
       "https://tenor.com/view/ignorant-fool-josh2funny-rude-fool-oblivious-fool-ignorant-idiot-gif-21992960",
       "https://tenor.com/view/fuck-fuck-you-middle-finger-middle-finger-gif-15294280",
       "https://tenor.com/view/pov-i-hate-you-hate-pov-i-hate-you-hate-you-gif-20122247",
       "https://tenor.com/view/go-to-hell-angry-upset-hate-you-mark-ruffalo-gif-15881145",
       "https://tenor.com/view/soldier-boy-the-boys-soldier-boy-soldier-boy-the-boys-and-you-might-wanna-gargle-my-ballsack-soldier-boy-pissed-off-gif-12002502617723457160"]


# COMMANDS
@client.event
async def en_ready():
    print("bot active.")
    print("------------")

@client.command()
async def talk(ctx):
    r = RandomWord()
    embedVar = nextcord.Embed(title=f"generated random word for testing: " + r.word(), color=0x00FF00)
    await ctx.send(embed=embedVar)

@client.command()
async def fact(ctx):
    fc = randfacts.get_fact()
    embedVar = nextcord.Embed(title=fc, color=0x00FF00)
    await ctx.send(embed=embedVar)

@client.command()
async def sus(ctx):
    await ctx.send(random.choice(susgifs))

@client.command()
async def info(ctx):
    embedVar = nextcord.Embed(title=f"I am a Discord bot here to make Discord Fun!.", color=0x0000FF)
    await ctx.send(embed=embedVar)

@client.command()
async def hlp(ctx):
    embedVar = nextcord.Embed(title=f"""bb:talk (sends a random word)
bb:fact (sends a random fact)
bb:sus  (sends a random sus GIF)
bb:info (tells you about the bot)
bb:members (tells you the current members)
bb:search (searches google inside discord)""", color=0xFF0080)
    await ctx.send(embed=embedVar)
    embedVar = nextcord.Embed(title=f"""bb:message (sends a message to the server owner)""", color=0xFF0080)
    await ctx.send(embed=embedVar)
    
@client.command()
async def members(ctx):
    embedVar = nextcord.Embed(title=f'There Are {ctx.guild.member_count} Members In This Server', color=0xFF0000)
    await ctx.send(embed=embedVar)

@client.command()
async def uptime(ctx):
    embedVar = nextcord.Embed(title=f'time when the bot was first started', color=0x0000FF)
    await ctx.send(embed=embedVar)
    embedVar = nextcord.Embed(title=start, color=0xFF0080)
    await ctx.send(embed=embedVar)

""" 
this is a partner command. 

if other people want to partner this bot can do it for you.

just add whatever message you want
"""
@client.command()
async def partnerhlp(ctx):
    embedVar = nextcord.Embed(title=f'ENTER YOUR MESAGE HERE', color=0x0000FF)
    await ctx.send(embed=embedVar)
    embedVar = nextcord.Embed(title=f'to advertise this server type bb:AD', color=0x0000FF)
    await ctx.send(embed=embedVar)

"""
add you server AD here
"""
@client.command()
async def AD(ctx):
    await ctx.send(f"""SERVER AD""")

@client.command()
async def partner(ctx, *, message: str):
    partner_channel = 1265023226367574037 
    target_channel = client.get_channel(partner_channel)
    if target_channel:
        await target_channel.send(f'@everyone {message}')
    else:
        await ctx.send("Target channel not found.")

@client.command()
async def serverAD(ctx):
    embedVar = nextcord.Embed(title=f'EXPLAIN TO THE DISCORD USERS HOW TO USE THE BOT TO PARTNER AND WHAT SERVER YOU WANT THEM TO RUN THE COMMAND IN', color=0x0000FF)
    await ctx.send(embed=embedVar)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# WORK WITH AND RESPOND TO MESSAGES
@client.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    # Debug print to check incoming messages
    print(f'Message from {message.author}: {message.content}')

    # Check if the message is in the specified channel
    channel_id = put_your_channel_id


    if message.channel.id == channel_id and message.content.lower() == "hi":
        await message.channel.send(random.choice(greetings))

    if message.channel.id == channel_id and message.content.lower() == "fuck you":
        await message.reply(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "your a bitch":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "you are a bitch":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "fuck u":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "shut up":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "stfu":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "shut the fuck up":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "bitch":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "stfu bitch":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "stupid":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "ur stupid":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "your stupid":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "you are stupid":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "hoe":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "bro":
        await message.channel.send("i'm not ur bro bitch")
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "wtf":
        await message.channel.send("dont wtf me dumb ass")

    if message.channel.id == channel_id and message.content.lower() == "Ciao":
        await message.channel.send("Ciao my dick bitch")
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "hey":
        await message.channel.send(random.choice(greetings))

    if message.channel.id == channel_id and message.content.lower() == "hello":
        await message.channel.send(random.choice(greetings))

    if message.channel.id == channel_id and message.content.lower() == "no":
        await message.channel.send("yes")

    if message.channel.id == channel_id and message.content.lower() == "yes":
        await message.channel.send("no")

    if message.channel.id == channel_id and message.content.lower() == "bye":
        await message.channel.send("you dont leave unless i tell u to bitch")
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "cya":
        await message.channel.send("where u goin fuck boy")
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "fuck this bot":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "bro fuck this bot":
        await message.channel.send(random.choice(insults))
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "omg":
        await message.channel.send("omg omg, STFU BITCH")
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "yo":
        await message.channel.send("yo, shut up and stop saying yo you dumb bitch")
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "stop":
        await message.channel.send("no")

    if message.channel.id == channel_id and message.content.lower() == "true":
        await message.channel.send("FAX!")

    if message.channel.id == channel_id and message.content.lower() == "lol":
        await message.channel.send("hahahahahahahahahahahaa, you got the whole squad laughing G ☠")
        time.sleep(2)
        await message.channel.send(random.choice(GIFS))

    if message.channel.id == channel_id and message.content.lower() == "sus":
        await message.channel.send(random.choice(susgifs)) 

    if client.user.mentioned_in(message):
        await message.channel.send("wtf do u want? (if your dumb and need help type bb:hlp to list the things i can do)")
        time.sleep(3)
        await message.channel.send("also")
        time.sleep(1)
        await message.channel.send(random.choice(insults))

    # STOP PEOPLE FROM SPAMMING
    global author_msg_counts

    author_id = message.author.id
    # Get current epoch time in milliseconds
    curr_time = datetime.datetime.now().timestamp() * 1000

    # Make empty list for author id, if it does not exist
    if not author_msg_times.get(author_id, False):
        author_msg_times[author_id] = []

    # Append the time of this message to the users list of message times
    author_msg_times[author_id].append(curr_time)

    # Find the beginning of our time window.
    expr_time = curr_time - time_window_milliseconds

    # Find message times which occurred before the start of our window
    expired_msgs = [
        msg_time for msg_time in author_msg_times[author_id]
        if msg_time < expr_time
    ]

    # Remove all the expired messages times from our list
    for msg_time in expired_msgs:
        author_msg_times[author_id].remove(msg_time)
    # ^ note: we probably need to use a mutex here. Multiple threads
    # might be trying to update this at the same time. Not sure though.

    if len(author_msg_times[author_id]) > max_msg_per_window:
        await message.channel.send("Stop Spamming")
        duration = datetime.timedelta(seconds=90, minutes=10, hours= 0, days=0)
        await message.author.timeout(duration, reason="spamming") 


    # Process bot commands
    await client.process_commands(message)

def google_search(query):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=3).execute()
    return res.get('items', [])

@client.command()
async def search(ctx, *, query: str):
    results = google_search(query)
    if not results:
        await ctx.send("No results found.")
        return
    
    for item in results:
        title = item['title']
        link = item['link']
        snippet = item['snippet']
        await ctx.send(f"**{title}**\n{link}\n{snippet}\n")

# SEND A MESSAGE TO THE OWNER OF THE SERVER
@client.command(name='message')
async def send_private_message(ctx, *, msg):
    user = client.get_user(USER_ID)
    if user:
        await user.send(f"Message from {ctx.author}: {msg}")
        await ctx.send("Your message has been sent!")
    else:
        await ctx.send("Couldn't find the user to send the message.")

@client.event
async def on_member_join(member):
    try:
        await member.send(f"Welcome to The server, {member.name}! this is a bot to make discord better.")
        time.sleep(2)
        await member.send(f"have fun and chill out in this server. the bot has a lot of cool commands like google searching inside of discord, sending messages to the server creator and more with a ton still being added so have fun and enjoy the server.")
        print(f"Sent welcome message to {member.name}")
    except Exception as e:
        print(f"Failed to send welcome message to {member.name}: {e}")


"""
remove the comments if you want the bot to give users a role

@client.command()
async def giverole(ctx):
    member = ctx.author
    guild = ctx.guild  
    role = guild.get_role(1263974394586202174)

    await member.add_roles(role)
    await ctx.send("here is ur role bitch")"""

client.run(BOT_KEY)