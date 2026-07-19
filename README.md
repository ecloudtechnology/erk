<div align="center">

# 🦅 Erk

### Türkçe için sıfırdan geliştirilmiş yapay zekâ modeli

*Dünya modelleri Türkçe'yi yabancı bir dil gibi harf harf söker.*
**Erk, dilin kökünü ve eklerini bir bütün olarak anlar.**

<br>

[![TurkishMMLU](https://img.shields.io/badge/TurkishMMLU-%25_69.7_🥇-2ea043?style=for-the-badge)](#-değerlendirme--evaluation)
[![Parametre](https://img.shields.io/badge/Parametre-14B-2563eb?style=for-the-badge)](#)
[![Dil](https://img.shields.io/badge/Dil-Türkçe-e30a17?style=for-the-badge)](#)

**Açık Türkçe modeller arasında TurkishMMLU birincisi**

[Türkçe](#türkçe) · [English](#english) · [eCloud Tech.](https://www.e-cloud.web.tr)

</div>

---

## Türkçe

### Erk nedir?

**Erk**, [eCloud Yazılım Teknolojileri](https://www.e-cloud.web.tr) tarafından
geliştirilen, **14 milyar parametreli**, Türkçe'ye özel bir büyük dil modelidir.

Bugün Türkçe kullanan yapay zekâ modellerinin neredeyse tamamı İngilizce için tasarlandı
ve Türkçe onlara sonradan öğretildi. Bu yaklaşımın bedelini her Türkçe kullanıcı öder:
model, Türkçe'nin sondan eklemeli yapısını tanımaz, kelimeleri anlamsız parçalara böler,
daha yavaş ve daha pahalı çalışır.

Erk bu yaklaşımı tersine çevirir. **Türkçe-native bir tokenizer**, **Türkçe derlemde
ön-eğitim** ve **gerçek belgelerle beslenen talimat ayarı** ile Erk, Türkçe'yi bir
ikinci dil olarak değil, ana dili olarak öğrenir.

### 🏆 Değerlendirme — Evaluation

Erk, bağımsız ve kamuya açık **TurkishMMLU** kıyaslamasında (9 ders, 0-shot doğruluk)
test edilen açık Türkçe modellerin **en iyisidir.**

| Sıra | Model | Ölçek | TurkishMMLU |
|:--:|:---|:--:|:--:|
| 🥇 | **Erk** | **14B** | **%69,7** |
| 🥈 | Qwen3 | 14B | %63,4 |
| 🥉 | Trendyol Asure | 12B | %60,9 |
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

### Neden Erk verimli? — Tokenizer

Türkçe sondan eklemelidir: *"gözlüklerimizdekilerdenmiş"* gibi tek bir kelimeye onlarca
ek eklenebilir. İngilizce için tasarlanmış tokenizer'lar bu yapıyı tanımaz ve kelimeyi
harf yığınına böler. Erk'in Türkçe-native tokenizer'ı ise kökü ve ekleri tanır.

Bağımsız test derlemlerinde ölçülen sonuç:

| Model | Kelime başına token (Türkçe) | Göreli maliyet |
|:---|:---:|:---:|
| **Erk** | **1.51** | **1.00×** |
| GPT-4o | 2.26 | 1.50× |
| GPT-4 | 3.01 | **1.99×** |
| Kimi K2 | 3.07 | 2.03× |

> **GPT-4, aynı Türkçe metni Erk'in iki katı token'a böler.** Bu, aynı içerik için
> iki kat işlem maliyeti, iki kat daha yavaş üretim ve yarı yarıya daralan bağlam
> penceresi demektir. Erk'in tokenizer'ı, test edilen 14 tokenizer'ın (diğer Türkçe
> modeller dahil) tümünü Türkçe'de geçer.

### Erk'i ayıran üç ilke

**1. Kökünden Türkçe.** Türkçe'ye özel tokenizer ve Türkçe derlemde ön-eğitimle, dilin
kendi yapısını temelden anlayan bir dil sezgisi. Uyarlama değil.

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
| Tokenizer | Türkçe-native byte-level BPE (65.536 sözlük) |
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

📧 Ticari kullanım ve iş birliği: **info@e-cloud.web.tr**

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

Erk reverses this. With a **Turkish-native tokenizer**, **pretraining on a Turkish
corpus**, and **instruction tuning grounded in real documents**, Erk learns Turkish as a
first language — not a second.

### 🏆 Evaluation

On the independent, public **TurkishMMLU** benchmark (9 subjects, 0-shot accuracy),
Erk is **the best of the open Turkish models tested.**

| Rank | Model | Size | TurkishMMLU |
|:--:|:---|:--:|:--:|
| 🥇 | **Erk** | **14B** | **69.7%** |
| 🥈 | Qwen3 | 14B | 63.4% |
| 🥉 | Trendyol Asure | 12B | 60.9% |
| 4 | Turkish-Gemma | 9B | 60.4% |
| 5 | Trendyol v4 | 7B | 53.0% |
| 6 | Kumru | 2B | 20.1% |

Strongest subjects: **Geography 85% · Philosophy 85% · Religion & Ethics 83% ·
History 76%.** All results measured with `lm-evaluation-harness` on the public
TurkishMMLU test set, 0-shot, with every model evaluated under identical conditions.

### Why is Erk efficient?

Turkish is agglutinative — dozens of suffixes attach to a single root. English-centric
tokenizers over-split Turkish words; Erk's Turkish-native tokenizer recognizes roots and
suffixes.

| Model | Tokens per word (Turkish) | Relative cost |
|:---|:---:|:---:|
| **Erk** | **1.51** | **1.00×** |
| GPT-4o | 2.26 | 1.50× |
| GPT-4 | 3.01 | **1.99×** |
| Kimi K2 | 3.07 | 2.03× |

**GPT-4 splits the same Turkish text into twice as many tokens as Erk** — meaning 2×
the cost, 2× slower generation, and half the effective context. Erk's tokenizer
outperforms all 14 tokenizers tested (including other Turkish models) on Turkish.

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
| Tokenizer | Turkish-native byte-level BPE (65,536 vocab) |
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

📧 Commercial use & partnerships: **info@e-cloud.web.tr**

The full training recipe is open at
[nanosohbet](https://github.com/ecloudtechnology/nanosohbet).

---

<div align="center">

Bir **[eCloud Yazılım Teknolojileri](https://www.e-cloud.web.tr)** projesidir.
<br>
*Yerli zekâ, küresel ölçek.*

</div>
