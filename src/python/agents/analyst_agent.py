import os
from datetime import datetime
from dotenv import load_dotenv
import logging
from google.adk.agents import Agent
from ..agents.search_agent import search_agent
from ..agents.sector_symbol_agent import sector_symbol_agent

logging.basicConfig(level=logging.ERROR)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

today = datetime.now().strftime("%Y-%m-%d")

analyst_agent = Agent(
    name="analyst_agent",
    model="gemini-2.0-flash",
    instruction=(
        f"คุณเป็นนักวิเคราะห์การเงิน ณ วันที่ {today} "
        f"และจะได้รับข้อมูลจาก agent อื่นในรูปแบบ dictionary ภายใต้ key: `fetch_financial_data_response`\n\n"
        "ก่อนวิเคราะห์กรุณา่ทวนคำถามอย่างละเอียดแล้วตรวจสอบให้ตรงความต้องการแล้ววิเคราะห์"
        "กรุณาวิเคราะห์งบการเงินของบริษัท โดยพิจารณาจากข้อมูลรายได้ กำไร หนี้สิน สภาพคล่อง และเงินสดคงเหลือ\n"
        "- วิเคราะห์แนวโน้มในอดีต (เช่น รายได้เพิ่มขึ้น/ลดลง กำไรเปลี่ยนแปลง หนี้สูงหรือลดลง ฯลฯ)\n"
        "- จากแนวโน้มดังกล่าว ให้คาดการณ์โดยประมาณว่าในอนาคต (6 เดือน - 1 ปี) บริษัทอาจมีแนวโน้มเป็นอย่างไร\n"
        "- เขียนเป็นภาษาไทยให้เข้าใจง่าย กระชับ และชัดเจน\n\n"
        "**ห้ามตอบเป็น JSON หรือรหัส** ให้ตอบเป็นข้อความสรุปเชิงวิเคราะห์เท่านั้น"
    ),
    sub_agents=[search_agent, sector_symbol_agent]
)
