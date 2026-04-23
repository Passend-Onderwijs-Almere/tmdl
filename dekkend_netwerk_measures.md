# Dekkend Netwerk — Measures

| Measure | Syntax | Beschrijving |
|---|---|---|
| `avg_cosy` | `AVERAGE('almeerse_matrix_v1 0'[cosy_rating])` | Gemiddelde cosy-rating uit de Almeerse matrix |
| `avg_cota` | `AVERAGE('almeerse_matrix_v1 0'[cota_rating])` | Gemiddelde cota-rating uit de Almeerse matrix |
| `avg_fymo` | `AVERAGE('almeerse_matrix_v1 0'[fymo_rating])` | Gemiddelde fymo-rating uit de Almeerse matrix |
| `avg_leco` | `AVERAGE('almeerse_matrix_v1 0'[leco_rating])` | Gemiddelde leco-rating uit de Almeerse matrix |
| `avg_soge` | `AVERAGE('almeerse_matrix_v1 0'[soge_rating])` | Gemiddelde soge-rating uit de Almeerse matrix |
| `avg_weta` | `AVERAGE('almeerse_matrix_v1 0'[weta_rating])` | Gemiddelde weta-rating uit de Almeerse matrix |
| `jaarbedrag_oorspronkelijk` | `CALCULATE(SUMX(dekkend_netwerk_stacked, [dekkend_netwerk_tarieven.tarief] * [aantal]))` | Totaal jaarbedrag op basis van het oorspronkelijke tarief (t1) × aantal plaatsen |
| `jaarbedrag_aug_dec` | `[jaarbedrag_oorspronkelijk] * 5/12` | Deel van het jaarbedrag (t1) voor augustus t/m december (5 maanden) |
| `jaarbedrag_jan_jul` | `[jaarbedrag_oorspronkelijk] * 7/12` | Deel van het jaarbedrag (t1) voor januari t/m juli (7 maanden) |
| `jaarbedrag_t2` | `CALCULATE(SUMX(dekkend_netwerk_stacked, [dekkend_netwerk_tarieven.t2] * [aantal]))` | Totaal jaarbedrag op basis van het geïndexeerde tarief (t2) × aantal plaatsen |
| `jaarbedrag_t2_aug_dec` | `[jaarbedrag_t2] * 5/12` | Deel van het t2-jaarbedrag voor augustus t/m december (5 maanden) |
| `jaarbedrag_t2_jan_jul` | `[jaarbedrag_t2] * 7/12` | Deel van het t2-jaarbedrag voor januari t/m juli (7 maanden) |
| `indexering_t2` | `VAR t1 = [jaarbedrag_oorspronkelijk]` `VAR t2 = [jaarbedrag_t2]` `RETURN DIVIDE(t2, t1)` | Indexeringsfactor: verhouding tussen t2- en t1-jaarbedrag (bijv. 1,03 = 3% stijging) |
| `jan_jul_verschil_t1_t2` | `VAR t1 = [jaarbedrag_jan_jul]` `VAR t2 = [jaarbedrag_t2_jan_jul]` `RETURN t2 - t1` | Verschil in kosten jan–jul tussen t2 en t1 (meerkosten door indexering) |
| `sum_plaatsen` | `SUM(dekkend_netwerk_stacked[aantal])` | Totaal aantal plaatsen in het dekkend netwerk |
