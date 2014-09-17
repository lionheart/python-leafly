import datetime
import json
import operator
import logging
import requests
import exceptions
import pprint

LEAFLY_API_ENDPOINT = "http://data.leafly.com/"

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
        self.components.append(k)
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

        kwargs = {
            'headers': headers
        }

        if self.components == ["strains"]:
            fun = requests.post
            page = kwargs.get('page', 0)
            take = kwargs.get('take', 10)
            kwargs['data'] = json.dumps({
                'Page': page,
                'Take': take
            })
        elif self.components == ["locations"]:
            fun = requests.post
            kwargs['data'] = params
        else:
            fun = requests.get

        response = fun(url, **kwargs)
        return response.json()

