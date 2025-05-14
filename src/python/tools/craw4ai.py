import asyncio

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://ai.pydantic.dev/",
        )
        print(result.markdown)
        
async def crawl( url: str):
    """ 
    Scrape a webpage and return the markdown content.
    
    Args:
        url (str): The URL of the webpage to scrape.
        
    Returns:
        str: The markdown content of the scraped webpage.
    
    """
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        return result.markdown
