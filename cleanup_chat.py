#!/usr/bin/env python
# coding: utf-8

# importing regular expression library
import re

# dominate library to easily create HTML pages in Python
import dominate
from dominate.tags import *
from dominate.util import raw

# date library to get date
from datetime import date

###################################### ACTUAL CODE ######################################

# opening the chat file
chat = open("meeting_saved_chat_19-03-Guillem.txt")

today = date.today()

# creating a list to put all the messages in
messages = []

# going through the chat line by line
for newline in chat:
    # if the line contains a timestamp append it to the messages list
    if re.search('[0-2][0-9]:[0-6][0-9]:[0-9][0-9]', newline):
        messages.append(newline)
        
    # if it DOESN'T have a timestamp, then it's part of the previous message, so append it to the last item of the list
    else:
        messages[-1] += newline
        # print(messages[-1])

# create a list for all the messages
chat_list = []

# looping in the messages list
for message in messages:
    # grabbing it's values
    date = message.split("\t ")[0]
    sender = message.split("\t ")[1].split(" : ")[0][5:]
    text = message.split("\t ")[1].split(" : ")[1]
    
    # creating a dictionary to then add to the chat_dict and print it
    dict = { "time": date, "from": sender, "message": text }
    chat_list.append(dict)
    
    #print(dict)
    
doc = dominate.document(title='Class chat of ' + today.strftime("%d/%m/%Y"))

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='content'):
        for msg in chat_list:
            s
            with div():
                attr(cls="chat_msg")
                h4(msg["from"])
                raw('<blockquote>' + str(msg["message"]) + '</blockquote>')
                h6(msg["time"])

#print(doc)

# Saves the document in an HTML file
html_file = open("chat-" + str(today) + ".html","w")
html_file.write(str(doc))
html_file.close()
