import os
import json
from termcolor import colored

def read_jsonl(path: str):
    with open(path) as fh:
        return [json.loads(line) for line in fh.readlines() if line]

def main():
    path = os.path.join("data/example_model_solutions.jsonl")
    qa_objs = read_jsonl(path)

    for qa_obj in qa_objs:
        question = qa_obj["question"]
        ground_truth = qa_obj["ground_truth"]

        def display(label, obj):
            is_correct = obj["is_correct"]
            correctstr = colored("[correct]", color="green") if is_correct else colored("[incorrect]", color="red")
            print(f"{label}: {correctstr}")
            print(obj["solution"])

        print("Q: " + question)
        print(ground_truth)

        print("")
        display("First Choice", qa_obj["First Choice"])

        print("")
        display("Second Choice", qa_obj["Second Choice"])

        print("")
        display("Thrd Choice", qa_obj["Thrd Choice"])

        print("")
        display("Fourth Choice", qa_obj["Thrd Choice"])

        input("press enter")

        print()
        print(f"########")
        print()

if __name__ == "__main__":
    main()