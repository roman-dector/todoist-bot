import os
from dotenv import load_dotenv


load_dotenv("./.env")

TODOIST_TOKEN = os.getenv("TODOIST_TOKEN")

