import time
from platform import platform

import praw
import yaml
from prawcore.exceptions import PrawcoreException


def load_config():
    config = None
    wiki = subreddit.wiki[wiki_page_path]
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


def main():
    # Gets the recent modmails and checks the first author name against the list of banned users
    # If the name matches the modmail gets archived.
    try:
        for modmail in subreddit.modmail.conversations():
            archive_and_mark_as_read(modmail)
            time.sleep(5)
    except PrawcoreException as praw_exception:
        print(praw_exception)
        time.sleep(10)
    except KeyboardInterrupt:
        print(time.strftime("The bot has stopped: %Y/%m/%d %I:%M:%S %r", time.localtime()))


if __name__ == '__main__':
    # Logging in reddit
    reddit = praw.Reddit('modmail_archiver_bot', user_agent=f"{platform()}:ModmailArchiver:1.0 (by /u/is_fake_Account)")

    subreddit_name = 'bramptonbois'
    subreddit = reddit.subreddit(subreddit_name)
    wiki_page_path = 'modmail_archiver_config'

    # Printing status
    print(f"Account Logged in {reddit.user.me()}")
    print(f"Subreddit configured: r/{subreddit_name}")
    print(f"Config page name: {wiki_page_path}")
    print(time.strftime("Bot Started at: %Y/%m/%d %I:%M:%S %r", time.localtime()))
    main()
