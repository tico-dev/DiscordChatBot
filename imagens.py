import aiohttp
import discord
import io


async def singed_image(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "https://cdn.discordapp.com/attachments/353252489639886849/697640149881978930/DFXtwAaXYAAQnod.png") as resp:
            if resp.status != 200:
                return await ctx.channel.send('Não consegui baixar a imagem :( ...')

            data = io.BytesIO(await resp.read())
            await ctx.channel.send(file=discord.File(data, 'singed.png'))


async def amongus_image(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "https://gaming.lenovo.com/emea/attachment.php?attachmentid=2823") as resp:
            if resp.status != 200:
                return await ctx.channel.send('Não consegui baixar a imagem :( ...')

            data = io.BytesIO(await resp.read())
            await ctx.channel.send(file=discord.File(data, 'tft.gif'))
