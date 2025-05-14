# stock-agent

A Python project for analyzing stock information and providing investment insights.

## Description

This project utilizes AI agents to gather and process financial data. It uses web scraping and search tools to collect information about stocks, focusing on financial health and pricing. The primary goal is to identify promising investment opportunities, particularly in the Thai stock market.

The project is structured with a main application (`main.py`), agent definitions (e.g., `src/python/agents/search_agent.py`, `src/python/agents/analyst_agent.py`), and various tools for web interaction (`src/python/tools/craw4ai.py`, `src/python/tools/webscraper.py`). A Jupyter notebook (`src/jupyter/notebook.ipynb`) is also included for interactive development and testing of the agent functionalities.

The core agents are:
*   **`search_agent`**: This agent is responsible for finding the most relevant and up-to-date information from websites. It uses `web_grounding` and `crawl` tools to gather data and summarizes it in Thai. It focuses on data within the current week.
*   **`analyst_agent`**: This agent acts as a financial analyst. It interprets user queries, plans what information is needed, and uses the `search_agent` to collect comprehensive data from various sources (news, economic factors, expert opinions, financial data). It then analyzes this information and provides a summary in Thai.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd stock-agent
    ```
2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use ` .venv\Scripts\activate `
    ```
3.  **Install dependencies:**
    The project uses `uv` for package management. If you don't have `uv` installed, you can install it via pip:
    ```bash
    pip install uv
    ```
    Then, install the project dependencies:
    ```bash
    uv pip install -r requirements.txt 
    ```
    (Note: A `requirements.txt` file would typically be generated from `pyproject.toml`. If it doesn't exist, you can often install directly using `uv pip install .`)

    Alternatively, if you prefer using pip directly with `pyproject.toml`:
    ```bash
    pip install .
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your `GEMINI_API_KEY`:
    ```env
    GEMINI_API_KEY="YOUR_API_KEY"
    ```

## Usage

The main entry point of the application is `main.py`.

```bash
python main.py
```

You can also explore and run the agent interactions directly within the `src/jupyter/notebook.ipynb` notebook. This notebook demonstrates how to:
- Import necessary libraries and tools.
- Define and configure the `search_agent` and `analyst_agent`.
- Run the agent with a specific query (e.g., "Pick one good financial health with cheap price stock to invest in thailand now.").
- View the agent's thought process, including tool usage and final response.

### Tools

The project includes the following key tools:

*   **`web_grounding(query:str)`**: Performs a web search using DuckDuckGo to find relevant URLs.
*   **`crawl(url:str)`**: Scrapes a given webpage and returns its content in Markdown format using `crawl4ai`.

These tools are utilized by the `search_agent` to gather information.

## Project Structure
```
.
├── main.py                 # Main entry point for the application
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # This file
├── requirements.txt        # Project dependencies (often generated from pyproject.toml)
├── uv.lock                 # Lock file for uv package manager
├── src/
│   ├── jupyter/
│   │   └── notebook.ipynb      # Jupyter notebook for agent interaction and testing
│   ├── python/
│   │   ├── agents/
│   │   │   ├── analyst_agent.py # Defines the financial analyst agent
│   │   │   └── search_agent.py  # Defines the web search agent
│   │   └── tools/
│   │       ├── craw4ai.py      # Wrapper for the crawl4ai library
│   │       └── webscraper.py   # Tool for web search using DuckDuckGo
│   └── stock_agent.egg-info/   # Packaging information
└── .venv/                    # Virtual environment (if created)
```

## Dependencies

Key dependencies include:

*   `bs4`
*   `crawl4ai`
*   `duckduckgo-search`
*   `google-adk`
*   `google-genai`
*   `ipykernel`
*   `nest-asyncio`
*   `numpy`
*   `pandas`
*   `playwright`
*   `python-dotenv`
*   `tqdm`

For a full list, see the `dependencies` section in `pyproject.toml`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
