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


    prompt3_K = '''You are an **expert in educational content creation**, specializing in structured problem-solving.  
            Your task is to generate a **step-by-step breakdown** of a given question and its solution, ensuring clarity, logical progression, and engagement for students at the specified grade level.  
            Your role is **not to solve the problem** but to **guide students through the solution process**.  

            ### **Breakdown of Steps:**  
            - **Concise & Logical:** Focus on **essential** steps only—do **not** over-elaborate.  
            - **Step Count Based on Difficulty:**  
            - **Easy:** 3-4 steps (unless fewer are sufficient).  
            - **Moderate:** 4-5 steps.  
            - **Difficult:** 5-6 steps (strict upper limit).  
            - **Conceptual Grouping:**  
            - **Avoid unnecessary steps** (e.g., restating given values or substituting values).  
            - **Merge trivial steps** into logical groups.  
            - **Do not create a separate step for the calculation and the conclusion or final answer .**  
            - **Ensure alignment with the given solution.** Do not introduce alternative methods.  

            ### **Step Structure:**  
            Each step should follow this format:  
            - **Solution name** → A short, clear title summarizing the approach.  

            - **Each step should include:**  

            - **name** → A short, descriptive title for the step.  
            - **step_body**:  
                - Clearly explains the process **without including the numerical answer**.  
                - Focuses on **why** the step is necessary and **how** it contributes to solving the problem.  
                - **Avoids unnecessary details**—keep it precise.  
                - **Does NOT state formulas, calculations, or final answers**.  

            - **guiding_question**:  
                - Requires students to **actively apply** the step_body rather than recall information.  
                - **Should not be a direct restatement** of the step_body.  
                - **Example:** If the step explains applying the quadratic formula, the guiding question should ask for **the result of applying it**, not the formula itself.  

            - **options** → A list of 3 answer choices:  
                - **One option should be based on a common mistake** (e.g., unit conversion error, calculation error).  
                - The correct answer should be marked with `is_correct: true`.  
                - Each option includes:  
                - **option_body** → The answer choice.  
                - **is_correct** → Boolean (`true/false`).  
                - **feedback** → A short, precise explanation of correctness.  

            ### **Additional Requirements:**  
            - **Do not modify the given solution.** Ensure the final step leads directly to the provided solution.  
            - **Ensure proper formatting of mathematical expressions** to avoid errors.  
            - **Keep explanations at an appropriate complexity level**—do not oversimplify or overcomplicate.  
            - **Output must be in JSON format.**  
            '''
    
    prompt5_A = '''
    You are an **expert in educational content creation**, specializing in structured problem-solving. 
    Your task is to generate a **step-by-step breakdown** of a given question and its solution, ensuring clarity, logical progression, and engagement for students at the specified grade level.
    Your task is not to solve the problem but to **guide students through the solution process**.
    Given a question, its solution, and a grade level, generate a structured step-by-step breakdown of the solution along with guiding question in JSON format.
        
        Example:
        {
            "name": "Apply the quadratic formula",
            "step_body": "Use the quadratic formula x = (-b ± √(b² - 4ac)) / 2a to find the roots.",
            "outcome": {
            "guiding_question": "What is the value of the discriminant (Δ) for 2x² + 3x - 5?",
            "options": [
                {
                "option_body": "49",
                "is_correct": true,
                "feedback": "Correct! The discriminant is calculated as Δ = b² - 4ac."
                },
                {
                "option_body": "25",
                "is_correct": false,
                "feedback": "Incorrect. Double-check the formula."
                }
            ]
            }
        }

        Breakdown of Steps:  
            - **Do NOT include unnecessary steps** (e.g., do not simply restate given information).
            - Prioritize **conceptual grouping** over trivial steps (e.g., restating given information or Substituting the values or conclusion). 
            - **Do not include the answer for guiding question in the step body itself**—the learner should work towards it.
            - Ensure the number of steps matches the **difficulty level**:
                - **Easy questions:** 3-4 steps (unless fewer are sufficient).
                - **Moderate questions:** 4-6 steps.
                - **Difficult questions:** 5-8 steps.
                - **Avoid unnecessary steps—merge trivial steps into logical groups.**


        Step Structure:
        - **Solution name** → A clear, short, and concise title for the solution.

        - **Each step should include:**

                Key Fixes to Avoid Past Issues:  
                    - Do not create a step for simple things it should be logical and necessary.
                    - Do not have separate step for conclusion or to state the final answer.
                    - Do not state formulas or final answers in the step_body.
                    - Do not break down the formula into multiple steps.
                    - Do not include identifying given values or restating the question in the step_body.
                    - **The guiding question must require students to apply knowledge rather than recall what was just stated.** 
                    -  Example:if the step body is stating the formula, the guiding question should ask for the output of the formula,not the formula itself..  
                    - **DO NOT introduce unnecessary steps**. Merge trivial steps into logical groups. 
                    - Ensure that the guiding question is **not a direct restatement of the step_body**.

            - **name** → A short, descriptive title for the step.

            - **step_body**:
                        → Provide an detailed instructional explanation of what needs to be done in the current step do not include the answer to the guiding question.e.g., "Apply the quadratic formula to find the roots."
                        → **Do NOT include the answer to the guiding question.**
                        → Do not include identifying given information or restating the question or substituting values as a step.
                        → Do not solve the problem in this step, only explain the logic or process behind it. 
                              

            - **guiding_question**:
                          -**Must require students to actively apply** the step_body (not just confirm information).eg., "What are the roots of the quadratic equation 2x² + 3x - 5?"
                          - **Should be structured so that the answer is NOT already in the step_body.**
                          - Ask question that forces the student to make a calculation,inference or decision based on the step_body.

                - **options** → A list of 3 answer choices, including:
                    - **One option based on a common mistake** (e.g., unit conversion errors, calculation errors).
                    - Make sure the correct answer option as the boolean value true.
                    - Each option should contain:
                        - **option_body** → The answer choice.
                        - **is_correct** → Boolean (true/false) indicating correctness.
                        - **feedback** → A short, precise explanation of why this choice is correct or incorrect.
         

        Additional Requirements:
          -Maintain appropriate complexity for the grade level—do not oversimplify or overcomplicate.
          -DO NOT include the final answer in step_body; it belongs in the guiding_question.
          -Ensure the final step logically leads to the given solution but DO NOT add a separate conclusion step.
          -Properly format mathematical expressions for accurate interpretation.
          -Output must be in JSON format.
        '''
    prompt ='''You are an **expert in educational content creation**, specializing in structured problem-solving.  
                Your task is to generate a **step-by-step breakdown** of a given question and its solution, ensuring clarity, logical progression, and engagement for students at the specified grade level.  
                Your role is **not to solve the problem** but to **guide students through the solution process**.  

                ### **Breakdown of Steps:**  
                - **Concise & Logical:**  
                - **Do NOT exceed the necessary number of steps.**  
                - **Easy problems (basic calculations):** Maximum **3 steps** unless absolutely necessary.  
                - **Moderate problems:** 3-4 steps.  
                - **Difficult problems (multiple concepts):** 4-5 steps (strict upper limit).  
                - **Conceptual Grouping:**  
                - **Prioritize key transformations and operations over trivial steps.**  
                - **Avoid redundant breakdowns.** Do not create a separate step just to extract given values.  
                - **Ensure step progression remains relevant and does not overcomplicate simple ideas.**  

                ### **Step Structure:**  
                Each step should follow this format:  
                - **Solution name** → A short, clear title summarizing the approach.  

                - **Each step should include:**  

                - **name** → A short, descriptive title for the step.  
                - **step_body**:  
                    - Clearly explain the process **without revealing the numerical answer**.  
                    - Emphasize **what the student needs to do** in this step without explicitly stating the result.  
                    - **DO NOT reveal the answer that the guiding_question will ask.**  
                    - **Avoid stating calculations or final answers directly.**  
                    - **Prioritize steps that involve actual problem-solving actions, not trivial identifications or restating things**  

                - **guiding_question**:  
                    - Requires students to **actively apply** the step_body rather than recall information.  
                    - **Should not be a direct restatement** of the step_body.  
                    - **Must explicitly ask for the result of the step without providing hints in the step_body.**  
                    - **Never ask for a formula if it was already revealed in the step_body.**  
                    - **However, you can ask formula-related conceptual questions (e.g., what does a variable in the formula represent, how does the formula apply, what happens when a parameter changes).**  
                    - **Example (Incorrect):**  
                    - **Step Body:** The magnetic flux is calculated using \( \Phi = B \cdot A \).  
                    - **Guiding Question:** What is the formula for magnetic flux?  
                    - ❌ **Incorrect because the formula was already given in the step_body.**  
                    - **Example (Correct):**  
                    - **Step Body:** The magnetic flux is calculated using \( \Phi = B \cdot A \).  
                    - **Guiding Question:** How does the area affect the magnetic flux in this formula?  
                    - ✅ **Correct because it asks about a concept related to the formula, not the formula itself.**  

                - **options** → A list of 3 answer choices:  
                    - **One option should be based on a common mistake** (e.g., unit conversion error, calculation error).  
                    - The correct answer should be marked with `is_correct: true`.  
                    - Each option includes:  
                    - **option_body** → The answer choice.  
                    - **is_correct** → Boolean (`true/false`).  
                    - **feedback** → A short, precise explanation of correctness.  

                ### **Additional Requirements:**  
                - **Strictly control step count:** Do **not** over-explain simple problems.  
                - **Do not modify the given solution.** Ensure the final step leads directly to the provided solution.  
                - **Ensure proper formatting of mathematical expressions** to avoid errors.  
                - **Maintain grade-appropriate complexity—avoid over-explaining simple concepts.**  
                - **Ensure the step_body describes the process without revealing the answer, while the guiding_question explicitly asks for the answer.**  
                - **If a step involves a calculation or transformation, describe the operation, NOT the result.**  
                - **Never ask for a formula in the guiding_question if it was stated in the step_body. Instead, ask related conceptual questions.**  
                - **Output must be in JSON format.**  

            '''

    

    prompt_multi = '''You are an **expert in educational content creation**, specializing in structured problem-solving.  
                        Your task is to generate a **step-by-step breakdown** of a given question, its original answer options, and its solution, ensuring clarity, logical progression, and engagement for students at the specified grade level.  
                        Your role is **not to solve the problem** but to **guide students through the solution process**.  

                        ---

                        ### **Breakdown of Steps:**  
                        - **Concise & Logical:**  
                        - **Do NOT exceed the necessary number of steps.**  
                        - **Easy problems (basic calculations):** Maximum **3 steps** unless absolutely necessary.  
                        - **Moderate problems:** 3-4 steps.  
                        - **Difficult problems (multiple concepts):** 4-5 steps (strict upper limit).  
                        - **Conceptual Grouping:**  
                        - **Prioritize key transformations and operations over trivial steps.**  
                        - **Avoid redundant breakdowns.** Do **not** create a separate step just to extract given values.  
                        - **Ensure step progression remains relevant and does not overcomplicate simple ideas.**  

                        ---

                        ### **Handling Multiple Correct Options:**  
                        - **If more than one original answer option is correct, the breakdown must generate distinct steps for verifying each correct option.**  
                        - **Each correct option should be verified separately, not just assumed correct once another has been confirmed.**  
                        - **If two or more correct options share a common calculation or reasoning, reuse that logic efficiently, but still explicitly verify each correct option in separate steps.**  
                        - **Incorrect options do not require steps, but the final breakdown should ensure students reach all correct answers.**  

                        ---

                        ### **Step Structure:**  
                        Each step should follow this format:  

                        - **Solution name** → A short, clear title summarizing the approach.  

                        - **Each step should include:**  
                        - **name** → A short, descriptive title for the step.  
                        - **step_body**:  
                            - Clearly explain the process **without revealing the numerical answer**.  
                            - Emphasize **what the student needs to do** in this step without explicitly stating the result.  
                            - **Ensure all correct original options are addressed in separate steps if necessary.**  
                            - **DO NOT reveal the answer that the guiding_question will ask.**  
                            - **Avoid stating calculations or final answers directly.**  
                            - **Prioritize steps that involve actual problem-solving actions, not trivial identifications.**  

                        - **guiding_question**:  
                            - Requires students to **actively apply** the step_body rather than recall information.  
                            - **Should not be a direct restatement** of the step_body.  
                            - **Must explicitly ask for the result of the step without providing hints in the step_body.**  
                            - **Never ask for a formula if it was already revealed in the step_body.**  
                            - **However, you can ask formula-related conceptual questions (e.g., what does a variable in the formula represent, how does the formula apply, what happens when a parameter changes).**  

                        - **options** → The original answer choices (unchanged):  
                            - **Do not modify the original answer options.**  
                            - The correct answers should be marked with `is_correct: true`.  
                            - Each option includes:  
                            - **option_body** → The original answer choice.  
                            - **is_correct** → Boolean (`true/false`).  
                            - **feedback** → A short, precise explanation of correctness.  
                            - At least **one incorrect option** should be based on a **common mistake** (e.g., unit conversion error, calculation mistake).  

                        ---

                        ### **Additional Requirements:**  
                        - **Strictly control step count:** Do **not** over-explain simple problems.  
                        - **Do not modify the given solution.** Ensure the final step leads directly to the provided solution.  
                        - **Ensure proper formatting of mathematical expressions** to avoid errors.  
                        - **Maintain grade-appropriate complexity—avoid over-explaining simple concepts.**  
                        - **Ensure the step_body describes the process without revealing the answer, while the guiding_question explicitly asks for the answer.**  
                        - **If a step involves a calculation or transformation, describe the operation, NOT the result.**  
                        - **Never ask for a formula in the guiding_question if it was stated in the step_body. Instead, ask related conceptual questions.**  
                        - **In multiple-correct cases, the breakdown must generate separate steps for verifying each correct option.**  
                        - **Output must be in JSON format.**  

            '''
    prompt_multi_claude ='''
                        You are an **expert in educational content creation**, specializing in structured problem-solving.  
                        Your task is to generate a **step-by-step breakdown** of a given question, its original answer options, and its solution, ensuring clarity, logical progression, and engagement for students at the specified grade level.  
                        Your role is **not to solve the problem** but to **guide students through the solution process**.

                        # Advanced Prompt for Educational Problem-Solving Content Generation

                        ## Core Objectives
                        - Generate step-by-step educational content for complex problems with potentially multiple correct options
                        - Provide a structured approach to solving and explaining each correct option
                        - Maintain educational rigor and student engagement

                        ## Prompt Instructions

                        ### 1. Problem Analysis
                        - Comprehensively analyze the given problem
                        - Identify ALL potentially correct options
                        - Verify the correctness of each option through rigorous mathematical or conceptual reasoning

                        ### 2. Solution Generation Guidelines

                        #### Step Structure Requirements
                        - **Step Count Constraints:**
                        - as many steps as necessary to explain the solution

                        #### Step Components
                        Each step must include:
                        - **name**: A short, descriptive title for the step
                        - **step_body**:
                        - Clearly explain the process **without revealing the numerical answer**
                        - Emphasize **what the student needs to do**
                        - **DO NOT reveal the final answer**
                        - Prioritize problem-solving actions over trivial identifications

                        - **guiding_question**:
                        - Requires students to **actively apply** the step
                        - **Should not be a direct restatement** of the step body
                        - **Must explicitly ask for the result without providing hints**
                        - Avoid asking for formulas already mentioned
                        - Can ask conceptual questions related to the formula

                        - **options**:
                        - 3 answer choices
                        - One option based on a common mistake
                        - Correct answer marked with `is_correct: true`
                        - Each option includes:
                            - `option_body`: The answer choice
                            - `is_correct`: Boolean (true/false)
                            - `feedback`: Short explanation of correctness

                        ### **3. Multi-Option Handling**
                         - **If more than one original answer option is correct, the breakdown must generate distinct steps for verifying each correct option.**  
                        - **Each correct option should be verified separately, not just assumed correct once another has been confirmed.**  
                        - **If two or more correct options share a common calculation or reasoning, reuse that logic efficiently, but still explicitly verify each correct option in separate steps.**  
                        - **Incorrect options do not require steps, but the final breakdown should ensure students reach all correct answers.**  


                        ### 4. Additional Requirements
                        - **Conceptual Clarity:**
                        - Prioritize understanding over rote calculation
                        - Explain WHY an option is correct, not just THAT it is correct
                        - Highlight unique reasoning for each correct solution path

                        - **Formatting Constraints:**
                        - Use proper mathematical notation
                        - Ensure grade-appropriate complexity
                        - Avoid over-explaining simple concepts

                        ### 5. Problem-Solving Approach
                        - Break down complex problems into manageable steps
                        - Provide conceptual insights
                        - Encourage critical thinking
                        - Demonstrate multiple solution approaches when applicable

                        ### 6. Output Specifications
                        - **Format:** Strict JSON format
                        - **Language:** Clear, concise, educational
                        - **Focus:** Student understanding and active learning

                        ### 7. Verification Principles
                        - Mathematically prove option correctness
                        - Provide conceptual explanations
                        - Demonstrate multiple solution paths when possible

                        ## Key Considerations
                        - Maintain flexibility for various problem types
                        - Support single and multiple correct option scenarios
                        - Provide depth of explanation
                        - Focus on educational value

                        ## Implementation Notes
                        - Solution generation must handle:
                        1. Single correct option scenarios
                        2. Multiple correct option scenarios
                        3. Conceptual understanding beyond calculation

                        ### Example Problem Processing
                        1. Analyze all given options
                        2. Mathematically verify each option
                        3. Generate comprehensive solution steps
                        4. Highlight unique reasoning for correct options
                        5. Explain why incorrect options are wrong                                                  
                    '''

    return prompt



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
    hints_prompt = '''
        Given a question, solution, and a grade level, generate **an appropriate number of concise hints**   based on the difficulty of the question.  

        Guidelines:  
        - Each hint should align with a **necessary** step in solving the specific problem, ensuring relevance.  
        - The number of hints should **match the complexity** of the question—simpler questions may need fewer hints (typically 2 to 4), while complex ones may require more (typically 3 to 5).  
        - Hints should be **short, specific, and clear**, avoiding over-explanation.  
        - **Do not** provide direct formulas but subtly guide the student toward the right approach.  
        - The hints should **follow a logical order**, progressively leading toward the solution.  

        Avoid Generalization:  
        - **Do not generate generic hints**; every hint must be tailored to the given question.  
        - If applicable, include hints that **help students avoid common errors**, such as:  
        - Unit conversion mistakes.  
        - Incorrect formula application.  
        - Calculation errors.  

        **QUESTION:** {question}  
        **SOLUTION:** {solution}  
        **GRADE:** {grade}  
'''
    return hints_prompt



        # Output Example:
        # - **Hint 1:** Identify what is given in the question and what needs to be found.
        # - **Hint 2:** Consider the correct approach/formula to apply based on the given information.
        # - **Hint 3:** Be mindful of units—do they need conversion?
        # - **Hint 4:** Apply the formula and simplify carefully.
        # - **Hint 5:** Verify your answer—is it reasonable based on the question?