import os
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5cde16efca0446f3ad555a6a834ba694'
secret = 'd366d2604be54abfa4a0ae72ba47622a'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

address_data = r'C:\Users\kelvi\OneDrive\Documentos\TCC\acoustic_data.csv'
adress_wroted = r'C:\Users\kelvi\OneDrive\Documentos\TCC\lines_wroted.csv'
adress_no_data = r'C:\Users\kelvi\OneDrive\Documentos\TCC\no_data.csv'

urls_spotify = open(r'C:\Users\kelvi\OneDrive\Documentos\TCC\music_urls.csv')
reader = csv.reader(urls_spotify)

next(reader)
header = ["danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "track_href", "duration_ms", "time_signature"]
if os.stat(adress_wroted).st_size == 0:    
            print("Adicionando header!")
            file = open(address_data,'w',newline='')
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(header)
            print("Header adicionado")
            lines_wroted = open(adress_wroted, 'w', newline='')
            writer_wroted = csv.writer(lines_wroted)
            writer_wroted.writerow(str(0))
            file.close()
            lines_wroted.close()
            lines_no_data = open(adress_no_data, 'w', newline='')
            writer_no_data = csv.writer(lines_no_data)
            writer_no_data.writerow(["track_href"])
            lines_no_data.close()
features = []
for music_url in reader:
    number = int(music_url[0])
    try: 
        lines_wroted = open(adress_wroted, 'r')
        wroted = int(lines_wroted.readline())
        lines_wroted.close()
        if(number >= wroted):
            track_url = str(music_url[1])
            features = sp.audio_features([track_url])
            if features[0] is None:
                lines_no_data = open(adress_no_data, 'a', newline='')
                writer_no_data = csv.writer(lines_no_data)
                writer_no_data.writerow([track_url])
                lines_no_data.close()
                print("Url sem dados disponíveis.")
                lines_wroted = open(adress_wroted, 'w', newline='')
                writer_wroted = csv.writer(lines_wroted)
                writer_wroted.writerow([number])
                lines_wroted.close()
                print("Linha sem dados: " + str(number) + ".")
                continue
        else:
            print("Informações da linha " + str(number) + " já adicionadas ao csv.")
            continue
    except:
        lines_wroted = open(adress_wroted, 'r')
        wroted = int(lines_wroted.readline())
        lines_wroted.close()
        if(number > wroted):
            lines_wroted = open(adress_wroted, 'w', newline='')
            writer_wroted = csv.writer(lines_wroted)
            writer_wroted.writerow([number])
            lines_wroted.close()
            print("Linha a ser lida: " + str(number) + ".")
        break

    response = str(features[0])
    print(response)
    atributes = response.split(", ")
    danceability = atributes[0].replace("{", "").split(": ")
    energy = atributes[1].split(": ")
    key = atributes[2].split(": ")
    loudness = atributes[3].split(": ")
    mode = atributes[4].split(": ")
    speechiness = atributes[5].split(": ")
    acousticness = atributes[6].split(": ")
    instrumentalness = atributes[7].split(": ")
    liveness = atributes[8].split(": ")
    valence = atributes[9].split(": ")
    tempo = atributes[10].split(": ")
    track_href = atributes[14].split(": ")
    duration_ms = atributes[16].split(": ")
    time_signature = atributes[17].replace("}", "").split(": ")

    file = open(address_data,'a', newline='')
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    data_csv = []
    data_csv.append(danceability[1])
    data_csv.append(energy[1])
    data_csv.append(key[1])
    data_csv.append(loudness[1])
    data_csv.append(mode[1])
    data_csv.append(speechiness[1])
    data_csv.append(acousticness[1])
    data_csv.append(instrumentalness[1])
    data_csv.append(liveness[1])
    data_csv.append(valence[1])
    data_csv.append(tempo[1])
    data_csv.append(track_href[1])
    data_csv.append(duration_ms[1])
    data_csv.append(time_signature[1])
    print("Adicionando linha!")
    writer.writerow(data_csv)
    print("Linhas adicionadas")
    lines_wroted = open(adress_wroted, 'w')
    writer_wroted = csv.writer(lines_wroted)
    writer_wroted.writerow([number])
    lines_wroted.close()
    print("Total de adicionadas: " + str(number))           
    file.close()
