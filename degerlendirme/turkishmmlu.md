# Erk — TurkishMMLU Değerlendirmesi

Bu belge, Erk'in TurkishMMLU üzerindeki değerlendirme sonuçlarını, metodolojisini ve
karşılaştırma verilerini tam ve şeffaf biçimde sunar.

## Genel sonuç

| Sıra | Model | Ölçek | TurkishMMLU (ort.) |
|:--:|:---|:--:|:--:|
| 1 | **Erk** | 14B | **%69,7** |
| 2 | Qwen3 | 14B | %63,4 |
| 3 | Trendyol Asure | 12B | %60,9 |
| 4 | Turkish-Gemma (YTÜ) | 9B | %60,4 |
| 5 | Trendyol v4 | 7B | %53,0 |
| 6 | Kumru (VNGRS) | 2B | %20,1 |

**Erk, test edilen açık Türkçe modellerin en iyisidir.**

## Erk — ders bazında doğruluk

| Ders | Doğruluk |
|:---|:--:|
| Coğrafya | %85 |
| Felsefe | %85 |
| Din ve Ahlak | %83 |
| Tarih | %76 |
| Biyoloji | %71 |
| Türk Dili ve Edebiyatı | %64 |
| Fizik | %62 |
| Kimya | %61 |
| Matematik | %40 |
| **Ortalama** | **%69,7** |

## Metodoloji

- **Kıyaslama:** TurkishMMLU (9 ders, çoktan seçmeli)
- **Koşul:** 0-shot (örnek verilmeden)
- **Araç:** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- **Metrik:** `acc` (doğruluk)
- **Adillik:** Karşılaştırılan tüm modeller birebir aynı koşullar, aynı araç ve aynı
  test setiyle değerlendirilmiştir. Sonuçlar seçilerek değil, tümüyle raporlanmıştır.

## Ek ölçüm: kirlilik dışı, şık döndürmeli protokol (Eylül 2026)

Yukarıdaki %69,7, TurkishMMLU'nun tamamında, lm-evaluation-harness ile 0-shot,
şık sırası döndürülmeden ölçülmüştür. Erk-32B çalışmasında geliştirdiğimiz daha
sıkı protokolle aynı model yeniden ölçüldü:

- Test kümesinin 900 sorusundan **113'ü (%12,6)** devam-eğitimi külliyatında
  birebir geçiyor ([liste](https://huggingface.co/datasets/ecloudtech/TurkishMMLU-Kirlilik));
  bunlar ve eğitim sırasında izlenen 150 soru dışarıda bırakıldı → **temiz 652**.
- Her soru şık sırası döndürülerek ölçüldü (harf/konum yanlılığı elenir).
- Fark, 10.000 yeniden örneklemeli eşli bootstrap %95 güven aralığıyla verildi.

| Model | Temiz 652, döndürülmüş |
|---|---|
| Qwen3-14B (taban) | %60,58 |
| **Erk-14B** | **%67,18** |
| Fark | **+6,60 [+3,07, +10,28]** |

İki sayı çelişmez: %69,7 ile %67,18 aynı modelin iki farklı koşulda ölçümüdür;
fark protokolden gelir. Tabana göre kazanç her iki koşulda da anlamlıdır
(+6,3 tam küme, +6,6 temiz küme). Yukarıdaki sıralama tablosu tam-küme
protokolüne aittir; karşılaştırılan diğer modeller temiz protokolle yeniden
ölçülmemiştir.

Protokolün tamamı ve yeniden üretim betikleri:
[Erk-32B — Ölçüm Protokolü](https://huggingface.co/ecloudtech/Erk-32B).

### English

The 69.7% above was measured on the full TurkishMMLU test set with
lm-evaluation-harness, 0-shot, without option rotation. Under the stricter
protocol developed for Erk-32B — 113/900 questions found verbatim in the
pretraining corpus excluded (plus 150 used for monitoring), remaining 652
measured with option rotation, paired bootstrap CIs — Erk-14B scores
**67.18%** vs **60.58%** for Qwen3-14B (+6.60 [+3.07, +10.28]). The two numbers
are the same model under two protocols; the gain over the base is significant
under both. The ranking table above is on the full-set protocol; other models
were not re-measured under the clean one. Full protocol and scripts:
[Erk-32B](https://huggingface.co/ecloudtech/Erk-32B).

## Notlar

- Erk'in en güçlü olduğu alanlar sözel/kültürel derinlik gerektiren derslerdir
  (coğrafya, felsefe, din ve ahlak, tarih).
- En zayıf alan matematiktir (%40); sayısal muhakeme gerektiren görevlerde çıktıların
  doğrulanması önerilir.
- Değerlendirme, modelin talimat ayarı (SFT) tamamlandıktan sonra yapılmıştır.
