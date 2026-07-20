<div align="center">

# Erk

### Türkçe için sıfırdan geliştirilmiş yapay zekâ modeli

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

> **"Sıfırdan" ne demek?** Erk'i, açık bir temel model üzerinde **sıfırdan kurduğumuz
> bir Türkçe eğitim hattıyla** geliştirdik: sıfırdan oluşturduğumuz Türkçe derlem,
> milyarlarca token'lık Türkçe sürekli ön-eğitim ve gerçek belgelerle talimat ayarı.
> Amacımız tekerleği yeniden icat etmek değil, **Türkçe'yi en iyi anlayan modeli**
> üretmekti. Sektördeki güçlü Türkçe modellerin çoğu gibi biz de güçlü bir açık temelden
> yola çıktık; asıl değeri katan ise Türkçe'ye özel geliştirme sürecimizdir — ve
> TurkishMMLU'da bu temeli geçerek bunu kanıtladık.

Bugün Türkçe kullanan yapay zekâ modellerinin çoğu İngilizce için tasarlandı ve Türkçe'ye
sonradan uyarlandı. Erk ise baştan sona Türkçe düşünülerek geliştirildi: kapsamlı Türkçe
ön-eğitim ve gerçek belgelerle beslenen talimat ayarıyla, Türkçe'yi bir ikinci dil olarak
değil, öncelikli dili olarak işler.

### Değerlendirme — Evaluation

Erk, bağımsız ve kamuya açık **TurkishMMLU** kıyaslamasında (9 ders, 0-shot doğruluk)
test edilen açık Türkçe modellerin **en iyisidir.**

| Sıra | Model | Ölçek | TurkishMMLU |
|:--:|:---|:--:|:--:|
| | **Erk** | **14B** | **%69,7** |
| | Qwen3 | 14B | %63,4 |
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

### Türkçe tokenizasyon araştırmamız

Türkçe sondan eklemelidir: *"gözlüklerimizdekilerdenmiş"* gibi tek bir kelimeye onlarca
ek eklenebilir. İngilizce için tasarlanmış tokenizer'lar bu yapıyı tanımaz ve kelimeyi
gereksiz parçalara böler.

Açık eğitim reçetemiz [nanosohbet](https://github.com/ecloudtechnology/nanosohbet)
kapsamında, Türkçe'ye özel bir tokenizer eğitip 14 tokenizer'la karşılaştırdık.
Ürettiğimiz Türkçe-native tokenizer, aynı Türkçe metni **GPT-4'ün yarısı kadar token'a
böler** (kelime başına 1,51'e karşı 3,01) ve test edilen tüm tokenizer'ları Türkçe'de
geçer.

| Tokenizer | Kelime başına token (Türkçe) | Göreli maliyet |
|:---|:---:|:---:|
| **Türkçe-native (nanosohbet)** | **1.51** | **1.00×** |
| GPT-4o | 2.26 | 1.50× |
| GPT-4 | 3.01 | **1.99×** |
| Kimi K2 | 3.07 | 2.03× |

Tam karşılaştırma:
[nanosohbet/results](https://github.com/ecloudtechnology/nanosohbet/tree/main/results).

### Erk'i ayıran üç ilke

**1. Kökünden Türkçe.** Kapsamlı Türkçe sürekli ön-eğitim ve Türkçe'ye özel geliştirme
sürecimizle, dilin kendi yapısını temelden anlayan bir dil sezgisi.

**2. Gerçek bilgiyle beslendi.** Erk yalnızca genel sohbetle değil; gerçek hukuki
belgeler, otoriter akademik kaynaklar, doğrulanmış güncel olaylar ve gerçek kullanıcı
konuşmalarıyla eğitildi. Bu yaklaşım, modelin uydurmaya (halüsinasyon) eğilimini azaltır
ve yanlış öncülleri reddetme yeteneği kazandırır.

**3. Açık ve tekrarlanabilir.** Erk'i doğuran eğitim reçetesinin her adımı —
tokenizer'dan ön-eğitime, talimat ayarına— [nanosohbet](https://github.com/ecloudtechnology/nanosohbet)
deposunda açıktır. İsteyen inceler, isteyen kendi Türkçe modelini eğitir.

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
  title  = {Erk: Türkçe için sıfırdan geliştirilmiş yapay zekâ modeli},
  author = {eCloud Yazılım Teknolojileri},
  year   = {2026},
  url    = {https://huggingface.co/ecloudtech/Erk-14B}
}
```

---

## English

### What is Erk?

**Erk** is a **14-billion-parameter, Turkish-native** large language model developed by
[eCloud Yazılım Teknolojileri](https://www.e-cloud.web.tr).

Almost every AI model used for Turkish today was designed for English, with Turkish
taught to it afterward. Every Turkish user pays the price: the model doesn't understand
Turkish's agglutinative structure, over-splits words, and runs slower and more expensively.

Erk takes a different path. We built it on a strong open base model, through a
**Turkish training pipeline we created from scratch**: a from-scratch Turkish corpus,
extensive Turkish continued pretraining, and instruction tuning grounded in real
documents. Like most strong Turkish models, we started from a capable open base — the
value we add is the Turkish-specific development, and we proved it by surpassing that
base on TurkishMMLU.

### Evaluation

On the independent, public **TurkishMMLU** benchmark (9 subjects, 0-shot accuracy),
Erk is **the best of the open Turkish models tested.**

| Rank | Model | Size | TurkishMMLU |
|:--:|:---|:--:|:--:|
| | **Erk** | **14B** | **69.7%** |
| | Qwen3 | 14B | 63.4% |
| | Trendyol Asure | 12B | 60.9% |
| 4 | Turkish-Gemma | 9B | 60.4% |
| 5 | Trendyol v4 | 7B | 53.0% |
| 6 | Kumru | 2B | 20.1% |

Strongest subjects: **Geography 85% · Philosophy 85% · Religion & Ethics 83% ·
History 76%.** All results measured with `lm-evaluation-harness` on the public
TurkishMMLU test set, 0-shot, with every model evaluated under identical conditions.

### Turkish tokenization research

Turkish is agglutinative — dozens of suffixes attach to a single root. English-centric
tokenizers over-split Turkish. As part of our open recipe
[nanosohbet](https://github.com/ecloudtechnology/nanosohbet), we trained a Turkish-native
tokenizer and compared 14 tokenizers: ours splits the same Turkish text into **half the
tokens of GPT-4** and beats every tokenizer tested.

| Tokenizer | Tokens per word (Turkish) | Relative cost |
|:---|:---:|:---:|
| **Turkish-native (nanosohbet)** | **1.51** | **1.00×** |
| GPT-4o | 2.26 | 1.50× |
| GPT-4 | 3.01 | **1.99×** |
| Kimi K2 | 3.07 | 2.03× |

Full comparison:
[nanosohbet/results](https://github.com/ecloudtechnology/nanosohbet/tree/main/results).

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
