import os
import openai
from unidecode import unidecode

def read_data():

    folder_path = 'datos'
    # Obtener la lista de archivos en la carpeta compartida
    file_list = os.listdir(folder_path)

    prompts = []

    # Recorrer la lista de archivos
    for file_name in file_list:
        # Ruta completa del archivo
        file_path = os.path.join(folder_path, file_name)

        # Leer el contenido del archivo como una cadena de texto
        with open(file_path,  encoding='utf-8') as file:
            content = file.read()

        # Agregar el contenido del archivo a la lista
        prompts.append(content)
        prompts.append('')
    print('Datos Cargados')
    return prompts

def detectar_persona(texto):
    """ Funcion para detectar con que persona quiere hablar 
    """
    texto = unidecode(texto.lower())
    CR7_words = ["cristiano","ronaldo","cr7"]
    Derbez_words = ['eugenio','derbez']
    Trump_words = ['donald','trump']
    personas = [CR7_words, Trump_words, Derbez_words]

    for i in range(len(personas)):
        for j in personas[i]:
            if j in texto:
                print('Cambio de personaje')
                return i

    return ''

def get_response(prompts:list, key:int, user_message:str):

    # API Key and Prompt
    openai.api_key = 'YOUR TOKEN OPENAI'
    data_prompt = prompts[key] + "\n\n" + "Q: " + user_message + "\nA:"

    # Create response data
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=data_prompt,
        max_tokens=100,
    ) 

    # Get response str
    output = response.choices[0].text.strip()
    print('Respuesta Generada')
    return output
