import requests

url = r"https://movie.douban.com/j/search_subjects"
query_data = {
    "type": "movie",
    "tag": "华语",
    "page_limit": 50,
    "page_start": 0
}

my_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}
r = requests.get('https://movie.douban.com/')
print(r.status_code)
