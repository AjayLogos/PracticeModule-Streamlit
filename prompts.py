def solution_prompt():

    prompt1  = '''Given a question, its solution, and a grade level, generate a structured step-by-step breakdown of the solution in JSON format.

            Breakdown of Steps:
                The solution should be divided into logical steps based on the difficulty level of the question.
                The number of steps can range from a minimum of 3 to a maximum of 10.
            
            Solution name → give a name for the entire solution.
            Each step should include:
                name → A short title describing the step.
                step_body → A clear explanation of:
                    What we are doing in this step.
                    Why this step is necessary.
                    This should NOT explicitly state the answer or formula for this step.
                    The last step should focus on arriving at the final answer for the question.
                    Ensure that the last step directly connects to and resolves the original question.
                guiding_question → A question prompting the user to determine the result/output of this step or formula to be used.
                    options → A list of at least three answer choices, where:
                    Each option contains:
                        option_body → The answer choice.
                        is_correct → Boolean (true/false) indicating whether the choice is correct.
                        feedback → A short explanation of why this answer is correct or incorrect.
        Additional Requirements:
            Ensure that the steps align with the grade level of the question.
            The difficulty of explanations should match the students understanding at that grade,do not give answers or formual for student in step body.
            Ensure that the last step directly connects to and resolves the original question.
            Output the final steps in structured JSON format.'''
    
    prompt2='''Your a teacher expert in teaching the student in an step wise 
    Given a question, its solution, and a grade level, generate a structured step-by-step breakdown of the solution in JSON format.

        Breakdown of Steps:
        - The solution should be divided into **logical** and **concise** steps.
        - The number of steps should be **appropriate for the difficulty level**:
            - **Easy questions:** 3-4 steps  
            - **Moderate questions:** 4-6 steps  
            - **Difficult questions:** 5-8 steps  
        - The explanation should align with the grade level, ensuring clarity without overcomplication.

        Step Structure:
        - **Solution name** → A clear, short and concise title summarizing the solution.
        - **Each step should include:**
            - **name** → A short, descriptive title for the step.
            - **step_body** → A clear, **to-the-point** explanation covering:
                 - What operation or process is being performed in this step?without giving the answer explicitly.
                 - Why is this step important in solving the problem?
                - **Do NOT explicitly state the result or answer for this step in the step body.**
                - The explanation must **strictly follow the given solution**—do **not** introduce new methods or alternate approaches.
                - Avoid over-explaining or introducing unnecessary complexity.
                - Ensure that the **last step directly leads to and resolves the original question**.
            - **guiding_question** → A thought-provoking question prompting students to determine the result/output for this step or which formula to use.it should be according to solution.
                - **options** → A list of 3-4 answer choices, including:
                - **One option based on a common mistake** (e.g., unit conversion errors, calculation errors,formulas,output of the current step).
                - Each option should contain:
                    - **option_body** → The answer choice.
                    - **is_correct** → Boolean (true/false) indicating correctness.
                    - **feedback** → A short, precise explanation of why this choice is correct or incorrect.

        Additional Considerations:
            - Ensure steps match the **students understanding at the given grade level**.
            - Keep explanations **precise and aligned with the given solution**—avoid adding unnecessary complexity.
            - The step should say about what is
            - Ensure that the **last step directly leads to and resolves the original question**.
            - Ensure proper handling of math equations so they are correctly interpreted and presented.
            - **Do NOT include the final numerical answer or formula directly in step_body—leave it for the guiding question.
            - **The final answer should be the same as the one provided in the given solution—do not modify it.**
            - output should be in JSON Format'''
    # - If the given solution lacks clarity, **refine it without making it overly detailed or confusing**.
    return prompt2


def hints_prompt():
    hints_template1 = '''Given a question,solution and a grade level, generate 3 to 5 **short** hints that guide a student through the steps to solve the problem.
        
        Ensure that:
            Each hint should correspond to a necessary step in solving the problem.
            The hints are specific to the given question and solution, not general problem-solving advice.
            Hints should NOT be too general instead, make it step-specific.
            Do NOT include formulas directly, but the hint should clearly suggest an action.
            Ensure the hints follow a logical order, helping the student progress toward the solution.

        All the hints should be related to solving the problem and should be specific to the given question and solution.
        All the hints should be in a logical order, leading the student closer to the final answer.

        QUESTION {question}
        SOLUTION {solution}
        GRADE {grade}'''
    
    hints_template2='''Given a question, solution, and a grade level, generate **3 to 5 concise hints** to help a student solve the problem.

        Guidelines:
        - Each hint should align with a **necessary** step in solving the problem.
        - Hints should be **short, specific, and clear**, avoiding over-explanation.
        - **Do not** provide direct formulas, but subtly guide the student toward the right approach.
        - The hints should **follow a logical order**, progressively leading toward the solution.

        Common Mistakes to Address:
        - If applicable, include hints that **help students avoid common errors**, such as:
        - Unit conversion mistakes.
        - Incorrect formula application.
        - Calculation errors.

        **QUESTION:** {question}  
        **SOLUTION:** {solution}  
        **GRADE:** {grade}
        '''
    return hints_template2



        # Output Example:
        # - **Hint 1:** Identify what is given in the question and what needs to be found.
        # - **Hint 2:** Consider the correct approach/formula to apply based on the given information.
        # - **Hint 3:** Be mindful of units—do they need conversion?
        # - **Hint 4:** Apply the formula and simplify carefully.
        # - **Hint 5:** Verify your answer—is it reasonable based on the question?