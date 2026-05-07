| Domein                | Naam measure                         | Eenheid            | Bron                                      | Formule |
|----------------------|--------------------------------------|--------------------|-------------------------------------------|---------|
| Algemeen             | TimeStamp                            | Datum              | Power BI systeemdatum                     | Toont de huidige datum (NOW), geformatteerd als dag-maand-jaar. |
| Grensverkeer         | uniek_aantal_bekostigde_ll_povo      | Aantal (uniek)     | duok_bekostigde_leerlingen_po_vo          | Telt het aantal unieke BSN-nummers van bekostigde leerlingen in po en vo. |
| Grensverkeer         | aantal_grens_inkomend                | Aantal             | duok_totaal_aantal_sbo_so_vso              | Som van het aantal leerlingen dat ondersteuningsbekostiging ontvangt vanuit een ander samenwerkingsverband. |
| Grensverkeer         | aantal_grens_uitgaand_distinct       | Aantal (uniek)     | duok_bekostigde_leerlingen_po_vo          | Telt het aantal unieke BSN-nummers van bekostigde leerlingen waarvan het vestigingsnummer niet gelijk is aan PO2401 of VO2401. |
``