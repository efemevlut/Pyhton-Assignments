age = input("Are you a cigarette addict older than 75 years old?(Yes/No) ").title().strip()
chronic = input("Do you have a severe chronic disease?(Yes/No)").title().strip()
immune = input("Is your immune system too weak?(Yes/No)").title().strip()
if age == "Yes" or chronic == "Yes" or immune == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")
