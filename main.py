import json
import random
from subprocess import run
import time
from typing import Any

def main() -> None:
  all_data = get_data()
  print("\033[31m" + "To answer any questions, clicking the enter key ", end="")
  print("means yes, but typing any letter, and then the enter key is no." + "\033[0m")
  input("Start: ")
  while True:
    theme, questions = pick(all_data, True)
    question, answer = pick(questions, True)
    if not input("Show answer: "): print(answer)
    else: break
    if input("Continue: "): break
    


def get_data() -> dict:
  with open("data.json", "r") as f:
    return json.load(f)


def pick(data: dict, print_to_console: bool = False) -> Any:
  keys = list(data.keys())
  picked_key = random.choice(keys)

  if len(keys) < 10:
    loops = 5
  elif len(keys) < 20:
    loops = 4
  elif len(keys) < 30:
    loops = 3
  elif len(keys) < 40:
    loops = 2
  else:
    loops = 1

  if print_to_console:
    for _ in range(loops):
      for key in keys:
        print(key)
        time.sleep(0.1)
        run(['clear'])

    print("\033[35m" + picked_key + "\033[0m")
    
  return picked_key, data[picked_key]


if __name__ == "__main__":
  main()