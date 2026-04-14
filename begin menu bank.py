banksaldo=0
transactions=[]
while True:
    print("Welkom bij SparenVoorIedereen!")
    print("Je banksaldo is: ", banksaldo)
    print("Wat wil je doen?")
    print("1. Geld storten")
    print("2. Geld opnemen")
    print("3. Transactie geschiedenis bekijken")
    print("4. Afsluiten")

    keuze = input("Maak een keuze: ")
    
    if keuze == "1":
        bedrag = float(input("Hoeveel geld wil je storten? "))
        banksaldo += bedrag
        transactions.append(f"Gestort: +{bedrag}")
        print(f"Je hebt {bedrag} gestort. Je nieuwe banksaldo is {banksaldo}.")
        
    elif keuze == "2":
        bedrag = float(input("Hoeveel geld wil je opnemen? "))
        if bedrag > banksaldo:
            print("Onvoldoende saldo.")
        else:
            banksaldo -= bedrag
            transactions.append(f"Opgenomen: -{bedrag}")
            print(f"Je hebt {bedrag} opgenomen. Je nieuwe banksaldo is {banksaldo}.")
            
    elif keuze == "3":
        print("\n--- Transactie Geschiedenis ---")
        if len(transactions) == 0:
            print("Nog geen transacties.")
        else:
            for transaction in transactions:
                print(transaction)
        print()
        

    elif keuze == "4":
        print("Bedankt voor het gebruiken van de SparenVoorIedereen. Tot ziens!")
        break
        
    else:
        print("Ongeldige keuze, probeer het opnieuw.")