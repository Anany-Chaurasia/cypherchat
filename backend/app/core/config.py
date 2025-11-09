
#This file is responsible for loading environment variables, DB URLs, API keys 

import os
from dotenv import load_dotenv

load_dotenv()

def os_getenv(key: str, default: str = None) -> str:
    return os.getenv(key, default)

