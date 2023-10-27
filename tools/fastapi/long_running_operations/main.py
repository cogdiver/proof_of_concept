# Python dependencies
import time
import logging

# External dependencies
from fastapi import FastAPI, BackgroundTasks, Query

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to api | Long Running Operation POC"
    }


def write_notification(email: str, message=""):
    logging.info('********** start background_tasks **********')

    with open("app.log", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)
        time.sleep(10)
        logging.info('********** finish background_tasks **********')


@app.get("/run", tags=["lro"])
async def send_notification(
    background_tasks: BackgroundTasks,
    email: str = Query(
        default="user@example.com",
        title="User Email",
        description="The email address of the user.",
        example="user@example.com",
    ),
):
    logging.info('********** start endpoint **********')

    background_tasks.add_task(write_notification, email, message="some notification")
    # write_notification(email, message="some notification")

    return {
        "message": "Notification sent in the background"
    }
