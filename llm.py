#%%

from typing import List, Dict
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Access variables
OPENAI_KEY = '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'
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

