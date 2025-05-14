import httpx

async def get_income_statement(symbol: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/symbol={symbol}/income/")
        response.raise_for_status()
        return response.json()

async def get_balance_sheet(symbol: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/symbol={symbol}/balancesheet/")
        response.raise_for_status()
        return response.json()

async def get_cashflow(symbol: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/symbol={symbol}/cashflow/")
        response.raise_for_status()
        return response.json()
