from datasets import DatasetDict, load_dataset

from config import DATASET_NAME


def get_dataset(dataset_name: str = DATASET_NAME) -> DatasetDict:
    """
    Load dataset from huggingface
    """
    dataset = load_dataset(dataset_name)
    return dataset


if __name__ == "__main__":
    dataset = get_dataset()
    print(dataset["train"].to_pandas())
