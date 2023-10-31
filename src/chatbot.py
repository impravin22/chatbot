import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="CreateAI | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**Mail** : contact@createai.com")
    st.write("**Created by CreateAI**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>CreateAI, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>
I am CreateAI, a smart chatbot that results from the synergy of Langchain and Streamlit. I utilize advanced language models to engage in context-aware conversations. My primary aim is to assist you in gaining a deeper comprehension of your data. I have the capability to handle various data formats, including PDF, TXT, CSV, and YouTube transcripts. </h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


# #Robby's Pages
# st.subheader("🚀 CreateAI's Pages")
# st.write("""
# - **CreateAI-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
# - **CreateAI-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
# - **CreateAI-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
# """)
# st.markdown("---")


#Contributing
st.markdown("### 🎯 In Progress")
st.markdown("""
**[CreateAI](https://createfyai.com/) is under regular development.**
""", unsafe_allow_html=True)
