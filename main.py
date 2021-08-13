import time
from platform import platform
from threading import Thread

import praw
import yaml
from prawcore.exceptions import PrawcoreException


def load_config():
    config = None
    wiki = subreddit_inst_1.wiki[wiki_page_path]
    try:
        config = yaml.safe_load(wiki.content_md)
    except yaml.YAMLError as yaml_err:
        # If could not load yaml file
        print(yaml_err)
    return config


def archive_and_mark_as_read(modmail):
    # Refresh the config to load new names
    config = load_config()

    if modmail.authors[0].name in config['name']:
        modmail.archive()
        modmail.read()


def modmail_streamer():
    modmail_stream = subreddit_inst_1.mod.stream.modmail_conversations(pause_after=-1, skip_existing=True)
    while running:
        try:
            # Streams the new modmails
            for modmail in modmail_stream:
                if modmail is None:
                    break
                archive_and_mark_as_read(modmail)
        except PrawcoreException as praw_exception:
            print(praw_exception)
            time.sleep(10)
    exit(0)


def archived_conversation_reader():
    # # Once the modmail is archived. the steam won't be able to see it
    # # So therefore this loop checks the archived modmails and marks them as read
    try:
        for modmail in subreddit_inst_2.modmail.conversations(state='archived'):
            archive_and_mark_as_read(modmail)
            time.sleep(5)

            if not running:
                exit(0)
    except PrawcoreException as praw_exception:
        print(praw_exception)
        time.sleep(10)


if __name__ == '__main__':
    # Logging in reddit
    # PRAW is not thread safe, therefore we need two instances of praw
    reddit1 = praw.Reddit('modmail_archiver_bot',
                          user_agent=f"{platform()}:ModmailArchiver:1.0 (by /u/is_fake_Account)")
    reddit2 = praw.Reddit('modmail_archiver_bot',
                          user_agent=f"{platform()}:ModmailArchiver:1.0 (by /u/is_fake_Account)")

    subreddit_name = 'bramptonbois'
    subreddit_inst_1 = reddit1.subreddit(subreddit_name)
    subreddit_inst_2 = reddit2.subreddit(subreddit_name)
    wiki_page_path = 'modmail_archiver_config'

    # Printing status
    print(f"Account Logged in {reddit1.user.me()}")
    print(f"Subreddit configured: r/{subreddit_name}")
    print(f"Config page name: {wiki_page_path}")
    print(time.strftime("Bot Started at: %Y/%m/%d %I:%M:%S %r", time.localtime()))

    try:
        # Running the bot
        running = True
        stream_thread = Thread(target=modmail_streamer)
        archived_conv_thread = Thread(target=archived_conversation_reader)
        stream_thread.start()
        archived_conv_thread.start()
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        running = False
        print("Stopping the bot... This may take few seconds")

    print(time.strftime("The bot has stopped: %Y/%m/%d %I:%M:%S %r", time.localtime()))