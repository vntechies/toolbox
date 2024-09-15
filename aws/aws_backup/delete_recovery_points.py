import boto3
import time

VaultName = str(input('Enter Vault Name: '))
def delete_recovery_points(vault_name, client):
    while True:
        response = client.list_recovery_points_by_backup_vault(BackupVaultName=vault_name)
        recovery_points = response['RecoveryPoints']

        if not recovery_points:
            break
        for recovery_point in recovery_points:
            recovery_point_arn = recovery_point['RecoveryPointArn']
            parent_recovery_point = recovery_point['IsParent']
            print(f"Process recovery point: {recovery_point_arn}")

            if parent_recovery_point:
                child_recovery_points = client.list_recovery_points_by_backup_vault(BackupVaultName=vault_name, ByParentRecoveryPointArn=recovery_point_arn)
                for child_recovery_point in child_recovery_points['RecoveryPoints']:
                    child_recovery_point_arn = child_recovery_point['RecoveryPointArn']
                    print(f"Deleting child recovery point: {child_recovery_point_arn}")

                    #Delete the child recovery point
                    try:
                        client.delete_recovery_point(BackupVaultName=vault_name, RecoveryPointArn=child_recovery_point_arn)
                        print(f"Deleted child recovery point successfully: {child_recovery_point_arn}")
                        time.sleep(5)
                    except Exception as e:
                        print(f"Failed in deleting child recovery point {child_recovery_point_arn}:  {e} ")
            #Delete the parent recovery point
            print(f"Deleting parent recovery point: {recovery_point_arn}")
            try:
                client.delete_recovery_point(BackupVaultName=vault_name,RecoveryPointArn=recovery_point_arn)
                print(f"Deleted parent recovery point successfully: {recovery_point_arn}")
            except Exception as e:
                print(f"Failed in deleting parent recovery point {recovery_point_arn}: {e}")

        if 'NextToken' in recovery_points:
            recovery_points = client.list_recovery_points_by_backup_vault(BackupVaultName=vault_name, NextToken=recovery_points['NextToken'])
        else:
            break
        # Wait for a short interval to avoid rate limiting
        time.sleep(5)

if __name__ == "__main__":
    vault_name = VaultName
    client = boto3.client('backup')
    delete_recovery_points(vault_name, client)