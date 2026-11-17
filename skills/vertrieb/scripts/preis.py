#!/usr/bin/env python3
"""Mindest- und Zielstundensatz für Selbstständige.

Beispiel:
  python3 preis.py --gehalt 60000 --kosten 800 --urlaub 6 --stunden 40 --abrechenbar 0.6
"""
import argparse
import json

p = argparse.ArgumentParser()
p.add_argument("--gehalt", type=float, required=True, help="Wunschgehalt pro Jahr vor Steuern")
p.add_argument("--kosten", type=float, default=0, help="Betriebskosten pro Monat")
p.add_argument("--urlaub", type=float, default=6, help="Wochen ohne Arbeit pro Jahr (Urlaub, Feiertage, Krankheit)")
p.add_argument("--stunden", type=float, default=40, help="Arbeitsstunden pro Woche")
p.add_argument("--abrechenbar", type=float, default=0.6, help="Anteil abrechenbarer Stunden (0–1)")
p.add_argument("--vorsorge", type=float, default=0.25, help="Aufschlag für Kranken- und Altersvorsorge auf das Gehalt")
p.add_argument("--puffer", type=float, default=0.1, help="Puffer für Leerlauf und Gewinn")
p.add_argument("--projektstunden", type=float, default=20)
a = p.parse_args()

wochen = 52 - a.urlaub
stunden = wochen * a.stunden * a.abrechenbar
bedarf = a.gehalt * (1 + a.vorsorge) + a.kosten * 12
mindest = bedarf / stunden
ziel = mindest * (1 + a.puffer)
print(json.dumps({
    "arbeitswochen": round(wochen, 1),
    "abrechenbare_stunden_pro_jahr": round(stunden),
    "jahresbedarf_netto": round(bedarf, 2),
    "mindest_stundensatz": round(mindest, 2),
    "ziel_stundensatz": round(ziel, 2),
    "ziel_tagessatz_8h": round(ziel * 8, 2),
    "noetiger_monatsumsatz": round(bedarf * (1 + a.puffer) / 12, 2),
    "projekt_beispiel": {"stunden": a.projektstunden, "mindestpreis": round(mindest * a.projektstunden, 2),
                          "zielpreis": round(ziel * a.projektstunden, 2)},
    "annahmen": vars(a),
}, ensure_ascii=False, indent=2))
