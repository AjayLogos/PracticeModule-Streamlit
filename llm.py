#%%

from typing import List, Dict
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
OPENAI_KEY = os.getenv("OPENAI_KEY")
class Option(BaseModel):
    option_body: str  # The answer choice
    is_correct: bool  # Tag to indicate if the answer is correct
    feedback: str  # Explanation for why the answer is correct or incorrect

class Outcome(BaseModel):
    guiding_question: str  # Question asking about the output of the step
    options: List[Option]  # List of multiple-choice options

class Step(BaseModel):
    name: str  # Name of the step
    step_body: str  # Description of the step to be taken
    outcome: Outcome  # The expected outcome of the step

class StepByStepSolution(BaseModel):
    steps: List[Step]  # List of all steps in the solution

class final(BaseModel):
    Name:str
    steps:List[StepByStepSolution]

class Hint(BaseModel):
    hint: str

class Hints(BaseModel):
    hints: List[Hint]
    
class Model:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_KEY)

    def structured_llm(self):
        return self.llm.with_structured_output(final)

    def hints_llm(self):
        return self.llm.with_structured_output(Hints)

