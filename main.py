import requests
from pprint import pprint
from InstagramScrape import grabData
#from IPython.display import HTML

#Assert forces the statement to be true, if not then it'll crash at compile time
subscriptionKey = "ec76f8560b6a4e8e926c35e63ef8fb2a"
assert subscriptionKey

textAnalyticsBaseUrl = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"

#The commented out portion is used for determining the language used in the text.
#This is not useful to me as of right now.
#
# language_api_url = text_analytics_base_url + "languages"
# print(language_api_url)
#
# documents = { 'documents': [
#     { 'id': '1', 'text': 'This is the big man.' },
#     { 'id': '2', 'text': 'Este es un document escrito en Español.' },
#     { 'id': '3', 'text': '这是一个用中文写的文件' }
# ]}
#
# headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
# response  = requests.post(language_api_url, headers=headers, json=documents)
# languages = response.json()
# pprint(languages)
#
# table = []
# for document in languages["documents"]:
#     text  = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
#     langs = ", ".join(["{0}({1})".format(lang["name"], lang["score"]) for lang in document["detectedLanguages"]])
#     table.append("<tr><td>{0}</td><td>{1}</td>".format(text, langs))
# HTML("<table><tr><th>Text</th><th>Detected languages(scores)</th></tr>{0}</table>".format("\n".join(table)))

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
