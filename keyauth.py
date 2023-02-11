#  https://github.com/Zempex

import os, requests, discord, time, random, string, re
from discord.ext import commands
from datetime import datetime
from discord.ext import commands
from discord import Embed, Member
from discord.utils import get
from typing import Optional

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT


prefix = "!" # replace with your prefix.
token = "" # replace with your discord bot token. for more information how you can create a token: https://discordpy.readthedocs.io/en/stable/discord.html
version = "V1.0"  # no need replace.
logschannid = "" # replace with your channel ID
sellerkey = "" #replace with your keyauth sellerkey
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
keyssss = {}
@bot.event
async def on_ready():      
	print("Bot Is Online !")
	print(f"Bot Username: {bot.user}")
	print(f"Bot ID: {bot.user.id}")
	bot.launch_time = datetime.utcnow()
	await bot.change_presence(status=discord.Status.online,activity=discord.Game(f"Prefix: {prefix} | Developer: Zempex#9999"))

@bot.group(invoke_without_command=True)
async def help(ctx):
	embed= discord.Embed(title="**Help**", description="List of commands")
	embed.add_field(name="**General**", value="!help General")
	embed.add_field(name="**Moderation**", value="!help Moderator")
	embed.add_field(name="**Auth**", value="!help Auth")
	await ctx.send(embed=embed)

@help.command()
async def General(ctx):
	embed= discord.Embed(title="**General**", description="List of General commands")
	embed.add_field(name="Commands", value="`:white_small_square: ping: **Return Bot Ping** \n:white_small_square: server: **Return Server Info** \n:white_small_square: botinfo: **Resturn Bot Info** \n:white_small_square: user <@user>: **Return User Info** \n:white_small_square: help: **Return Help Menu**\n:white_small_square: claim <serial>: **Claim + Create Account**\n:white_small_square: ut: **Bot Uptimw**\n:white_small_square: si: **Server Info**``")
	await ctx.author.send(embed=embed)
	await ctx.send(embed=discord.Embed(title="**Avilable Commands!**",description=f"{ctx.author.mention}, We sent  the avilable commands to your ``DM!``",colour=0x42F56C))

@help.command()
async def Moderator(ctx):
	embed= discord.Embed(title="**Moderator**", description="List of Moderator commands")
	embed.add_field(name="Commands", value=":white_small_square: warn <@user> <reason>: **Warn User** \n:white_small_square: kick <@user> <reason>: **Kick User** \n:white_small_square: ban <@user> <reason>: **Ban User** \n:white_small_square: unban <@user> <reason>: **Unban User** \n:white_small_square: cooldown <sec>: **Cooldown Channel**\n:white_small_square: clear <limit>: **Clear Channel**\n:white_small_square: modnickname <@user> <nick>: **Change User Nickname**\n:white_small_square: resetnickname <@user>: **Reset User Nickname**")
	await ctx.author.send(embed=embed)
	await ctx.send(embed=discord.Embed(title="**Avilable Commands!**",description=f"{ctx.author.mention}, We sent  the avilable commands to your ``DM!``",colour=0x42F56C))

@help.command()
async def Auth(ctx):
	embed= discord.Embed(title="**Auth**", description="List of Auth commands")
	embed.add_field(name="Commands", value=":white_small_square: reset <username> <reason>: **Reset Username** \n:white_small_square: deleteuser <username> <reason>: **Delete Username** \n:white_small_square: banaccount <username> <reason>: **Ban Account** \n:white_small_square: unbanaccount <username> <reason>: **Unban Account** \n:white_small_square: deletelicense <license>: **Delete License**\n:white_small_square: extend <username> <sub> <days>: **Extend Account Period**\n:white_small_square: blacklist <ip/hwid/username> <reason>: **Blacklist Account**\n:white_small_square: unblacklist <ip/hwid/username> <reason>: **Unblacklist Account**\n:white_small_square: accountinfo <username>: **Return Account Info**")
	await ctx.author.send(embed=embed)
	await ctx.send(embed=discord.Embed(title="**Avilable Commands!**",description=f"{ctx.author.mention}, We sent  the avilable commands to your ``DM!``",colour=0x42F56C))



