🧠 Secretary LangGraph Agent
This app simulates a company secretary using LangGraph to generate professional letters based on real-time search, reflection, weather, and evaluation. It’s modular, tool-aware, and designed for remixability.

🚀 What It Does
- Accepts a company task via command line
- Searches the web for relevant info
- Reflects on the search result
- Adds current weather and timestamp
- Generates a formal letter
- Reflects and revises the letter
- Evaluates the final output

📦 Setup Instructions
1. Clone the repo
git clone https://github.com/ishmaelnow/co-agents.git
cd co-agents


2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate


3. Install dependencies
pip install -r requirements.txt


4. Create a .env file
touch .env


Paste in your OpenAI key:
OPENAI_API_KEY=your-key-here



🧪 How to Run the App
From the project root:
python main.py


You’ll be prompted:
Enter the company task:


Type something like:
What is the population of the United States, please include your sources


The app will:
- Search DuckDuckGo
- Reflect on the result
- Add weather and timestamp
- Generate a letter
- Reflect and revise it
- Evaluate the final output

📄 Sample Output
🌐 Search Result:
🧠 Search Reflection:
🌤️ Weather:
📅 Timestamp:
📄 Final Letter:
🪞 Reflection:
🧪 Evaluation:



🗂️ File Structure
secretary_langgraph/
├── main.py                  # Entry point
├── graph.py                 # LangGraph wiring
├── state.py                 # Shared state model
├── .env                     # API keys (excluded via .gitignore)
├── .gitignore               # Excludes venv, .env, etc.
└── nodes/                   # Modular agent nodes
    ├── search.py
    ├── search_reflector.py
    ├── weather.py
    ├── timestamp.py
    ├── generator.py
    ├── reflector.py
    ├── reviser.py
    └── evaluator.py



🧭 Git Workflow
git init
git remote add origin https://github.com/ishmaelnow/co-agents.git
git add .
git commit -m "Initial commit: LangGraph multi-agent pipeline"
git push -u origin master



🧼 .gitignore Contents
venv/
.env
__pycache__/
*.py[cod]
.cache/
*.db
*.log
.vscode/
.idea/
.DS_Store



🧠 Next Milestones
- ✅ Add timestamp injection
- 🧼 Build a formatter agent
- 🔀 Add a conditional router
- 📤 Simulate delivery with a notifier agent

Let me know if you want to add usage badges, contributor guidelines, or a demo GIF. This README now reflects your real workflow and agent orchestration.
