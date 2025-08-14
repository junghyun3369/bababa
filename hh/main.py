from datasets import load_dataset
import os
data = load_dataset("json", data_files="pair.jsonl")
# print(data)
dir = "leejunghyeon/study"
token = os.getenv("HUGGING_TOKEN")
data.push_to_hub(dir, token=token)
