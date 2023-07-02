from funciones import *
import discord
from discord.ext import commands
import sys

# Cargar Datos 
data = read_data()

# Personajes
names = ['Cristiano Ronaldo',
         'Donald Trump',
         'Eugenio Derbez']

# Saludos
grt = ['Hola, Soy Cristiano Ronaldo. ¡Siuuu!',
       'Hello, Soy Mr. Donald Trump!',
       '¡Hola amigo! Soy Eugenio.'
       ]

# Imagenes
img = ['cr7.jpg', 'trump.jpg', 'derbez.jpg', ]



# Obtener mensaje y respuesta para enviar a discord
async def send_message(message, key, user_message):
    
    # Intentar responder a discord
    try:
        print(key)
        response = get_response(data, key, user_message)  
        await message.channel.send(response)   

    except Exception as e:
        print(e)


TOKEN = "YOUR TOKEN"

def chat(): 

    print("\n*Para finalizar nuestra conversación di: 'adios','bye' or 'q' de quit \n")

    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix = "--",
                          case_insensitive = True,
                          intents = intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Bot en accion')


    @client.event
    async def on_message(message):
            global key
            # Si el mensaje es del bot, no responder
            if message.author == client.user:
                return
            
            # Obtener mensaje y datos del usuario
            username = str(message.author)
            user_message = str(message.content)            
            channel = str(message.channel)

            # Achicar las letras del mensaje
            user_message = user_message.lower()

    # Respuestas ------- ------------------------------------------
            # Responder
            cambio = detectar_persona(user_message)

            if user_message in ['hi', 'hola', 'h','hello']:
                await message.channel.send('Hola, soy GodPT Bot :)')
                await message.channel.send('¿Con que persona te gustaria hablar?')
                await message.channel.send('¿Cristiano Ronaldo, Eugenio Derbez o Donald Trump?')
                key = 0
            else:
                if user_message in ['adios', 'q', 'bye', 'by', 'adiós']:

                    # Valores predeterminados
                    # with open('fotos/bot.png', 'rb') as f:
                    #     pic = f.read()
                    # await client.user.edit(avatar = pic)
                    # await client.user.edit(username='GodPT Bot - [CR7, Trump, Derbez]')
                            
                    # Acabar conversación
                    await message.channel.send('Un placer hablar contigo.')
                    client.close()
                    sys.exit()

                else:
                    # Si hay cambio de personaje
                    if cambio in [0, 1, 2]:

                        key = cambio

                        # Cambiar foto y nombre del personaje

                        # with open('fotos/' + img[key], 'rb') as f:
                        #     pic = f.read()
                        # await client.user.edit(avatar = pic)
                        # await client.user.edit(username = names[key] + ' - [GodPT Bot]')
                        
                        await message.channel.send(grt[key])
                        
                    else:
                        # Respuesta de API       
                        await send_message(message, key, user_message)

    client.run(TOKEN)

chat()