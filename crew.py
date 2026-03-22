
import os
from dotenv import load_dotenv
load_dotenv()

import yaml
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

agents_config = load_yaml("config/agents.yaml")
tasks_config  = load_yaml("config/tasks.yaml")

def make_agent(key):
    cfg = agents_config[key]
    return Agent(
        role=cfg["role"],
        goal=cfg["goal"],
        backstory=cfg["backstory"],
        llm=llm,
        verbose=False
    )

ceo                = make_agent("ceo")
employee           = make_agent("employee")
minister_of_energy = make_agent("minister_of_energy")
cleaner            = make_agent("cleaner")
report_writer      = make_agent("report_writer")

def make_task(key, agent):
    cfg = tasks_config[key]
    return Task(
        description=cfg["description"],
        expected_output=cfg["expected_output"],
        agent=agent
    )

ceo_task      = make_task("ceo_analysis_task",      ceo)
employee_task = make_task("employee_analysis_task", employee)
minister_task = make_task("minister_analysis_task", minister_of_energy)
cleaner_task  = make_task("cleaner_analysis_task",  cleaner)
report_task   = make_task("final_report_task",      report_writer)

class RemoteWorkIranCrisisCrew:
    def crew(self):
        return Crew(
            agents=[ceo, employee, minister_of_energy, cleaner, report_writer],
            tasks=[ceo_task, employee_task, minister_task, cleaner_task, report_task],
            process=Process.sequential,
            verbose=False
        )