@bot.event
async def on_command_error(ctx,error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(embed=discord.Embed(title="**Command Failure**",description=f"{ctx.author.mention}, Unknown commands you can do `!help` for all commands!",colour=0xE74C3C))
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(embed=discord.Embed(title="**Command Failure**",description=f"{ctx.author.mention}, Command Missing Argument!",colour=0xE74C3C))
	print(error)

@bot.command()
@commands.has_permissions(kick_members=True) 
async def kick(ctx, member: discord.Member, *, reason=None):
	try:
		await member.kick(reason=reason)
		embed=discord.Embed(title="**Moderation: User was Kicked**",description=f"{member}, Has been Kicked from Zempex Server.\nReason is `{reason}`. This Kick was requested from\n{ctx.author.mention}",colour=0x42F56C)
		embed.add_field(name="Expiration:", value=f"``Permantly``", inline=True)
		embed.add_field(name="Kicked By:", value=f"``{ctx.author}``", inline=True)
		await ctx.send(embed=embed)
		logs_channel = bot.get_channel(int(logschannid))
		await logs_channel.send(embed=embed)
	except Exception as e:
		await ctx.send(f"Failed to kick: {e}  ")

@bot.command()
@commands.has_permissions(ban_members=True) 
async def ban(ctx, member: discord.Member, *, reason=None):
	try:
		await member.ban(reason=reason)
		embed=discord.Embed(title="**Moderation: User was Banned**",description=f"{member}, Has been banned from Zempex Server.\nReason is `{reason}`. This ban was requested from\n{ctx.author.mention}",colour=0x42F56C)
		embed.add_field(name="Expiration:", value=f"``Permantly``", inline=True)
		embed.add_field(name="Banned By:", value=f"``{ctx.author}``", inline=True)
		await ctx.send(embed=embed)
		logs_channel = bot.get_channel(int(logschannid))
		await logs_channel.send(embed=embed)
	except Exception as e:
		await ctx.send(f"Failed to ban: {e}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def cooldown(ctx, seconds:int):
	await ctx.channel.edit(slowmode_delay=seconds)
	await ctx.send(embed=discord.Embed(title=":hourglass_flowing_sand: SlowMode!",description=f"SlowMode Is {seconds} in {ctx.channel.mention}",colour=0x42F56C))
	logs_channel = bot.get_channel(int(logschannid))
	await logs_channel.send(embed=discord.Embed(title=":hourglass_flowing_sand: SlowMode!",description=f"SlowMode Is {seconds} in {ctx.channel.mention}",colour=0x42F56C))

@bot.command()
@commands.has_permissions(ban_members=True) 
async def unban(ctx, username,*, reason=None):
	banlist = await ctx.guild.bans()
	user = None
	for ban in banlist:
		if ban.user.name == username:
			user = ban.user
	await ctx.guild.unban(user,reason=reason)
	embed=discord.Embed(title="**Moderation: User was Unbanned**",description=f"{user}, Has been Unbanned from Zempex Server.\nReason is `{reason}`. This Unban was requested from\n{ctx.author.mention}",colour=0x42F56C)
	embed.add_field(name="UnBanned By:", value=f"``{ctx.author}``", inline=True)
	await ctx.send(embed=embed)
	logs_channel = bot.get_channel(int(logschannid))
	await logs_channel.send(embed=embed)
	
	
@bot.command()
async def ping(ctx):
	await ctx.message.delete()
	await ctx.send(embed=discord.Embed(title=":ping_pong: Pong!",description=f"The bot latency is {round(bot.latency * 1000)}ms.",colour=0x42F56C))

@bot.command(aliases=['purge','clear','cls'])
@commands.has_permissions(manage_messages=True)
async def clean(ctx,tot:int):
	if tot == 0:
		await ctx.send("Please specify the number of messages you want to delete!")
	elif tot <= 0:
		await ctx.send("The number must be bigger than 0!")
	else:
		await ctx.channel.purge(limit=tot + 1)

@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, member: discord.Member, nick=None):
	await member.edit(nick=nick)
	await ctx.send(f'Nickname was changed to {nick}')
	await ctx.send(embed=discord.Embed(title=":robot: Nickname!",description=f'Nickname was changed to {nick}',colour=0x42F56C))
	

@bot.command()
async def botinfo(ctx):
	members = 0
	for guild in bot.guilds:
		members += guild.member_count - 1
	embed=discord.Embed(title="**Discord Bot Information**",colour=0x42F56C)
	embed.add_field(name="**Discord Name:**", value=f"``{bot.user}``", inline=True)
	embed.add_field(name="**Discord ID:**", value=f"``{bot.user.id}``", inline=True)
	embed.add_field(name="**Bot Created:**", value=f"``{bot.user.created_at}``", inline=True)
	embed.add_field(name="**Server Count:**", value=f"``{len(bot.guilds)}``", inline=True)
	embed.add_field(name="**Total Members From All Servers:**", value=f"``{members}``", inline=True)
	embed.add_field(name="Bot Status:", value=f"``🟢 Online | 💙 Version: {version}``", inline=True)
	embed.add_field(name="Developer", value=f"``Zempex#9492``", inline=True)
	await ctx.send(embed=embed)
	
@bot.command()
async def check_auth(ctx):
    try:
        response = requests.get('https://keyauth.win/')
        response_time = response.elapsed.total_seconds()
        if response.status_code == 200:
            website_status = "Website is working"
        else:
            website_status = f"Website is not working, status code: {response.status_code}"

        url2 = f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=getsettings&format=json"
        response2 = requests.get(url2)
        rq = response2.json()

        embed = discord.Embed(title="Keyauth Auth Status", color=0x42F56C)
        embed.add_field(name="Website", value=website_status)
        embed.add_field(name="Response Time", value=response_time)
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/111366720?s=200&v=4")
        await ctx.send(embed=embed)
    except:
        await ctx.send("An error occurred.")


@bot.command()
@commands.has_permissions(change_nickname=True)
async def resetnick(ctx, member: discord.Member, nick=None):
	await member.edit(nick=nick)
	await ctx.send(embed=discord.Embed(title=":robot: Nickname!",description=f'Nickname was changed to {nick}',colour=0x42F56C))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason=None):
	try:
		embed=discord.Embed(title="**Moderation: User was warned**",description=f"{member.mention}, has been warned from {ctx.author.mention} Reason is ``{reason}``.\nThis warn was requested from {ctx.author.mention}",colour=0x42F56C)
		embed.add_field(name="**Expiration:**", value=f"``Permantly``", inline=True)
		embed.add_field(name="**Warned By:**", value=f"``{ctx.author}``", inline=True)
		embed.set_footer(text=f"Requested From: {ctx.author}")
		await ctx.send(embed=embed)
		await member.send(embed=discord.Embed(title="**You Have Been Warned**",description=f"{member}, you been warned from {ctx.author.mention} Reason is ``{reason}``.\nThis warn was requested from {ctx.author}",colour=0x42F56C))
		logs_channel = bot.get_channel(int(logschannid))
		await logs_channel.send(embed=embed)
	except:
		await ctx.send(embed=discord.Embed(title="**You Have Been Warned**",description=f"{member}, you been warned from {ctx.author.mention} Reason is ``{reason}``.\nThis warn was requested from {ctx.author.mention}",colour=0x42F56C))
