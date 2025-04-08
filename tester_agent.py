from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import List




GENERATOR_PROMPT = "You are an expert software tester. Analyze the given user story in depth and generate a comprehensive set of test cases, including functional, edge, and boundary cases, to ensure complete test coverage of the functionality."

load_dotenv()

class TestCase(BaseModel):
    test_case_id: int = Field(..., description="Unique identifier for the test case.")
    test_title: str = Field(..., description="Test Case Title")
    description: str = Field(..., description="Test Case Description")
    preconditions: str = Field(..., description="Test Case Precondition")
    postconditions: str = Field(..., description="Test Case Postcondition")
    test_steps: str = Field(..., description="A step-by-step guide on how to execute the test.")
    expected_result: str = Field(..., description="The anticipated outcome if the application works correctly.")
    comments: str = Field(..., description="Additional notes or observations.")
    severity: int = Field(..., description="Severity level of the test case")
    priority: int = Field(..., description="Priority level of the test case")



class OutputSchema(BaseModel):
    test_cases: List[TestCase] = Field(..., description="List of test cases.")

class State(TypedDict):
    test_cases:OutputSchema
    user_story: str

graph_builder = StateGraph(State)

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

llm_with_structured_output = llm.with_structured_output(OutputSchema)


def test_cases_generator(state:State):
    prompt = f'''{GENERATOR_PROMPT} \n\n
                Here is the user story :\n\n 
                {state['user_story']}'''


    response = llm_with_structured_output.invoke(prompt)
    return {"test_cases": response}


graph_builder.add_node('generator',test_cases_generator)
graph_builder.set_entry_point('generator')
graph_builder.set_finish_point('generator')

graph = graph_builder.compile()

def generate_test_cases(user_input: str):
    test_cases = []
    for event in graph.stream({'test_cases':[],'user_story':user_input}):
        for value in event.values():
           test_cases_list = value.get('test_cases', {}).test_cases if value.get('test_cases') else []
           test_cases = test_cases_list

    return test_cases

