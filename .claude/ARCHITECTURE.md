# ISG Platform — Sistem Mimarisi

Version: 1.4 (Post F2-002 isg_risk)
Updated: 24 Ağustos 2026

Modül Bağımlılıkları
- isg_core (root)
- isg_legislation (mevzuat)
- isg_compliance (uygunluk)
- isg_penalty (ceza)
- isg_simulator (simülasyon)
- isg_risk (risk değerlendirmesi)
- isg_capa (kök neden / aksiyon)

Veri Akışı
1. Workplace profili
2. Yükümlülük listele (isg_legislation)
3. Uygunluk değerlendir (isg_compliance)
4. Risk değerlendir (isg_risk → kontrol → CAPA)
5. Ceza hesapla (isg_penalty)
6. Simülasyon yap (isg_simulator)

ACL: readonly / expert / manager

Parity: %90.6 (29/32 modül)

Sırada: isg_osgb, F5-001, F1-002 (bloklu)
