#!/usr/bin/env python
# encoding: utf-8

import unittest


class TestReadMe(unittest.TestCase):

    def testReadMeExample(self):
        from kkbox_developer_sdk.auth_flow import KKBOXOAuth
        from .env import ClientInfo
        auth = KKBOXOAuth(ClientInfo.client_id, ClientInfo.client_secret)
        token = auth.fetch_access_token_by_client_credentials()
        from kkbox_developer_sdk.api import KKBOXAPI
        kkboxapi = KKBOXAPI(token)
        artist_id = '8q3_xzjl89Yakn_7GB'
        artist = kkboxapi.artist_fetcher.fetch_artist(artist_id)
        assert(artist != None)

if __name__ == '__main__':
    unittest.main()
