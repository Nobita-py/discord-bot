import discord
from discord.ext import commands
import os

# Proper intents setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

RAIDS = {
    "🔱 RAIDS": {
        "5 Raids": "Buddha",
        "10 Raids": "Dough",
        "15 Raids": "Dough + Buddha",
        "20 Raids": "Gas",
        "25 Raids": "Gas + T-Rex",
        "30 Raids": "Gas + 40M",
        "50 Raids": "Torment or Tiger + Gas",
        "100 Raids": "Green or Kitsune",
        "200 Raids": "Divine Portal+ or Dragon East"
    }
}

ADVANCED_RAIDS = {
    "1 Raid": "T-Rex",
    "2 Raids": "Dough",
    "3 Raids": "Dough + Buddha",
    "4 Raids": "Gas",
    "Max": "Tiger"
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

V4_TRIALS = {
    "1 Trial": "T-Rex",
    "2 Trials": "Dough",
    "3 Trials": "Dough + Buddha",
    "4 Trials": "Gas",
    "MAX": "Gas + T-Rex"
}

SEA_EVENTS_LEVI = {
    "1 Levi": "Gas + T-Rex",
    "2 Levi": "Tiger or Yeti",
    "3 Levi": "Kitsune",
    "4 Levi": "Divine Portal",
    "5 Levi": "Dragon East"
}

FIGHTING_STYLES = {
    "Sanguine Art": "Kitsune",
    "God Human": "Control / Tiger + Gas",
    "Other Styles & V2s": "Custom Price - Contact Staff Team"
}

BOSSES = {
    "Dark Beard": "Gas",
    "Indra": "Gas",
    "Dough King": "Gas",
    "Cake Prince": "Dough",
    "Soul Reaper": "Dough",
    "Tyrant of the Sky": "Dough"
}

BELI_WITHOUT_2X = {
    "5 Million": "Dough + T-Rex",
    "10 Million": "Gas + Dough",
    "15 Million": "Lightning + Gas",
    "20 Million": "Tiger or Yeti",
    "25 Million": "Kitsune",
    "50 Million": "Divine Portal",
    "100 Million": "East Dragon",
    "500 Million": "Perm Gas or above",
    "1 Billion": "Perm Dragon"
}

BELI_WITH_2X = {
    "5 Million": "T-Rex",
    "10 Million": "T-Rex + Dough",
    "15 Million": "Lightning + T-Rex",
    "20 Million": "Gas + T-Rex",
    "25 Million": "Tiger + Yeti",
    "50 Million": "Kitsune + Tiger",
    "100 Million": "Divine Portal",
    "500 Million": "East Dragon",
    "1 Billion": "Perm Gas"
}

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')
    try:
        synced = await bot.tree.sync()
        print(f'✅ Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'❌ Failed to sync: {e}')

@bot.event
async def on_guild_channel_create(channel):
    if "ticket" in channel.name.lower():
        embed = discord.Embed(
            title="📋 Welcome to your ticket!",
            description="Use the commands below to see our services and pricing:",
            color=discord.Color.blue()
        )
        embed.add_field(name="/raids", value="View Raids pricing", inline=False)
        embed.add_field(name="/advance-raid", value="View Advanced Raid pricing", inline=False)
        embed.add_field(name="/trials", value="View Trial Packages pricing", inline=False)
        embed.add_field(name="/sea-events", value="View Sea Events pricing", inline=False)
        embed.add_field(name="/weapon-acquiring", value="View Weapon Acquiring pricing", inline=False)
        embed.add_field(name="/fighting-styles", value="View Fighting Styles pricing", inline=False)
        embed.add_field(name="/bosses", value="View Bosses pricing", inline=False)
        embed.add_field(name="/races", value="View Races pricing", inline=False)
        embed.add_field(name="/raging-demon", value="View Raging Demon pricing", inline=False)
        embed.add_field(name="/beli", value="View BELI Grinding pricing", inline=False)
        embed.set_footer(text="Choose a command above to see pricing details!")
        try:
            await channel.send(embed=embed)
        except:
            pass

@bot.tree.command(name="raids")
async def raids(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔱 RAIDS",
        description="✅ Fast Clears ✅ Fragment Farming ✅ Trusted Service ✅ Host Available if Needed",
        color=discord.Color.red()
    )
    
    for category, pricing in RAIDS.items():
        embed.add_field(name=category, value="", inline=False)
        for raid_tier, reward in pricing.items():
            embed.add_field(name=f"⚔️ {raid_tier}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="advance-raid")
async def advance_raid(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚔️ ADVANCED RAID SERVICE",
        description="Premium raid service with guaranteed rewards",
        color=discord.Color.orange()
    )
    
    embed.add_field(name="Pricing", value="", inline=False)
    for raid_level, reward in ADVANCED_RAIDS.items():
        embed.add_field(name=f"🎯 {raid_level}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="trials")
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

@bot.tree.command(name="v4-trials")
async def v4_trials(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🏯 V4 TRIALS",
        description="Fast and reliable V4 Trial service",
        color=discord.Color.blue()
    )
    
    embed.add_field(name="Pricing", value="", inline=False)
    for trial_name, reward in V4_TRIALS.items():
        embed.add_field(name=f"🔱 {trial_name}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="sea-events")
async def sea_events(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌊 SEA EVENTS",
        description="Premium sea event services",
        color=discord.Color.teal()
    )
    
    embed.add_field(name="🐉 LEVI", value="", inline=False)
    for levi_level, reward in SEA_EVENTS_LEVI.items():
        embed.add_field(name=f"⚓ {levi_level}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="weapon-acquiring")
async def weapon_acquiring(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚔️ WEAPON ACQUIRING",
        description="Get powerful weapons fast!",
        color=discord.Color.from_rgb(200, 100, 0)
    )
    
    # GUNS Section
    embed.add_field(name="🔫 GUNS - IF NOT MATERIALS", value="", inline=False)
    embed.add_field(name="Soul Guitar", value="Gas + Dough", inline=False)
    embed.add_field(name="Dragon Storm", value="Gas + Dough", inline=False)
    
    embed.add_field(name="🔫 GUNS - IF MATERIALS", value="", inline=False)
    embed.add_field(name="Soul Guitar", value="Dough", inline=False)
    embed.add_field(name="Dragon Storm", value="Custom depending on belt progress", inline=False)
    
    # SWORDS Section
    embed.add_field(name="⚔️ SWORDS", value="", inline=False)
    embed.add_field(name="Yama", value="T-Rex", inline=False)
    embed.add_field(name="Tushita", value="Gas", inline=False)
    embed.add_field(name="TTK Swords", value="Gas per sword", inline=False)
    embed.add_field(name="TTK Full (From Start)", value="Tiger / Yeti / Control + T-Rex", inline=False)
    embed.add_field(name="Shark Anchor", value="Lightning (if no materials)", inline=False)
    embed.add_field(name="Dragon Heart", value="Dough + T-Rex", inline=False)
    embed.add_field(name="Fox Lamp", value="Kitsune (10 Kitshrine attempts)", inline=False)
    embed.add_field(name="CDK", value="Custom according to progress", inline=False)
    embed.add_field(name="Tushita & Yama", value="Dough per trial", inline=False)
    embed.add_field(name="Darkblade V3", value="Kitsune", inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="fighting-styles")
async def fighting_styles(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌀 FIGHTING STYLES",
        description="Master powerful combat techniques!",
        color=discord.Color.from_rgb(255, 100, 200)
    )
    
    embed.add_field(name="Pricing", value="", inline=False)
    for style_name, reward in FIGHTING_STYLES.items():
        embed.add_field(name=f"💥 {style_name}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="bosses")
async def bosses(interaction: discord.Interaction):
    embed = discord.Embed(
        title="👹 BOSSES",
        description="Defeat powerful bosses and earn rewards!",
        color=discord.Color.dark_red()
    )
    
    embed.add_field(name="Pricing", value="", inline=False)
    for boss_name, reward in BOSSES.items():
        embed.add_field(name=f"⚔️ {boss_name}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="races")
async def races(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🏃 RACES",
        description="Awaken your race and become powerful!",
        color=discord.Color.from_rgb(100, 200, 255)
    )
    
    # V1 Section
    embed.add_field(name="🔷 V1 AWAKENING", value="", inline=False)
    embed.add_field(name="Ghoul", value="Lightning", inline=False)
    embed.add_field(name="Cyborg", value="Lightning", inline=False)
    embed.add_field(name="Draco", value="Lightning + Dough (from base belts)", inline=False)
    
    # V2 Section
    embed.add_field(name="🔶 V2 AWAKENING", value="", inline=False)
    embed.add_field(name="Draco", value="Dough", inline=False)
    embed.add_field(name="All Other Races", value="T-Rex", inline=False)
    
    # V3 Section
    embed.add_field(name="🟡 V3 AWAKENING", value="", inline=False)
    embed.add_field(name="Draco", value="Dough", inline=False)
    embed.add_field(name="Ghoul", value="T-Rex", inline=False)
    embed.add_field(name="All Other Races", value="Buddha", inline=False)
    
    # Special
    embed.add_field(name="⚡ SPECIAL", value="", inline=False)
    embed.add_field(name="Mirage + Blue Gear", value="Gas", inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="raging-demon")
async def raging_demon(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚡ Raging Demon",
        description="Pricing based on fruit values",
        color=discord.Color.purple()
    )
    
    embed.add_field(name="💰 Pricing", value="x2 Portal (24M) or equivalent fruits", inline=False)
    embed.add_field(name="📍 Examples", value="Dough (30M) / Buddha (12M) + Portal (12M) / T-Rex (20M) + Love (1.2M) + Quake (1M)", inline=False)
    embed.add_field(name="📍 Fruit Values", value="Check: https://fantasyblox.com/games/blox-fruits/values", inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="first-of-darkness")
async def first_of_darkness(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌑 First of Darkness Services",
        description="Premium dungeon services",
        color=discord.Color.from_rgb(50, 50, 50)
    )
    
    embed.add_field(name="💰 Pricing", value="", inline=False)
    embed.add_field(name="🐉 Black Beard", value="50M", inline=False)
    embed.add_field(name="🤖 Cyborg", value="250M", inline=False)
    embed.add_field(name="⚫ DB V3", value="450M", inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="beli")
async def beli(interaction: discord.Interaction):
    embed = discord.Embed(
        title="💰 BELI - Money Grinding Service",
        description="Earn big money fast!",
        color=discord.Color.gold()
    )
    
    embed.add_field(name="WITHOUT 2X 💸 MONEY", value="", inline=False)
    for amount, reward in BELI_WITHOUT_2X.items():
        embed.add_field(name=f"💵 {amount}", value=reward, inline=False)
    
    embed.add_field(name="WITH 2X 💵 MONEY", value="", inline=False)
    for amount, reward in BELI_WITH_2X.items():
        embed.add_field(name=f"💰 {amount}", value=reward, inline=False)
    
    embed.set_footer(text="🎟️ Open a ticket to order")
    await interaction.response.send_message(embed=embed)

token = os.getenv('DISCORD_TOKEN')
if not token:
    print("ERROR: DISCORD_TOKEN not set!")
    exit(1)

bot.run(token)
