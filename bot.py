import openai
import discord

# Insert your Discord bot token  
TOKEN = 'discord Token Goes Here'

# OpenAI API key here
openai.api_key = 'Your openai API Goes here"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_text = message.content
    response = openai.Completion.create(
        engine='text-davinci-003',
        temperature=0.5,
        prompt=user_text,
        max_tokens=100,
        n=1,
        stop=None
    )
    
    
    response = response["choices"][0]["text"]
    await message.channel.send(response)

client.run(TOKEN)
