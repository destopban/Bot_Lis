import discord
from discord import utils
from discord.ext import commands
import config
import json
import random
import datetime as dt
import pyautogui
from threading import *
import time


# from keep_alive import keep_alive

pyautogui.FAILSAFE = False
##########################################__SETTINGS__################################################################


symbol = "."
emoji_id = 863182729012707328
emoji_pp = f"<:newsord:{emoji_id}>"
event_info = ''

works_plus = [':white_check_mark: вы выграли турнир на faceit и получили ' + emoji_pp + ' {0}',
              ':white_check_mark: вы нашли сокровище в размере ' + emoji_pp + ' {0}',
              ':white_check_mark: Cтаc просто жирдяй(всёравно это никто не читает) ' + emoji_pp + ' {0}',
              ':white_check_mark: помог перейти бабушке дорогу и она дала вам ' + emoji_pp + ' {0}',
              ':white_check_mark: удачно вложился и получил ' + emoji_pp + ' {0}',
              ':white_check_mark: выпал крутой скин в CS:GO и продал его за ' + emoji_pp + ' {0}',
              ':white_check_mark: поддержка от правительства в размере ' + emoji_pp + ' {0}',
              ':white_check_mark: продал алмаз на jc за ' + emoji_pp + ' {0}']

slut_plus = [':white_check_mark: я не знаю, что вы сделали, но стасу приятно и вы получили' + emoji_pp + ' {0}',
             ':white_check_mark: вы сделали очень хороший boob-job за' + emoji_pp + ' {0}',

             ':white_check_mark: вам дали деньги со словами nice ass' + emoji_pp + ' {0}',
             ':white_check_mark: вы стали тестировщиком секс-игрушек и вы получили за это' + emoji_pp + ' {0}']

slut_minus = [':red_square: вы вступили в Gachimuchi Russian Community Club ♂ , но вам пришлось заплатить взнос в размере' + emoji_pp + ' {0}',
              ':red_square: кто прочитал это, тот лох ' + emoji_pp + ' {0}',
              ':red_square: вы купили крутую смазку за' + emoji_pp + ' {0}',
              ':red_square: вы пошли с мишей в бк, а он вас там изнасиловал и забрал у вас' + emoji_pp + ' {0}',
              ':red_square: вы Стас и вам отдали компьтер, но вы в первый же день забыли почистить историю браузера и вам пришлось потратить ' + emoji_pp + ' {0}, чтобы всё уладить',
              ':red_square: вы разорвали свой анус и вам пришлось делать операцию по зашиву за' + emoji_pp + ' {0}']

crime_plus = [':white_check_mark: ваша банда ограбила банк и вы получили вашу долю в размере' + emoji_pp + ' {0}',
              ':white_check_mark: ваша ферма марихуаны принесла вам' + emoji_pp + ' {0}',
              ':white_check_mark: ваш сайт в даркнете выстрельнул и вы продали больше марихуаны, этим заработали ' + emoji_pp + ' {0}',
              ':white_check_mark: вы наладили похишение и продажу детей в даркнете и вы получили с этого' + emoji_pp + ' {0}',
              ':white_check_mark: ваша подработка киллером принесла вам ' + emoji_pp + ' {0}']

crime_minus = [':red_square: на вас напал гопник и он отжал у вас телефон за' + emoji_pp + ' {0}',
               ':red_square: вы пытались украсть машину, но у вас не получилось и вы заплатили штраф в размере ' + emoji_pp + ' {0}',
               ':red_square: вас спалили как вы ищите заклатки и вы заплатили штрав в размере' + emoji_pp + ' {0}',
               ':red_square: ваш конкурент по продажи травы устроил налёт на одну из вашу ферм и вы понесли потери в размере' + emoji_pp + ' {0}']

works_max = 897
works_min = 40

slut_max = 10000
slut_min = -15000

crime_max = 15000
crime_min = -50000

slut_pause = dt.timedelta(hours=9, minutes=0, seconds=0)
works_pause = dt.timedelta(hours=10, minutes=0, seconds=0)
crime_pause = dt.timedelta(hours=9, minutes=0, seconds=0)

######################################################################################################################


with open('time_work.txt') as file:
    data = json.load(file)
    time_work = data

with open('shop.txt') as file:
    data = json.load(file)
    shop = data

with open('things.txt') as file:
    data = json.load(file)
    things = data

with open('time_slut.txt') as file:
    data = json.load(file)
    time_slut = data

with open('time_crime.txt') as file:
    data = json.load(file)
    time_crime = data

with open('datebase.txt') as file:
    data = json.load(file)
    db = data


def save():
    with open('datebase.txt', 'w') as file:
        json.dump(db, file)


def save_time():
    with open('time_work.txt', 'w') as file:
        json.dump(time_work, file)


def save_time_slut():
    with open('time_slut.txt', 'w') as file:
        json.dump(time_slut, file)


def save_time_crime():
    with open('time_crime.txt', 'w') as file:
        json.dump(time_slut, file)


def save_things():
    with open('things.txt', 'w') as file:
        json.dump(things, file)


def save_shop():
    with open('shop.txt', 'w') as file:
        json.dump(shop, file)


