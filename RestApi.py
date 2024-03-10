#Amalia Jamaludin
# Develop a set of REST APIs capable of reading a JSON file deployed 
# on a server and returning information by using a collection of simple HTTP 
# requests invoked through Postman.

from flask import Flask, jsonify
import json
import re
import urllib.request

app = Flask(__name__)

#Load JSON file from the URL given
with urllib.request.urlopen('https://foyzulhassan.github.io/files/favs.json') as f:
    data = json.load(f)
    
#Get all tweets (create time, id, and tweet text) available in the archive.
@app.route('/tweets', methods = ['GET'])
def getTweets():
    tweets = []
    for tweet in data:
        tweetInfo = {
            'created_at': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        }
        tweets.append(tweetInfo)
    return jsonify(tweets)
    
#Get a list of all external links (all links that appear in tweet text field. Use regular expressions to extract the links , the links should be grouped based on tweet ids.
@app.route('/links', methods = ['GET'])
def getLinks():
    linksByTweet = {}
    for tweet in data: 
         links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet['text']) 
         linksByTweet[tweet['id']] = links
    return jsonify(linksByTweet)

#Get the details (tweet created_at, text, user screen_name) about a given tweet (given the tweet’s id).
@app.route('/tweets/<tweet_id>', methods=['GET'])
def getTweet(tweet_id):
    for tweet in data:
        if tweet['id'] == int(tweet_id):
            tweetInfo = {
                'created_at': tweet['created_at'],
                'text': tweet['text'],
                'screen_name': tweet['user']['screen_name'],
                'lang': tweet['lang']
            }
            return jsonify(tweetInfo)
    return jsonify({'error': 'Tweet not found'})

#Get detailed profile (location, description, followers_count, friends_count) information about a given Twitter user (given the user’s screen name).
@app.route('/users/<screen_name>', methods=['GET'])
def getUser(screen_name):
    for tweet in data:
        if tweet['user']['screen_name'] == screen_name:
            userInfo = {
                'name': tweet['user']['name'],
                'description': tweet['user']['description'],
                'followers_count': tweet['user']['followers_count'],
                'friends_count': tweet['user']['friends_count'],
                'favourites_count': tweet['user']['favourites_count']
            }
            return jsonify(userInfo)
    return jsonify({'error': 'User not found'})

if __name__ == '__main__':
    app.run()