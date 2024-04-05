from langchain.llms import HuggingFaceHub
from aiogram import Dispatcher, Bot, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
telegram_token = os.environ.get('TELEGRAM_API_TOKEN')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

llm_hug = HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", 
                             huggingfacehub_api_token=HUGGINGFACE_API_KEY, 
                             model_kwargs={"temperature":0.01, "max_length":10000})

#print(llm_hug("WHat is India's pincode?"))

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)

@dp.message_handler()
async def chat_llm(message:types.Message):
    query = message.text
    response = llm_hug(query)
    await bot.send_message(chat_id=message.chat.id, text=response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
