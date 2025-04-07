#%%
import json
from llm import Model
from utils import get_prompt


llm = Model()
solution_llm = llm.structured_llm()
hints = llm.hints_llm()
#%%
def get_reponse(id):
    query = get_prompt(id)
    return query
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            # %%
def get_hints(query:list):
    response = hints.invoke(query)
    res = []
    for hint in response.hints:
        res.append(hint.hint)
    print("hints:" , res)
    return res


# %%
def get_solution(query:list):
    response = solution_llm.invoke(query)
    # print(response)
    response = response.model_dump(mode="json")
    print("solution:" , response)
    print("----------------------------------------------------------------------------------------")
    return response

# %%
# text = {'Title': 'Calculating the Value of (X/20Y) for Gas Behavior', 'steps': [{'steps': [{'name': 'Understanding the Ideal Gas and Compressibility', 'step_body': 'In this step, we consider both the behavior of the gas according to real conditions (where it is not ideal) and how it behaves as an ideal gas. The compressibility factor z helps us understand the deviation from the ideal behavior.', 'outcome': {'guiding_question': 'What is the compressibility factor of the gas under given conditions?', 'options': [{'option_body': '0.5', 'is_correct': True, 'feedback': 'Correct, the compressibility factor is given as 0.5.'}, {'option_body': '1.0', 'is_correct': False, 'feedback': 'Incorrect, 1.0 is the compressibility factor for ideal gases.'}, {'option_body': '2.0', 'is_correct': False, 'feedback': 'Incorrect, 2.0 is not given as the compressibility factor.'}]}}, {'name': 'Express Ideal Gas Behavior (PV=ZRT)', 'step_body': 'Here we set up the equation PV=ZRT considering the compressibility factor z and solve for pressure (P) using the given compressibility factor and temperature.', 'outcome': {'guiding_question': 'What equation represents the real gas behavior including the compressibility factor?', 'options': [{'option_body': 'P=ZRT', 'is_correct': True, 'feedback': 'Correct, this accounts for the compressibility factor in real gas behavior.'}, {'option_body': 'P=RT', 'is_correct': False, 'feedback': 'Incorrect, this would not account for the gas behavior deviation.'}, {'option_body': 'P=R/ZT', 'is_correct': False, 'feedback': 'Incorrect, this manipulates the compressibility factor incorrectly.'}]}}, {'name': 'Find Pressure Using Compressibility Equation', 'step_body': 'By rearranging the equation to find pressure, you substitute the values for R, T, and z into the equation to calculate the partial pressure of the gas.', 'outcome': {'guiding_question': 'How is pressure (P) represented in terms of R, T, and Z?', 'options': [{'option_body': 'P = 0.5 RT', 'is_correct': True, 'feedback': 'Correct, substituting z into the equation gives this relation.'}, {'option_body': 'P = 1.5 RT', 'is_correct': False, 'feedback': 'Incorrect, the factor 0.5 is needed here.'}, {'option_body': 'P = RT/0.5', 'is_correct': False, 'feedback': 'Incorrect, this equation is not correctly set up for P.'}]}}, {'name': 'Solving for Molar Volume Under Ideal Conditions', 'step_body': 'Next, by considering the gas behaving ideally under the same conditions, the molar volume of the gas (Vm) is calculated based on the ideal gas law (PV = RT).', 'outcome': {'guiding_question': 'What is the expression for molar volume under ideal conditions?', 'options': [{'option_body': 'Vm = RT/P', 'is_correct': True, 'feedback': 'Correct, under ideal conditions Vm is RT over P.'}, {'option_body': 'Vm = P/RT', 'is_correct': False, 'feedback': 'Incorrect, this inverse expression is wrong.'}, {'option_body': 'Vm = zRT/P', 'is_correct': False, 'feedback': 'Incorrect, z should not appear in the correlation for ideal.'}]}}, {'name': 'Calculate the Ratio x/(20y)', 'step_body': 'Using the molar volume from ideal gas behavior and comparing it to real gas pressure, the problem ultimately asks us to find the expression x/(20y). This is found by manipulating previously found expressions.', 'outcome': {'guiding_question': 'What is the final computed value of (x/20y)?', 'options': [{'option_body': '5', 'is_correct': True, 'feedback': 'Correct, the calculations give this ratio.'}, {'option_body': '10', 'is_correct': False, 'feedback': 'Incorrect, check calculations again.'}, {'option_body': '25', 'is_correct': False, 'feedback': 'Incorrect, this answer does not match the logical calculation.'}]}}]}]}
# with open("solution1.json", "w", encoding="utf-8") as json_file:
#     json.dump(text, json_file, indent=4, ensure_ascii=False)
# # %%
# import pandas as pd
# import json
# from docx import Document
# from docx.shared import Pt
# from docx.oxml import OxmlElement
# from docx.oxml.ns import qn


# def format_entry(hints, entry):
#     """Formats a single dictionary entry into a readable text format with bold headings."""
#     formatted_text = []
    
#     # Add hints as an ordered list
#     if hints:
#         formatted_text.append(("Hints:", ""))
#         for i, hint in enumerate(hints, 1):
#             formatted_text.append((f"{i}. ", hint))

#     for step_group in entry.get('steps', []):
#         for step in step_group.get('steps', []):
#             formatted_text.append(("Step Name: ", step['name']))
#             formatted_text.append(("Step Body: ", step['step_body']))
            
#             outcome = step.get('outcome', {})
#             formatted_text.append(("Guiding Question: ", outcome.get('guiding_question', '')))
            
#             for option in outcome.get('options', []):
#                 correctness = "True" if option['is_correct'] else "False"
#                 formatted_text.append(("  - Option: ", option['option_body']))
#                 formatted_text.append(("    - Correct: ", correctness))
#                 formatted_text.append(("    - Feedback: ", option['feedback']))
    
#     return formatted_text

# def write_to_docx(df, filename="output.docx"):
#     """Writes the formatted text to a .docx file in a table format with bold headings."""
#     doc = Document()
#     table = doc.add_table(rows=1, cols=2)
#     table.style = 'Table Grid'
    
#     # Setting up header row
#     hdr_cells = table.rows[0].cells
#     hdr_cells[0].text = "CMS-ID"
#     hdr_cells[1].text = "step_by_step_solution"
    
#     for _, row in df.iterrows():
#         cms_id = row["CMS-ID"]
#         try:
#             prompt = get_reponse(cms_id)
#         except:
#             continue
#         hints = get_hints(prompt['hints_prompt'])  # Fetch hints for ID
#         entry = get_solution(prompt['solution_prompt'])  # Fetch solution for ID
#         formatted_text = format_entry(hints, entry)
        
#         row_cells = table.add_row().cells
#         row_cells[0].text = str(cms_id)  # ID column
        
#         # Add formatted text to the second column with bold headings
#         p = row_cells[1].paragraphs[0]
#         for bold_text, normal_text in formatted_text:
#             run = p.add_run(bold_text)
#             run.bold = True
#             p.add_run(normal_text + "\n")
    
#     doc.save(filename)

# import pandas as pd
# df = pd.read_csv("C:/Users\Abcom\Desktop\data_updated.csv")
# df_sampled = df.groupby("Subject").sample(n=20, random_state=42)  
# # Writing to a Word document
# write_to_docx(df_sampled)  
# # %%

# # %%
# df_sampled
# %%


#docker run --name redis-container -p 6379:6379 -d redis