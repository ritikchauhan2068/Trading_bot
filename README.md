# Binance Futures Trading Bot (Testnet)

This project is a **CLI-based trading bot** built in **Python** for placing **Market and Limit orders** on **Binance USDT-M Futures Testnet**.  
It follows a clean, modular structure with proper **validation**, **logging**, and **error handling**.

---

## 📁 Project Structure

Binance_Bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance client connection
│ ├── orders.py # Market & Limit order logic
│ ├── validators.py # Input validation
│
├── cli.py # CLI entry point
├── bot.log # Logs for orders & errors
├── README.md
├── requirements.txt
├── .env # API keys (not committed)


---

## ⚙️ Setup Steps

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd trading_bot

2️⃣ Create virtual environment (recommended)
python -m venv myenv
myenv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create .env file

Create a .env file in the project root:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key


⚠️ Make sure the API keys are from Binance Futures Testnet
URL: https://testnet.binancefuture.com

# ▶️ How to Run (Examples)

All commands must be run from the project root.

✅ Market Order Example
python cli.py symbol BTCUSDT side BUY type MARKET qty 0.001

✅ Limit Order Example
python cli.py symbol BTCUSDT side SELL type MARKET qty 0.001

# 📝 Logs

All API requests, responses, and errors are logged in:

bot.log


This includes:

Order placement details

API errors

Validation errors

# 📌 Assumptions

The bot is designed for Binance USDT-M Futures Testnet only.

The user has:

A valid Binance Futures Testnet account

Futures enabled for the API key

Internet connection is available.

The bot executes one order per run (no continuous trading loop).

Streamlit UI is optional and not required for core functionality.

# 🧠 Author Notes

This project focuses on:

Clean architecture

Reusability

Industry-style CLI design

Proper logging & validation


---

# 📄 `requirements.txt`

```txt
python-binance
python-dotenv
loguru

