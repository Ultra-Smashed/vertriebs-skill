# Modul Preis-Kalkulator

Ziel: Der Mensch kennt seinen Mindestpreis und verkauft nie wieder unter Wert.

## Fragen (in einer Nachricht, nur was fehlt)

1. Wie viel willst du im Jahr verdienen, vor Steuern, also was dir als Gehalt bleiben soll?
2. Wie hoch sind deine Betriebskosten im Monat (Software, Büro, Versicherungen, Auto, Weiterbildung)?
3. Wie viele Wochen Urlaub, Feiertage und Krankheit planst du im Jahr ein?
4. Wie viele Stunden pro Woche arbeitest du, und wie viele davon kannst du Kunden berechnen (meist 50–70 %)?
5. Rücklagen: Krankenversicherung und Altersvorsorge selbst zahlen? (Standard: ja, ~25 % Aufschlag auf das Wunschgehalt, wenn keine Zahl genannt wird. Als Annahme kennzeichnen.)

## Rechnen

`python3 scripts/preis.py --gehalt 60000 --kosten 800 --urlaub 6 --stunden 40 --abrechenbar 0.6 --vorsorge 0.25 --puffer 0.1`

Ohne Befehle: dieselbe Rechnung selbst mit Code. Formel:
- Arbeitswochen = 52 − Urlaub/Feiertage/Krankheit
- abrechenbare Stunden = Arbeitswochen × Stunden × Anteil abrechenbar
- Jahresbedarf = Gehalt × (1 + Vorsorge) + Kosten × 12
- Mindestsatz = Jahresbedarf / abrechenbare Stunden; Zielsatz = Mindestsatz × (1 + Puffer)

## Zeigen

- **Mindest-Stundensatz** (darunter verlierst du Geld) und **Zielsatz** (mit Puffer für Leerlauf und Gewinn)
- Tagessatz (× 8) und Monatsumsatz, der nötig ist
- Ein Projektbeispiel: „Ein Projekt mit 20 Stunden muss mindestens X € kosten.“
- Alle Annahmen als Liste, damit der Mensch sie ändern kann

## Projektpreis statt Stunden

Fragt der Mensch nach einem Projektpreis: Aufwand schätzen lassen (Stunden je Schritt), × Zielsatz, + 15–25 % Risikoaufschlag für Unbekanntes, auf eine glatte Zahl runden. Zusätzlich fragen, was das Ergebnis dem Kunden wert ist (mehr Umsatz, gesparte Zeit). Liegt der Wert weit über dem Aufwandspreis, auf wertbasierten Preis hinweisen.

Keine Steuerberatung: Einkommensteuer und Umsatzsteuer sind nicht im Mindestsatz (Preise sind netto). Darauf hinweisen.
