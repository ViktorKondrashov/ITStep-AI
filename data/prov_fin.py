from langchain_classic import hub

prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")

print(prompt_template)