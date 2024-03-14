from pprint import pprint
from requests import get

pprint(get('http://localhost:5000/api/v2/news').json())