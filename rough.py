from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful {topic}"),
    ("user", "Tell me a joke about {topic}")
])

result = prompt_template.invoke({"topic": "cats"})
print(result)