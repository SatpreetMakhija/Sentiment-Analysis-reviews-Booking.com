import json
import nltk
import string

from pathlib import Path 
import os
from nltk.tokenize import word_tokenize
#stopwords are words such as "a", "an", "be", "I", etc. We will remove them when analysing the sentiments.
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

checkout_array = list()
checkout_hotel_details_array = list()


#fetch the json file
current_path = str(Path().absolute())
data_path = current_path + "/dataset/singapore.json"

#we will use the nltk's SentimentAnalyzer to get the return value
def analyse_sentiment(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    positive, negative, neutral, compound = score["pos"], score["neg"], score["neu"], score["compound"]
    return compound
# test = list()
# test.append("good")
# test.append("value") 
# # = ["good", "value", "money"]
# x = analyse_sentiment(test)
# print(x)



with open(data_path) as file:
    data_content = json.loads(file.read())

for i in range(len(data_content)):
    temp_list = list()
    for j in data_content[i]["reviews"]:
        current_review = data_content[i]["reviews"][j]["content"]
        current_review = current_review.lower()
        #remove special characters from the review comments
        review_comments = current_review.translate(str.maketrans('', '', string.punctuation))
        tokenized_reviews = word_tokenize(review_comments, "english")

        final_review_comments = list()
        #time to remove stopwords from the tokenized_review
        for word in tokenized_reviews:
            if word not in stopwords.words("english"):
                final_review_comments.append(word)

        total = analyse_sentiment(review_comments)
        temp_list.append(abs(total))

    checkout_array.append([float(data_content[j]['score']), statistics.median(temp_list) * 10])
    checkout_hotel_details_array.append([ statistics.median(temp_list) * 10, data_content[j]['name'], data_content[j]['location']])
    
checkout_hotel_details_array.sort()
kuala_lumpur_hotel_final = json.dumps(checkout_hotel_details_array[: 10], indent = 4)
with open ('singapore_details.json', 'w') as f:
    f.write(kuala_lumpur_hotel_final)
# Saving the top 10 hotels data to csv
with open('singapore_details.csv', 'w', newline='') as myfile:
    header_names = ["V1", "V2"]
    wr = csv.writer(myfile)
    wr.writerows(checkout_hotel_details_array[: 10])








