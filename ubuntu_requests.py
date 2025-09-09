# ubuntu_requests.py
# This script fetches and processes data from the the website https://pixabay.com/
# It retrieves image data  and saves it into a CSV file.


# Step one: Import necessary libraries

import requests
import os
from urllib.parse import urlparse
import mimetypes

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get URLs from user
    urls = input("Please enter the image URLs (comma-separated): ").split(',')

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        for url in urls:
            url = url.strip()
            if not url:
                continue

            # Define headers with a User-Agent
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            # Fetch the image with headers
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Validate Content-Type header
            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"✗ Skipping {url}: Not an image (Content-Type: {content_type})")
                continue

            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Check for duplicate images
            if os.path.exists(filepath):
                print(f"✗ Skipping {filename}: Duplicate image")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()

