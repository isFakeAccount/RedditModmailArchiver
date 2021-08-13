
# RedditModmailArchiver  
  
This bot will allow you to continuously archive the modmail by certain users. This is to prevent malicious users to clog your modmail.

### How to use the bot
1. First download this repository to your maching
2.  Create a file called `praw.ini`. There you will provide the api keys and secret. 
`Praw.ini` should look like this 
```
[modmail_archiver_bot]  
client_id=Y4PJOclpDQy3xZ
client_secret=UkGLTe6oqsMk5nHCJTHLrwgvHpr
password=pni9ubeht4wd50gk
username=fakebot1
``` 
(*Substitute the  example id, secret, username, and password values with actual values*)

3. The next part is installing requirements from requirements.txt. This can be done via terminal using command
```
 pip3 install -r requirements.txt
```
4. Change the subreddit name to the actual subreddit name in main.py
5. Lastly run the main.py file
### Config File
The bot will look at the wiki page to gets its config information. In the wiki page you can mention the usernames of account which should be shadowbanned from the modmail. It's format should be
```
name:
   - username1
   - username2
   - username3
```
Note: Do not add u\ before username. Also, the formating should be like above, otherwise bot will not work. Similar to Automoderator, the config is YAML. Learn more about [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

### FAQ
**How it is better than muting?**
For the most cases, you are better off muting user. However, in rare ocassions, if the user is bypassing the mute by creating multtiple accounts. This bot will come in handy. It is in a way modmail shadowban.

**The modmail gets archived but it is still unread.**
Unfortunately, this is not a fixable issue. The bot can move the modmail to archive and mark it read from its side. However, for other moderations, it will show as unread in archived box. A solution would be that each moderator has to go to archive box and select mark all read in top right corner. 

[Archive messages showing unread](https://www.reddit.com/r/ModSupport/comments/oktfda/archive_messages_showing_unread/)