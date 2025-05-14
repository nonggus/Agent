import os
from datetime import datetime
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")
import logging
logging.basicConfig(level=logging.ERROR)

from ..tools.api_tools import get_income_statement, get_balance_sheet, get_cashflow
from google.adk.agents import Agent

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

today = datetime.now().strftime("%Y-%m-%d")

async def fetch_financial_data(symbol: str):
    income = await get_income_statement(symbol)
    balance = await get_balance_sheet(symbol)
    cashflow = await get_cashflow(symbol)

    return {
        "symbol": symbol.upper(),
        "income_statement": income.get("Income Statement", []),
        "balance_sheet": balance.get("Balance Sheet Statement", []),
        "cash_flow": cashflow.get("Cash Flow Statement", []),
        "source": "API",
        "date_retrieved": today
    }

search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
     instruction=(
        "คุณทำหน้าที่ดึงข้อมูลงบการเงินของบริษัทในตลาดหุ้นไทยผ่าน API "
        "โดยใช้ tool `fetch_financial_data(symbol)` เท่านั้น\n\n"
        "เมื่อได้รับคำสั่ง ให้เรียกใช้ฟังก์ชันนี้โดยส่ง symbol "
        "แล้วคืนผลลัพธ์เป็น dictionary ที่มี income_statement, balance_sheet, cash_flow, symbol, source, date_retrieved\n\n"
        "**อย่าตอบเป็นข้อความ** หรือสรุปเอง"
    ),
    tools=[fetch_financial_data],
    description="ดึงงบการเงิน 3 ประเภทของบริษัทจาก API และคืนข้อมูลให้ agent หลักวิเคราะห์"
)
