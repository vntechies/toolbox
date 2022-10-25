#  https://github.com/vntechies/toolbox
#
#  License: MIT
#
# This script adds tags to a deployment group's machines in bulk
# Specify the tags to change and the machines to update the tags

import json

import requests

# These should be configured via pipeline variables or runtime env
ORGANIZATION = ""
PROJECT = ""
# To find this Id, hit the endpoint
# "https://{ORGANIZATION}.visualstudio.com/{PROJECT}/_apis/distributedtask/deploymentgroups"
# replacing the project with the one you're looking for the deployment
# group in
DEPLOYMENT_GROUD_ID = 123
AUTH_TOKEN = ""
# Comma-separated  list of tags to add (e.g., "tag1,tag2,tag3")
TAGS_TO_ADD = ""
# Comma-separated  list of tags to delete (e.g., "tag1,tag2,tag3")
TAGS_TO_DELETE = ""
# Comma-separated list of names of the machines that need to change (e.g.,
# "machine1, machine2")
MACHINES_TO_CHANGE = ""
DG_API_URL = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT}/_apis/distributedtask/deploymentgroups/{DEPLOYMENT_GROUD_ID}/targets?api-version=6.0-preview.1"
HEADER = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json",
    "Authorization": AUTH_TOKEN,
}

# This gets all the machines that belong to the specified deployment group


def get_all_machine(url, header):
    print(f"Target machines defs API:{url}")

    response = requests.request("GET", url, headers=header)

    if response.status_code != 200:
        error_message = "Expected status code 200, but got %d, with response: %s" % (
            response.status_code,
            response.text,
        )
        raise requests.ConnectionError(error_message)

    return response


# This update the configured machines with the updated tags
def update_tags(url, header, payload):

    response = requests.request(
        "PATCH", url, headers=header, data=payload.encode("utf-8")
    )

    if response.status_code != 200:
        error_message = "Expected status code 200, but got %d, with response: %s" % (
            response.status_code,
            response.text,
        )
        raise requests.ConnectionError(error_message)

    return response


def main():
    response = get_all_machine(DG_API_URL, HEADER)
    machines = json.loads(response.text)["value"]

    machines_to_change = MACHINES_TO_CHANGE.split(",")
    tags_to_add = TAGS_TO_ADD.split(",")
    tags_to_delete = TAGS_TO_DELETE.split(",")
    updated_machines = []

    for machine in machines:
        machine_name = machine["agent"]["name"]
        if machine_name in machines_to_change:
            current_tags = machine["tags"]
            print("*" * 30)
            print(f"Updating tag(s) on machine {machine_name}")
            print(f"Current tag(s): {','.join(current_tags)}")

            updated_tags = current_tags

            if len(tags_to_add) > 0 and tags_to_add[0] != "":
                print(f"Adding tag(s): {','.join(tags_to_add)}")
                for tag in tags_to_add:
                    if tag not in current_tags:
                        updated_tags.append(tag)

            if len(tags_to_delete) > 0 and tags_to_delete[0] != "":
                print(f"Deleting tag(s): {','.join(tags_to_delete)}")
                updated_tags = [
                    tag for tag in updated_tags if tag not in tags_to_delete
                ]

            updated_machines.append({"tags": updated_tags, "id": machine["id"]})

    json_data = json.dumps(updated_machines)
    response = update_tags(DG_API_URL, HEADER, json_data)
    machines = json.loads(response.text)["value"]

    for machine in machines:
        print("-" * 20)
        print(f"Machine ID: {machine['id']} | Machine name: {machine['agent']['name']}")
        print(
            f"Added tags: {','.join(machine['addedTags'])} / Deleted tags: {','.join(machine['deletedTags'])}"
        )
    print("The tag(s) have been updated!")
    print("*" * 30)


if __name__ == "__main__":
    main()
