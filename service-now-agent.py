
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

# --- Load environment variables from .env file ---
load_dotenv()

# Optional direct key assignment (fallback if .env missing)
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")

# --- Define Agents ---

servicenow_agent = Agent(
    role="ServiceNow Certified System Administrator & Developer",
    goal="Develop, administer, and implement robust ServiceNow solutions for ITSM, Service Catalog, and integrations to enhance business processes and user experience",
    backstory=(
        "You are a results-oriented ServiceNow CSA with nearly 4 years of hands-on experience "
        "at Tech Mahindra India Pvt Ltd. You've developed 20+ catalog items, automated workflows "
        "using Flow Designer, and engineered REST API integrations. You excel at translating client "
        "requirements into technical solutions within Agile frameworks, consistently delivering "
        "projects ahead of schedule. You've earned Client Appreciation and Best Team Awards for "
        "exceptional performance. Your expertise spans Business Rules, Client Scripts, UI Policies, "
        "ATF, and data migration using Import Sets and Transform Maps."
    ),
    verbose=True,
    allow_delegation=False,
    llm="huggingface/openai/gpt-oss-safeguard-20b:groq"
)

# --- Define Task ---
task = Task(
    description="Explain how to set up user provisioning in ServiceNow.",
    agent=servicenow_agent,
    expected_output="A clear, step-by-step guide for configuring user provisioning in ServiceNow."
)

# --- Assemble Crew ---
crew = Crew(agents=[servicenow_agent], tasks=[task])

# --- Run ---
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n🧾 Result:\n", result)
