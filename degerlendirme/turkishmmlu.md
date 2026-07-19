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

## Notlar

- Erk'in en güçlü olduğu alanlar sözel/kültürel derinlik gerektiren derslerdir
  (coğrafya, felsefe, din ve ahlak, tarih).
- En zayıf alan matematiktir (%40); sayısal muhakeme gerektiren görevlerde çıktıların
  doğrulanması önerilir.
- Değerlendirme, modelin talimat ayarı (SFT) tamamlandıktan sonra yapılmıştır.
