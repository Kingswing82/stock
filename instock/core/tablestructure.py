#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import DATE, NVARCHAR, FLOAT, BIGINT, SmallInteger, DATETIME
from sqlalchemy.dialects.mysql import BIT
import talib as tl
from instock.core.strategy import enter
from instock.core.strategy import turtle_trade
from instock.core.strategy import climax_limitdown
from instock.core.strategy import low_atr
from instock.core.strategy import backtrace_ma250
from instock.core.strategy import breakthrough_platform
from instock.core.strategy import parking_apron
from instock.core.strategy import low_backtrace_increase
from instock.core.strategy import keep_increasing
from instock.core.strategy import high_tight_flag

__author__ = 'myh '
__date__ = '2023/3/10 '

RATE_FIELDS_COUNT = 100  # Number of rate fields for N-day returns

TABLE_STOCK_WATCHLIST = {
    'name': 'cn_stock_attention',
    'en': 'Stock Watchlist',
    'columns': {
        'datetime': {'type': DATETIME, 'en': 'Date', 'size': 0},
        'code': {'type': NVARCHAR(6), 'en': 'Code', 'size': 60}
    }
}

TABLE_ETF_DAILY = {
    'name': 'cn_etf_spot',
    'en': 'Daily ETF Data',
    'columns': {
        'date': {'type': DATE, 'en': 'Date', 'size': 0},
        'code': {'type': NVARCHAR(6), 'en': 'Code', 'size': 60},
        'name': {'type': NVARCHAR(20), 'en': 'Name', 'size': 120},
        'new_price': {'type': FLOAT, 'en': 'Latest Price', 'size': 70},
        'change_rate': {'type': FLOAT, 'en': 'Change Rate', 'size': 70},
        'ups_downs': {'type': FLOAT, 'en': 'Change Amount', 'size': 70},
        'volume': {'type': BIGINT, 'en': 'Volume', 'size': 90},
        'deal_amount': {'type': BIGINT, 'en': 'Turnover', 'size': 100},
        'open_price': {'type': FLOAT, 'en': 'Open Price', 'size': 70},
        'high_price': {'type': FLOAT, 'en': 'High Price', 'size': 70},
        'low_price': {'type': FLOAT, 'en': 'Low Price', 'size': 70},
        'pre_close_price': {'type': FLOAT, 'en': 'Previous Close', 'size': 70},
        'turnoverrate': {'type': FLOAT, 'en': 'Turnover Rate', 'size': 70},
        'total_market_cap': {'type': BIGINT, 'en': 'Total Market Cap', 'size': 120},
        'free_cap': {'type': BIGINT, 'en': 'Free Float Market Cap', 'size': 120}
    }
}