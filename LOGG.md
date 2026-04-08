# Fordypning_Databaser

Tirsdag-4.8.2026: I dag fikset jeg slik at jeg kunne logge inn på psql terminalen og lage databaser der, jeg gjorde det ved hjelp fra chatgpt og her er en oppsummering av hva jeg gjorde. 
- Problem: psql ble ikke gjenkjent i PowerShell
Løsning: Kjørte psql.exe direkte fra PostgreSQL‑installasjonsmappen.
- Problem: Innlogging med brukeren joachim1 feilet
Løsning: Opprettet brukeren manuelt i PostgreSQL.
- Problem: Feil: database "joachim1" does not exist
Løsning: Logget inn ved å spesifisere databasen postgres med -d postgres.
- Problem: joachim1 kunne ikke opprette databaser
Løsning: Identifiserte at brukeren manglet CREATEDB‑rettigheter (må bruke postgres‑brukeren eller gi rettigheten).
