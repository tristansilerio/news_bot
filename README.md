# News/Headlines Bot

This project was made out personal interest in automation and keeping up with current news everyday. In a similar vein as NPR UpFirst, I wanted a way to quickly get some news to my email so that I could then further look into interesting issues. 

Purpose: 
Send me email every morning with top news headlines of the day so that I can quickly see what I may want to read more about. 

Implementation:
Using the News API, I was able to grab the news information that I wanted (i.e. business, US news, international, etc.). From there, I used The Simple Mail Transfer Protocol (SMTP) and Secure Sockets Layer (SSL) in Python to access my email address and send myself and email with the formatted data from the News API. 

TODO: 
Everything is functionally working, just need to hookup code to a server that is running 24/7 so that I do not have to reply on computer staying open


