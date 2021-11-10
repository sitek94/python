import requests
import secrets

# Twitter API v2 Sample Code
# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Search/recent_search.py

# Step-by-step guide to making your first request to the new Twitter API v2
# https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2

bearer_token = secrets.twitter.get('bearer_token')

search_url = 'https://api.twitter.com/2/tweets/search/recent'
query_params = {
    'query': '(from:twitterdev -is:retweet) OR #twitterdev',
    'tweet.fields': 'author_id'
}


def bearer_oauth(req):
    req.headers['Authorization'] = f"Bearer {bearer_token}"
    return req


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)

    tweets = json_response.get('data')

    for tweet in tweets:
        print(tweet.get('text'))


main()
