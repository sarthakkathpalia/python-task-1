import pandas as pd

list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def merge_lists(list_1, list_2) -> list:
  l1=pd.DataFrame(list_1)
  l2=pd.DataFrame(list_2)

  data_merge = pd.merge(l1,l2,on='id',how='outer')
  print(data_merge.to_dict('records'))

list_3 = merge_lists(list_1, list_2)