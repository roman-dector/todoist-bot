from todoist import TodoistAPI

from servises import run_polling
from config import TODOIST_TOKEN


api = TodoistAPI(TODOIST_TOKEN)

if __name__ == "__main__":
    print(TODOIST_TOKEN)
    run_polling(api)

