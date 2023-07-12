import requests
from bs4 import BeautifulSoup
from colorama import Fore,init
import os

os.system("cls")

init()

# Replace with the URL of the website you want to scrape.

print("    ")
print("    ")

url = input(Fore.YELLOW+' Enter URL : ')

# Send a GET request to the URL and store its response.

response = requests.get(url)

# Create a BeautifulSoup object from the HTML content of the response.

soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page and print their href attributes.

print("    ")
print("    ")
print(Fore.BLUE+" Links => ")
print("    ")
print("    ")

for link in soup.find_all('a'):
    print(Fore.GREEN+link.get('href'))

# Find all images on the page and print their src attributes.

print("    ")
print("    ")
print(Fore.BLUE+" Images => ")
print("    ")
print("    ")

for image in soup.find_all('img'):
    print(Fore.GREEN+image.get('src'))

# Find all headings on the page and print their text content.

print("    ")
print("    ")
print(Fore.BLUE+" Headings => ")
print("    ")
print(Fore.GREEN+"    ")

for heading in soup.find_all(['h1', 'h2', 'h3']):
    print(heading.text.strip)

print(Fore.WHITE+"    ")
