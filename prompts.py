def solution_prompt():
    system  = '''Given a question solution and a grade level, generate a structured step-by-step solution in the following format:
    Break the solution into logical steps based on the difficulty level of the question can have a Minimum of 3 steps and Maximum of 10 steps, 
    where each step contains:
        -name → Name of the step.
        -step_body → What is the step to be taken? A detailed explanation of what we are doing in this step and why it is necessary.
                     This should not explicitly give away the answer for this step.This should align with grade as well.
        -guiding_question → A question prompting the user to determine the result/output of this step.
            options → A list of possible answers for the guiding question.A minimun of 3 options should be there. Each option should include:
                option_body → The answer choice.
                is_correct → A tag (true/false) indicating whether this option is correct.
                feedback → A short explanation for why this option is correct or incorrect.

        Ensure that the steps align with the given grade level. 
        Output the steps in structured JSON format.
        QUESTION {question}
        SOLUTION {solution}
        GRADE {grade}
        '''
    system1  = '''Given a question, its solution, and a grade level, generate a structured step-by-step breakdown of the solution in JSON format.

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
    return system1


def hints_prompt():
    hints_template = '''Given a question,solution and a grade level, generate 3 to 5 **short** hints that guide a student through the steps to solve the problem.
        
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
    return hints_template