#  https://github.com/vntechies/toolbox
#
#  License: MIT
#
# This script deletes an index from Azure search service using Azure API

import requests

# These should be configured via pipeline variables or runtime env
INDEX_NAME = ""
API_VERSION = ""
SEARCH_SERVICE_NAME = ""
SEARCH_API_KEY = ""


def main():
    try:
        print("Delete indexes via AzureAPI")
        url = "https://%s.search.windows.net/indexes/%s?api-version=%s" % (
            SEARCH_SERVICE_NAME,
            INDEX_NAME,
            API_VERSION,
        )

        payload = {}
        headers = {
            "Content-Type": "application/json  ",
            "api-key": SEARCH_API_KEY,
        }

        print(
            "Deleting the %s index from %s search service."
            % (INDEX_NAME, SEARCH_SERVICE_NAME)
        )

        response = requests.request("DELETE", url, headers=headers, data=payload)
        if response.status_code == 204:
            message = "Successfully deleted the %s index from %s search service." % (
                INDEX_NAME,
                SEARCH_SERVICE_NAME,
            )
            print(message)
        elif response.status_code == 404:
            message = "There is no %s index on %s service" % (
                INDEX_NAME,
                SEARCH_SERVICE_NAME,
            )
            print(message)
        else:
            raise requests.ConnectionError(
                "Expected status code 204, but got %d, with response: %s"
                % (response.status_code, response.text)
            )

    except Exception as ex:
        error = "Exception on deleting %s index of %s service: %s" % (
            INDEX_NAME,
            SEARCH_SERVICE_NAME,
            ex,
        )
        print(error)
        raise ex from None


if __name__ == "__main__":
    main()
