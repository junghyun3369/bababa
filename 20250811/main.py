from datasets import load_dataset
from huggingface_hub import login, delete_repo
# dataset = load_dataset("leejunghyeon/aitest")
# print(dataset)
import os

# jsonFile = "ai_test.jsonl"
# dataset = load_dataset("json", data_files=jsonFile)
# print(dataset)

repo_name = "leejunghyeon/aitest"
token = os.getenv("HUGGING_TOKEN")

# 입력 및 추가
# dataset.push_to_hub(repo_name, token=token)

# 삭제
# login(token=token)
# delete_repo(repo_id=repo_name, repo_type="dataset")




