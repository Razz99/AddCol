import boto3
import json

dynamodb = boto3.client('dynamodb')

def update_records():
    with open('stuff.json', 'r') as datafile:
        records = json.load(datafile)
    for data in records:
        item = {
                'id':{'S':data['id']},
                'created':{'S':data['created']},
                'test':{'S': '1'}
        }
        print(item)
        response = dynamodb.put_item(
            TableName='stuff', 
            Item=item
        )
        print("UPLOADING ITEM")
        print(response)

if __name__ == '__main__':
    update_records()