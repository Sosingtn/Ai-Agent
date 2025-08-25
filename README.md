Ai-Agent ist ein kleines, modular aufgebautes Python-Projekt, das die Grundlagen eines „tool-fähigen“ KI-Agents demonstriert. Der Agent nimmt natürliche Sprachaufgaben entgegen und löst sie, indem er bei Bedarf definierte Funktionen aufruft (z. B. einen Taschenrechner), Ergebnisse interpretiert und die Antwort zurückgibt. Damit eignet sich das Repo als Lern- und Startpunkt, um eigene Agenten mit Funktionsaufrufen, Prompts und Tests zu bauen. 
GitHub

Was der Agent kann

Aufgaben annehmen und in strukturierte „Aufrufe“ übersetzen (z. B. Rechnen, einfache Utility-Funktionen).

Passende Tools/Funktionen selektieren, ausführen und das Resultat in eine verständliche Antwort einbetten.

Konfiguration und Prompts getrennt verwalten, damit sich Verhalten und „Persönlichkeit“ des Agents leicht anpassen lassen.

Über ein Hauptskript ausführbar; grundlegende Tests sind enthalten. 
GitHub

Architektur auf einen Blick

Hauptlauf: main.py – Startpunkt, der Eingaben verarbeitet und den Agent-Flow koordiniert.

Funktionsaufrufe: call_function.py – Brücke zwischen natürlicher Aufgabe und konkreter Python-Funktion (z. B. Rechenoperationen).

Tools/Module: Ordner calculator und functions – kapseln die tatsächlich ausführbaren Fähigkeiten des Agents.

Prompting: prompts.py – enthält System-/Rollen-Prompts und Formatvorgaben für den Funktionsaufruf.

Konfiguration: config.py – zentrale Settings (z. B. Schlüssel, Flags, Laufzeitoptionen).

Qualität: tests.py – Basis-Tests für Kernpfade.

Verpackung: pyproject.toml und uv.lock – Projekt- und Abhängigkeitsmanagement. 
GitHub

Typische Use-Cases

Rechenaufgaben oder strukturierte Mini-Workflows über den Calculator.

Beispiel für „Function-Calling“: vom Prompt zur gezielten Python-Funktion.

Ausgangsbasis, um weitere Tools (Datei-I/O, Web-APIs, Datenbankabfragen) einzuhängen und den Agent zu erweitern.

Für wen ist es gedacht?

Entwickler:innen, die schnell verstehen möchten, wie agentische Muster (Auswahl von Tools, kontrollierte Ausführung, Prompt-Trennung) praktisch aussehen.

Einsteiger:innen, die ein überschaubares, testbares Beispiel suchen, um eigene Agent-Features hinzuzufügen.
