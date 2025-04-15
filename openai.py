import streamlit as st
import tiktoken

# Token cost data for different models
model_costs = {
    'GPT-3 (Ada)': 0.000004,
    'GPT-3 (Babbage)': 0.000005,
    'GPT-3 (Curie)': 0.00002,
    'GPT-3 (Davinci)': 0.00004,
    'GPT-3.5 (Turbo)': 0.00003,
    'GPT-4 (8k context)': 0.00003,
    'GPT-4 (32k context)': 0.00006,
    'GPT-4 (Turbo)': 0.00006,
    'Gemini 1': 0.00002,
    'Gemini 1.5': 0.00003,
    'Claude 1': 0.00006,
    'Claude 2': 0.00007,
    'Claude 3': 0.00008,
    'Cohere Command R': 0.00001,
    'Cohere Command R (10B)': 0.00002,
    'Mistral 7B': 0.00003,
    'Mistral Mix': 0.00004,
}

# Set up the page
st.set_page_config(page_title="Token Counter & Cost Estimator", page_icon="📚", layout="wide")

# Title and Introduction
st.title("📚 Token Counter & Cost Estimator")
st.markdown("""
    This tool helps you calculate the number of tokens in your text and estimate the cost for using various AI models, such as GPT-3, GPT-4, and more.
    You can choose from a variety of models in the dropdown and see the estimated cost based on the number of tokens.
""", unsafe_allow_html=True)

# Text area input for the user to input their content
text_input = st.text_area("**Type or paste your text here...**", height=200)

# Model selection dropdown
st.subheader("Select an AI Model for Token Count & Cost Estimation", anchor="model_selector")

model_name = st.selectbox("**Choose a Model:**", list(model_costs.keys()), help="Choose the AI model you'd like to use for token cost estimation.")

# Button to calculate token count and cost
if st.button("Calculate", use_container_width=True):
    if text_input.strip() == "":  # Check if the input is empty
        st.warning("Please enter some text to calculate tokens.")
    else:
        # Token counting
        enc = tiktoken.get_encoding("cl100k_base")
        tokens = len(enc.encode(text_input))
        
        # Calculate the cost
        cost_per_token = model_costs[model_name]
        total_cost = tokens * cost_per_token
        
        # Display results
        st.markdown(f"<div style='text-align: center;'><h3 style='font-size: 20px;'>Number of tokens: {tokens}</h3></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center;'><h3 style='font-size: 20px;'>Estimated cost for '{model_name}' : ${total_cost:.6f}</h3></div>", unsafe_allow_html=True)

# Footer (Optional)
st.markdown("""
    <footer style="text-align:center;">
        <p>Powered by Vinay Maurya | <a href="https://github.com/VinayM563">GitHub</a></p>
    </footer>
""", unsafe_allow_html=True)