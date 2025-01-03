from pyjiit.wrapper import Webportal
from pyjiit.wrapper import API
from pyjiit.default import CAPTCHA
import os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()


class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"


def get_add_drop_endpoint_status():

    ENDPOINT = "/addDropSubjectRequest/getStudentInfo"

    w = Webportal()
    USERNAME = os.getenv("JIIT_USERNAME")
    PASSWORD = os.getenv("JIIT_PASSWORD")

    w.student_login(USERNAME, PASSWORD, CAPTCHA)
    PAYLOAD = {
        "instituteid": "11IN1902J000001",
        "bypassValue": "XuVHxhCQsRmMyK7cUdFClQ==",
    }
    resp = w._Webportal__hit("POST", API + ENDPOINT, json=PAYLOAD, authenticated=True)
    response_status = resp["status"]["responseStatus"]
    if response_status == "Failure":
        return Status.CLOSED.value
    return Status.OPEN.value


if __name__ == "__main__":
    print(get_add_drop_endpoint_status())
