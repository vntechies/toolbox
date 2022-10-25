#  https://github.com/vntechies/toolbox
#
#  License: MIT
#
# This script get an index's statistics from Azure search service using Azure API

import requests
import json

# These should be configured via pipeline variables or runtime env
INDEX_NAME = ""
API_VERSION = ""
SEARCH_SERVICE_NAME = ""
SEARCH_API_KEY = ""


def main():
    try:
        print("Getting statistics for indexes via AzureAPI")

        url = "https://%s.search.windows.net/indexes/%s/stats?api-version=%s" % (
            SEARCH_SERVICE_NAME, INDEX_NAME, API_VERSION)
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'api-key': SEARCH_API_KEY
        }

        print("Getting statistics of %s index on %s service" % (
            INDEX_NAME, SEARCH_SERVICE_NAME))
        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            documentCount = json.loads(response.text)['documentCount']
            storageSize = json.loads(response.text)['storageSize']
            message = "Statistics of %s index on %s service: Document count: %s, Storage Size: %s" % (
                INDEX_NAME, SEARCH_SERVICE_NAME, documentCount, storageSize)
            print(message)
        elif response.status_code == 404:
            message = "There is no %s index on %s service" % (
                INDEX_NAME, SEARCH_SERVICE_NAME)
            print(message)
        else:
            raise requests.ConnectionError(
                "Expected status code 200, but got %d, with response: %s" % (response.status_code, response.text))
    except Exception as ex:
        error = "Exception on getting statistics of %s index on %s service: %s" % (
            INDEX_NAME, SEARCH_SERVICE_NAME, ex)
        print(error)
        raise ex from None


if __name__ == "__main__":
    main()
