import requests
from bs4 import BeautifulSoup

# Step 1: Set the URL
base_url = "https://ia902808.us.archive.org/28/items/DarsENizamiDarjaSaniah2ndYear1/"

# Step 2: Fetch the web page content
response = requests.get(base_url)
html = response.text

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 4: Find all PDF file names
pdf_filenames = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith('.pdf') and "urdu" not in href.lower():
        pdf_filenames.append(href)

# Step 5: Save file names to a .txt file
with open("pdf_filenames.txt", "w", encoding="utf-8") as f:
    for name in pdf_filenames:
        f.write(name + "\n")

print("✅ File names saved to pdf_filenames.txt")

for name in pdf_filenames:
    print(name)
