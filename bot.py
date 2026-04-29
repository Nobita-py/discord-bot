import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

RAIDS = {
    "🔥 Normal Raid Pricing": {
        "1–5 Raids": "Quake (1M) / Love (1.2M)",
        "6–10 Raids": "Spider (1.5M) / Phoenix (3M)",
        "11–15 Raids": "Sound (3M) / Buddha (12M) / Portal (12M)",
        "16–20 Raids": "T-Rex (20M) / Venom (25M)",
        "21–25 Raids": "Dough (30M)",
        "26–30 Raids": "Gas (60M) / Rumble (90M)",
        "30+ Raids": "Yeti (140M) / Kitsune (620M)"
    },
    "🔥 Advanced Raid Pricing": {
        "1 Advanced Raid": "Sound (3M)",
        "2 Advanced Raids": "Spirit (10M) / Mammoth (9M)",
        "3 Advanced Raids": "Buddha (12M) / Portal (12M)",
        "4 Advanced Raids": "T-Rex (20M)",
        "5 Advanced Raids": "Venom (25M)",
        "6 Advanced Raids": "Dough (30M)",
        "7 Advanced Raids": "Gas (60M)",
        "8 Advanced Raids": "Rumble (90M)",
        "9 Advanced Raids": "Control (120M)",
        "10 Advanced Raids": "Yeti (140M) / Kitsune (620M)"
    }
}

TRIALS = {
    "Prehistoric Island (Draco V4)": {
        "Trial 1 (Single Trial)": "Dough (30M) or T-Rex (20M)",
        "Trial 2 (Two Trials)": "x2 Dough (60M) or x2 T-Rex (40M)",
        "Trial 3 (Three Trials)": "Control (120M) or Gas (60M)",
        "Full Draco V4 Awakening (All 4 Trials)": "Kitsune (620M) or x2 Control (240M) or x2 Gas (120M) or Yeti (140M)"
    },
    "Race Trial Packages (Awaken V4)": {
        "Trial 1 (Single Trial)": "Buddha (12M) or Portal (12M)",
        "Trial 2 (Two Trials)": "T-Rex (20M)",
        "Trial 3 (Three Trials)": "Dough (30M)",
        "Full V4 Awakening (All 4 Trials)": "Gas (60M) or Rumble (90M) for race trial"
    }
}

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')
    await asyncio.sleep(1)
    try:
        synced = await bot.tree.sync()
        print(f'✅ Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'❌ Failed to sync commands: {e}')

@bot.event
async def on_guild_channel_create(channel):
    if "ticket" in channel.name.lower():
        embed = discord.Embed(
            title="📋 Welcome to your ticket!",
            description="Use the commands below to see our services and pricing:",
            color=discord.Color.blue()
        )
        embed.add_field(name="/raids", value="View Raid Services pricing", inline=False)
        embed.add_field(name="/trials", value="View Trial Packages pricing", inline=False)
        embed.add_field(name="/raging-demon", value="View Raging Demon pricing", inline=False)
        embed.set_footer(text="Choose a command above to see pricing details!")
        
        try:
            await channel.send(embed=embed)
        except Exception as e:
            print(f"Error sending message: {e}")

@bot.tree.command(name="raids", description="View Raid Services pricing")
async def raids(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 Raid Services Available 🔥",
        description="✅ Fast Clears ✅ Fragment Farming ✅ Trusted Service ✅ Host Available if Needed",
        color=discord.Color.red()
    )
    
    for category, pricing in RAIDS.items():
        embed.add_field(name=category, value="", inline=False)
        for raid_tier, reward in pricing.items():
            embed.add_field(name=f"⚔️ {raid_tier}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order | Values from FantasyBlox")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="trials", description="View Trial Packages pricing")
async def trials(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📦 Trial Packages",
        description="Fast and reliable service",
        color=discord.Color.gold()
    )
    
    for package_name, trials_list in TRIALS.items():
        embed.add_field(name=f"📦 {package_name}", value="", inline=False)
        for trial_name, reward in trials_list.items():
            embed.add_field(name=f"  • {trial_name}", value=f"  {reward}", inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order | Values from FantasyBlox")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="raging-demon", description="View Raging Demon pricing")
async def raging_demon(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚡ Raging Demon",
        description="Pricing based on fruit values",
        color=discord.Color.purple()
    )
    
    embed.add_field(name="💰 Pricing", value="x2 Portal (24M) or equivalent fruits", inline=False)
    embed.add_field(name="📍 Examples", value="Dough (30M) / Buddha (12M) + Portal (12M) / T-Rex (20M) + Love (1.2M) + Quake (1M)", inline=False)
    embed.add_field(name="📍 Fruit Values", value="Check values at: https://fantasyblox.com/games/blox-fruits/values", inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

token = os.getenv('DISCORD_TOKEN')
if not token:
    print("ERROR: DISCORD_TOKEN environment variable not set!")
    exit(1)

bot.run(token)
