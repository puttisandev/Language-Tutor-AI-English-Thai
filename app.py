from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

# Define the prompt for bilingual grammar correction and explanation
prompt = ChatPromptTemplate.from_template(
    """You are a bilingual language tutor fluent in English and Thai.
You will:
1. Detect whether the input is in English or Thai.
2. Correct grammar and provide the corrected version.
3. Give a short explanation of the corrections.
4. Suggest useful vocabulary or expressions if appropriate.

Input sentence: {question}

Your response should be clear and helpful for learners of that language."""
)

# Chain: prompt → LLM → output parser
model = ChatOpenAI(temperature=0.5)
chain = prompt | model | StrOutputParser()


@cl.on_chat_start
async def on_chat_start():
    # Store the chain in the session
    cl.user_session.set("runnable", chain)
    await cl.Message(
        content="👋 Welcome to your Language Tutor! Send me an English or Thai sentence and I’ll help you correct and understand it."
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")
    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
