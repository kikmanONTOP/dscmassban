import discord
from discord.ext import commands
from colorama import init, Fore

print(Fore.LIGHTCYAN_EX + '''

 .S_SsS_S.    .S_SSSs      sSSs    sSSs   .S_SSSs     .S_SSSs     .S_sSSs    
.SS~S*S~SS.  .SS~SSSSS    d%%SP   d%%SP  .SS~SSSSS   .SS~SSSSS   .SS~YS%%b   
S%S `Y' S%S  S%S   SSSS  d%S'    d%S'    S%S   SSSS  S%S   SSSS  S%S   `S%b  
S%S     S%S  S%S    S%S  S%|     S%|     S%S    S%S  S%S    S%S  S%S    S%S  
S%S     S%S  S%S SSSS%S  S&S     S&S     S%S SSSS%P  S%S SSSS%S  S%S    S&S  
S&S     S&S  S&S  SSS%S  Y&Ss    Y&Ss    S&S  SSSY   S&S  SSS%S  S&S    S&S  
S&S     S&S  S&S    S&S  `S&&S   `S&&S   S&S    S&S  S&S    S&S  S&S    S&S  
S&S     S&S  S&S    S&S    `S*S    `S*S  S&S    S&S  S&S    S&S  S&S    S&S  
S*S     S*S  S*S    S&S     l*S     l*S  S*S    S&S  S*S    S&S  S*S    S*S  
S*S     S*S  S*S    S*S    .S*P    .S*P  S*S    S*S  S*S    S*S  S*S    S*S  
S*S     S*S  S*S    S*S  sSS*S   sSS*S   S*S SSSSP   S*S    S*S  S*S    S*S  
SSS     S*S  SSS    S*S  YSS'    YSS'    S*S  SSY    SSS    S*S  S*S    SSS  
        SP          SP                   SP                 SP   SP          
        Y           Y                    Y                  Y    Y           
                                                                             ''')

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.MAGENTA + "discord bot token: ")
guild_id = input("server id: ")

@bot.event
async def on_ready():
    print(f"massban is ready as {bot.user}")

    
    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    
    for member in guild.members:
        if member == bot.user:
            continue

        try:
            await member.ban()
            print(Fore.YELLOW + f'banned {member.name}')
        except:
            print(f'banning error {member.name}')

bot.run(token)