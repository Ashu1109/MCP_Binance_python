#!/usr/bin/env python3
import asyncio
import json
from apis import (
    exchange_info_of_a_symbol,
    exchange_info_of_all_symbols,
    get_trade_data,
    agg_trades,
    trade_history,
    depth,
    current_avg_price,
    price_ticker_in_24hr,
    trading_day_ticker,
    symbol_price_ticker,
    symbol_order_book_ticker,
    rolling_window_ticker
)

async def test_apis():
    """Test all Binance API functions."""
    # Test symbol
    symbol = "BTCUSDT"
    
    print("\n==== Testing Exchange Info for a Symbol ====")
    result = await exchange_info_of_a_symbol(symbol)
    print(result[:200] + "..." if len(result) > 200 else result)
    
    print("\n==== Testing Get Trade Data ====")
    result = await get_trade_data(symbol, "1h", limit=5)
    print(result[:200] + "..." if len(result) > 200 else result)
    
    print("\n==== Testing Aggregate Trades ====")
    result = await agg_trades(symbol)
    print(result[:200] + "..." if len(result) > 200 else result)
    
    print("\n==== Testing Current Average Price ====")
    result = await current_avg_price(symbol)
    print(result)
    
    print("\n==== Testing Symbol Price Ticker ====")
    result = await symbol_price_ticker(symbol)
    print(result)
    
    print("\n==== Testing Multiple Symbol Price Ticker ====")
    result = await symbol_price_ticker(symbols=["BTCUSDT", "ETHUSDT"])
    print(result[:200] + "..." if len(result) > 200 else result)

if __name__ == "__main__":
    asyncio.run(test_apis())
