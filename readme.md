Background:
- have a live production DynamoDB with a roughly 5 millino records.
- records contains followinf fields:
    - id: partition key
    - created: sort key
- latest version of records will have additional fild "test"

Rerquirement: 
- Old record does not contains "test".
- needs to add default value as 1 for all existing records.

Assumptions:
- I am assuming we have backup of existing data with the name "stuff.json". If we don't have backup we can first perform "get_item" operation and retrive all existing data.


Solution Approach:
- Perform Database Update operation with default value for "test" field.
- database function "put_item"
        - it replaces the existing records if it finds existing records with the same key 
        - if no records match it will add new records.
        - in our scenario put_item operation will find "id" and "created" attribute in "stuff" table so it will replace these two value and adds new field "test"


complexity analysis:
- for n records this scripts runs n times so time complexity will be Big-O of N (i.e.O(n))







