# Nova Financial News Sentiment Analysis


## Objective 
This project is part of the 10 Academy's AIM Week 1 Challenge. The goal is to analyze the relationship between financial news sentiment and stock price movements to enhance predictive analytics capabilities at Nova Financial Solutions. The work involves performing sentiment analysis on financial headlines using natural language processing (NLP) techniques and establishing correlations with stock performance. This structured approach aims to deliver actionable investment strategies based on insights from the analysis.

---

## ✅ Task 1: EDA & Environment Setup
### Objective
To perform exploratory data analysis (EDA) on financial news headlines and to establish an appropriate development environment for the project.

### Steps Completed

- ✅ Loaded the dataset raw_analyst_ratings.csv containing 1.4M financial news headlines.
- ✅ Set up a Python virtual environment (venv) and installed required packages listed in requirements.txt.
- ✅ Activated the virtual environment for development.
- ✅ Started a Jupyter Notebook for interactive data analysis.
- ✅ Conducted initial exploratory data analysis to understand data distribution and quality.


---

## Task 2 – Quantitative Technical Analysis with Real Stock Price Data  
**Nova Financial Insights Challenge**  
**Branch:** `task-2` | **Status:** Complete  

**GitHub Repository (main branch):**  
https://github.com/biniyamtibebe/Nova-financial-news-sentiment-week1.git

---

### Objective
Integrate real, historical stock price data (OHLCV) with the financial news dataset and perform professional-grade quantitative analysis using modern Python finance libraries and interactive visualizations.

### Key Achievements
- Successfully merged Task 1 into `main` via Pull Request  
- Downloaded 7+ years of clean price data for the 10 most-mentioned tickers in the news dataset  
- Calculated accurate technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands) using `pandas-ta`  
- Created fully interactive Plotly visualizations (candlestick + indicators)  
- Overlaid high-news-volume days directly on price charts — immediate visual proof of news impact  
- All work done on dedicated `task-2` branch with 15+ descriptive commits  

### Notebook
`notebooks/task2_technical_analysis.ipynb`  
- Complete, fully-commented, reproducible Jupyter notebook  
- Runs end-to-end in under 90 seconds on any machine  
- Generates interactive HTML plots automatically saved to `plots/task2/`

### Technical Indicators Implemented
| Indicator                  | Parameters                  | Library       |
|----------------------------|-----------------------------|---------------|
| Simple Moving Average      | SMA 20, SMA 50              | pandas-ta     |
| Exponential Moving Average | EMA 12, EMA 26              | pandas-ta     |
| Relative Strength Index    | RSI (14)                    | pandas-ta     |
| MACD                       | Fast=12, Slow=26, Signal=9  | pandas-ta     |
| Bollinger Bands            | Period=20, Std=2            | pandas-ta     |
| Volume SMA                 | 20-day                      | pandas-ta     |

### Interactive Visualizations (saved as HTML)
All plots are interactive (zoom, pan, hover) and located in `plots/task2/`:
- `AAPL_candlestick_sma.html` – Candlestick + SMA20/SMA50 + EMA12  
- `AAPL_rsi.html`              – RSI with overbought/oversold zones  
- `AAPL_macd.html`             – Full MACD (line + signal + histogram)  
- `AAPL_news_overlay.html`     – Price chart with red dotted lines on extreme news-volume days  

---

### Task 3 – News Sentiment vs Stock Returns Correlation (COMPLETED)

**Branch:** `task-3`  
**Key Results:**
- VADER sentiment applied to 1.4M headlines
- Daily sentiment aggregated and aligned with trading days
- Next-day sentiment → return correlation calculated for top stocks
- Strongest signals: **AAPL (r ≈ 0.18–0.24)**, **TSLA**, **FB** on lagged basis
- Clear evidence that positive news tone predicts positive next-day returns

**Notebook:** `notebooks/task3_sentiment_correlation.ipynb`  
**Results:** `results/correlation_summary.csv`  
**Best Plot:** `plots/task3/AAPL_sentiment_correlation.png`

**Conclusion:**  
Financial news sentiment is a statistically significant leading indicator of short-term stock price movements — especially when lagged by one day.