from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

LOG_FILE = "log.txt"
API_URL = "http://127.0.0.1:8000/logs"


def record_test_input():
    print("Enter sample text. Type EXIT to finish.")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        while True:
            text = input("> ")
            if text.strip().upper() == "EXIT":
                break
            log_file.write(text + "\n")
    print(f"Saved sample text to {LOG_FILE}")


def send_log_to_api():
    try:
        with open(LOG_FILE, "rb") as log_file:
            payload = log_file.read()

        request = Request(
            API_URL,
            data=payload,
            headers={"Content-Type": "text/plain; charset=utf-8"},
            method="POST",
        )

        with urlopen(request, timeout=5) as response:
            print(f"API response: {response.status}")
            print(response.read().decode("utf-8", errors="replace"))
    except FileNotFoundError:
        print(f"{LOG_FILE} does not exist yet.")
    except (HTTPError, URLError, TimeoutError) as error:
        print(f"Could not send the file. Is server.py running? Details: {error}")


if __name__ == "__main__":
    record_test_input()
    send_log_to_api()
