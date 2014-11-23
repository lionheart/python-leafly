import datetime
import json
import operator
import logging
import requests
import exceptions
import pprint

LEAFLY_API_ENDPOINT = "http://data.leafly.com/"

logger = logging.getLogger(__name__)

class Leafly(object):
    BOOLEAN_FIELDS = [
        "storefront",
        "delivery",
        "retail",
        "medical",
        "creditcards",
        "hasclones",
        "hasconcentrates",
        "hasedibles",
        "veterandiscount"
    ]

    def __init__(self, app_id, key):
        self.app_id = app_id
        self.key = key

    def __getattr__(self, k):
        return LeaflyCall(self.app_id, self.key, k)


class LeaflyCall(object):
    def __init__(self, app_id, key, path):
        self.app_id = app_id
        self.key = key
        self.components = [path]

    def __getattr__(self, k):
        self.components.append(k)
        return self

    def __getitem__(self, k):
        self.components.append(str(k))
        return self

    def __call__(self, *args, **kwargs):
        url = "{}{}".format(LEAFLY_API_ENDPOINT, "/".join(self.components))

        params = kwargs.copy()

        for field in Leafly.BOOLEAN_FIELDS:
            if field in kwargs:
                if isinstance(kwargs[field], bool):
                    if kwargs[field]:
                        params[field] = "true"
                    else:
                        # Don't add the param if it is not True
                        pass

        headers = {
            'app_id': self.app_id,
            'app_key': self.key
        }

        new_kwargs = {
            'headers': headers
        }

        if self.components == ["strains"]:
            fun = requests.post
            new_kwargs['data'] = json.dumps(params)
        elif self.components == ["locations"]:
            fun = requests.post
            new_kwargs['data'] = params
        else:
            fun = requests.get
            new_kwargs['data'] = params

        response = fun(url, **new_kwargs)

        logger.debug(url)
        return response.json()

if __name__ == "__main__":
    import sys
    leafly = Leafly(*sys.argv[1:])

