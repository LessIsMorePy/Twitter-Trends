# Twitter-Trends
Get trends from Twitter, these scripts helps you to see what is people posting about. Make a stream, store data, see a bar plot or make all in real time. You choose what you want to do.

## Description
The main features of these Python scripts are monitoring Twitter with a list of words that you choose, all the tweets capture while you make a stream are stored in a CSV file.

After a data is stored, in "real time" you could see a bar plot. The plot shows you what is posting people about, depending on your filter words you are searching. 

Once you have a csv file, you could studie the captured tweets using the this same Python scripts.

## See how it works

```
https://www.youtube.com/watch?v=uIcIPD4E9vo

```
## How to use it?
* First, make sure you have these scripts: "trend_reader_v2.py", "stream.py" and "get_trends.py"
* After, you should install the next Python modules:

  * tweepy

  * matplotlib

  * pandas

  * json

  * re

  * threading

### Getting ready before you run the scripts
Into the script "get_trends.py" make sure to establish the next parameters:

* file: A name file for store the data.
* ck: Consumer Key.
* api_s: API secret.
* at: Access token. 
* at_s: Access token secret.
* filter_list: A list with the words you want to filter from Twitter.
* store: True o False, if you choose False, you just visualize the tweets in your console.
* column_research: In the example the program search the words(in "find_words") in the column called 'text', but also you can seach another things like languajes in the column 'lan'. See in the python scripts for more information. 
* find_words: This list has the words you can find in the tweets.
* real_time: True or False.
* task: 'run_all', 'plot' or 'stream'. This allows you making some of this tasks. "Plot" just read a csv file and shows you a bar plot. "stream" allows you to make a streaming Twitter and store or not the data. Finally "run_all" makes all at the same time.  

```
# Parameters
    file = 'candidatos2018.csv'
    
    ck = 'get it from your Twitter account'
    api_s = 'get it from your Twitter account'
    at = 'get it from your Twitter account'
    at_s = 'get it from your Twitter account'
    
    filter_list = ['AMLO', 'Meade', 'Anaya', 'Marichuy', 'Bronco']
    store = True
    
    column_research = 'text'
    find_words = ['AMLO', 'Meade', 'Anaya', 'Marichuy', 'Bronco']
    real_time = True
    
    task = 'run_all'
    
    # Run task
    RunScripts(file, ck, api_s, at, at_s, filter_list, store, 
               column_research, find_words, real_time, 
               task).run_task()
```
### Ready
After you establish the parameters mentioned before run the script "get_trends.py". Have fun!

### Note 
You can see more than one plot :)

## Limitations 
I've tested the scripts by 5 hours approximately, but when the data are by thousands the program it is not efficient. 

Early I will search a solution because the issue is that the for loops have a lot of data to iterate. This generates a memory problem. 

## Note
Recall, these Python scripts just count if a word appears in the tweet and this means that it doesn't matter if the post is positive or negative. 

The main task is counting if a word appeas in a tweet and plotting howcolumn_research: in the example, the program searches for the words in "find_words" in the column called "text", but you can also search for other things like languages in the "lan" column. See in the scripts. many times certain words are posting. 
