# Remote Work During Iran War & Oil Crisis — CrewAI Mini Project

This project is a small **CrewAI multi-agent system** built for a class exercise on **Multi-Agent Systems**.  
The goal is to generate a short report about **remote work during the current Iran war and oil crisis** by combining perspectives from multiple stakeholders.

The project follows the pattern shown in the lecture material: define **agents**, define **tasks**, and connect them in a **sequential crew workflow** using `agents.yaml`, `tasks.yaml`, and `crew.py`. :contentReference[oaicite:0]{index=0}

---

## Project Objective

Write a report on:

> **Remote work during current Iran war & oil crisis**

using these stakeholder perspectives:

- CEO of a company
- Employee
- Minister of Energy
- Cleaner that gets paid by working day

Each agent contributes a role-specific analysis, and a final writer agent combines all outputs into one balanced report.

---

## Why this project uses multiple agents

Instead of asking one LLM to write everything at once, this project separates viewpoints by responsibility:

- **CEO** → focuses on business continuity, cost, productivity, and safety
- **Employee** → focuses on daily life, stress, flexibility, and work conditions
- **Minister of Energy** → focuses on national fuel usage, policy, and crisis response
- **Cleaner** → focuses on income loss and inequality for workers who cannot work remotely
- **Report Writer** → combines all stakeholder inputs into a final structured report

This makes the output more balanced and closer to real-world decision-making.

---

## Architecture

This project uses a **sequential workflow**:

1. CEO writes their analysis
2. Employee writes their analysis
3. Minister of Energy writes their analysis
4. Cleaner writes their analysis
5. Report Writer reads all previous outputs and writes the final report

This matches the lecture idea that tasks can be chained and the final task can use earlier tasks as **context**. :contentReference[oaicite:1]{index=1}

---

## Files in this project

```text
project/
├─ main.py
├─ crew.py
└─ config/
   ├─ agents.yaml
   └─ tasks.yaml