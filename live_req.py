import requests_cache

session = requests_cache.CachedSession('demo_cache')
for i in range(60):
    a = session.get('https://httpbin.org/delay/1')
    print(a.content.decode())
