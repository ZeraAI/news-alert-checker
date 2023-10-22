import requests
from bs4 import BeautifulSoup
import time
import pygame


# Initialize pygame mixer
pygame.mixer.init()

# Define a list of news article URLs to monitor
news_sites = [
    "https://www.nytimes.com/live/2023/10/22/world/israel-hamas-war-gaza-news",
    "https://edition.cnn.com/middleeast/live-news/israel-hamas-war-gaza-news-10-22-23/index.html",
    "https://apnews.com/article/israel-palestinian-gaza-war-syria-lebanon-916edd66e3af095d49e5ba1c59d90c2a",
    "https://www.nbcnews.com/news/world/live-blog/israel-hamas-war-live-updates-rcna121580",
]

# Initialize a dictionary to store the last fetched content for each site
last_content = {url: "" for url in news_sites}

# Define a function to fetch and check for updates for a given URL
def check_for_updates(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article')
        if article:
            article_content = article.text
            if article_content != last_content[url]:
                print(f"New update detected for {url}!")
                pygame.mixer.music.load("notification_sound.mp3")  # Replace with the path to your notification sound
                pygame.mixer.music.play()
                last_content[url] = article_content
            else:
                print(f"No new updates for {url}.")
        else:
            print(f"No 'article' element found on {url}.")
    else:
        print(f"Failed to fetch the content for {url}.")


# Define the main function
def main():
    while True:
        for url in news_sites:
            check_for_updates(url)
        # Adjust the interval as needed (in seconds)
        time.sleep(120)  # Check for updates every 2 minutes

if __name__ == "__main__":
    print("Starting news alert...")
    main()
