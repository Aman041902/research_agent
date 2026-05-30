# ResearchMind

ResearchMind is a Streamlit-based multi-agent research assistant that chains together search, scraping, writing, and critique agents to generate polished research reports on any topic.

## 🚀 What it does

- Uses a **search agent** to gather recent and reliable information.
- Uses a **reader agent** to scrape and extract deeper content from linked sources.
- Uses a **writer chain** to compose a structured research report.
- Uses a **critic chain** to evaluate and improve the final output.

## 🧩 Project structure

- `app.py` — Streamlit application with interactive pipeline UI and progress tracking.
- `pipeline.py` — Scripted research pipeline for CLI usage and debugging.
- `agents.py` — Agent builder definitions, prompt templates, and model setup.
- `tools.py` — External tool integrations for web search and scraping.
- `requirements.txt` — Python dependencies.

## ⚙️ Requirements

- Python 3.10+ recommended
- `venv` or another virtual environment
- `TAVILY_API_KEY` for Tavily web search integration

## ✅ Quick start

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/research_agent.git
cd research_agent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # PowerShell
# or
.\venv\Scripts\activate.bat  # cmd
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with:

```dotenv
TAVILY_API_KEY=your_tavily_api_key_here
```

5. Run the app:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## 💡 Usage

### Streamlit UI

- Open `app.py` in your browser via Streamlit.
- Enter a research topic.
- Click **Run Research Pipeline**.
- The UI will show step-by-step progress across the search, reader, writer, and critic agents.

### CLI usage

Run the pipeline directly:

```bash
python pipeline.py
```

The CLI version will prompt for a topic and print progress messages.

## 🔧 Environment variables

The app uses environment variables loaded from `.env`:

- `TAVILY_API_KEY` — required for web search functionality.

> If you use a different search provider or custom API, update `tools.py` accordingly.

## 🧠 Notes

- `agents.py` uses `langchain_mistralai.ChatMistralAI` with `mistral-small-latest`.
- `tools.py` scrapes pages with `requests` and `jina.ai` markdown extraction.
- The pipeline is intentionally modular so you can swap tools, prompts, or models easily.

## 📌 Recommended enhancements

- Add error handling and retry logic around failed tool calls.
- Save generated reports to files automatically.
- Add support for multiple search results and content aggregation.

## License

Add a license file if you want to publish this repository publicly.
