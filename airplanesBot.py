import wolframalpha, tweepy, time

#tweepy setup block
TWITTER_CONSUMER_KEY = 'secret'
TWITTER_CONSUMER_SECRET = 'secret'
TWITTER_ACCESS_KEY = 'secret'
TWITTER_ACCESS_SECRET = 'secret'

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

#wolframalpha setup
WOLFRAMALPHA_ID = 'secret'

client = wolframalpha.Client(WOLFRAMALPHA_ID)
query = "flights overhead"

#i guess this is where the gps stuff would go in the future
#get results for query
res = client.query(query)
#get result pod, then find aircraft type
result = next(res.results)

a = ((next(result.subpods).plaintext).split("slant distance")[1]).split("\n")

i = 0;
planes = ""
flights = ""
a.pop(0)
for string in a:
    if(i < 5):
        print string + "\n"
        string = string.split("|")
        plane = string[1]
        flight = string[0]
        plane = plane.replace("Canadair Regional Jet ", "")
        flight = flight.replace("Airlines ", "")
        
        if(plane == " "):
            plane = "No Data"
        planes += str(i+1) + ": " + plane + "| "
        flights += str(i+1) + ": " + flight + "| "
        i+=1
    else:
        break

planes = planes.rstrip("| ")
flights = flights.rstrip("| ")
planes = planes[:140]
flights = flights[:140]

api.update_status(flights)
time.sleep(5)
api.update_status(planes)
