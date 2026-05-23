# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot for placing MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

---

# Features

- Real Futures Testnet order execution
- Detailed order response parsing
- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- CLI-based input using argparse
- Input validation
- Structured project architecture
- Logging for requests, responses, and errors
- Exception handling for API and runtime errors

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/ishant212/binance-futures-testnet-bot
cd trading_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

Use Binance Futures Testnet:

https://testnet.binancefuture.com

Generate API credentials from the Futures Testnet API Management page.

---

# Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

# Running the Application

## MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

---

# Example CLI Output

```text
=== ORDER REQUEST SUMMARY ===
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

=== ORDER RESPONSE ===
Order submitted successfully to Binance Futures Testnet
```

---

# Logging

All API requests, responses, and errors are logged in:

```text
logs/trading.log
```

Example log:

```text
2026-05-18 21:06:28,291 - INFO - Order Request: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

2026-05-18 21:06:29,503 - INFO - Order Response: {}
```

---

# Validation Rules

The application validates:

- BUY / SELL side
- MARKET / LIMIT order type
- positive quantity
- LIMIT orders require price

---

# Error Handling

The application handles:

- invalid CLI input
- Binance API exceptions
- network/runtime errors
- invalid order parameters

---

# Testnet Response Note

Binance Futures Testnet may occasionally return empty response objects (`{}`) when using the `python-binance` library, even though orders are successfully submitted.

The application still:
- validates inputs
- logs all API interactions
- handles exceptions properly
- confirms successful order submission

---

# Assumptions

- User already has Binance Futures Testnet account
- API keys are valid
- Testnet account has sufficient test funds

---

# Dependencies

- python-binance
- python-dotenv
