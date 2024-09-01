import discord
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} OLARAK GİRİŞ YAPTI.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('//merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('//bye'):
        await message.channel.send(":wave:")
    elif message.content.startswith('//EN BÜYÜK'):
        await message.channel.send("<:besiktas:1277555518348722280>")
    elif message.content.startswith('//sayı'):
        await message.channel.send(random.randint(0,1000))     
    elif message.content.startswith('//en iyi oyun'):
        await message.channel.send("<:mc:1277625358845214750>")
    elif message.content.startswith('//creator'):
        await message.channel.send("My Creator is kuxst.com")
    elif message.content.startswith('sa'):
        await message.channel.send("Aleyküm Selam Mümin kardeşim")
    elif message.content.startswith('help TenZics'):
        await message.channel.send("||//merhaba  |  //bye  |  //EN BÜYÜK  |  //sayı  |  //en iyi oyun  |  //creator  |  sa ||")                           

client.run("bot TOKEN")
