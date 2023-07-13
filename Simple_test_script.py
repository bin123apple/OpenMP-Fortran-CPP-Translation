from transformers import OPTForCausalLM, AutoTokenizer
from transformers import pipeline
import torch
from datasets import load_dataset

model = OPTForCausalLM.from_pretrained("facebook/opt-2.7b").to('cuda:2')
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-2.7b")

dataset = load_dataset("Bin12345/HPC_Fortran_CPP")['test']

translated_texts = []

for i in range(len(dataset['cpp'])):
    input_prompt = "Translate the following cpp code to Fortran " + dataset['cpp'][i]
    input_ids = tokenizer.encode(input_prompt, return_tensors="pt").to('cuda:2')
    if len(input_prompt) < 1024:
        outputs = model.generate(input_ids, max_length=2*len(input_prompt), num_return_sequences=1)
        predicted_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        new_chars = predicted_answer[len(input_prompt):]
        translated_texts.append(new_chars)

with open("output.txt", "w") as f:
    for text in translated_texts:
        f.write(text + '\n')