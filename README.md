# Nexus

Een kleine Flask-oefening met een formulier waarmee je een plaatsnaam verstuurt.

## Flask starten

Open een terminal in de hoofdmap van je project en voer deze opdrachten uit:

```bash
cd Nexus
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Als de server gestart is, open je deze URL in je browser:

```text
http://127.0.0.1:5000
```

Stop de server met `Ctrl+C` in de terminal. De virtuele omgeving sluit je daarna af met:

```bash
deactivate
```

## Hoe het werkt

- `app.py` start de Flask-app en bevat de routes.
- De route `/` toont `templates/index.html`.
- Het formulier in `templates/index.html` gebruikt `GET` en verstuurt de plaatsnaam naar `/weather`.
- Flask leest de plaatsnaam met `request.args.get("city")` en geeft die door aan de template.
- `static/style.css` verzorgt de opmaak van het dashboard.
- `requirements.txt` bevat de Python-pakketten die het project nodig heeft.

De zoekopdracht toont nu een bevestigingsbericht. De app haalt nog geen echte weersgegevens op.
