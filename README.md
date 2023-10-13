# Fortran-CPP-HPC-code-translation-dataset

Our paper is avaliable at [http://arxiv.org/abs/2307.07686](http://arxiv.org/abs/2307.07686).

This repository contains training and testing dataset and a simple test script.

We collect data form three different source: 

[Polybench](https://web.cse.ohio-state.edu/~pouchet.2/software/polybench/)

[NAS Parallel Benchmarks](https://www.nas.nasa.gov/software/npb.html)

[dataracebench](https://github.com/LLNL/dataracebench)

You can also download the dataset from : [My Huggingface](https://huggingface.co/datasets/Bin12345/HPC_Fortran_CPP)

Here is one data pair example:

![Here is one data pair example:](https://github.com/bin123apple/OpenMP-Fortran-CPP-Translation/blob/main/Figures/Data%20Pair%20Example.png)

We will add more data pairs in the future and will add a new "nature language" column for code generation task.

## Reproduce our result

1. Finetune the model by using deepspeed
```
deepspeed --master_port 12345 main.py \
   --data_path Bin12345/HPC_Fortran_CPP \
   --model_name_or_path path/to/starcoder_model \
   --per_device_train_batch_size 1 \
   --per_device_eval_batch_size 1 \
   --max_seq_len 128 \
   --learning_rate 9.65e-6 \
   --weight_decay 0.1 \
   --num_train_epochs 3 \
   --gradient_accumulation_steps 2 \
   --lr_scheduler_type cosine \
   --num_warmup_steps 0 \
   --seed 1234 \
   --zero_stage $ZERO_STAGE \
   --deepspeed \
   --output_dir $OUTPUT \
   &> $OUTPUT/training.log
```

2. Use the finetuned model to generate the prompts. You can try our simple test scripts. And for different models, there might be slightly difference.

{% include licenses/NOTICE %}

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
