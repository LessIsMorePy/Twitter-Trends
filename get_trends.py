'''
Name: get_trends.py
Version Python 3.5

@Description:
The script allows you running at the same time the task stream.py and 
trend_reader_v2.py, also you can just run one of them.

The parameters must be specified as arguments in the class "RunScripts".

Created on 10/02/2018

@author: Luis Antonio V R
'''
# Modules
import threading

# My modules
from trend_reader_v2 import Search_Trend
from stream import stream

class RunScripts:
    
    def __init__(self, *args):
        
        self.file = args[0]
        
        self.ck = args[1]
        self.api_s = args[2]
        self.at = args[3]
        self.at_s = args[4]
        self.filter_list = args[5]
        self.store = args[6]
    
        self.column_research = args[7]
        self.find_words = args[8]
        self.real_time = args[9]
        
        self.task = args[10]
        
    def strem(self):
        """
            It run the module stream.
        """
        streaming = threading.Thread(target=stream(self.ck, 
                                                   self.api_s, 
                                                   self.at, 
                                                   self.at_s, 
                                                   self.filter_list, 
                                                   self.store, 
                                                   self.file))
        streaming.start()
    
    def bar_plot(self):
        """
            It plot the module trend_reader.
        """
        reader = threading.Thread(target=Search_Trend(self.file, 
                                                      self.column_research, 
                                                      self.find_words, 
                                                      self.real_time).show_plot())
        reader.start()
    
    def run_task(self):
        """
            It evaluate what kind of task it will perform.
        """
        task = self.task.lower()
        
        if task == 'stream':
            self.strem()
        elif task == 'plot':
            self.bar_plot()
        elif task == 'run_all':
            self.strem()
            self.bar_plot()
        else:
            print('You should choose one of this tasks: stream, plot or run_all')
    
if __name__ == '__main__':
    
    # Parameters
    file = 'candidatos.csv'
    
    ck = '***'
    api_s = '***'
    at = '***'
    at_s = '***'
    
    filter_list = ['AMLO', 'Anaya', 'Marichuy', 'Meade', 'Bronco', 'Candidatos 2018 mexico']
    store = True
    
    column_research = 'text'
    find_words = ['AMLO', 'Anaya', 'Marichuy', 'Meade', 'Bronco']
    real_time = True
    
    task = 'run_all'
    
    # Run task
    RunScripts(file, ck, api_s, at, at_s, filter_list, store, 
               column_research, find_words, real_time, 
               task).run_task()
