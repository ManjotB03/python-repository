import requests
#send a simple request
#r = requests.get('https://requestb.in/wpo4xjwp')

#reading the response
#r = requests.get('https://reqres.in/api/users/2')
#print(r.text) #if response is 200 that means successful
#json_data = r.json()
#print(json_data['data']['first_name'])

#passing URL parameters
#r = requests.get('https://requestb.in/wpo4xjwp?key1=value1&key2=value2')

#payload = {'first': 'one', 'second' : 'two'}
#r = requests.get('https://requestb.in/wpo4xjwp', params=payload)

#custome headers
#headers = {'my-token' : '37739489hbfhjdbfejfjkdf8'}
#r = requests.get('https://requestb.in/wpo4xjwp', headers = headers)

#changing the request method
#r=requests.post('https://requestb.in/wpo4xjwp')

#r=requests.delete('https://requestb.in/wpo4xjwp')

#r=requests.put('https://requestb.in/wpo4xjwp')

#r=requests.patch('https://requestb.in/wpo4xjwp')

#sending a request with JSON
#payload = {'name' : 'Anthony', 'job' : 'Programmer'}
#r = requests.post('https://reqres.in/api/users', json=payload)
#print(r)
#print(r.text)

#sending request with form data
#payload = {'name' : 'Anthony', 'location' : 'Las Vegas'}
#r = requests.post('https://requestb.in/wpo4xjwp', params=payload)
#r = requests.post('https://httpbin.org/post', data=payload)
#print(r.text)

#sending files
#files = {'file': open('cat.jpg', 'rb'), 'image/jpeg')}
#r = requests.post('https://requestb.in/wpo4xjwp', files=files)

#saving an image
#r = requests.get('https://httpbin.org/image/jpeg')
#print(r.headers)

#with open('image.jpeg', 'wb') as fd:
#    for chunk in r.iter_content(chunk_size=500):
#        fd.write(chunk)

#exceptions
#r = requests.get('https://httpbin.org/status/423')
#try:
#    r.raise_for_status()
#except requests.exceptions.HTTPError:
#    print('ERROR! ERROR! ERROR!')

#print(r)

#try:
#    r=requests.get('https://dfjjbhbshbvhj.com')
#except requests.exceptions.ConnectionError:
#    print('CONNECTION ERROR!')

#timeout
#try:
#    r = requests.get('https://httpbin.org/delay/10', timeout=5)
#except requests.exceptions.ReadTimeout:
#    print('TIMED OUT!!!')

#HTTP Basic Authentication