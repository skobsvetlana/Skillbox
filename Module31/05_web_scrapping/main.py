import re
import requests

path = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(path)
text = response.text
pattern = r'<h3.+>(.+)</h3>'
res = re.findall(pattern=pattern, string=text)

print(res)


