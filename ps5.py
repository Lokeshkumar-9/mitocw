# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import time
import feedparser
import string
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        print(entry)
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("EST"))
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory:
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
    
# PHRASE TRIGGERS

# Problem 2

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower().strip()
        
    def is_phrase_in(self, text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        text = ' '.join(text.split())
        words = text.split()
        index = 0
        for word in words:
            if word == self.phrase.split()[index]:
                index += 1
                if index == len(self.phrase.split()):
                    return True
            else:
                index = 0
                    
        return False    
    
# Problem 3

class TitleTrigger(PhraseTrigger):
    
    def __init__(self, phrase):
        super().__init__(phrase)
    
    def evaluate(self, news_story):
        title = news_story.get_title()
        return self.is_phrase_in(title)

# Problem 4

class DescriptionTrigger(PhraseTrigger):
    
    def __init__(self, phrase):
        super().__init__(phrase)
        
    def evaluate(self, news_story):
        description = news_story.get_description()
        return self.is_phrase_in(description)
        
# TIME TRIGGERS

# Problem 5

class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
        
# Problem 6

class BeforeTrigger(TimeTrigger):
    def evaluate(self, news_story):
        story_time = news_story.get_pubdate()
        story_time = story_time.replace(tzinfo=pytz.timezone("EST"))
        return story_time < self.time
    
class AfterTrigger(TimeTrigger):   
    def evaluate(self, news_story):
        story_time = news_story.get_pubdate()
        story_time = story_time.replace(tzinfo=pytz.timezone("EST"))
        return story_time > self.time

# COMPOSITE TRIGGERS

# Problem 7

class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger
        
    def evaluate(self, news_story):
        return not self.other_trigger.evaluate(news_story)

# Problem 8

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, news_story):
        return self.trigger1.evaluate(news_story) and self.trigger2.evaluate(news_story)

# Problem 9

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, news_story):
        return self.trigger1.evaluate(news_story) or self.trigger2.evaluate(news_story)

    
#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered = []
    for news_story in stories:
        if any(trigger.evaluate(news_story) for trigger in triggerlist):
            filtered.append(news_story)
    return filtered

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_list = []
    named_triggers = {}
    file_trigger = open(filename, 'r')
    
    for line in file_trigger:
        line = line.strip()
        if not line or line.startswith('//'):
            continue
        elements = [elem.strip() for elem in line.split(',')]
        if elements[0] == 'ADD':
            for trigger_name in elements[1:]:
                    trigger = named_triggers.get(trigger_name)
                    if trigger:
                        trigger_list.append(trigger)
                    else:
                        trigger_type = elements[0], elements[1]
                        trigger_arg = elements[2:]
                        if trigger_type == 'DESCRIPTION':
                            trigger = DescriptionTrigger(trigger_arg[0])
                        elif trigger_type == 'TITLE':
                            trigger = TitleTrigger(trigger_arg[0])
                        elif trigger_type == 'AND':
                            trigger1, trigger2 = named_triggers[trigger_arg[0]], named_triggers[trigger_arg[1]]
                            trigger = AndTrigger(trigger1, trigger2)
                        elif trigger_type == 'OR':
                            trigger1. trigger2 = named_triggers[trigger_arg[0]], named_triggers[trigger_arg[1]]
                            trigger = OrTrigger(trigger1, trigger2)
                        elif trigger_type == 'AFTER':
                            trigger_time = trigger_arg[0]
                            trigger = AfterTrigger(trigger_time)
                        elif trigger_type == 'BEFORE':
                            trigger_time = trigger_arg[0]
                            trigger = BeforeTrigger(trigger_time)
                        named_triggers[trigger_name] = trigger    

    return trigger_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11

        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):                
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

