from requests import get

response = get('https://swapi.dev/api/people/1')
print(response.content)
print(response.text)
print(response.status_code)
