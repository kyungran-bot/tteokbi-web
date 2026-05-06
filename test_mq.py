import urllib.request, time
try:
    urllib.request.urlopen('http://localhost:8000/style.css').read()
    print("server is up")
except Exception as e:
    print(e)