def num(n):
    a = str(n)
    p = ","
    if n > 0:
        if 4 <= len(a) < 7:
            return a[:-3] + p + a[-3:]
        elif len(a) >= 7:
            return a[:-6] + p + a[-6:-3] + p + a[-3:]
        else:
            return a
    else:
        if 5 <= len(a) < 8:
            return a[:-3] + p + a[-3:]
        elif len(a) >= 8:
            return a[:-6] + p + a[-6:-3] + p + a[-3:]
        else:
            return a


intents = discord.Intents.default()
client = commands.Bot(command_prefix=f"{symbol}", intents=intents)
client.remove_command("help")


@client.command(pass_context=True)
async def help(ctx):
    await ctx.send(f"список команд:"
                   f"```{symbol}m -команда которая показывает сколько у кого деняг```"
                   f"```{symbol}w -команда которая приносить от {works_min} до {works_max}```"
                   f"```{symbol}sl -команда которая приносить от {slut_min} до {slut_max}```"
                   f"```{symbol}s -команда которая позволяет отпраять деньги или вещи из магазина другому человеку```"
                   f"```{symbol}с -команда которая приносить от {crime_min} до {crime_max}```"
                   f"```{symbol}sh -команда которая показывает список предметов из магазина```"
                   f"```{symbol}b -команда с пмощью которой можно купить вещщи из магазина```"
                   f"```{symbol}t -команда которая показывает ваши вещи в инвентроре```"
                   f"```{symbol}d -команда с помощью котрой вы можите удалять предметы из своего инвенторя```"
                   f'чтобы узнать информацию про команду напишите```{symbol}<команда> <"-h", "-help", "h" или "help">``` ')


@client.command(pass_context=True)
async def h(ctx):
    await ctx.send(f"список команд:"
                   f"```{symbol}m -команда которая показывает сколько у кого деняг```"
                   f"```{symbol}w -команда которая приносить от {works_min} до {works_max}```"
                   f"```{symbol}sl -команда которая приносить от {slut_min} до {slut_max}```"
                   f"```{symbol}s -команда которая позволяет отпраять деньги или вещи из магазина другому человеку```"
                   f"```{symbol}с -команда которая приносить от {crime_min} до {crime_max}```"
                   f"```{symbol}sh -команда которая показывает список предметов из магазина```"
                   f"```{symbol}b -команда с пмощью которой можно купить вещщи из магазина```"
                   f"```{symbol}t -команда которая показывает ваши вещи в инвентроре```"
                   f"```{symbol}d -команда с помощью котрой вы можите удалять предметы из своего инвенторя```"
                   f'чтобы узнать информацию про команду напишите```{symbol}<команда> <"-h", "-help", "h" или "help">``` ')


@client.command(pass_context=True)
async def i(ctx):
    await ctx.send(event_info)


