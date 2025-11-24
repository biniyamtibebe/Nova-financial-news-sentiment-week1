from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def score_headline(text):
    if pd.isna(text) or text.strip()=="":
        return 0.0
    return analyzer.polarity_scores(text)['compound']

def score_df(df, headline_col='headline'):
    df = df.copy()
    df['sentiment'] = df[headline_col].fillna("").apply(score_headline)
    return df
