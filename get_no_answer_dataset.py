#!/usr/bin/env python
import json
import random
import argparse

def get_no_answer_samples(data):
    new_data = []
    question_paragraph_idx = []
    questions = []
    for di, doc in enumerate(data):
        for pi, para in enumerate(doc["paragraphs"]):
            for qi, qa in enumerate(para["qas"]):
                question_paragraph_idx.append([di, pi, qi])
                questions.append(qa["question"])
                data[di]["paragraphs"][pi]["qas"][qi]["is_impossible"] = False
    for di, doc in enumerate(data):
        new_doc = {"title": doc["title"], "paragraphs": []}
        for pi, para in enumerate(doc["paragraphs"]):
            new_qas = []
            for qi, qa in enumerate(para["qas"]):
                selected_idx = random.choice(list(range(len(question_paragraph_idx))))
                while question_paragraph_idx[selected_idx][0] == di and question_paragraph_idx[selected_idx][1] == pi:
                    selected_idx = random.choice(list(range(len(question_paragraph_idx))))
                question = questions[selected_idx]
                new_qas.append({"question": question, "answers": [], "id": qa["id"] + "-neg", "is_impossible": True})
            new_doc["paragraphs"].append({"context": para["context"], "qas": new_qas})
        new_data.append(new_doc)
    new_data = data + new_data
    return new_data

parser = argparse.ArgumentParser()

with open("./TASA/data/squad/dev-v1.1.json", "r", encoding="utf-8") as f:
    train_data = json.load(f)
new_train_data = get_no_answer_samples(train_data["data"])
with open("squad_unanswerable.json", "w", encoding="utf-8") as f:
    json.dump({"data": new_train_data, "version": train_data["version"], "len": train_data["len"] * 2}, f)
