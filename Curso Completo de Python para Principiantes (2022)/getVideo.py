import tweepy
import requests
import os

# Configura tus credenciales de la API de Twitter
consumer_key = "x3kbXJ4I9TRAaWsiy13JjzqWe"
consumer_secret = "g0I4QeBzvb3ihlDoBi1cX3Ptr99fKT8FCr28z61IQGLMuhFtRx"
access_token = "634783197-JePA7IgWlRE87Anow1O9Srzx7Gbkv6BfTJVmf7nR"
access_token_secret = "xCLkSHzVPnsFq6TvICcBs2yzNbbN9ku8gFmdifluReFVU"

# Autenticación con la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def descargar_video_twitter(url, ruta_destino):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            # Extraer el URL del video desde el tweet
            video_url = respuesta.json()['variants'][0]['url']

            # Descargar el video
            respuesta_video = requests.get(video_url, stream = True)

            if respuesta_video.status_code == 200:
                # Guardar el video
                with open(ruta_destino, 'wb') as archivo:
                    for fragmento in respuesta_video.iter_content(chunk_size = 1024):
                        archivo.write(fragmento)
                print(f'Video descargado y guardado en: {ruta_destino}')
            else:
                print('No se pudo descargar el video. Verifica la URL.')
        else:
            print('No se pudo obtener la información del tweet. Verifica la URL.')
    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')


if __name__ == "__main__":
    url_tweet = input("Ingrese la URL del tweet que contiene el video: ")
    ruta_destino = input("Ingrese la ruta completa donde desea guardar el video (por ejemplo, 'video.mp4'): ")

    # Verificar si el archivo ya existe
    if os.path.exists(ruta_destino):
        respuesta = input("El archivo ya existe. ¿Desea sobrescribirlo? (S/n): ")
        if respuesta.lower() != 's':
            print("Descarga cancelada.")
            exit()

    # Extraer el ID del tweet de la URL
    id_tweet = url_tweet.split('/')[-1]

    # Obtener información del tweet
    tweet = api.get_status(id_tweet, tweet_mode = 'extended')

    if 'extended_entities' in tweet._json:
        media = tweet.extended_entities.get('media', [])
        if media:
            tipo_media = media[0]['type']
            if tipo_media == 'video':
                variantes_video = media[0]['video_info']['variants']
                url_video = max(variantes_video, key = lambda x: x['bitrate'])['url']
                descargar_video_twitter(url_video, ruta_destino)
            else:
                print('El tweet no contiene un video.')
        else:
            print('El tweet no contiene un video.')
    else:
        print('No se pudo obtener información del tweet.')

