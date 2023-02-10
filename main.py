
import yaml
import discord
import discord.ext

with open("config.yaml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

discord_token = config["discord_token"]

# setting up the bot
intents = discord.Intents.all() 
# if you don't want all intents you can do discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


# sync the slash command to your server
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1041020628012113971))
    # print "ready" in the console when the bot is ready to work
    print("ready")

# make the slash command
@tree.command(name="name", description="description", guild=discord.Object(id=1041020628012113971))
async def slash_command(int: discord.Interaction):    
    await int.response.send_message("command")
    
client.run(discord_token)
