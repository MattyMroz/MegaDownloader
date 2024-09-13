# 1. GO TO:
# https://lightning.ai/

# 2. INSTALL ON LINUX:
# sudo apt install megatools

# 3. RUN:
# python MegaDownloader.py

# MANUAL:
# https://manpages.ubuntu.com/manpages/focal/en/man7/megatools.7.html
# https://manpages.ubuntu.com/manpages/focal/en/man1/megadl.1.html

import re
import subprocess
import os
from typing import Optional


def generate_mega_link(input_link: str, script_dir: str) -> Optional[str]:
    match = re.search(r'(file|folder)/([^/#]+)#([^/]+)', input_link)
    if match:
        type, id1, id2 = match.groups()
        if type == 'file':
            return f"megadl 'https://mega.co.nz/#!{id1}!{id2}' --path '{script_dir}'"
        elif type == 'folder':
            return f"megadl 'https://mega.co.nz/#F!{id1}!{id2}' --path '{script_dir}' --choose-files"
    return None


def download_from_mega(input_link: str, script_dir: str) -> None:
    mega_link = generate_mega_link(input_link, script_dir)
    if mega_link:
        print(f"Wykonuję komendę: {mega_link}")
        subprocess.run(mega_link, shell=True)
    else:
        print("Nieprawidłowy format linku! 😕")


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("Witaj w pobieraczu MEGA! 😎🚀")
    print(f"Pliki będą pobierane do: {script_dir} 📂")

    while True:
        try:
            input_link = input(
                "Podaj link do pobrania z MEGA (lub wpisz 'q' aby zakończyć): ")
            if input_link.lower() == 'q':
                print("Dzięki za korzystanie z pobieracza MEGA! Pa pa! 👋")
                break
            download_from_mega(input_link, script_dir)
            print("\n")
        except KeyboardInterrupt:
            print("\nPrzerwano działanie programu. Pa pa! 👋")
            break


if __name__ == "__main__":
    main()
