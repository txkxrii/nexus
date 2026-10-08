# Reflectie: mijn voortgang met Flask

Deze reflectie is gebaseerd op de stappen die ik tot nu toe in dit project heb gezet.

## Wat ik al goed heb gedaan

- Ik heb een duidelijk idee voor mijn Weather Dashboard en weet welke onderdelen het moet hebben: een titel, een invoerveld voor een plaats en een zoekknop.
- Ik heb de projectbestanden leren verdelen over `app.py`, `templates/`, `static/` en `requirements.txt`.
- Ik weet dat Flask standaard de map `templates` gebruikt voor HTML en `static` voor CSS.
- Ik heb gekozen voor een GET-formulier en begrijp dat de plaatsnaam dan in de URL meegaat, bijvoorbeeld `/weather?city=Amsterdam`.
- Ik heb zelf benoemd wat ik met de oefening wil leren: formulierdata ontvangen in Flask en gegevens aan een template doorgeven.
- Ik heb gemerkt dat de ontwikkelomgeving soms verwarrend kan zijn als er nog een tab openstaat van een oude bestandslocatie.

## Waar ik tegenaan liep

- De oude map `template` en de nieuwe map `templates` stonden door elkaar in mijn IDE-tabs. Daardoor was het niet meteen duidelijk welk `index.html` bij de Flask-app hoorde.
- Ik dacht dat `style.css` leeg was, terwijl het bestand op schijf wel inhoud had. Dat wijst erop dat ik moet controleren of de editor de actuele versie van het juiste bestand toont.
- Ik had nog geen vaste, opgeschreven stappen om de virtuele omgeving te activeren en de Flask-app te starten.

## Wat ik hiervan meeneem

- Bij twijfel controleer ik eerst het volledige bestandspad en open ik het bestand opnieuw vanuit de projectboom.
- Voor Flask gebruik ik `templates/` en `static/` als mapnamen.
- Ik kan de app lokaal starten vanuit de projectmap met `source .venv/bin/activate` en `python app.py`. De volledige stappen staan in `README.md`.

## Volgende leerstap

De app ontvangt nu een plaatsnaam en toont een bevestigingsbericht. Een logische volgende stap is om te leren hoe een Flask-route de invoer controleert en daarna echte weersgegevens ophaalt van een weer-API.
