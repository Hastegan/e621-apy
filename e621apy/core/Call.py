"""
Contains the Call class
"""

import os

from requests import get, codes as httpstatus

from e621apy import helpers
from e621apy import Post
from e621apy import PostQuery
from e621apy import Parser

__all__ = [
    'Call',
]

class Call(object):
    """
    Call communicates with the e621 API
    """

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    api_root = 'https://e621.net'
    interfaces = {
        'post': 'post',
    }
    actions = {
        'list': 'index.json',
    }

    def __init__(self, query):
        """
        Constructor
        """
        self._query = query
        self.type = None
        self.action = 'list'

        self._define_query()

    def _define_query(self):
        """
        Set the type of the query
        """
        if isinstance(self._query, PostQuery):
            self.type = "post"

    def fetch(self):
        """
        Execute the current query
        """
        params = self._query.get_url_params()
        return self._request(params)

    def _request(self, params):
        """
        Send a request to the API and handle its answer
        """
        headers = {'User-Agent': self.user_agent}
        response = get(self.build_url(), params=params, headers=headers)

        if response.status_code is not httpstatus.ok:
            raise Exception(response.status_code)

        return response.json()

    def build_url(self):
        """
        Return the url corresponding to the e621 api endpoint
        """
        return "{domain}/{interface}/{action}".format(
            domain=self.api_root,
            interface=self.interfaces[self.type],
            action=self.actions[self.action]
        )

    def get(self):
        """
        Return objects in the call content
        """
        data = self.fetch()
        parser = Parser(self.type)
        return parser.parse(data)
