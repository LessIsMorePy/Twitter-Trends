'''
Name: stream.py
Version Python 3.5
 
@Description:

This script helps you to make a stream using the module "tweepy", 
in addition if you want you can save all the data from the streaming 
in a csv file.
 
Created on 10 january 2018
Last version 20 february 2018
 
@author: Luis Antonio V R
'''

# Modules
import json
import pandas as pd
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

def stream(*args):
    
    """
        This function start the streaming. If you choose
        store = True then the csv file it should be created 
        at the same directory from you run this script.
        
        stream(consumer_key, api_secret, access_token, access_token_secret,
        filter_list, store, name_file)

        consumer_key: Get this key from your Twitter account  
        api_secret: Get this key from your Twitter account 
        access_token: Get this key from your Twitter account
        access_token_secret: Get this key from your Twitter account
        
        filter_list: Pass a list with the words you wanna find in tweets, 
                    i.e. ['something', 'something 2', 'something 3']
        store: Choose True or False if you wanna store the streming tweets 
              or just view the data in your console
        name_file = Pass a string with the name file, i.e. 'data.csv' 
    """
    
    authorize = auth(args[0], args[1], args[2], args[3])
    api = API(authorize)
    mystream = Stream(api.auth, listener(args[5], args[6]))
    mystream.filter(track = args[4], encoding='utf-8', async=True)
    
def auth(*args):
    """
        Build and return the user acces.
        
        auth('consumer_key', 
             'api_secret', 
             'access_token',
             'access_token_secret')  
    """
    
    auth = OAuthHandler(args[0], args[1])
    auth.set_access_token(args[2], args[3])
    
    return auth 

class listener(StreamListener):

    def __init__(self, store=False, name_file='data.csv'):
        
        self.store = store
        self.name_file = name_file
         
    def on_data(self, data):
        
        # It decode
        data = json.loads(data)
        
        # It get data from JSON
        nick_name = '@' + data['user']['screen_name']
        name =   data['user']['name']
        user_id = data['user']['id']
        description = data['user']['description']
        location = data['user']['location']
        time_zone = data['user']['time_zone']
        try:
            for value in data['geo'].items():
                geo = value[1]
        except:
            geo = None
        followers_count = data['user']['followers_count']
        statuses_count = data['user']['statuses_count']
        account_date = data['user']['created_at']
        image_profile = data['user']['profile_image_url_https'] 
        text = data['text']
        created_at = data['created_at']
        lang = data['lang']
        source = data['source']
        
        # It create a csv file 
        if self.store:
            
            # It build a dictionary with data for store or shows it
            data_dic = {'nick_name': [nick_name], 
                        'name': [name], 
                        'user_id': [user_id], 
                        'description': [description], 
                        'location': [location], 
                        'time_zone': [time_zone], 
                        'geo': [geo], 
                        'followers_count': [followers_count], 
                        'statuses_count': [statuses_count], 
                        'account_date': [account_date], 
                        'image_profile': [image_profile],
                        'text': [text], 
                        'created_at': [created_at], 
                        'lang': [lang], 
                        'source': [source]}
            
            df = pd.DataFrame(data_dic)
            df.to_csv(self.name_file, sep=',', mode='a', line_terminator='\n', header=False, index=False)
        
        # It show tweets from the stream in your console
        print(nick_name,'\n',name,'\n', user_id,'\n',
              description, '\n', location, '\n',
              time_zone, '\n', geo, '\n', followers_count, '\n',
              statuses_count, '\n', account_date, '\n',
              image_profile, '\n', text, '\n', created_at, '\n',
              lang, '\n', source, '\n')
        
        return True
