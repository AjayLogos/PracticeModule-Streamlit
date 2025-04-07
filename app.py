from main import get_prompt , get_hints , get_solution 
import streamlit as st
import base64
import re
from io import BytesIO
from PIL import Image
# from database import insert_hints_solution , get_hints_solution

def extract_base64_images(text):
    pattern = r"(data:image\/(?:png|jpeg|jpg);base64,[a-zA-Z0-9+/=]+)"
    pattern = r"data:image\/(?:png|jpeg|jpg);base64,([a-zA-Z0-9+/=]+)"
    return re.findall(pattern, text)  # Returns a list of base64 image URLs

# # Function to extract base64 image
# def extract_base64_image(text):
#     match = re.search(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', text)
#     if match:
#         return match.group(1)
#     return None

# Streamlit UI
st.sidebar.title("Input Section")
id = st.sidebar.text_input("Enter ID:").strip()
generate_button = st.sidebar.button("Generate")

st.title("Practice Module")
if generate_button and id :
    # db_result = get_hints_solution(id)

    prompt = get_prompt(id)

    # Check if the response contains an error
    if "error" in prompt:
        st.error(prompt["error"])
        st.write(prompt["details"])  # Display additional error details
    else:
        st.subheader("Question")
        # Extract base64 image
        base64_image = extract_base64_images(prompt['Question'])
       
        # Display question text
        question_text = re.sub(r'<img.*?>', '', prompt['Question'])  # Remove image tags
        st.markdown(question_text, unsafe_allow_html=True)

        # Display image if found
        if base64_image:
            for img in base64_image:
                image_bytes = base64.b64decode(img)
                image = Image.open(BytesIO(image_bytes))
                st.image(image, caption="Embedded Image", use_container_width=True)
        

        st.subheader("Options")
        options = prompt['options']
        print(options)
        for i, option in enumerate(options):
            option = re.sub(r'<img.*?>', '', option)
            st.markdown(option, unsafe_allow_html=True)


        st.subheader("Solution")
        # Extract base64 image
        base64_image = extract_base64_images(prompt['Solution'])
        # Display question text
        question_text = re.sub(r'<img.*?>', '', prompt['Solution'])  # Remove image tags
        st.markdown(question_text, unsafe_allow_html=True)

        # Display image if found
        if base64_image:
            for img in base64_image:
                image_bytes = base64.b64decode(img)
                image = Image.open(BytesIO(image_bytes))
                st.image(image, caption="Embedded Image", use_container_width=True)
        
        st.subheader("Hints")
        db_result = None
        if db_result:
            hints = db_result[0]
            solution = db_result[1]
        else:
            hints = get_hints(prompt['hints_prompt'])
            solution = get_solution(prompt['solution_prompt'])
            # insert_hints_solution(id, hints, solution)

        
        for hint in hints:
            st.write(f"- {hint}")

        st.title("Solution")
        st.title(solution['Name'])
        for step in solution['steps'][0]['steps']:
            st.subheader(step['name'])
            st.write(step['step_body'])

            outcome = step['outcome']
            st.write(f"**Guiding Question:** {outcome['guiding_question']}")

            for option in outcome['options']:
                if option['is_correct']:
                    st.success(f"✅ {option['option_body']}")  # Green for correct
                else:
                    st.error(f"❌ {option['option_body']}")  # Red for incorrect
                st.write(f"📝 Feedback: {option['feedback']}")  # Show feedback

            st.divider()

elif generate_button:
    st.warning("Please enter an ID before generating.")



