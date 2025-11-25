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


df = pd.read_csv(r'C:\Users\hp\Documents\nova-financial-news-sentiment\Nova-financial-news-sentiment-week1\data\raw_analyst_ratings.csv', parse_dates=["date"])
df = score_df(df)
df.to_csv(r'C:\Users\hp\Documents\nova-financial-news-sentiment\Nova-financial-news-sentiment-week1\data\raw_analyst_ratings.csv', index=False)
df = pd.read_csv("data/processed/news_scored.csv", parse_dates=['date'])


daily_sentiment = (
    df.groupby(['stock', 'trading_date'])['sentiment']
    .agg(['mean','count','std'])
    .rename(columns={'mean':'sentiment_mean','count':'sentiment_count','std':'sentiment_std'})
    .reset_index()
)
daily_sentiment.to_csv("data/processed/daily_sentiment.csv", index=False)
