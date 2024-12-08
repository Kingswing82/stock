# InStock Trading System

InStock is a comprehensive stock market analysis system that captures daily stock and ETF data, calculates various technical indicators, identifies chart patterns, provides integrated stock screening, and includes multiple built-in trading strategies. The system supports backtesting, automated trading, and batch processing. It runs efficiently and is accessible on PC, tablet, and mobile devices. A Docker image is also provided for easy installation.

Project Repository: https://github.com/myhhub/stock
Docker Image: https://hub.docker.com/r/mayanghua/instock (Optimized build only 170MB)

## Features

### 1. Comprehensive Stock Screening
The system supports over 200 screening criteria across multiple categories:

```
1. Market Scope
   - Markets, Industries, Regions, Concepts
   - Styles, Index Components, Listing Date

2. Fundamentals
   - Valuation Metrics
   - Per-share Indicators
   - Profitability Metrics
   - Growth Potential
   - Capital Structure and Solvency
   - Share Capital and Shareholders

3. Technical Analysis
   - MACD Golden Cross
   - KDJ Golden Cross
   - Volume Breakout
   - Low-level Fund Inflow
   - High-level Fund Outflow
   - Moving Average Breakout
   - Bullish MA Alignment
   - Bearish MA Alignment
   - Continuous Rise with Volume
   - Decline without Volume
   - Single Large Yang Line
   - Double Large Yang Line
   - Rising Sun
   - Strong Momentum
   - Seven Consecutive Negative Days
   - Eight Consecutive Positive Days
   - Nine Consecutive Positive Days
   - Four Consecutive Yang
   - Super Volume Rules
   - Volume Breakout
   - And many more pattern indicators...

4. Market News
   - Major Announcements
   - Institutional Coverage
   - Number of Institutional Shareholders
   - Institutional Shareholding Ratio

5. Popularity Metrics
   - Stock Forum Rankings
   - Ranking Changes
   - Consecutive Ranking Increases
   - Consecutive Ranking Decreases
   - New Ranking Highs
   - New Ranking Lows
   - New Follower Ratio
   - Core Follower Ratio
   - 7-day Attention Ranking
   - Daily View Ranking

6. Market Data
   - Price Performance
   - Trading Volume
   - Capital Flow
   - Market Statistics
   - Stock Connect Data
```

### 2. Daily Stock Data
Includes:
- Daily stock data
- Capital flow analysis
- Dividend distribution
- Top trader activity
- Block trades
- Fundamental data
- Industry capital flow
- Concept capital flow
- Daily ETF data

The system captures key A-share market data daily and encapsulates the data collection methods for easy system expansion.

### 3. Technical Indicators
Based on TA-Lib and pandas, the system efficiently calculates various technical indicators:

```
1. MACD    2. KDJ     3. BOLL    4. TRIX, TRMA    5. CR     6. SMA     7. RSI
8. VR, MAVR    9. ROC    10. DMI, +DI, -DI, DX, ADX, ADXR    11. W&R
12. CCI    13. TR, ATR    14. DMA, AMA    15. OBV    16. SAR    17. PSY
18. BRAR    19. EMV    20. BIAS    21. TEMA    22. MFI    23. VWMA
24. PPO    25. WT    26. Supertrend    27. DPO    28. VHF    29. RVI
30. FI    31. ENE    32. STOCHRSI
```

### 4. Buy/Sell Signal Analysis
Identifies potential buy/sell signals based on technical indicators:

```
KDJ:
1. Overbought: K>80, D>70, J>90
   - Price likely to decline
   - Outside investors should avoid chasing
   - Existing holders consider selling

2. Oversold: K<20, D<30
   - Price likely to rise
   - Holders should avoid panic selling
   - Good entry opportunity

RSI:
1. 6-day RSI>80: Overbought warning
   RSI>90: Severe overbought, high reversal risk

2. 6-day RSI<20: Oversold signal
   RSI<10: Severe oversold, potential bottom

[Additional indicator signals detailed in original documentation]
```

### 5. Chart Pattern Recognition
Accurately identifies 61 chart patterns, including:
```
1. Two Crows                     2. Three Black Crows
3. Three Inside Up/Down         4. Three-Line Strike
5. Three Outside Up/Down        6. Three Stars in South
7. Three White Soldiers         8. Abandoned Baby
[Complete pattern list in original documentation]
```

Pattern recognition results:
```
Negative: Sell signal
0: Pattern not present
Positive: Buy signal
```

### 6. Trading Strategies
Built-in strategies include volume breakout, platform detection, annual line pullback, and more. Strategy template available for custom implementation.

[Detailed strategy specifications maintained from original]

### 7. Strategy Validation
Backtesting support for validating indicators and strategies.

### 8. Automated Trading
Supports automated trading with built-in IPO subscription strategy. Includes trading logs and strategy-specific logging.

**Note**: IPO subscription triggers at 10:00 AM on trading days. Remove stagging.py or disable trading service to prevent automatic IPO subscription.

### 9. Watchlist
Supports stock watchlist with pinned and highlighted display across modules.

### 10. Batch Processing
Supports:
```
------ Full Job Batch Processing ------
Current date:    python execute_daily_job.py
Single date:     python execute_daily_job.py 2022-03-01
Multiple dates:  python execute_daily_job.py 2022-01-01,2021-02-08,2022-03-12
Date range:      python execute_daily_job.py 2022-01-01 2022-03-01

------ Individual Jobs with Automatic Backfill ------
Basic real-time data:      python basic_data_daily_job.py
Non-real-time basic data:  python basic_data_other_daily_job.py
Indicator calculation:     python indicators_data_daily_job.py
Pattern recognition:       python klinepattern_data_daily_job.py
Strategy execution:        python strategy_data_daily_job.py
Backtesting:              python backtest_data_daily_job.py
```

[Installation instructions and remaining sections translated in subsequent messages due to length...]

Would you like me to continue with the installation instructions and remaining sections of the README?