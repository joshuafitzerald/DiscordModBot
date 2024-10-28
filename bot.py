import ssl

# Disable SSL verification temporarily
ssl._create_default_https_context = ssl._create_unverified_context

import certifi
print(certifi.where())
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Enables the bot to access member information
intents.message_content = True  # For moderating messages

# Set the command prefix to '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# List of banned words (you can add to this list dynamically)
banned_words = ["badword1", "badword2", "badword3"]

# Profanity filter in the on_message event
@bot.event
async def on_message(message):
    # Ignore messages from bots
    if message.author.bot:
        return

    # Check if the message contains any banned words
    for word in banned_words:
        if word in message.content.lower():  # Case-insensitive matching
            await message.delete()  # Delete the offending message
            await message.channel.send(f"{message.author.mention}, please watch your language!")
            return  # Stop further checks after finding one banned word

    # Process other bot commands
    await bot.process_commands(message)

# Example command to add words to the banned list dynamically
@bot.command(name='addword')
@commands.has_permissions(administrator=True)
async def addword(ctx, *, word: str):
    banned_words.append(word.lower())  # Add the word in lowercase for consistent checks
    await ctx.send(f'The word "{word}" has been added to the banned words list.')

# Example command to show the banned words (admin only)
@bot.command(name='bannedwords')
@commands.has_permissions(administrator=True)
async def bannedwords(ctx):
    await ctx.send(f"Banned words: {', '.join(banned_words)}")

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# A simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Kick a member from the server
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for {reason}')

# Ban a member from the server
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for {reason}')

#unban
@bot.command(name='unban_member')
@commands.has_permissions(ban_members=True)
async def unban_member(ctx, *, member):
    print("Unban command triggered")  # Debugging step

    # Get the list of banned users (async generator)
    async for ban_entry in ctx.guild.bans():
        user = ban_entry.user
        print(f"Checking banned user: {user.name}")  # Debugging step

        # Compare with the provided member username (case-insensitive)
        if user.name.lower() == member.lower():
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            print(f"Unbanned user: {user.name}")  # Debugging step
            return

    # If the user is not found in the banned list
    await ctx.send(f'Member `{member}` not found.')
    print(f"Member {member} not found in the banned list.")  # Debugging step

# Clear messages in the chat
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Add your bot token here
bot.run('YOUR-DISCORD-BOT-TOKEN')
