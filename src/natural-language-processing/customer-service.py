import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('subjectivity')
nltk.download('movie_reviews')

analyzer = SentimentIntensityAnalyzer()

while True:
    next_message = input('Message: ')
    sentiment_score = analyzer.polarity_scores(next_message)
    compound_score = sentiment_score['compound']
    if (compound_score > 0):
        print("Positive comment")
    elif compound_score < 0:
        print("Negative comment")
    else:
        print("Neutral comment")
