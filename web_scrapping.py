import requests
from bs4 import BeautifulSoup
import os
import urllib.request

# Step 1: Set the base URL
base_url = "https://ia902808.us.archive.org/28/items/DarsENizamiDarjaSaniah2ndYear1/"

# Step 2: Get the HTML content of the page
response = requests.get(base_url)
html = response.text

# Step 3: Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 4: Find all PDF links
pdf_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    #if href and href.endswith('.pdf')
    if href and href.endswith('.pdf') and "urdu" not in href.lower():
        full_url = base_url + href
        pdf_links.append(full_url)

# Step 5: Create a folder to save downloads
download_dir = "dars_nizami_pdfs"
os.makedirs(download_dir, exist_ok=True)

# Step 6: Download all PDFs
for pdf_url in pdf_links:
    filename = pdf_url.split('/')[-1]
    file_path = os.path.join(download_dir, filename)
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(pdf_url, file_path)

print("✅ All PDF files downloaded successfully!")
