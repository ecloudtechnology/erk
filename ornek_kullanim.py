"""
Erk — örnek kullanım
====================

Erk'i Hugging Face'ten indirip çeşitli Türkçe görevlerde deneyen basit bir örnek.

Kurulum:
    pip install "transformers>=4.44" torch accelerate

Model: https://huggingface.co/ecloudtech/Erk-14B
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "ecloudtech/Erk-14B"


def yukle():
    tokenizer = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL,
        trust_remote_code=True,
        device_map="auto",
        torch_dtype="auto",
    )
    return tokenizer, model


def sor(tokenizer, model, soru, max_yeni=512):
    mesajlar = [{"role": "user", "content": soru}]
    metin = tokenizer.apply_chat_template(
        mesajlar, tokenize=False, add_generation_prompt=True
    )
    girdi = tokenizer(metin, return_tensors="pt").to(model.device)
    with torch.no_grad():
        cikti = model.generate(
            **girdi,
            max_new_tokens=max_yeni,
            temperature=0.6,
            top_p=0.9,
            repetition_penalty=1.05,
        )
    return tokenizer.decode(
        cikti[0][girdi.input_ids.shape[1]:], skip_special_tokens=True
    ).strip()


if __name__ == "__main__":
    tokenizer, model = yukle()

    sorular = [
        "Osmanlı Devleti'nin kuruluşunu kısaca anlatır mısın?",
        "Kıdem tazminatına ne zaman hak kazanılır?",
        "Yapay zekâ nedir, günlük hayatta nasıl kullanılır?",
        "Karadeniz Bölgesi'nin coğrafi özellikleri nelerdir?",
    ]

    for soru in sorular:
        print("=" * 70)
        print("Soru:", soru)
        print("Erk :", sor(tokenizer, model, soru))
