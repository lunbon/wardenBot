from discord.ext import commands
import discord
import asyncio
import os

bot = commands.Bot(command_prefix="!")
token = os.environ["TOKEN"]
server_id = "417269196850987027"
role_id="469879370425827348"
admin_id = "440831065028820992"
channel_id = "417269196850987029"

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('-'*18)

async def check():
	await bot.wait_until_ready()
	server = bot.get_server(server_id)
	role = discord.utils.get(server.roles, id=role_id)
	admin = discord.utils.get(server.roles, id=admin_id)
	channel=server.get_channel(channel_id)
	while not bot.is_closed:
		for member in server.members:
			if str(member.status) is "offline":
				if role in member.roles:
					await bot.send_message(channel,admin.mention+' '
						+member.name+' is offline!')
		await asyncio.sleep(3600)

bot.loop.create_task(check())
bot.run(token)