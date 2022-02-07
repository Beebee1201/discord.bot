import discord
import json
from discord.message import Message
import pyautogui
import time
import googletrans
from discord.channel import TextChannel
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext.commands.converter import TextChannelConverter


translator = googletrans.Translator()
islock = 0
DCmember = ['chi','bee','boyo','nini','siyu','duo','sana','yy','cyc','xray','shin']



bot = commands.Bot(command_prefix= '/')
cbot = discord.Client()


@bot.event
async def on_ready():
    print("---嘿嘿---")

async def on_message(msg):
    if msg.author.id == '727208984649531423':
        await msg.channel.send('kkk')

'''
@bot.event
async def on_message(self,msg):

'''
'''

@bot.event()
async def on_messge(msg):
    if msg.content == 'aaa':
         await msg.channel.send(bot.user.id)

    if msg.user.id == 727208984649531423:
        await msg.channel.send('@蜜蜂')
'''



@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command(pass_context=True)
async def myid(ctx):
    await ctx.send("{} is your id".format(ctx.message.author.id))

@bot.command()
async def member(ctx ,a:int,b:int):
    await ctx.send( )
    
@bot.command()
async def toe(ctx,*,t:str):
    embed=discord.Embed(color=0x61bf99)
    embed.add_field(name="from %s"%(ctx.message.author.name), value=translator.translate(t, dest='en').text, inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def toc(ctx,*,t:str):
    embed=discord.Embed(color=0x61bf99)
    embed.add_field(name="from %s"%(ctx.message.author.name), value=translator.translate(t, dest='zh-tw').text, inline=True)
    await ctx.send(embed=embed)



@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))



@bot.command()
async def call(ctx, member:str ,times = 1):
    if member == '@蜜蜂':
        await ctx.send('叫我主人幹嘛')
    else:
        if times > 5:
            await ctx.send('媽的叫那麼多次衝三小')
        else :
            for i in range(times):
                await ctx.send('{} 上線上線上線'.format(member))


@bot.command()
async def date(ctx):
    await ctx.send(time.asctime( time.localtime(time.time()) ))




@bot.command()
async def say(ctx,thing:str ,times = 1):
    await ctx.message.delete()
    for i in range(times):
        await ctx.send(thing)



'''
@bot.command()
async def lock(ctx,password):
    if password == 662992:
        if islock == 1:
            await ctx.send('已經上鎖了喔')
        else:
            islock = 1
            await ctx.send('鎖好了喔')
    else:
        
'''





@bot.command()
async def prt(ctx):

    run = {"run":'f'}
    with open("pokemon_run.json", mode="w" ) as file:
            json.dump(run, file)

    await ctx.send('截圖中...')
    pyautogui.press('printscreen')
    time.sleep(1)
    await ctx.send('圖片傳送中...')
    pyautogui.hotkey('ctrlleft','v')
    time.sleep(1)
    pyautogui.typewrite('\n')







@bot.command()
async def run(ctx,thing = 'f'):
    run = {"run":thing}

    if thing == 'f':
        with open("pokemon_run.json", mode="w" ) as file:
            json.dump(run, file)
        await ctx.send('停止刷等了喔')

    elif thing == 't':
        with open("pokemon_run.json", mode="w" ) as file:
            json.dump(run, file)
        await ctx.send('開始刷等了喔')

    else :
        await ctx.send('停止[蜜蜂]的刷等請輸入/run f,開始請輸入/run t')





@bot.command()
async def catch(ctx,thing):
    pyautogui.typewrite('p!c ')
    pyautogui.typewrite(thing)
    pyautogui.typewrite('\n')
    await ctx.send('抓到了嗎抓到了嗎')




#以下為among us 用


@bot.command()
async def add(ctx,score:int,member:str):
    with open("DCbot2.json", mode="r" ) as file:
        data = json.load(file)
        oldScore = 0
    memberName = ("%s"%(member))
    counterOfLoop = 0
    for i in data:
        if i['name'] == memberName:
            oldScore = int(i['score'])
            break
        counterOfLoop += 1
    data[counterOfLoop]['score'] = ("%d"%(oldScore + score))

    with open("DCbot2.json", mode="w" ) as file:
        json.dump(data, file)
    await ctx.send("{}的分數已更新至{}分".format(member,oldScore + score))




@bot.command()
async def set(ctx,score:int,member:str):
    with open("DCbot2.json", mode="r" ) as file:
        data = json.load(file)

    memberName = ("%s"%(member))
    counterOfLoop = 0

    for i in data:
        if i['name'] == memberName:
            break
        counterOfLoop += 1
    data[counterOfLoop]['score'] = ("%d"%(score))

    with open("DCbot2.json", mode="w" ) as file:
        json.dump(data, file)
    await ctx.send("{}的分數已更新至{}分".format(member,score))







@bot.command()
async def r(ctx):
    with open("DCbot2.json", mode="r" ) as file:
        data = json.load(file)

    membersScore = []
    membersName = []
    rankedScore = []

    for i in data:
        membersScore.append(i["score"])
        membersName.append(i["name"])
        rankedScore.append(i["score"])

    rankedName = []

    int_list = list(map(int, rankedScore))
    int_list.sort(reverse=True)
    rankedScore = int_list
    
    print(rankedScore)

    for i in rankedScore:
        counterOfLoop = 0
        for n in membersScore:
            if int(n) == i:
                rankedName.append(membersName[counterOfLoop])
                del membersScore[counterOfLoop]
                del membersName[counterOfLoop]
                print(i)
                print(n)
                break
            else:
                counterOfLoop += 1


    counterOfLoop = 0
    for i in rankedScore:
         await ctx.send('{}. {} : {}'.format(counterOfLoop+1,rankedName[counterOfLoop],rankedScore[counterOfLoop]))
         print('{}. {} : {}'.format(counterOfLoop+1,rankedName[counterOfLoop],rankedScore[counterOfLoop]))
         counterOfLoop += 1

bot.run('')
