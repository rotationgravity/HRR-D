# HRR-D Spiralstackning – Rödskiftssimulering

Detta är en Python-baserad simulering av ackumulerat rödskift i HRR-D-modellen (Harmonisk Roterande Rumtids-Dynamik).

## Vad det gör

- Simulerar ljusets färd genom ett spiralformat rum
- Beräknar det totala rödskiftet från flera spiralvarv
- Jämför med observerat z från t.ex. extremt avlägsna kvasarer
- Visualiserar hur z byggs upp varv för varv

## Användning

```bash
python spiralstackning_simulering.py
```

## Parametrar

- `omega_0`: Initial spiralrotation
- `r_c`: Dämpningsradie för rotation
- `num_varv`: Antal spiralvarv som simuleras
