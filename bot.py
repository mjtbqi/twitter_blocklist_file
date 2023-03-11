import tweepy
import csv

# Set up Twitter API authentication credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate the Twitter API client
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the list of blocked users
blocked_users = api.get_blocked_ids()

# Set up a CSV file for saving the data
csv_file = open('blocked_users.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Write the header row
csv_writer.writerow(['user_id', 'screen_name'])

# Loop over each blocked user and write their data to the CSV file
for user_id in blocked_users:
    user = api.get_user(user_id=user_id)
    csv_writer.writerow([user_id, user.screen_name])

# Close the CSV file
csv_file.close()
