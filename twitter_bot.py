from paralleldots import set_api_key,get_api_key,sentiment
import tweepy
import time
con067='Yuzm090wATmHky08LKRnWETqg'
con_sc='OqS3VC186qItBYrwWFb2VjexE0Y5NMuaLpOQo9T9vuAsKhRocB'
access_token='1011126637881057282-EJWliVvpf6okh4i1w1WDcb7sLRqaMw'
Access_Token_Secret='I1N1yyE3BK5YgFcqwzG9vDMCeXJFW39I83q6z1Jemx48D'
auth=tweepy.OAuthHandler(con067,con_sc)
auth.set_access_token(access_token,Access_Token_Secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)
def menu():
    print("\n\t\t\t\t\t TwitterBot\n\n")
    print("\t\t\4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4\t\tWELCOME TO OUR YOU Twitter Bot   \t\t\4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4\n")
    print("\t\n Choose your option form 1-to-6\n")
    print("\t1.Retrieve Tweets\n")
    print("\t2.Count the followers\n ")
    print("\t3.Determine the sentiment\n")
    print("\t4.Determine location,language and time zone.\n")

    print("\t5.Compare Follower \n")
    print("\t6. Tweet a message \n")
    print("\t 7. Exit \n")
    me = int(input())
    if (me == 1):
        retrieve()

    elif (me == 2):
        followers()
    elif (me == 3):
        sentimentel()
    elif (me == 4):
        loc()
    elif (me == 5):
        com()

    elif(me==6):
        mess()
    else :
        exit()
def retrieve():
    user=input("Enter any Hash Tag or Search:-")
    tweets = api.search(user, lang='en', count=10, tweet_mode="extended")

    for tweet in tweets:
        print("-----------------------")
        print(tweet.full_text)
        print("-----------------------")
    n=int(input("Do you want program is continue: Press is Zero:-"))
    if(n==0):
        menu()
def followers():
    try:
        us=input("Enter Any twitter id for Serch Number of follower:-")
        targets = [us]  # All your targets here

        for target in targets:
            user = api.get_user(target)
            print(user.name, user.followers_count)
    except Exception:
        print("sorry Its is worng id")
    n = int(input("Do you want program is continue: Press is Zero:-"))
    if (n == 0):
        menu()
def loc():
    user_id = input("Enter ani id to see location:-")
    try:

        user=api.get_user(user_id)
        print("loction of user:-",user.location)
        print("Time Zone :-",user.time_zone)
        print("language:- :-", user.lang)
    except Exception:
        print("sorry Its is id worng")
    n = int(input("Do you want program is continue: Press is Zero:-"))
    if (n == 0):
        menu()
def sentimentel():
    us=str(input("Enter any Hash tag form search:-"))
    tweets=api.search(us,lang="english",count="10",tweet_mode="extended")
    set_api_key("DKBTUqoyRQkX2XYPOAnCz8LhAltJjUvg9SE0ZQMvAL0")
    get_api_key()
    for tweet in tweets:
        time.sleep(2)
        a=sentiment(tweet.full_text)
        print(a)
    n = int(input("Do you want program is continue: Press is Zero:-"))
    if (n == 0):
        menu()
def com():
    user_id =input("Enter ist id to compare:-")
    try:
        user=api.get_user(user_id)
        x=user.followers_count
    except Exception:
        print("sorry Its is id worng")

    user_id1=input("Enter 2nd id to compare:-")
    try:
        user1=api.get_user(user_id1)
        y=user1.followers_count
    except Exception:
        print("sorry Its is id worng")
    if x>y:
        print("{} is the best user of twitter :-",format(user.name))
    else:
        print("{} is the best user of twitter :-", format(user1.name))
    n = int(input("Do you want program is continue: Press is Zero:-"))
    if (n == 0):
        menu()
def mess():
    user_id=input("Enter any id to send msg:-")
    msg=input("Enetr any msg:-")
    try:
        api.send_direct_message(user=user_id,text=msg)
    except Exception:
        print("sorry Its is not follower")

    n = int(input("Do you want program is continue: Press is Zero:-"))
    if (n == 0):
        menu()
menu()