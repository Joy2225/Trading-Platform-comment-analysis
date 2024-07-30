from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.nextbillion.groww',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=300
)

# write only the comments part of each dictionary in reviews.txt
with open('reviews.txt', 'w') as f:
    for review in result:
        try:
            f.write(review['content'])
            f.write('\n')
        except:
            continue
