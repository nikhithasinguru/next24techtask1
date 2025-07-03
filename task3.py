import tkinter as tk
from tkinter import messagebox, scrolledtext
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Selenium setup
def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)

def get_lyrics():
    artist = artist_entry.get().strip()
    title = title_entry.get().strip()
    if not artist or not title:
        messagebox.showerror("Input Error", "Please enter both artist and song title.")
        return

    driver = create_driver()
    try:
        query = f"{title} {artist} site:genius.com"
        search_url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        driver.get(search_url)
        time.sleep(1)

        # Click first Genius link
        link_elem = driver.find_element("xpath", "//a[contains(@href,'genius.com') and contains(text(),'genius.com')]")
        if not link_elem:
            raise Exception("Lyrics page not found.")
        link = link_elem.get_attribute("href")

        driver.get(link)
        time.sleep(2)  # wait for page to render

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        # Extract lyrics
        lyrics = ""
        divs = soup.find_all("div", {"data-lyrics-container": "true"})
        if divs:
            lyrics = "\n".join([d.get_text("\n") for d in divs]).strip()

        if not lyrics:
            divs = soup.find_all("div", class_="Lyrics__Container")
            if divs:
                lyrics = "\n".join([d.get_text("\n") for d in divs]).strip()

        if not lyrics:
            div = soup.find("div", class_="lyrics")
            if div:
                lyrics = div.get_text("\n").strip()

        if not lyrics:
            raise Exception("Lyrics found but not extracted.")

        lyrics_text.config(state='normal')
        lyrics_text.delete("1.0", tk.END)
        lyrics_text.insert(tk.END, lyrics[:20000])
        lyrics_text.config(state='disabled')

    except Exception as e:
        driver.quit()
        messagebox.showerror("Error", f"{str(e)}")

# GUI setup
root = tk.Tk()
root.title("Lyrics Finder (Selenium)")
root.geometry("500x600")
root.config(bg="#f0f8ff")

tk.Label(root, text="🎵 Lyrics Finder 🎵", font=("Segoe UI",20,"bold"), bg="#f0f8ff").pack(pady=10)
tk.Label(root, text="Artist:", font=("Segoe UI",12), bg="#f0f8ff").pack()
artist_entry = tk.Entry(root, font=("Segoe UI",12),width=40)
artist_entry.pack(pady=5)
tk.Label(root, text="Song Title:", font=("Segoe UI",12), bg="#f0f8ff").pack()
title_entry = tk.Entry(root, font=("Segoe UI",12),width=40)
title_entry.pack(pady=5)
tk.Button(root, text="Get Lyrics",command=get_lyrics,font=("Segoe UI",12,"bold"),
          bg="#007acc",fg="white",padx=10,pady=5).pack(pady=15)

lyrics_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI",12),
                                        height=20, width=58, state="disabled", bg="#ffffff")
lyrics_text.pack(pady=10)

root.mainloop()
