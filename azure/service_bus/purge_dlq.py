#  https://github.com/vntechies/toolbox
#
#  License: MIT
#
# This script purges all messages in Azure service bus DLQ

from azure.servicebus import ServiceBusClient, ServiceBusSubQueue
from azure.servicebus.management import ServiceBusAdministrationClient

# These should be configured via pipeline variables or runtime env
CONNETION_STRING = ""
TOPIC_NAME = ""
SUBSCRIPTION_NAME = ""


def main():
    try:
        # Get the count of dead letter queue (DLQ) messages at the time that the execution starts
        servicebus_admin_client = ServiceBusAdministrationClient.from_connection_string(
            conn_str=CONNETION_STRING
        )
        subscription_properties = (
            servicebus_admin_client.get_subscription_runtime_properties(
                topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME
            )
        )
        dlq_messages_count = subscription_properties.dead_letter_message_count

        # No DLQ messages
        if dlq_messages_count < 1:
            print("No DLQ messages")
            return

        servicebus_client = ServiceBusClient.from_connection_string(
            conn_str=CONNETION_STRING
        )
        with servicebus_client:
            dlq_receiver = servicebus_client.get_subscription_receiver(
                topic_name=TOPIC_NAME,
                subscription_name=SUBSCRIPTION_NAME,
                sub_queue=ServiceBusSubQueue.DEAD_LETTER,
            )
            with dlq_receiver:
                deleted_msg_count = 0
                received_msgs = dlq_receiver.receive_messages(
                    max_message_count=1000, max_wait_time=10
                )
                # DLQ messages might be added to the subscription during the execution,
                # we have to limit the number of messages to be deleted, or this will be an infinity loop
                while len(received_msgs) > 0 and deleted_msg_count < dlq_messages_count:
                    for msg in received_msgs:
                        # delete DLQ messages
                        dlq_receiver.complete_message(msg)
                        deleted_msg_count += 1
                    received_msgs = dlq_receiver.receive_messages(
                        max_message_count=1000, max_wait_time=10
                    )
                if deleted_msg_count > 0:
                    print(
                        "Number of DLQ messages that have been purged: ",
                        deleted_msg_count,
                    )
        print("DQL Purge is completed.")
    except Exception as ex:
        print(ex.message)
        if "could not be found" not in ex.message and "Not Found" not in ex.message:
            raise ex from None


if __name__ == "__main__":
    main()
