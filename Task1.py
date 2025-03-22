import re

def is_url(url):
    url_pattern = re.compile(
        r'^(https?:\/\/)'  
        r'([\da-z\.-]+)\.([a-z\.]{2,6})'  
        r'([\/\w \.-]*)*\/?$'
    )
    return bool(url_pattern.match(url))

def validate_url(url):
    if not is_url(url):
        raise ValueError("Некорректный аргумент: строка не является URL")
    return url


try:
    url = "https://example.com"
    if is_url(url):
        print(f"'{url}' является URL")
    validated_url = validate_url(url)
    print(f"Валидный URL: {validated_url}")
except ValueError as e:
    print(e)

try:
    url = "example.com"
    if is_url(url):
        print(f"'{url}' является URL")
    validated_url = validate_url(url)
    print(f"Валидный URL: {validated_url}")
except ValueError as e:
    print(e)