@bot.command()
async def claim(ctx,lic):
	global keyssss
	try:
		password = "".join(random.choice(string.ascii_letters+string.digits) for i in range(10))
		username = "".join(random.choice(string.ascii_letters+string.digits) for i in range(10))
		req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=activate&user={username}&key={lic}&pass={password}")
		if req.json()["success"] == True:
			expire = req.text.split('"expiry":"')[1].split('"')[0]
			expire = datetime.utcfromtimestamp(int(expire)).strftime('%Y-%m-%d %H:%M:%S')
			sub = keyssss[lic]
			keyssss.pop(lic)
			await ctx.send(embed=discord.Embed(title="**License Activated**",description=f"{ctx.author.mention}, Your **{sub}** key has been activated. Your Subscription expires: `{expire}`",colour=0x42F56C))
			embed=discord.Embed()
			embed.add_field(name="Username:", value=f"``{username}``", inline=True)
			embed.add_field(name="Password:", value=f"``{password}``", inline=True)
			embed.add_field(name="License:", value=f"``{lic}``", inline=True)
			embed.add_field(name="Claimed ID:", value=f"``{ctx.author} : {ctx.author.id}``", inline=True)
			embed.add_field(name="Expire:", value=f"``{expire}``", inline=True)
			await ctx.author.send(embed=embed)
			logs_channel = bot.get_channel(int(logschannid))
			await logs_channel.send(embed=discord.Embed(title="Key Redeemed", description=f"Redeemed by: {ctx.author}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nLicense Key: {lic}\nUsername: {username}", color=0x42F56C))
			
            
		else:
			await ctx.send(embed=discord.Embed(title="**Account creation failure!**",description=f"License is invalid, sent information to (DM)[{ctx.author.mention}]",colour=0xE74C3C))
			await ctx.author.send(req.json()["message"])
	except Exception as m:
		await ctx.send("Something Went Wrong!")
		await ctx.send(m)