@client.command()
async def m(ctx, arg=None):
    if arg is None:
        if str(ctx.author.id) in db:
            await ctx.send(
                embed=discord.Embed(description=f"сейчас име"
                                                f"ет {emoji_pp} {num(db[str(ctx.author.id)])}", color=0x42aaff).set_author(name=f"{ctx.author.name}",
                                                                                                                           icon_url=ctx.author.avatar_url))
        else:
            db[str(ctx.author.id)] = 0
            await ctx.send(
                embed=discord.Embed(description=f"сейчас име"
                                                f"ет {emoji_pp} {0}", color=0x42aaff).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            save()
    elif arg == "-h" or arg == "-help" or arg == "h" or arg == "help":
        await ctx.send(
            embed=discord.Embed(description=f" эта команда показвает сколько у человека деняг:```{symbol}m <имя>``` или сколько у тебя деняг:```{symbol}m```", color=0x42aaff).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        _id = arg.strip("<@!>")
        a = await client.fetch_user(int(_id))
        if a is None:
            await ctx.send(
                embed=discord.Embed(description=f"нет такого человека под именем {arg}", color=0xFF2A00).set_author(
                    name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
        else:
            if _id in db:
                await ctx.send(
                    embed=discord.Embed(description=f"сейчас име"
                                                    f"ет {emoji_pp} {num(db[_id])}", color=0x42aaff).set_author(name=f"{a.name}", icon_url=a.avatar_url))
            else:
                db[_id] = 0
                await ctx.send(
                    embed=discord.Embed(description=f"сейчас име"
                                                    f"ет {emoji_pp} {db[_id]}", color=0x42aaff).set_author(name=f"{a.name}", icon_url=a.avatar_url))
                save()


@client.command()
async def w(ctx, arg=None):
    if arg is None:
        p = str(ctx.author.id)
        if p in time_work:
            timel = dt.datetime.strptime(time_work[p], "%Y-%m-%d %H:%M:%S.%f")
            timer = works_pause - (dt.datetime.now() - timel)
            if timer <= dt.timedelta(minutes=0):
                n = random.randint(works_min, works_max)
                await ctx.send(
                embed=discord.Embed(description=random.choice(works_plus).format(num(n)), color=0x4cbb17)
                    .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                if p in db:
                    db[p] += n
                else:
                    db[p] = n
                time_work[p] = str(dt.datetime.now())
                save()
                save_time()
            else:
                hours, remainder = divmod(timer.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                await ctx.send(
                    embed=discord.Embed(description=f" осталось {hours} часов и {minutes} минут" if hours > 1 else f" осталось {minutes} минут и {seconds} секунд", color=0x42aaff)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                # await self.get_channel(message.channel.id).send(
                #     f"{message.author.mention} осталось {hours} часов и {minutes} минут" if hours > 1 else f"{message.author.mention} осталось {minutes} минут и {seconds} секунд")
        else:
            n = random.randint(works_min, works_max)
            await ctx.send(
                embed=discord.Embed(description=random.choice(works_plus).format(num(n)), color=0x4cbb17)
                    .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            if p in db:
                db[p] += n
            else:
                db[p] = n
            time_work[p] = str(dt.datetime.now())
            save()
            save_time()
    elif arg == "-h" or arg == "-help" or arg == "h" or arg == "help":
        await ctx.send(
            embed=discord.Embed(description=f" эта команда приносит тебе от {emoji_pp} {works_min} до {emoji_pp} {works_max}", color=0x42aaff).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        await ctx.send(
            embed=discord.Embed(description=f"немного не понятно", color=0xFF2A00).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))


@client.command()
async def sl(ctx, arg=None):
    if arg is None:
        p = str(ctx.author.id)
        if p in time_slut:
            timel = dt.datetime.strptime(time_slut[p], "%Y-%m-%d %H:%M:%S.%f")
            timer = slut_pause - (dt.datetime.now() - timel)
            if timer <= dt.timedelta(minutes=0):
                n = random.randint(slut_min, slut_max)
                if db[p] < 0:
                    n = random.randint(slut_min - (slut_min // 2), slut_max)
                if n >= 0:
                    await ctx.send(
                        embed=discord.Embed(description=random.choice(slut_plus).format(num(n)), color=0x4cbb17)
                            .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                else:
                    await ctx.send(
                        embed=discord.Embed(description=random.choice(slut_minus).format(num(n)), color=0xFF2A00)
                            .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                if p in db:
                    db[p] += n
                else:
                    db[p] = n
                time_slut[p] = str(dt.datetime.now())
                save()
                save_time()
            else:
                hours, remainder = divmod(timer.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                await ctx.send(
                    embed=discord.Embed(description=f" осталось {hours} часов и {minutes} минут" if hours > 1 else f" осталось {minutes} минут и {seconds} секунд", color=0x42aaff)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                # await ctx.send(
                #     f"{message.author.mention} осталось {hours} часов и {minutes} минут" if hours > 1 else f"{message.author.mention} осталось {minutes} минут и {seconds} секунд")
        else:
            n = random.randint(slut_min, slut_max)
            if db[p] < 0:
                n = random.randint(slut_min - (slut_min // 2), slut_max)
            if n >= 0:
                await ctx.send(
                    embed=discord.Embed(description=random.choice(slut_plus).format(num(n)), color=0x4cbb17)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            else:
                await ctx.send(
                    embed=discord.Embed(description=random.choice(slut_minus).format(num(n)), color=0xFF2A00)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            if p in db:
                db[p] += n
            else:
                db[p] = n
            time_slut[p] = str(dt.datetime.now())
            save()
            save_time()
    elif arg == "-h" or arg == "-help" or arg == "h" or arg == "help":
        await ctx.send(
            embed=discord.Embed(description=f" эта команда приносит тебе от {emoji_pp} {slut_min} до {emoji_pp} {slut_max}", color=0x42aaff).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        await ctx.send(
            embed=discord.Embed(description=f"немного не понятно", color=0x42aaff).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))


@client.command()
async def c(ctx, arg=None):
    if arg is None:
        p = str(ctx.author.id)
        if p in time_crime:
            timel = dt.datetime.strptime(time_crime[p], "%Y-%m-%d %H:%M:%S.%f")
            timer = crime_pause - (dt.datetime.now() - timel)
            if timer <= dt.timedelta(minutes=0):
                n = random.randint(crime_min, crime_max)
                if db[p] < 0:
                    n = random.randint(crime_min - (crime_min // 2), crime_max)
                if n >= 0:
                    await ctx.send(
                        embed=discord.Embed(description=random.choice(crime_plus).format(num(n)), color=0x4cbb17)
                            .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                else:
                    await ctx.send(
                        embed=discord.Embed(description=random.choice(crime_minus).format(num(n)), color=0xFF2A00)
                            .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                if p in db:
                    db[p] += n
                else:
                    db[p] = n
                time_crime[p] = str(dt.datetime.now())
                save()
                save_time()
            else:
                hours, remainder = divmod(timer.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                await ctx.send(
                    embed=discord.Embed(description=f" осталось {hours} часов и {minutes} минут" if hours > 1 else f" осталось {minutes} минут и {seconds} секунд", color=0x42aaff)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                # await ctx.send(
                #     f"{ctx.author.mention} осталось {hours} часов и {minutes} минут" if hours > 1 else f"{ctx.author.mention} осталось {minutes} минут и {seconds} секунд")
        else:
            n = random.randint(crime_min, crime_max)
            if db[p] < 0:
                n = random.randint(crime_min - (crime_min // 2), crime_max)
            if n >= 0:
                await ctx.send(
                    embed=discord.Embed(description=random.choice(crime_plus).format(num(n)), color=0x4cbb17)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            else:
                await ctx.send(
                    embed=discord.Embed(description=random.choice(crime_minus).format(num(n)), color=0xFF2A00)
                        .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            if p in db:
                db[p] += n
            else:
                db[p] = n
            time_crime[p] = str(dt.datetime.now())
            save()
            save_time()
    elif arg == "-h" or arg == "-help" or arg == "h" or arg == "help":
        await ctx.send(
            embed=discord.Embed(description=f" эта криминальная команда приносит тебе от {emoji_pp} {crime_min} до {emoji_pp} {crime_max}", color=0x42aaff).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        await ctx.send(
            embed=discord.Embed(description=f"немного не понятно", color=0x42aaff).set_author(
                name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))


@client.command()
async def l(ctx, arg=None):
    if arg is None:
        h = sorted(db, key=lambda x: db[x], reverse=True)
        best = []
        nn = 1
        for i in h:
            best.append(f"**{nn}.{await client.fetch_user(int(i))}** • {emoji_pp}{num(db[i])}")
            nn += 1
        answ = ''
        for i in best:
            answ += i + "\n"
        await ctx.send(
            embed=discord.Embed(description=answ, color=0x42aaff)
                .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        await ctx.send(embed=discord.Embed(description="эта команда показывает все счета и сортирует их по количеству деняг", color=0x42aaff)
                       .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))


@client.command()
async def s(ctx, *args):
    if len(args) == 2:
        h = args
        p = str(ctx.author.id)
        user = h[-2].strip("<>@!")
        try:
            nuser = await client.fetch_user(user)
        except:
            await ctx.send(
                embed=discord.Embed(description="нет такого пользователя", color=0xFF2A00))
            return
        if h[-1].isnumeric():
            n = int(h[-1])

            if user == p:
                await ctx.send(
                    embed=discord.Embed(description="в чём прикол отправлять самому себе?", color=0xFF2A00))
            elif n <= 0:
                await ctx.send(
                    embed=discord.Embed(description="ты дебил, какой 0 ??", color=0xFF2A00))
                # await self.get_channel(message.channel.id).send(
                #     f"не надо всё ломать !!!")
            elif db[p] < n:
                await ctx.send(
                    embed=discord.Embed(description=f"недостаточно сордов, у вас только{emoji_pp}{num(db[p])}, а ", color=0xFF2A00).set_author(name=f"{ctx.author.name}",
                                                                                                                                               icon_url=ctx.author.avatar_url))
            elif nuser is None:
                await ctx.send(
                    embed=discord.Embed(description=f"нет такого пользователя", color=0xFF2A00).set_author(
                        name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            else:
                if p not in db:
                    db[p] = 0
                if user not in db:
                    db[user] = 0
                db[p] -= n
                db[user] += n
                await ctx.send(
                    embed=discord.Embed(description=f"перевёл {emoji_pp}{num(n)} на счёт {await client.fetch_user(int(user))}", color=0x42aaff).set_author(
                        name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                # await self.get_channel(message.channel.id).send(
                #     f"{message.author.mention} перевёл {self.get_emoji(emoji_id)}{n} на счёт {h[-2]}")
                save()
        else:
            if str(ctx.author.id) in things:
                user = args[-2].strip("<>@!")
                if args[-1] not in things[str(ctx.author.id)]:
                    await ctx.send(
                        embed=discord.Embed(description=f'у тебя отсутствует "{args[-1]}"', color=0xFF2A00).set_author(
                            name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                elif nuser is None:
                    await ctx.send(
                        embed=discord.Embed(description=f"нет такого пользователя", color=0xFF2A00).set_author(
                            name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                else:
                    if user not in things:
                        things[user] = [str(args[-1])]
                        things[str(ctx.author.id)].remove(args[-1])
                        save_things()
                    else:
                        things[user].append(args[-1])
                        things[str(ctx.author.id)].remove(args[-1])
                        save_things()
                    await ctx.send(
                        embed=discord.Embed(description=f'{ctx.author.mention} отправил {args[-2]} вещь под названием "{args[-1]}" ', color=0x42aaff).set_author(
                            name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
            else:
                things[str(ctx.author.id)] = []
                await ctx.send(
                    embed=discord.Embed(description=f'у тебя нету "{args[-1]}"', color=0xFF2A00).set_author(
                        name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))

    elif args[0] == "-h" or args[0] == "-help" or args[0] == "h" or args[0] == "help":
        await ctx.send(
            embed=discord.Embed(description=f"это команда нужна для того чтобы отправить кому-нибудь деняг или товар из магазина : ```{symbol}s <челове> <сумма или название предмета>```",
                                color=0x42aaff).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        await ctx.send(
            embed=discord.Embed(description=f"немного не понятно",
                                color=0xFF2A00).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))


@client.command()
async def sh(ctx, arg=None):
    if arg is None:
        answ = ""
        for n, i in enumerate(shop, 1):
            answ += f"**{n}.{i}** • {emoji_pp}{num(shop[i])}" + "\n"
        await ctx.send(
            embed=discord.Embed(description=answ, color=0x42aaff)
                .set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
    else:
        await ctx.send(embed=discord.Embed(description=f"команда с помощью котрой вы можите посмотреть список всех товаров из магазинов", color=0x42aaff).set_author(name="Магазин"))


@client.command()
async def d(ctx, arg=None):
    if arg is None or arg == "-help" or arg == "-h" or arg == "h" or arg == "help":
        await ctx.send(embed=discord.Embed(description=f"команда с помощью котрой вы можите удалять предметы из своего инвенторя: ```{symbol}d <название предмета>```", color=0x42aaff).set_author(
            name="Инвентарь"))
    else:
        if str(ctx.author.id) not in things:
            await ctx.send(embed=discord.Embed(description=f"у вас нет {arg}", color=0xFF2A00).set_author(
                name="Инвентарь"))
            things[str(ctx.author.id)] = []
            save_things()
        elif arg not in things[str(ctx.author.id)]:
            await ctx.send(embed=discord.Embed(description=f"у вас нет {arg}", color=0xFF2A00).set_author(
                name="Инвентарь"))
        else:
            things[str(ctx.author.id)].remove(arg)
            save_things()


@client.command()
async def b(ctx, arg=None):
    if arg is not None and arg != "-help" and arg != "-help":
        if arg not in shop:
            await ctx.send(
                embed=discord.Embed(description="такой вещи нет в магазине", color=0xFF2A00)
                    .set_author(name="Магазин"))
        elif shop[arg] > db[str(ctx.author.id)]:
            await ctx.send(
                embed=discord.Embed(description="у тебя не хватает деняг", color=0xFF2A00)
                    .set_author(name="Магазин"))
        else:
            if str(ctx.author.id) in things:
                things[str(ctx.author.id)].append(arg)
                db[str(ctx.author.id)] -= shop[arg]
                save_things()
                save()
                await ctx.send(
                    embed=discord.Embed(description=f'вы купили вешь из магазина под названием "{arg}"', color=0x42aaff).set_author(
                        name="Магазин"))
            else:
                things[str(ctx.author.id)] = [arg]
                db[str(ctx.author.id)] -= shop[arg]
                save_things()
                save()
                await ctx.send(
                    embed=discord.Embed(description=f'вы купили вешь из магазина под названием "{arg}"', color=0x42aaff).set_author(
                        name="Магазин"))
    elif arg == "-help" or arg == "-h" or arg == "h" or arg == "help":
        await ctx.send(
            embed=discord.Embed(description=f"команда которая показывает ве предметы в магазине и их цены, а купить их можно с помощью ```{symbol}b <название предмета>```", color=0x42aaff).set_author(
                name="Магазин"))
    else:
        await ctx.send(
            embed=discord.Embed(description=f"немного не понятно", color=0xFF2A00).set_author(
                name="Магазин"))


@client.command()
async def t(ctx, arg=None):
    if arg is None:
        if str(ctx.author.id) in things:
            answ = ""
            for n, i in enumerate(things[str(ctx.author.id)], 1):
                answ += f"**{n} . {i}**" + "\n"
            if answ == "":
                await ctx.send(
                    embed=discord.Embed(description=f"у вас нет вещей", color=0x42aaff).set_author(
                        name="Инвентарь"))
            else:
                await ctx.send(
                    embed=discord.Embed(description=answ, color=0x42aaff)
                        .set_author(name="Инвентарь"))
        else:
            things[str(ctx.author.id)] = []
            await ctx.send(
                embed=discord.Embed(description=f"у вас пока что нет вещей", color=0x42aaff).set_author(
                    name="Инвентарь"))
    elif arg == "-h" or arg == "-help" or arg == "h" or arg == "help":
        await ctx.send(
            embed=discord.Embed(description=f"команда которая показывает предметы в вашем инвенторе", color=0x42aaff).set_author(
                name="Инвентарь"))
    else:
        p = arg.strip("<>@!")
        if p in things:
            answ = ""
            for n, i in enumerate(things[p], 1):
                answ += f"**{n} . {i}**" + "\n"
            if answ == "":
                await ctx.send(
                    embed=discord.Embed(description=f"у этого человека пока что нет вещей", color=0x42aaff).set_author(
                        name="Инвентарь"))
            else:
                await ctx.send(
                    embed=discord.Embed(description=answ, color=0x42aaff)
                        .set_author(name="Инвентарь"))
        else:
            things[p] = []
            await ctx.send(
                embed=discord.Embed(description=f"у этого человека пока что нет вещей", color=0x42aaff).set_author(
                    name="Инвентарь"))


def wait(n, key):
    print(f"{key}: {n}: start")
    time.sleep(float(n))
    print(f"{key}: {n}: finished")
    pyautogui.keyUp(key)


def wait_mouse(n, key):
    print(f"{key}: {n}: start")
    time.sleep(float(n))
    print(f"{key}: {n}: finished")
    pyautogui.mouseUp(button=key)


@client.command()
async def game(ctx, *arg):
    if arg is []:
        await ctx.send(
            embed=discord.Embed(description=f"нет команд", color=0x42aaff).set_author(
                name="Ивент"))
    elif arg[0] in ['w', 'a', 's', 'd', 'e', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'c', 'space', 'q', 'shift']:
        pyautogui.keyDown(arg[0])

        if len(arg) == 2:
            Thread(target=wait, args=(arg[1], arg[0])).start()
        else:
            Thread(target=wait, args=(0.5, arg[0])).start()

    elif arg[0] == "click":
        if len(arg) < 2:
            await ctx.send(
                embed=discord.Embed(description=f"не хватает команд", color=0x42aaff).set_author(
                    name="Ивент"))
        elif arg[1] == "left":
            pyautogui.mouseDown(button='left')
            if len(arg) == 3:
                Thread(target=wait_mouse, args=(arg[2], arg[1])).start()
            else:
                Thread(target=wait_mouse, args=(0.5, arg[1])).start()
        elif arg[1] == "right":
            if len(arg) == 3:
                Thread(target=wait_mouse, args=(arg[2], arg[1])).start()
            else:
                Thread(target=wait_mouse, args=(0.5, arg[1])).start()
        else:
            await ctx.send(
                embed=discord.Embed(description=f"нет такой команды", color=0x42aaff).set_author(
                    name="Ивент"))
    elif arg[0] == "mouse":
        if len(arg) < 2:
            await ctx.send(
                embed=discord.Embed(description=f"не хватает команд", color=0x42aaff).set_author(
                    name="Ивент"))
        elif len(arg) == 3:
            if arg[1] == "up":
                pyautogui.move(1, -float(arg[2]), 0.25)
            elif arg[1] == "down":
                pyautogui.move(1, float(arg[2]), 0.25)
            elif arg[1] == "left":
                pyautogui.move(-float(arg[2]), 0, 0.25)
            elif arg[1] == "right":
                pyautogui.move(float(arg[2]), 0, 0.25)
            else:
                await ctx.send(
                    embed=discord.Embed(description=f"нет такой команды", color=0x42aaff).set_author(
                        name="Ивент"))
        elif len(arg) == 2:
            if arg[1] == "up":
                pyautogui.move(0, -100, 0.25)
            elif arg[1] == "down":
                pyautogui.move(0, 100, 0.25)
            elif arg[1] == "left":
                pyautogui.move(-100, 0, 0.25)
            elif arg[1] == "right":
                pyautogui.move(100, 0, 0.25)
            else:
                await ctx.send(
                    embed=discord.Embed(description=f"нет такой команды", color=0x42aaff).set_author(
                        name="Ивент"))
    else:
        await ctx.send(
            embed=discord.Embed(description=f"нет такой команды", color=0x42aaff).set_author(
                name="Ивент"))


# @client.event
# async def on_message(self, message):
#     if message.author.bot:
#         return
#     if message.author.id in [474230378421420033]:
#         await self.get_channel(message.channel.id).send(
#             embed=discord.Embed(description="стас лох", color=0x4cbb17)
#                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#     elif str(message.content).startswith(symbol):
#         a = str(message.content)
#         p = str(message.author.id)
#         if ("help" in a or "h" in a) and "-" not in a and "s" not in a:
#             await self.get_channel(message.channel.id).send(f"чтобы узнать про команду напишите```{symbol}<команда> -h``` или ```{symbol}<команда> -help``` список команд:"
#                                                             f"```{symbol}w -команда которая приносить от {works_min} до {works_max}```"
#                                                             f"```{symbol}sl -команда которая приносить от {slut_min} до {slut_max}```"
#                                                             f"```{symbol}s -команда которая позволяет отпраять деньги или вещи другому человеку```"
#                                                             f"```{symbol}с -команда которая приносить от {crime_min} до {crime_max}```"
#                                                             f"```{symbol}sh -команда которая показывает список предметов из магазина```"
#                                                             f"```{symbol}b -команда с пмощью которой можно купить вещщи из магазина```")
#
#         elif "m" in a:
#             if "-h" not in a and "-help" not in a:
#                 name = a.strip(" ").split(" ")[-1]
#                 if (symbol + "m") in name:
#                     if p in db:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=f"сейчас име"
#                                                             f"ет {self.get_emoji(emoji_id)}{num(db[p])}", color=0x42aaff).set_author(name=f"{message.author.name}",
#                                                                                                                                      icon_url=message.author.avatar_url))
#                     else:
#                         db[p] = 0
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=f"сейчас име"
#                                                             f"ет {self.get_emoji(emoji_id)}{0}", color=0x42aaff).set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         save()
#                 else:
#                     name = name.strip("<>@!")
#                     if name in db:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=f"сейчас име"
#                                                             f"ет {self.get_emoji(emoji_id)}{num(db[name])}", color=0x42aaff).set_author(name=f"{self.get_user(int(name))}",
#                                                                                                                                         icon_url=self.get_user(int(name)).avatar_url))
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"{symbol}m <имя>", color=0x42aaff).set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#
#         elif 'w' in a:
#             if "-h" not in a and "-help" not in a:
#                 if p in time_work:
#                     timel = dt.datetime.strptime(time_work[p], "%Y-%m-%d %H:%M:%S.%f")
#                     timer = works_pause - (dt.datetime.now() - timel)
#                     if timer <= dt.timedelta(minutes=0):
#                         n = random.randint(works_min, works_max)
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=random.choice(works_plus).format(num(n)), color=0x4cbb17)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         if p in db:
#                             db[p] += n
#                         else:
#                             db[p] = n
#                         time_work[p] = str(dt.datetime.now())
#                         save()
#                         save_time()
#                     else:
#                         hours, remainder = divmod(timer.seconds, 3600)
#                         minutes, seconds = divmod(remainder, 60)
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=f" осталось {hours} часов и {minutes} минут" if hours > 1 else f" осталось {minutes} минут и {seconds} секунд", color=0x42aaff)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         # await self.get_channel(message.channel.id).send(
#                         #     f"{message.author.mention} осталось {hours} часов и {minutes} минут" if hours > 1 else f"{message.author.mention} осталось {minutes} минут и {seconds} секунд")
#                 else:
#                     n = random.randint(works_min, works_max)
#                     await self.get_channel(message.channel.id).send(
#                         embed=discord.Embed(description=random.choice(works_plus).format(num(n)), color=0x4cbb17)
#                             .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                     if p in db:
#                         db[p] += n
#                     else:
#                         db[p] = n
#                     time_work[p] = str(dt.datetime.now())
#                     save()
#                     save_time()
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"команда, которая приносит от{works_min} до {works_max}", color=0x42aaff).set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#         elif "sl" in a:
#             if "-h" not in a and "-help" not in a:
#                 if p in time_slut:
#                     timel = dt.datetime.strptime(time_slut[p], "%Y-%m-%d %H:%M:%S.%f")
#                     timer = slut_pause - (dt.datetime.now() - timel)
#                     if timer <= dt.timedelta(minutes=0):
#                         n = random.randint(slut_min, slut_max)
#                         if db[p] < 0:
#                             n = random.randint(slut_min - (slut_min // 2), slut_max)
#                         if n >= 0:
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description=random.choice(slut_plus).format(num(n)), color=0x4cbb17)
#                                     .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         else:
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description=random.choice(slut_minus).format(num(n)), color=0xFF2A00)
#                                     .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         if p in db:
#                             db[p] += n
#                         else:
#                             db[p] = n
#                         time_slut[p] = str(dt.datetime.now())
#                         save()
#                         save_time()
#                     else:
#                         hours, remainder = divmod(timer.seconds, 3600)
#                         minutes, seconds = divmod(remainder, 60)
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=f" осталось {hours} часов и {minutes} минут" if hours > 1 else f" осталось {minutes} минут и {seconds} секунд", color=0x42aaff)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         # await self.get_channel(message.channel.id).send(
#                         #     f"{message.author.mention} осталось {hours} часов и {minutes} минут" if hours > 1 else f"{message.author.mention} осталось {minutes} минут и {seconds} секунд")
#                 else:
#                     n = random.randint(slut_min, slut_max)
#                     if db[p] < 0:
#                         n = random.randint(slut_min - (slut_min // 2), slut_max)
#                     if n >= 0:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=random.choice(slut_plus).format(num(n)), color=0x4cbb17)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                     else:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=random.choice(slut_minus).format(num(n)), color=0xFF2A00)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                     if p in db:
#                         db[p] += n
#                     else:
#                         db[p] = n
#                     time_slut[p] = str(dt.datetime.now())
#                     save()
#                     save_time()
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"команда которая приносит от {slut_min} до {slut_max}", color=0x42aaff).set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#         elif "sh" in a:
#             if "-h" not in a and "-help" not in a:
#                 answ = ""
#                 for i in shop:
#                     answ += f"*{i}* • {emoji_pp} {num(shop[i])}" + "\n"
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=answ, color=0x42aaff)
#                         .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"команда которая показывает ве предметы в магазине и их цены, а купить их можно с помощью ```{symbol}b <название предмета>```", color=0x42aaff).set_author(name="Магазин"))
#
#         elif "b" in a:
#             if "-h" not in a and "-help" not in a:
#                 p = a.split(" ")[-1]
#                 if p not in shop:
#                     await self.get_channel(message.channel.id).send(
#                         embed=discord.Embed(description=f"глаза раскрой там нет такой вещи",
#                                             color=0x42aaff).set_author(name=f"{message.author.name}",
#                                                                        icon_url=message.author.avatar_url))
#                 elif shop[p] > db[p]:
#                     await self.get_channel(message.channel.id).send(
#                         embed=discord.Embed(description=f"ты нищеброд и у тебя не хватает деняг",
#                                             color=0x42aaff).set_author(name=f"{message.author.name}",
#                                                                        icon_url=message.author.avatar_url))
#                 else:
#                     pass
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"с помощью этой командой можно покупать товары из макгазина и используеться она так ```{symbol}b <название предмета>```",
#                                         color=0x42aaff).set_author(name=f"{message.author.name}",
#                                                                    icon_url=message.author.avatar_url))
#         elif "c" in a:
#             if "-h" not in a and "-help" not in a:
#                 if p in time_crime:
#                     timel = dt.datetime.strptime(time_crime[p], "%Y-%m-%d %H:%M:%S.%f")
#                     timer = crime_pause - (dt.datetime.now() - timel)
#                     if timer <= dt.timedelta(minutes=0):
#                         n = random.randint(crime_min, crime_max)
#                         if db[p] < 0:
#                             n = random.randint(crime_min - (crime_min // 2), crime_max)
#                         if n >= 0:
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description=random.choice(crime_plus).format(num(n)), color=0x4cbb17)
#                                     .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         else:
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description=random.choice(crime_minus).format(num(n)), color=0xFF2A00)
#                                     .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         if p in db:
#                             db[p] += n
#                         else:
#                             db[p] = n
#                         time_crime[p] = str(dt.datetime.now())
#                         save()
#                         save_time()
#                     else:
#                         hours, remainder = divmod(timer.seconds, 3600)
#                         minutes, seconds = divmod(remainder, 60)
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=f" осталось {hours} часов и {minutes} минут" if hours > 1 else f" осталось {minutes} минут и {seconds} секунд", color=0x42aaff)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                         # await self.get_channel(message.channel.id).send(
#                         #     f"{message.author.mention} осталось {hours} часов и {minutes} минут" if hours > 1 else f"{message.author.mention} осталось {minutes} минут и {seconds} секунд")
#                 else:
#                     n = random.randint(crime_min, crime_max)
#                     if db[p] < 0:
#                         n = random.randint(crime_min - (crime_min // 2), crime_max)
#                     if n >= 0:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=random.choice(crime_plus).format(num(n)), color=0x4cbb17)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                     else:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description=random.choice(crime_minus).format(num(n)), color=0xFF2A00)
#                                 .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                     if p in db:
#                         db[p] += n
#                     else:
#                         db[p] = n
#                     time_crime[p] = str(dt.datetime.now())
#                     save()
#                     save_time()
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"С помощью этой команды можно получить от {crime_min} до {crime_max}", color=0x42aaff).set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#
#         elif "l" in a:
#             if "-h" not in a and "-help" not in a:
#                 h = sorted(db, key=lambda x: db[x], reverse=True)
#                 best = []
#                 nn = 1
#                 for i in h:
#                     best.append(f"**{nn}.{await client.fetch_user(int(i))}** • {emoji_pp}{num(db[i])}")
#                     nn += 1
#                 answ = ''
#                 for i in best:
#                     answ += i + "\n"
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=answ, color=0x42aaff)
#                         .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description="эта команда нужна для вывода всех пользователей отсортированных по их сбережениям", color=0x42aaff)
#                         .set_author(name=f"{message.author.name}", icon_url=message.author.avatar_url))
#
#         elif "s" in a:
#             if "-h" not in a and "-help" not in a:
#                 h = a.split(" ")
#                 if len(h) != 3:
#                     await self.get_channel(message.channel.id).send(f"{symbol}s <челове> <сумма>")
#                 else:
#                     user = h[-2].strip("<>@!")
#                     if h[-1].isnumeric() and user != p:
#                         n = int(h[-1])
#                         if p not in db:
#                             db[p] = 0
#                         if user not in db:
#                             db[user] = 0
#                         if n <= 0:
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description="ты дебил, какой 0 ??", color=0xFF2A00))
#                             # await self.get_channel(message.channel.id).send(
#                             #     f"не надо всё ломать !!!")
#                         elif db[p] < n:
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description=f"недостаточно сордов, у вас только{self.get_emoji(emoji_id)}{num(db[p])}", color=0xFF2A00).set_author(name=f"{message.author.name}",
#                                                                                                                                                                        icon_url=message.author.avatar_url))
#                         else:
#                             db[p] -= n
#                             db[user] += n
#                             await self.get_channel(message.channel.id).send(
#                                 embed=discord.Embed(description=f"перевёл {self.get_emoji(emoji_id)}{num(n)} на счёт {self.get_user(int(user))}", color=0xFF2A00).set_author(
#                                     name=f"{message.author.name}", icon_url=message.author.avatar_url))
#                             # await self.get_channel(message.channel.id).send(
#                             #     f"{message.author.mention} перевёл {self.get_emoji(emoji_id)}{n} на счёт {h[-2]}")
#                             save()
#
#                     else:
#                         await self.get_channel(message.channel.id).send(
#                             embed=discord.Embed(description="не надо всё ломать !!!", color=0xFF2A00))
#             else:
#                 await self.get_channel(message.channel.id).send(
#                     embed=discord.Embed(description=f"это команда нужна для того чтобы отправить кому-нибудь деняг и используеться она вот так: ```{symbol}s <челове> <сумма>```", color=0xFF2A00))


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == config.POST_ID:
        channel = client.get_channel(
            payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(
            payload.message_id)  # получаем объект сообщения
        member = payload.member  # получаем объект пользователя который поставил реакцию
        try:
            # await client.http.delete_message(817028253318774794, 856885834762289233)

            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.ROLES[emoji]
                             )  # объект выбранной роли (если есть)

            await client.get_channel(693468575062818897).send(
                f"{member.mention} " + "получил роль: " + f"**{role}**")
            # await client.get_channel(817028253318774794).send(f"$add-money <@{payload.member.mention}> 34659")
            if (len([
                i for i in member.roles
                if i and i.id not in config.EXCROLES
            ]) <= config.MAX_ROLES_PER_USER):
                await member.add_roles(role)
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.
                      format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == config.POST_ID:
        channel = client.get_channel(
            payload.channel_id)  # получаем id канала
        message = await channel.fetch_message(payload.message_id
                                              )  # получаем id сообщения
        user_id = payload.user_id  # по сути эта херня не нужна, но на всякий случай не трож
        member = await (await
                        client.fetch_guild(payload.guild_id
                                           )).fetch_member(payload.user_id)

        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.ROLES[emoji]
                             )  # объект выбранной роли (если есть)
            await client.get_channel(693468575062818897).send(
                f"{member.mention} " + "потерял роль: " + f"**{role}**")
            await member.remove_roles(role)

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id in config.channels:
            role = utils.get(member.guild.roles, id=config.channels[after.channel.id])
            await member.add_roles(role)
    elif before.channel is not None and after.channel is None:
        if before.channel.id in config.channels:
            role = utils.get(member.guild.roles, id=config.channels[before.channel.id])
            await member.remove_roles(role)
    else:
        if before.channel.id in config.channels and after.channel.id in config.channels:
            role = utils.get(member.guild.roles, id=config.channels[before.channel.id])
            await member.remove_roles(role)
            role = utils.get(member.guild.roles, id=config.channels[after.channel.id])
            await member.add_roles(role)


# RUN

# keep_alive()
# client.run(os.environ['token'])
client.run(config.TOKEN)
