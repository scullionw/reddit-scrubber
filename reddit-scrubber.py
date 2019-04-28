import praw
import getpass
import sys
from config import credentials

def scrubber(user, content, sorted_by):
    """ Scrubs all content available in a given sorting, max 100 per scrub call """
    scrubbed = 0
    for el in getattr(getattr(user, content), sorted_by)(limit=None):
        try:
            el.edit('scrubbed')
        except:
            pass
        el.delete()
        scrubbed += 1
    return scrubbed

def main():
    print("Username: ", end="")
    credentials['username'] = input()
    credentials['password'] = getpass.getpass()

    user = praw.Reddit(**credentials).user.me()
    for content in ['comments', 'submissions']:
        for sorted_by in ['new', 'hot', 'top', 'controversial']:
            while scrubber(user, content, sorted_by):
                pass

if __name__ == '__main__':
    sys.exit(main())