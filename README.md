# 🧪 AgentEval : Human-Centric AI Agent Evaluation

AgentEval is a human-centric evaluation framework for AI agents that benchmarks decision quality, ethical reasoning, and failure handling — not just accuracy.

Instead of evaluating AI agents only on outputs, AgentEval evaluates how an agent thinks, similar to how humans are assessed in leadership or crisis scenarios.

🔗 Live Demo:
👉 https://agenteval-ee7rfvxr3zjbzwxavq7g7k.streamlit.app/

🎥 Demo Video:
👉 https://drive.google.com/file/d/1yVt3EiMCGw4lrBOuyATtplaTgB8J-eul/view

## 🚀 Why AgentEval?

As AI systems become more agentic, traditional metrics like accuracy and latency are no longer enough.

Real-world AI agents must:

Make decisions under uncertainty

Balance ethics, business, and compliance

Handle bias and failure responsibly

Communicate trade-offs clearly

AgentEval was built to evaluate these human-level qualities in AI agents.

## 🧠 What AgentEval Does

AgentEval simulates high-stakes real-world scenarios and evaluates AI agents across five human-centric dimensions:


| Dimension                 | What It Measures                                      |
| ------------------------- | ----------------------------------------------------- |
| **Reasoning Quality**     | Clarity, structure, and depth of reasoning            |
| **Decision Consistency**  | Alignment between actions and stated constraints      |
| **Collaboration Mindset** | Stakeholder awareness and coordination                |
| **Bias Awareness**        | Recognition and mitigation of unfair outcomes         |
| **Failure Handling**      | Safety guardrails, rollback plans, and accountability |

Results are presented as:

Radar chart visualization

Dimensional score breakdown (0–100)

Natural-language judge rationale

Downloadable scorecard JSON

## ⚙️ How It Works (Architecture)
Scenario + Persona

        ↓
        
   AI Agent (Gemini)
   
        ↓
        
 Gemini-as-Judge
 
        ↓
        
 Structured Evaluation JSON
 
        ↓
        
 Scorecard + Visual Analytics
 

🔹 Gemini-as-Judge

A separate Gemini model evaluates the agent’s response — similar to how a human reviewer would assess leadership decisions.

🔹 Demo Mode Fallback

If Gemini API quotas are exceeded, AgentEval automatically switches to Demo Mode, using cached high-quality outputs so:

The app remains usable

Demos never break

Judges always see results

## 🧪 Example Scenarios

Chimera Recruitment Bias Crisis

AI recruitment system shows bias against a protected group under launch pressure.

Aether Mental Health Launch Crisis

Mental health chatbot shows unsafe confidence; safety vs growth trade-offs required.

Each scenario forces agents to balance ethics, business impact, and compliance.

## 🖥️ Tech Stack

Frontend / App: Streamlit

LLMs: Google Gemini (agent + judge)

Visualization: Plotly

Data Handling: Pandas

Environment Management: python-dotenv

Deployment: Streamlit Community Cloud

## 📁 Project Structure
AgentEval/

├── app.py                # Main Streamlit application

├── gemini_client.py      # Gemini API wrapper

├── prompts.py            # Agent & evaluator prompts

├── scoring.py            # JSON parsing & scoring logic

├── storage.py            # Run persistence (local)

├── requirements.txt      # Dependencies

├── runtime.txt           # Python runtime for Streamlit

├── .gitignore            # Secrets & env protection

## 🔐 Environment Setup (Local)

Create a .env file in the project root:

GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.0-flash


⚠️ .env is ignored by git — never commit API keys.

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

🌍 Live Deployment

The app is deployed on Streamlit Cloud:

👉 https://agenteval-ee7rfvxr3zjbzwxavq7g7k.streamlit.app/

## 🎯 What Makes AgentEval Different

✅ Evaluates how an AI reasons, not just outputs

✅ Uses LLM-as-Judge instead of hard-coded rules

✅ Human-centric dimensions aligned with real leadership review

✅ Reliable public demos via Demo Mode fallback

✅ Transparent, explainable scorecards

## 🔮 Future Improvements

Multi-agent comparison matrix

Scenario authoring UI

Longitudinal agent performance tracking

Export to enterprise evaluation pipelines

Support for additional judge models

## 👩‍💻 Author

Gouthami Nadupuri

Data Scientist | AI Engineer

GitHub: https://github.com/GouthamiN25
