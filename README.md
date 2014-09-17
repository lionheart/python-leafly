python-leafly
=============

[Leafly API Documentation](https://developer.leafly.com/docs)

Installation
------------

python-leafly is available for download through the Python Package Index (PyPi). You can install it right away using pip or easy_install.

```
pip install leafly
```

Usage
-----

To get started, you're going to need to sign up as a developer on the Leafly developer site. Once you've got an application ID and a key, you're ready to go.

```python
import leafly

leafly = Leafly(app_id, key)
```

To turn on debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Strain Search

python-leafly maps directly to the Leafly API itself. E.g., to get all available strains:

```python
response = leafly.strains()
strains = response['Strains']
for strain in strains:
    print strain['UrlName']
```

### Strain Details

To retrieve strain details, just use the `UrlName` attribute (i.e., a slug) on a strain object and pass it in as a component to the leafly object.

```python
response = leafly.strains['blue-dream']()
```

### Reviews

```python
response = leafly.strains['blue-dream'].reviews(take=10, page=0)
for review in response['reviews']:
    print review['id'], review['text']
```

### Review Details

```python
response = leafly.strains['blue-dream'].reviews[1234]()
print response['rating']
```

### Strain Photos

```python
response = leafly.strains['blue-dream'].photos(take=10, page=0)
for photo in response['photos']:
    print photo['thumb']
```

### Strain Availability

```python
response = leafly.strains['blue-dream'].availability(lat=47.606, lon=-122.333)
for dispensary in response:
    print dispensary['name']
```

### Dispensary Search

```python
response = leafly.locations(take=10, page=0, latitude=47.606, longitude=-122.333, hasedibles=True)
for dispensary in response['stores']:
    print dispensary['name']
```

### Dispensary Details

```python
response = leafly.locations['herbal-nation']()
print response['permalink']
```

### Dispensary Menu

```python
response = leafly.locations['herbal-nation'].menu()
for item in response:
    print item['name']
```

### Dispensary Reviews

```python
response = leafly.locations['herbal-nation'].reviews(skip=0, take=10)
for review in response['reviews']
    print review['comments']
```
