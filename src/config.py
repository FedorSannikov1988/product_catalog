"""
Loading a token for a bot from environment variables
"""
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_BOT = os.getenv('TOKEN_FOR_BOT')
