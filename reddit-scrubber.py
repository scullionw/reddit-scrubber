import sys
import praw
from credentials import credentials

def auth():
    """ Returns authenticated redditor model from PRAW """
    reddit = praw.Reddit(client_id=credentials['CLIENT_ID'],
                     client_secret=credentials['CLIENT_SECRET'],
                     user_agent='Scrubber',
                     username=credentials['USERNAME'],
                     password=credentials['PASSWORD'])

    return reddit.user.me()


def scrubber(user, content, sorted_by, pass_number):
    """ Scrubs all content available in a given sorting, max 100 per scrub call """
    scrubbed = 0
    for el in getattr(getattr(user, content), sorted_by)(limit=None):
        try:
            el.edit('scrubbed')
        except:
            pass
        else:
            print('Item {0} of {1} sorted by {2}, pass {3}. EDITED'.format(scrubbed + 1, content, sorted_by, pass_number))

        try:
            el.delete()
        except:
            pass
        else:
            print('Item {0} of {1} sorted by {2}, pass {3}. DELETED'.format(scrubbed + 1, content, sorted_by, pass_number))
            scrubbed += 1

    return scrubbed


def main():
    try:
        user = auth()
    except Exception as err:
        print('Error during user authentication:', err)
    content_list = ['comments', 'submissions']
    sorted_by_list = ['new', 'hot', 'top', 'controversial']
    for content in content_list:
        for sorted_by in sorted_by_list:
            pass_number = 1
            while scrubber(user, content, sorted_by, pass_number):
                pass_number += 1

if __name__ == '__main__':
    sys.exit(main())