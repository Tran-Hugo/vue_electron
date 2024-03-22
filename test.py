import time

# Boucle pendant 5 minutes
start_time = time.time()
while time.time() - start_time < 1 * 30:
    # Votre code ici
    print("Bonjour")

# Après 5 minutes, le script s'arrête
print("Le script s'est arrêté")