@bot.command()
@commands.has_permissions(administrator = True)
async def resethwid(ctx,user,reason):
	role = discord.utils.get(ctx.guild.roles, name="[Perms] Reset") 
	if role not in ctx.author.roles:
		return
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=resetuser&user={user}")
	
	if req.json()["success"] == True:
		await ctx.send(embed=discord.Embed(title="**Reset Completed!**",description=f"Reset For User `{user}` was reset for reason `{reason}`",colour=0x42F56C))
		logs_channel = bot.get_channel(int(logschannid))
		await logs_channel.send(embed=discord.Embed(title="**Reset Completed!**",description=f"{ctx.author.mention}, Used Reset command for `{user}`  reset  reason `{reason}`",colour=0x42F56C))
	else:
		await ctx.send("Failed To Reset The User!")

@bot.command()
@commands.has_permissions(administrator = True)
async def deleteuser(ctx,user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=deluser&user={user}")
	if req.json()["success"] == True:
		await ctx.send(embed=discord.Embed(title="Username Deleted!",description='Succesfully Deleted User',colour=0x42F56C))
	else:
		await ctx.send("Failed To Delete The User!")

@bot.command()
@commands.has_permissions(administrator = True)
async def banaccount(ctx,user,*,reason=None):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=banuser&user={user}&reason={reason}")
	if req.json()["success"] == True:
		embed=discord.Embed(title="**Moderation: User was Banned**",description=f"{user}, Has been banned from Zempex Server.\nReason is `{reason}`. This ban was requested from\n{ctx.author.mention}",colour=0x42F56C)
		embed.add_field(name="Expiration:", value=f"``Permantly``", inline=True)
		embed.add_field(name="Banned By:", value=f"``{ctx.author}``", inline=True)
		await ctx.send(embed=embed)
		
	else:
		await ctx.send("Failed To Ban The User!")

@bot.command()
@commands.has_permissions(administrator = True)
async def unbanaccount(ctx,user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=unbanuser&user={user}")
	if req.json()["success"] == True:	
		embed=discord.Embed(title="**Moderation: User was unbanned**",description=f"{user}, Has been unbanned from Zempex Server.\nReason is `{reason}`. This Unban was requested from\n{ctx.author.mention}",colour=0x42F56C)
		embed.add_field(name="UnBanned By:", value=f"``{ctx.author}``", inline=True)
		await ctx.send(embed=embed)
	else:
		await ctx.send("Failed To unban The User!")

@bot.command()
async def deletelicense(ctx,lic):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=del&key={lic}")
	if req.json()["success"] == True:
		await ctx.send(embed=discord.Embed(title="Licnese Deleted!",description='Succesfully Deleted License',colour=0x42F56C))
	else:
		await ctx.send("Something went wrong.")

@bot.command()
@commands.has_permissions(administrator = True)
async def extend(ctx,user,sub,days):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=extend&user={user}&sub={sub}&expiry={days}")
	print(req.text)
	if req.json()["success"] == True:
		await ctx.send(embed=discord.Embed(title="Extended!",description='Succesfully Extended User',colour=0x42F56C))
	else:
		await ctx.send("Failed To Extend The User!")

@bot.command()
@commands.has_permissions(administrator = True)
async def blacklist(ctx,inputofuser):
	role = discord.utils.get(ctx.guild.roles, name="[Perms] Control") 
	if role not in ctx.author.roles:
		return
	if len(inputofuser) == 44:
		oii = f"hwid={inputofuser}"
	else:
		oii = f"ip={inputofuser}"
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=black&{oii}")
	if req.json()["success"] == True:
		await ctx.send(embed=discord.Embed(title="**Succesfully BlackListed!**",description=f"{ctx.author.mention}, Added {inputofuser} To Blacklist",colour=0x42F56C))
	
		await logs_channel.send(embed=discord.Embed(title="**Succesfully BlackListed!**",description=f"{ctx.author.mention}, Added {inputofuser} To Blacklist",colour=0x42F56C))
		
	else:
		await ctx.send(embed=discord.Embed(title="**Failure BlackListed!**",description=f"{ctx.author.mention}, Cannot Blacklist!",colour=0xE74C3C))

@bot.command()
@commands.has_permissions(administrator = True)
async def unblacklist(ctx,inputofuser):
	role = discord.utils.get(ctx.guild.roles, name="[Perms] Control") 
	if role not in ctx.author.roles:
		return
	if len(inputofuser) == 44:
		oii = f"hwid={inputofuser}"
	else:
		oii = f"ip={inputofuser}"
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=delblack&{oii}")
	if req.json()["success"] == True:
		await ctx.send(embed=discord.Embed(title="**Succesfully UnBlackListed!**",description=f"{ctx.author.mention}, Unblacklisted {inputofuser}",colour=0x42F56C))
		logs_channel = bot.get_channel(int(logschannid))
		await logs_channel.send(embed=discord.Embed(title="**Succesfully UnBlackListed!**",description=f"{ctx.author.mention}, Unblacklisted {inputofuser}",colour=0x42F56C))
	else:
		await ctx.send(embed=discord.Embed(title="**Failure UnBlackList!**",description=f"{ctx.author.mention}, something went wrong",colour=0xE74C3C))
																													


@bot.command()
@commands.has_permissions(administrator = True)
async def gen(ctx,day:int):
	global keyssss
	role = discord.utils.get(ctx.guild.roles, name="[Perms] Generator") 
	if role not in ctx.author.roles:
		return
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=add&expiry={day}&mask=XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX&level=1&amount=1&format=json")
	if req.json()["success"] == True:
		if day == 1:
			sub = "daily"
		elif day == 7:
			sub = "weekly"
		elif day == 30:
			sub = "monthly"
		elif day == 365:
			sub = "yearly"
		else:
			sub = "lifetime"
		key = req.json()["key"]
		keyssss[key] = sub
		await ctx.send(embed=discord.Embed(title="**Key Generated**",description=f"{ctx.author.mention}, We Sent You `1` of `{sub}_subscripton` via your DM",colour=0x42F56C))
		await ctx.author.send(embed=discord.Embed(title="**Key Generated**",description=f"Your Key: `{key}`",colour=0x42F56C))
		logs_channel = bot.get_channel(int(logschannid))
		await logs_channel.send(embed=discord.Embed(title="**Key Generated**",description=f"{ctx.author.mention}, Generated `1` of `{sub}_subscripton` ",colour=0x42F56C))
	else:
		await ctx.send("Failed To Gen The Key!")

@bot.command()
@commands.has_permissions(administrator = True)
async def accountinfo(ctx,user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=userdata&user={user}")
	if req.json()["success"] == True:
		ip = req.text.split('ip":"')[1].split('"')[0]
		hwid = req.text.split('hwid":"')[1].split('"')[0]
		lastlogin = req.text.split('"lastlogin":"')[1].split('","')[0]
		lastlogin = datetime.utcfromtimestamp(int(lastlogin)).strftime('%Y-%m-%d %H:%M:%S')
		creation = req.text.split('"createdate":"')[1].split('","')[0]
		creation = datetime.utcfromtimestamp(int(creation)).strftime('%Y-%m-%d %H:%M:%S')
		embed = discord.Embed()
		embed.add_field(name = f"Username Info: ", value = f":white_small_square: Username: **{user}** \n:white_small_square: IP: **{ip}** \n:white_small_square: HWID: **{hwid}** \n:white_small_square: Last Login: **{lastlogin}** \n:white_small_square: Creation: **{creation}**")
		await ctx.author.send(embed=embed)
		await ctx.send(embed=discord.Embed(title="**Account Info**",description=f"{ctx.author.mention}, Info Was Sent To Your DM",colour=0x42F56C))
		
	else:
		await ctx.send("Something Went Wrong!")


@bot.command(name="uptime", aliases=["ut"])
async def uptime(ctx):
	delta_uptime = datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	await ctx.send(embed=discord.Embed(title=":hourglass_flowing_sand: Uptime !",description=f"**{days}** day, **{hours}** hours, **{minutes}** minutes and **{seconds}** seconds"))

@bot.command(name="avatar", aliases=["av"])
async def avatar(ctx,member:discord.Member=None):
	if member is None:
		member = ctx.author
	await ctx.send(member.avatar_url)
	
@bot.command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
async def server_info(ctx):
	embed = discord.Embed()
	text_channels = len(ctx.guild.text_channels)
	voice_channels = len(ctx.guild.voice_channels)
	categories = len(ctx.guild.categories)
	inv = len(await ctx.guild.invites())
	channels = text_channels + voice_channels
	embed.set_thumbnail(url = str(ctx.guild.icon_url))
	embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime('%a, %d %b %Y | %H:%M:%S %ZGMT')}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Roles **{len(ctx.guild.roles)}** \n:white_small_square: Invites **{inv}** \n:white_small_square: Splash: **{ctx.guild.splash}**")
	await ctx.send(embed=embed)

@bot.command(name="userinfo", aliases=["memberinfo", "ui", "mi","user"])
async def user_info(ctx,target:Optional[Member]):
	target = target or ctx.author
	print(target.desktop_status)
	embed = Embed(title="User information",colour=target.colour,timestamp=datetime.utcnow())
	embed.set_thumbnail(url=target.avatar_url)
	fields = [("Name",str(target),True),("ID",target.id,True),("Bot?",target.bot,True),("Top role",target.top_role.mention,True),("Status",str(target.status).title(),True),("Activity",f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}",True),("Created at",target.created_at.strftime("%d/%m/%Y %H:%M:%S"),True),("Joined at",target.joined_at.strftime("%d/%m/%Y %H:%M:%S"),True),("Boosted",bool(target.premium_since),True)]
	for name,value,inline in fields:
		embed.add_field(name=name,value=value,inline=inline)
	await ctx.send(embed=embed)
	
@bot.command()
@commands.has_permissions(administrator = True)
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    logs_channel = bot.get_channel(int(logschannid))
    await logs_channel.send(embed=discord.Embed(title="Bot Shut Down", description=f"Shut down by: {ctx.author}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", color=0x42F56C))
    await bot.close()	
	
bot.run(token)
