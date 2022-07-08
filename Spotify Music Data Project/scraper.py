from datetime import datetime
import spotipy
import csv
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
cid =config['DEFAULT']['cid']
secret = config['DEFAULT']['secret']

sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=cid,
                                                           client_secret=secret))
list_of_genres = ['samba','eletronic','rock','folk','blues','soul','country','reggae','house','latin','dubstep','pop', 'pop rock','sertanejo','indie','lofi','romantic','forro']
# First Fetch of data
data_raw = {}
print('Running....')
for genre in list_of_genres:
    results = sp.search(type='track' ,q= f'genre:{genre}', limit=20)
    data_raw[f'{genre}'] = []
    for idx, track in enumerate(results['tracks']['items']):
        data_raw[f'{genre}'].append([track['id'],track['popularity'],track['name']])
print("It's Done!....😃")
# Let's save it on CSV


# open the file in the write mode
date = str(datetime.today()).split()[0]

# create the csv writer
tables = data_raw.keys()
# write a row to the csv file
for genre in data_raw:
    f = open(f'scraped_raw_data_top_10/raw_{genre}_{date}.txt', 'w')
    writer = csv.writer(f)
    writer.writerow(['id','popularity','name'])
    for data_tuple in data_raw[genre]:
        writer.writerow([data_tuple[0],data_tuple[1],data_tuple[2]])

# close the file
f.close()
