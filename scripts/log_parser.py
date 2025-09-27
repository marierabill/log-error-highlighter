import re
import argparse
from colorama import Fore, Style

def highlight_errors(file_path, keywords=None):
    """
    Reads a log file and highlights error/warning lines.
    :param file_path: Path to the log file
    :param keywords: List of keywords to search for
    """
    if keywords is None:
        keywords = ["ERROR", "Error", "error", "WARNING", "Warning", "warning", "CRITICAL"]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, start=1):
                if any(keyword in line for keyword in keywords):
                    print(f"{Fore.RED}[Line {line_num}] {line.strip()}{Style.RESET_ALL}")
                else:
                    print(f"{line.strip()}")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}File {file_path} not found.{Style.RESET_ALL}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highlight errors/warnings in logs.")
    parser.add_argument("file", help="Path to the log file")
    parser.add_argument("-k", "--keywords", nargs="+", help="Custom keywords to search for")
    args = parser.parse_args()

    highlight_errors(args.file, args.keywords)
