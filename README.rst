
"API Documentation":https://developer.leafly.com/docs

.. code:: python

   if __name__ == "__main__":
       leafly = Leafly(APP_ID, KEY)
       response = leafly.strains(take=1)
       for strain in response['Strains']:
           print strain['UrlName']
