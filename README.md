<div align="center">

# Erk

### Türkçe için geliştirilmiş yapay zekâ modeli

*Dünya modelleri Türkçe'yi yabancı bir dil gibi harf harf söker.*
**Erk, dilin kökünü ve eklerini bir bütün olarak anlar.**

<br>

[![Hugging Face](https://img.shields.io/badge/🤗_Model-ecloudtech%2FErk--14B-ffcc00?style=for-the-badge)](https://huggingface.co/ecloudtech/Erk-14B)
[![TurkishMMLU](https://img.shields.io/badge/TurkishMMLU-%25_69.7-2ea043?style=for-the-badge)](degerlendirme/turkishmmlu.md)
[![Parametre](https://img.shields.io/badge/Parametre-14B-2563eb?style=for-the-badge)](#)

**Açık Türkçe modeller arasında TurkishMMLU birincisi**

[Modeli indir (🤗)](https://huggingface.co/ecloudtech/Erk-14B) · [Türkçe](#türkçe) · [English](#english) · [eCloud Tech.](https://www.e-cloud.web.tr)

</div>

---

## Türkçe

### Erk nedir?

**Erk**, [eCloud Yazılım Teknolojileri](https://www.e-cloud.web.tr) tarafından
geliştirilen, **14 milyar parametreli**, Türkçe odaklı bir büyük dil modelidir.

> **Temel model ve şeffaflık.** Erk, açık kaynaklı **[Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)**
> temel alınarak geliştirilmiştir; mimari, tokenizer ve sohbet formatı bu temelden gelir.
> eCloud'un kattığı değer, bunun üzerine kurduğumuz **Türkçe geliştirme hattıdır**: kapsamlı
> Türkçe sürekli ön-eğitim (continued pretraining) ve gerçek belgelerle talimat ayarı (SFT).
> Sektördeki güçlü Türkçe modellerin çoğu gibi (Trendyol → Llama, Turkish-Gemma → Gemma) biz de
> güçlü bir açık temelden yola çıktık; asıl farkı katan Türkçe'ye özel eğitim sürecimizdir — ve
> TurkishMMLU'da temel modeli **%63,4'ten %69,7'ye** çıkararak bunu kanıtladık.

Bugün Türkçe kullanan yapay zekâ modellerinin çoğu İngilizce için tasarlandı ve Türkçe'ye
sonradan uyarlandı. Erk'in Türkçe geliştirme hattı ise Türkçe önceliklidir: kapsamlı Türkçe
sürekli ön-eğitim ve gerçek belgelerle beslenen talimat ayarıyla, temel modeli Türkçe'de
belirgin biçimde ileri taşır.

### Değerlendirme — Evaluation

Erk, bağımsız ve kamuya açık **TurkishMMLU** kıyaslamasında (9 ders, 0-shot doğruluk)
test edilen açık Türkçe modellerin **en iyisidir.**

| Sıra | Model | Ölçek | TurkishMMLU |
|:--:|:---|:--:|:--:|
| | **Erk** | **14B** | **%69,7** |
| | Qwen3-14B *(temel model)* | 14B | %63,4 |
| | Trendyol Asure | 12B | %60,9 |
| 4 | Turkish-Gemma (YTÜ) | 9B | %60,4 |
| 5 | Trendyol v4 | 7B | %53,0 |
| 6 | Kumru (VNGRS) | 2B | %20,1 |

**Ders bazında Erk:**

| Ders | Doğruluk | | Ders | Doğruluk |
|:---|:--:|:--:|:---|:--:|
| Coğrafya | %85 | | Fizik | %62 |
| Felsefe | %85 | | Kimya | %61 |
| Din ve Ahlak | %83 | | Türk Dili ve Edebiyatı | %64 |
| Tarih | %76 | | Matematik | %40 |
| Biyoloji | %71 | | | |

> **Metodoloji:** Tüm sonuçlar `lm-evaluation-harness` ile, bağımsız ve kamuya açık
> TurkishMMLU test setinde, 0-shot koşulunda ölçülmüştür. Karşılaştırılan tüm modeller
> aynı koşullarda değerlendirilmiş ve şeffaf biçimde birlikte raporlanmıştır.

Tüm ders skorları ve metodoloji: [`degerlendirme/turkishmmlu.md`](degerlendirme/turkishmmlu.md)

### Tokenizer hakkında

Erk, temel model **Qwen3-14B'nin tokenizer'ını** kullanır (ChatML formatı, ~152K sözlük).
Bu, temel modelle tam uyumu korur.

> **Not — ayrı bir araştırma:** Açık eğitim reçetemiz
> [nanosohbet](https://github.com/ecloudtechnology/nanosohbet) kapsamında, sıfırdan model
> eğitimi senaryosu için Türkçe'ye özel bir BPE tokenizer eğittik ve 14 tokenizer'la
> karşılaştırdık. Bu Türkçe tokenizer aynı Türkçe metni GPT-4'ün yaklaşık yarısı kadar
> token'a böler (kelime başına 1,51'e karşı 3,01). **Bu tokenizer araştırma amaçlıdır ve
> Erk-14B'de kullanılmamaktadır** — nanosohbet reçetesiyle sıfırdan model eğitmek isteyenler
> içindir. Ayrıntı: [nanosohbet/results](https://github.com/ecloudtechnology/nanosohbet/tree/main/results).

### Erk'i ayıran üç ilke

**1. Derinlemesine Türkçe.** Kapsamlı Türkçe sürekli ön-eğitim ve Türkçe'ye özel geliştirme
sürecimizle, temel modelin Türkçe yetkinliğini belirgin biçimde ileri taşıyan bir dil sezgisi.

**2. Gerçek bilgiyle beslendi.** Erk yalnızca genel sohbetle değil; gerçek hukuki
belgeler, otoriter akademik kaynaklar, doğrulanmış güncel olaylar ve gerçek kullanıcı
konuşmalarıyla eğitildi. Bu yaklaşım, modelin uydurmaya (halüsinasyon) eğilimini azaltır
ve yanlış öncülleri reddetme yeteneği kazandırır.

**3. Açık ve şeffaf.** Erk açık kaynaklıdır ve Qwen3-14B temeli açıkça belirtilmiştir.
Türkçe eğitim yaklaşımımızın dayandığı açık reçete —tokenizer'dan sıfırdan ön-eğitime,
talimat ayarına— [nanosohbet](https://github.com/ecloudtechnology/nanosohbet) deposundadır;
isteyen inceler, isteyen o reçeteyle kendi Türkçe modelini sıfırdan eğitir.

### Kullanım

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ecloudtech/Erk-14B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "ecloudtech/Erk-14B",
    trust_remote_code=True,
    device_map="auto",
    torch_dtype="auto",
)

mesajlar = [
    {"role": "user", "content": "Osmanlı Devleti'nin kuruluşunu kısaca anlatır mısın?"}
]
metin = tokenizer.apply_chat_template(mesajlar, tokenize=False, add_generation_prompt=True)
girdi = tokenizer(metin, return_tensors="pt").to(model.device)
cikti = model.generate(**girdi, max_new_tokens=512, temperature=0.6, top_p=0.9)
print(tokenizer.decode(cikti[0][girdi.input_ids.shape[1]:], skip_special_tokens=True))
```

### Örnek yetenekler

Erk, yalnızca akıcı Türkçe üretmekle kalmaz; **yanlış öncülleri reddeder**:

> **Kullanıcı:** Fatih İstanbul'u fethederken Toyota marka araçla mı gitti?
>
> **Erk:** Hayır. Fatih Sultan Mehmet İstanbul'u 1453'te fethetti; Toyota ise 1937'de
> Japonya'da kurulan bir otomobil markasıdır ve o dönemde henüz yoktu. Bu nedenle soru
> tarihî gerçeklerle örtüşmemektedir.

### Model kartı

| Özellik | Değer |
|:---|:---|
| Geliştirici | eCloud Yazılım Teknolojileri |
| Model tipi | Nedensel dil modeli (decoder-only) |
| Parametre | 14 milyar |
| Dil | Türkçe |
| Bağlam uzunluğu | 32.768 token |
| Bilgi kesim tarihi | Ağustos 2026 |
| Sohbet formatı | ChatML |
| Kesinlik | bfloat16 |
| TurkishMMLU | **%69,7** (açık Türkçe modellerde 1.) |
| Lisans | [eCloud Açık Topluluk Lisansı](LICENSE) |

### Sınırlamalar

Erk güçlü bir Türkçe modelidir; ancak her dil modeli gibi sınırları vardır:

- **Matematik ve sayısal muhakeme** en zayıf olduğu alandır (%40). Karmaşık hesaplama
  gerektiren görevlerde çıktıları doğrulayın.
- Çok spesifik, güncel olaylara dair ayrıntılarda hata yapabilir.
- Bilgi kesim tarihi Ağustos 2026'dır; sonraki gelişmeleri bilmez.
- Üretilen içerik olgusal olarak yanlış olabilir; kritik kullanımlarda doğrulama gerekir.

### Lisans ve ticari kullanım

Erk **açık kaynaklıdır**: herkes indirebilir, çalıştırabilir, inceleyebilir ve üzerine
türev çalışmalar (ince ayar, uyarlama) geliştirebilir.

**Ticari kullanım** — Erk'in veya türevlerinin bir ürün, hizmet ya da gelir getirici
faaliyette kullanılması — eCloud Yazılım Teknolojileri'nden yazılı izin gerektirir.

Ticari kullanım ve iş birliği: **info@e-cloud.web.tr**

### Sırada: Erk-32B

Erk'in genişletilmiş ölçekli sürümü **Erk-32B** üzerindeki çalışmalar başlıyor. Daha
büyük kapasite, daha derin muhakeme ve alan uzmanlığı hedefleniyor.

### Atıf

```bibtex
@misc{erk2026,
  title  = {Erk: Türkçe için geliştirilmiş yapay zekâ modeli (Qwen3-14B tabanlı)},
  author = {eCloud Yazılım Teknolojileri},
  year   = {2026},
  url    = {https://huggingface.co/ecloudtech/Erk-14B}
}
```

---

## English

### What is Erk?

**Erk** is a **14-billion-parameter, Turkish-focused** large language model developed by
[eCloud Yazılım Teknolojileri](https://www.e-cloud.web.tr).

> **Base model & transparency.** Erk is built on the open-source
> **[Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)**; the architecture, tokenizer
> and chat format come from that base. eCloud's contribution is the **Turkish development
> pipeline** layered on top: extensive Turkish continued pretraining and instruction tuning
> (SFT) grounded in real documents. Like most strong Turkish models (Trendyol → Llama,
> Turkish-Gemma → Gemma), we start from a capable open base — the value we add is the
> Turkish-specific training, and we proved it by lifting the base from **63.4% to 69.7%**
> on TurkishMMLU.

Almost every AI model used for Turkish today was designed for English, with Turkish
taught to it afterward. Every Turkish user pays the price: the model doesn't understand
Turkish's agglutinative structure, over-splits words, and runs slower and more expensively.
Erk's Turkish pipeline targets exactly this: extensive Turkish continued pretraining and
instruction tuning that move the base model meaningfully forward in Turkish.

### Evaluation

On the independent, public **TurkishMMLU** benchmark (9 subjects, 0-shot accuracy),
Erk is **the best of the open Turkish models tested.**

| Rank | Model | Size | TurkishMMLU |
|:--:|:---|:--:|:--:|
| | **Erk** | **14B** | **69.7%** |
| | Qwen3-14B *(base model)* | 14B | 63.4% |
| | Trendyol Asure | 12B | 60.9% |
| 4 | Turkish-Gemma | 9B | 60.4% |
| 5 | Trendyol v4 | 7B | 53.0% |
| 6 | Kumru | 2B | 20.1% |

Strongest subjects: **Geography 85% · Philosophy 85% · Religion & Ethics 83% ·
History 76%.** All results measured with `lm-evaluation-harness` on the public
TurkishMMLU test set, 0-shot, with every model evaluated under identical conditions.

### About the tokenizer

Erk uses the tokenizer of its base model, **Qwen3-14B** (ChatML format, ~152K vocab),
preserving full compatibility with the base.

> **Note — separate research:** As part of our open recipe
> [nanosohbet](https://github.com/ecloudtechnology/nanosohbet), we trained a Turkish-specific
> BPE tokenizer for the *train-from-scratch* scenario and compared 14 tokenizers: it splits
> the same Turkish text into about half the tokens of GPT-4 (1.51 vs 3.01 per word).
> **This tokenizer is research-only and is not used in Erk-14B** — it is for people training
> their own Turkish model from scratch with the nanosohbet recipe. Details:
> [nanosohbet/results](https://github.com/ecloudtechnology/nanosohbet/tree/main/results).

### Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ecloudtech/Erk-14B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "ecloudtech/Erk-14B", trust_remote_code=True, device_map="auto", torch_dtype="auto"
)

messages = [{"role": "user", "content": "Explain the founding of the Ottoman Empire in Turkish."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=512, temperature=0.6, top_p=0.9)
print(tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

### Model details

| Property | Value |
|:---|:---|
| Developer | eCloud Yazılım Teknolojileri |
| Type | Causal decoder-only LM |
| Parameters | 14 billion |
| Language | Turkish |
| Context length | 32,768 tokens |
| Knowledge cutoff | August 2026 |
| Chat format | ChatML |
| Precision | bfloat16 |
| License | eCloud Open Community License |

### Limitations

- **Mathematics and numerical reasoning** is the weakest area (40%). Verify outputs on
  computation-heavy tasks.
- May err on very specific, recent factual details. Knowledge cutoff is August 2026.
- Generated content can be factually incorrect; verify for critical use.

### License & commercial use

Erk is **open source**: anyone may download, run, study and build derivatives.
**Commercial use** requires written permission from eCloud Yazılım Teknolojileri.

Commercial use & partnerships: **info@e-cloud.web.tr**

The full training recipe is open at
[nanosohbet](https://github.com/ecloudtechnology/nanosohbet).

---

<div align="center">

Bir **[eCloud Yazılım Teknolojileri](https://www.e-cloud.web.tr)** projesidir.
<br>
*Yerli zekâ, küresel ölçek.*

</div>
