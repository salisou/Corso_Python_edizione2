import pandas as pd
import requests

# 1. Chiediamo all'utente quale città vuole cercare
citta_da_cercare = input("Inserisci il nome della città che vuoi cercare: ")

# 2. Configuriamo l'endpoint di geocoding di Open-Meteo
url_geocoding = "https://geocoding-api.open-meteo.com/v1/search"
parametri = {
    "name": citta_da_cercare,
    "count": "10",  # Mostra fino a un massimo di 10 risultati
    "language": "it",  # Nome dei paesi in italiano
}

# 3. Facciamo la richiesta
risposta = requests.get(url_geocoding, params=parametri)
dati = risposta.json()

# 4. Verifichiamo se l'API ha trovato qualcosa
if "results" in dati:
    # Trasformiamo la lista dei risultati in un DataFrame Pandas per vederla chiaramente
    df_citta = pd.DataFrame(dati["results"])

    # Selezioniamo solo le colonne più utili da mostrare a schermo
    colonne_utili = [
        "name",
        "country",
        "admin1",
        "latitude",
        "longitude",
        "timezone",
    ]
    # Gestiamo il caso in cui alcune colonne opzionali (es. la regione 'admin1') siano assenti
    colonne_presenti = [col for col in colonne_utili if col in df_citta.columns]

    df_pulito = df_citta[colonne_presenti]

    # Rinominiamo le colonne per renderle leggibili in italiano
    rinomina = {
        "name": "Città",
        "country": "Nazione",
        "admin1": "Regione/Stato",
        "latitude": "Latitudine",
        "longitude": "Longitudine",
        "timezone": "Fuso Orario",
    }
    df_pulito = df_pulito.rename(columns=rinomina)

    print(f"\nEcco i risultati trovati per '{citta_da_cercare}':")
    print(df_pulito.to_string())

else:
    print(f"\nNessun risultato trovato per '{citta_da_cercare}'. Controlla l'ortografia!")