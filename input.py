import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_url(year: int, day: int):
    return f"https://adventofcode.com/{year}/day/{day}/input"

def get_headers():
    return {
      'Cookie': 'session=' + os.getenv('AOC_SESSION'),
    }

def download_input(year: int, day: int):
    url = get_url(year, day)
    data = requests.get(url, headers=get_headers())
    if data.ok:
        with open(f'data/year-{year}/day-{day}.txt', 'w') as f:
            f.write(data.text)
    else:
        raise Exception(f"Couldn't download {data.text=}")
