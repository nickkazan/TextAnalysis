import requests
from pprint import pprint
from InstagramScrape import grabData
#from IPython.display import HTML

#Assert forces the statement to be true, if not then it'll crash at compile time
subscriptionKey = "ec76f8560b6a4e8e926c35e63ef8fb2a"
assert subscriptionKey

textAnalyticsBaseUrl = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"

sentimentApiUrl = textAnalyticsBaseUrl + "sentiment"
documentsTest = {'documents' : [
  {'id': '1', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}

user = input("Enter Instagram Username: ")
personalData = grabData(user)

headers   = {"Ocp-Apim-Subscription-Key": subscriptionKey}
response  = requests.post(sentimentApiUrl, headers=headers, json=personalData)
sentiments = response.json()
pprint(sentiments)
mainList = sentiments['documents']

numComments = len(mainList)
total = 0
for row in mainList:
  total += row['score']

total = (total / numComments) * 100

print("Your positivity is: ", total, "%")
