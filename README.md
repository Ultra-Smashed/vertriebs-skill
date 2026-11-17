# Vertriebs-Skill

Ein Skill für Claude. Der Vertriebs-Skill nimmt dir die Akquise ab: Er recherchiert Kunden vor dem Erstgespräch, macht aus Notizen ein Angebot mit drei Paketen, rechnet deinen Mindestpreis aus, fasst nach, ohne zu nerven, und schreibt Kaltakquise-Nachrichten. Der Einwand-Trainer spielt deinen schwierigsten Kunden und zeigt dir danach, wo du eingeknickt bist. Kostenlos, MIT-Lizenz.

| Modul | Was es macht |
| --- | --- |
| **Gesprächsvorbereitung** | Firmensteckbrief aus Website, Stellenanzeigen, News und Bewertungen, dazu die richtigen Fragen fürs Erstgespräch. |
| **Angebot** | Aus Gesprächsnotizen oder Sprachmemo wird ein Angebot mit drei Paketen, Ausgangslage in den Worten des Kunden und klarem nächsten Schritt. |
| **Preis-Kalkulator** | Aus Wunschgehalt, Kosten, Urlaub und Auslastung wird dein Mindest- und Zielstundensatz. Ein kleines Skript rechnet, nicht Claude im Kopf. |
| **Nachfassen** | Drei Nachrichten an Tag 3, 7 und 14, jede mit einem eigenen Anlass statt „wollte nur mal nachhaken“. |
| **Einwand-Trainer** | Claude spielt den Kunden: „zu teuer“, „ich muss noch überlegen“. Danach bekommst du eine Note, die Stelle, an der du eingeknickt bist, und bessere Antworten. |
| **Kaltakquise** | Für jede Firma auf deiner Liste ein echter Aufhänger und eine kurze Nachricht. Mit Hinweis, wo E-Mail-Werbung in Deutschland Grenzen hat. |

## Installation

### Claude-App (Web, Desktop)

Am schnellsten: den Link in einen neuen Chat einfügen und Claude bitten, den Skill zu installieren:

```
https://github.com/Ultra-Smashed/vertriebs-skill

Installier diesen Skill für mich.
```

Oder von Hand:

1. [`vertrieb.zip`](https://github.com/Ultra-Smashed/vertriebs-skill/raw/main/vertrieb.zip) herunterladen (nicht entpacken).
2. In Claude unter **Settings → Capabilities** den Schalter **Code execution and file creation** einschalten. In der neueren Ansicht heißt er **Create and edit files**.
3. **Customize → Skills** öffnen, auf **+** klicken, dann **Create skill → Upload a skill** und die ZIP-Datei wählen.

Als Plugin: **Customize → Plugins**, bei den persönlichen Plugins auf **+**, dann **Add from a repository** und `Ultra-Smashed/vertriebs-skill` eintragen.

Die Menünamen stehen hier so, wie Anthropic sie in der Hilfe nennt. In der deutschen Oberfläche können sie übersetzt sein.

### Claude Code

Als Plugin:

```
/plugin marketplace add Ultra-Smashed/vertriebs-skill
/plugin install vertrieb@vertrieb
```

Oder den Ordner kopieren:

```bash
git clone https://github.com/Ultra-Smashed/vertriebs-skill.git
cp -r vertriebs-skill/skills/vertrieb ~/.claude/skills/
```

## Benutzen

Einfach schreiben, was du brauchst, zum Beispiel:

> Ich habe morgen ein Erstgespräch mit der Firma Holzbau Meier. Bereite mich vor.

> Hier sind meine Notizen vom Gespräch. Mach daraus ein Angebot mit drei Paketen.

> Spiel meinen schwierigsten Kunden. Ich verkaufe ein Website-Paket für 4.900 Euro.

Der Skill erfindet keine Referenzen, Zahlen oder Kundenstimmen. Fehlt ein Beweis, lässt er eine markierte Lücke. Die füllst du mit etwas Echtem.

## Dateien

```
skills/vertrieb/SKILL.md            Ablauf, Module, Regeln
skills/vertrieb/modes/               eine Anleitung pro Modul
skills/vertrieb/scripts/             Hilfsskripte (Python 3, ohne Zusatzpakete)
vertrieb.zip                       derselbe Skill-Ordner als ZIP für die Claude-App
.claude-plugin/                     plugin.json, marketplace.json
```

Nach einer Änderung im Skill-Ordner die ZIP neu bauen: `cd skills && zip -r ../vertrieb.zip vertrieb`.

Anleitung: [thanisch.co/wissen/guides/vertriebs-skill-claude](https://thanisch.co/wissen/guides/vertriebs-skill-claude)

MIT-Lizenz, siehe [LICENSE](LICENSE). Von [Christopher Thanisch](https://thanisch.co).
