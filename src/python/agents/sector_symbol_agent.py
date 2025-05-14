import os
import pandas as pd
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

CSV_PATH = r"D:\งานฉัน\PiProject\test-agent\src\listed_companies.csv"
companies_df = pd.read_csv(CSV_PATH)

def name_to_symbol(name: str) -> str:
    """รับชื่อบริษัทบางส่วน เช่น 'ปตท' แล้วคืน symbol เช่น 'PTT'"""
    match = companies_df[companies_df["company"].str.contains(name, case=False, na=False)]
    return match["symbol"].values[0] if not match.empty else "ไม่พบบริษัทที่ระบุ"

def get_symbols_by_sector(sector: str) -> list:
    """รับชื่อกลุ่มอุตสาหกรรม เช่น 'เทคโนโลยี' แล้วคืน symbol ที่ตรงกันทั้งหมด"""
    matched = companies_df[companies_df["industry_group"].str.contains(sector, case=False, na=False)]
    return matched["symbol"].tolist()

sector_symbol_agent = Agent(
    name="sector_symbol_agent",
    model="gemini-2.0-flash",
    instruction=(
        "คุณคือผู้ช่วยด้านหุ้นไทย รู้จักชื่อบริษัท และกลุ่มอุตสาหกรรมต่างๆ\n"
        "- ถ้าผู้ใช้ถามชื่อบริษัท เช่น 'ปตท' ให้ใช้ name_to_symbol\n"
        "- ถ้าผู้ใช้ถามหุ้นในกลุ่ม เช่น 'เทคโนโลยี' ให้ใช้ get_symbols_by_sector\n"
        "- หากไม่สามารถตอบได้ ให้ตอบว่าไม่พบข้อมูล"
    ),
    tools=[name_to_symbol, get_symbols_by_sector],
    description="Agent ช่วยแปลงชื่อบริษัทเป็น symbol หรือแนะนำหุ้นในกลุ่มอุตสาหกรรม"
)