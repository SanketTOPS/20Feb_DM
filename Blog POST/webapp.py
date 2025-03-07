import webbrowser
import subprocess

# List of URLs to open
urls = [
    "https://learnaidigital.blogspot.com/",
    "https://learnaidigital.blogspot.com/2025/03/top-digital-marketing-trends-in-2025.html",
    "https://learnaidigital.blogspot.com/2025/03/digital-marketing-with-ai-tools-future.html",
    "https://learnaidigital.blogspot.com/2025/02/ai-in-digital-marketing-revolutionizing.html",
]

# Paths to different browsers (Update these paths based on your system)
browsers = {
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "firefox": "C:/Program Files/Mozilla Firefox/firefox.exe",
    "edge": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
}

# Open each URL in all browsers
for url in urls:
    for browser, path in browsers.items():
        try:
            subprocess.run([path, url])  # Open URL in the specified browser
            print(f"Opened {url} in {browser}")
        except Exception as e:
            print(f"Could not open {url} in {browser}: {e}")
