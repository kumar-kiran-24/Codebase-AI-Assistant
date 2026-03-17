import os 
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory


class Bot:
    store={}
    context_store={}
    def __init__(self):
        api_key=os.getenv("GROQ_API")
        self.llm=ChatGroq(model="llama-3.1-8b-instant",api_key=api_key)
        self.prompt =ChatPromptTemplate.from_messages([
                                    (
                                        "system",
                                        """
                                You are an expert AI Codebase Assistant.

                                You are given code from a repository. Your job is to answer questions ONLY using the provided context.

                                STRICT RULES:
                                - DO NOT guess or assume anything
                                - DO NOT say "it appears", "might be", or "probably"
                                - If the answer is not in the context, respond EXACTLY:
                                "Not found in the codebase."

                                ANSWER REQUIREMENTS:
                                - Always mention the file name(s)
                                - Explain clearly and technically
                                - Refer to actual code logic
                                - Be concise but informative

                                OUTPUT FORMAT:

                                File: <file_name>

                                Explanation:
                                <clear explanation of what the code does>

                                Code Reference:
                                <relevant snippet or description>

                                If multiple files are involved, list each separately.
                                """
                                    ),
                                    MessagesPlaceholder(variable_name="history"),
                                    (
                                        "human",
                                        """
                                Context:
                                {context}

                                Question:
                                {question}
                                """
                                    )
                                ])


    def initate_bot(self,question,session_id,context):
        
        model=self.llm
        prompt=self.prompt

        store=self.store
        context_store=self.context_store
        

        if session_id not in context_store:
            context_store[session_id]=context
        

        def get_session_history(session_id):
            if session_id not in store:
                store[session_id]=InMemoryChatMessageHistory()
            return store[session_id]
        
        self.saved_context=context_store[session_id]
        self.session_id=session_id
        

        chain=prompt|model

        self.bot=RunnableWithMessageHistory(
            chain,
            get_session_history=get_session_history,
            input_messages_key="question",
            history_messages_key="history"
        )

        response=self.bot.invoke({"question":question,"context":self.saved_context},
                                 config={"configurable":{"session_id":self.session_id}}
                                 )
        
        print(response.content)
        return response.content
    

        