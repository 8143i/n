import urllib.request

# Download the webpage and save it as webpage.html
urllib.request.urlretrieve("https://www.google.com/", "webpage.html")

print("Web page downloaded successfully!")
