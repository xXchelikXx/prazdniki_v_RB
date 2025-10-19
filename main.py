import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    api_key = os.getenv("api_key")

    holidays_url = f"https://calendarific.com/api/v2/holidays"

    params = {"api_key": api_key, "country": "BY", "year": 2025}
    response = requests.get(holidays_url, params=params)
    response.raise_for_status()

    holidays = response.json()["response"]["holidays"]

    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]

    for about_holiday in holidays:
        print(f"""
    Дата праздника: {about_holiday["date"]["datetime"]["day"]} {months[about_holiday["date"]["datetime"]["month"] - 1]}
    Название: {about_holiday["name"]}
    Описание: {about_holiday["description"]}""")


if __name__=="__main__":
    main()
