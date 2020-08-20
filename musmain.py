import praw 
import time
with open('/home/dwas/Desktop/redditPy/id.txt') as f:
    sam=f.read()
    f.close
    
with open('/home/dwas/Desktop/redditPy/sec.txt') as g:
    dam=g.read()
    g.close()


reddit=praw.Reddit(client_id='2h0HRacer4ko0w',
                   client_secret='6-WH4a9vMIT3oycw1Hsr7--DBqo',
                   username='MrRobot_666',
                   password='walle2837',
                   user_agent='exp bot by u/experi_bot')

subreddit = reddit.subreddit("eXperimNnt")

# for submission in subreddit.hot(limit=5):
#     print("Title: ", submission.title)
#     print("Text: ", submission.selftext)
#     print("Score: ", submission.score)
#     print("---------------------------------\n")

textphrase='!mote'
while True:
    for cmmnt in subreddit.stream.comments():
        if textphrase in cmmnt.body:
            cmmnt.reply('mote chor bhate khate lamo')
    time.sleep(30)

    
        
