import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

RAIDS = {
    "🔥 Normal Raid Pricing": {
        "1–5 Raids": "Love / Quake",
        "6–10 Raids": "Spider / Phoenix",
        "11–15 Raids": "Buddha / Portal",
        "16–20 Raids": "Rumble / Blizzard",
        "21–25 Raids": "T-Rex",
        "26–30 Raids": "Dough / Venom",
        "30+ Raids": "Gas / Yeti / Kitsune"
    },
    "🔥 Advanced Raid Pricing": {
        "1 Advanced Raid": "Buddha / Portal",
        "2 Advanced Raids": "blizzard",
        "3 Advanced Raids": "venom",
        "4 Advanced Raids": "dough",
        "5 Advanced Raids": "Mammoth/spirit",
        "6 Advanced Raids": "rumble",
        "7 Advanced Raids": "Control",
        "8 Advanced Raids": "T-Rex",
        "9 Advanced Raids": "Dough",
        "10 Advanced Raids": "Gas / Leopard"
    }
}

TRIALS = {
    "Prehistoric Island (Draco V4)": {
        "Trial 1 (Single Trial)": "Dough or T-Rex",
        "Trial 2 (Two Trials)": "x2 Dough or x2 T-Rex",
        "Trial 3 (Three Trials)": "Leo or Gas",
        "Full Draco V4 Awakening (All 4 Trials)": "Kitsune or x2 Leo or x2 Gas or Yeti"
    },
    "Race Trial Packages (Awaken V4)": {
        "Trial 1 (Single Trial)": "buddha or portal",
        "Trial 2 (Two Trials)": "trex",
        "Trial 3 (Three Trials)": "Dough",
        "Full V4 Awakening (All 4 Trials)": "gas rumble for race trial"
    }
}


@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    await bot.tree.sync()


@bot.event
async def on_message(message):
    # Check if a new ticket channel is created
    if message.type == discord.MessageType.channel_name_change:
        # Check if it's a ticket channel (you can customize this check)
        if "ticket" in message.channel.name.lower():
            embed = discord.Embed(
                title="📋 Welcome to your ticket!",
                description="Use the commands below to see our services and pricing:",
                color=discord.Color.blue()
            )
            embed.add_field(name="/raids", value="View Raid Services pricing", inline=False)
            embed.add_field(name="/trials", value="View Trial Packages pricing", inline=False)
            embed.add_field(name="/raging-demon", value="View Raging Demon pricing", inline=False)
            embed.set_footer(text="Choose a command above to see pricing details!")

            await message.channel.send(embed=embed)


@bot.event
async def on_guild_channel_create(channel):
    # When a new ticket channel is created, send welcome message
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

        await channel.send(embed=embed)


@discord.app_commands.command(name="raids", description="View Raid Services pricing")
async def raids(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 Raid Services Available 🔥",
        description="✅ Fast Clears ✅ Fragment Farming ✅ Trusted Service ✅ Host Available if Needed",
        color=discord.Color.red()
    )

    for category, pricing in RAIDS.items():
        embed.add_field(name=category, value="", inline=False)
        for raids, reward in pricing.items():
            embed.add_field(name=f"⚔️ {raids}", value=reward, inline=False)

    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)


@discord.app_commands.command(name="trials", description="View Trial Packages pricing")
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

    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)


@discord.app_commands.command(name="raging-demon", description="View Raging Demon pricing")
async def raging_demon(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚡ Raging Demon",
        description="Pricing based on fruit values",
        color=discord.Color.purple()
    )

    embed.add_field(name="💰 Pricing", value="Fruits valued 20M in total or single fruit", inline=False)
    embed.add_field(name="📍 Fruit Values", value="Check values at: https://fantasyblox.com/games/blox-fruits/values",
                    inline=False)

    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

import os
token = os.getenv('TOKEN')
if not token:
   token = 'YOUR_TOKEN_HERE'
bot.run(token)
