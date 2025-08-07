import boto3

client = boto3.client('logs', region_name='ap-south-1')  # Change region if needed

response = client.describe_log_groups()

log_groups = [group['logGroupName'] for group in response['logGroups']]

print(f"Total Log Groups Found: {len(log_groups)}")
print("Available Log Groups:")

for i, group_name in enumerate(log_groups):
    print(f"{i+1}. {group_name}")

if not log_groups:
    print("❌ No log groups found. Please check your AWS region or credentials.")
else:
    choice = int(input("Select a log group (number): "))
    log_group = log_groups[choice - 1]
    print(f"✅ You selected: {log_group}")
