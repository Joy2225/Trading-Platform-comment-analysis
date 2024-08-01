import praw

import credentials

reddit = praw.Reddit(client_id=credentials.client_id, client_secret=credentials.client_secret,
    user_agent=credentials.user_agent, username=credentials.username, password=credentials.password)



def get_comments(url,replace_more_comments=False):
    submission = reddit.submission(url=url)
    if replace_more_comments:
        submission.comments.replace_more(limit=0)
    return submission.comments.list()



url = "https://www.reddit.com/r/computerscience/comments/10d016l/looking_for_books_videos_or_other_resources_on/"

submissions = get_comments(url)
for submission in submissions:
    print(submission.body)


