'''
Name: trend_reader.py
Version Python 3.5

@Description:
It allows you to visualize trends from data in a csv file getting it by the stream. 

Just you need put some arguments like name file, the column you want to research, 
a list with the words to find and finally turn on real time for visualize 
changes into the plot during the streaming.  

Created on 10/02/2018
@author: Luis Antonio V R
'''
# Modules
import pandas as pd
import re
import matplotlib.pyplot as plt
plt.style.use('ggplot')

class Search_Trend:
    
    def __init__(self, name_file='data.csv', column_research='text', find_words=['tweepy'], real_time = False):
        
        self.file = name_file
        self.colum_research = column_research
        self.find_words = find_words
        self.real_time = real_time
        
    def word_in_text(self, word, text):
        """
            It return a bolean value depends if the word makes a match in the text
            you wanna search.
        """
        try:
            word_lower = word.lower()
            text_lower = text.lower()
            match = re.search(word_lower, text_lower)
        
            if match:
                return True
            return False
        
        except AttributeError:
            return False

    def analize_data(self):
        """
            It counts all the times when the words in a csv file makes a match 
            with your list find_words, then it builds a list with the results. 
        """
            
        # Read file
        df = pd.read_csv(self.file)
        
        df.columns = ['account_date',
                      'created_at',
                      'description',
                      'followers_count',
                      'geo',
                      'image_profile',
                      'lang',
                      'location',
                      'name',
                      'nick_name',
                      'source',
                      'statuses_count',
                      'text', 
                      'time_zone', 
                      'user_id']
        
        numbers_list = []
    
        # Start to count 
        for word in self.find_words:
            i = 0
            for row in df[self.colum_research]:  
                i += self.word_in_text(word, row)
            
            numbers_list.append(i)
        
        return numbers_list
    
    def bar_plot(self):
        """
            It shows a bar plot with the results from the method analize_data().
        """
        # It gets the results from analize data
        counter = self.analize_data()
        
        # Range builds a numbers list of the find_words size
        dim  = range(len(self.find_words))
        
        # Shows plot
        _ = plt.title('Twitter trends')
        _ = plt.ylabel('People posting about')
        _ = plt.xlabel('Targets')
        _ = plt.bar(dim, counter,width=0.4, align='center', color='green', alpha = 0.3)
        _ = plt.xticks(dim, self.find_words) 
        
    def show_plot(self):
        """
            Evaluate if the bar plot it will update
        """
        if self.real_time:
        
            while True:
                self.bar_plot()
                plt.pause(0.3)
            
        self.bar_plot()
        plt.show()    
        