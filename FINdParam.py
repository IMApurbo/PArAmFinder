import requests
from bs4 import BeautifulSoup
import os
import time
from colorama import Fore, Style
from urllib.parse import urljoin

# ANSI color escape codes
BLUE = Fore.BLUE
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL

def print_with_animation(text, color):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for speed
    print(RESET)

def print_colored_figlet_text(text, color):
    try:
        os.system(f"figlet -f slant '{text}' > temp_figlet.txt")  # Generate figlet text to a temporary file
        with open("temp_figlet.txt", "r") as file:
            figlet_output = file.read()
        os.remove("temp_figlet.txt")  # Remove temporary file

        colored_text = f"{color}{figlet_output}{RESET}"  # Apply color after figlet
        print(colored_text)
    except FileNotFoundError:
        print(f"{RED}Error:{RESET} 'figlet' command not found. Please install figlet.")

def extract_links(url, base_url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        filtered_links = [urljoin(base_url, link) for link in links if link and any(symbol in link for symbol in ['=', '&', '?'])]
        return filtered_links
    except Exception as e:
        print(f"{RED}Error:{RESET}", e)
        return []

def crawl(url, depth, base_url, print_header=True):
    if depth == 0:
        return

    if print_header:
        print(f"{BLUE}Links extracted from {url}:{RESET}")
        print_header = False

    links = extract_links(url, base_url)
    for link in links:
        print(link)  # Print each filtered link individually
        crawl(link, depth - 1, base_url, print_header=False)

if __name__ == "__main__":
    print_colored_figlet_text("KORISHEE THE CYBERMASTER", GREEN)
    print_with_animation("PRESENTING A AUTOMATED SQL PARAMETER FINDER FOR SQLI", RED)
    starting_url = input(f"{BLUE}Enter the domain name (e.g., https://example.com): ")
    max_depth = 2  # Set the maximum depth of crawling, change as needed
    crawl(starting_url, max_depth, starting_url)
