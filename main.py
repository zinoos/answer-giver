# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="FractalAIResearch/Fathom-Search-4B")

import os
import time
from keyboard import is_pressed
import sys

os.system("cls")

BANNER = r"""
░█████╗░███╗░░██╗░██████╗░██╗░░░░░░░██╗███████╗██████╗░
██╔══██╗████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝██╔══██╗
███████║██╔██╗██║╚█████╗░░╚██╗████╗██╔╝█████╗░░██████╔╝
██╔══██║██║╚████║░╚═══██╗░░████╔═████║░██╔══╝░░██╔══██╗
██║░░██║██║░╚███║██████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝
- answers might get cut of due to token limitations
"""

def clear_screen():
    os.system('cls')

def main():
    while True:
        clear_screen()
        print(BANNER)
        length = input("Answer length? (s)hort, (m)edium, (l)ong > ").lower()
        max_tokens = 30 if length == "s" else 100 if length == "m" else 200
        question = input("\nWhat do you want to know?\n> ")

        if question.lower() in ["exit", "quit"]:
            break

        print("\nAnswering...\n")
        time.sleep(1)

        

        prompt = f"Answer the following question in one sentence:\n\n{question}\n\n"
        output = pipe(prompt, max_new_tokens=max_tokens)

        clear_screen()

        generated = output[0]["generated_text"]
        answer_only = generated[len(prompt):].strip()

        if answer_only.lower().startswith("answer:"):
            answer_only = answer_only[7:].strip()

        print(BANNER)
        print(f"\nAnswer: {answer_only}\n")

        input("\nPress Enter to continue...")

            

        

if __name__ == "__main__":
    main()

 



