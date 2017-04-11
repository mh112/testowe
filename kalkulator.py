def get_help():
	print("To jest prosty program kalkulatora. WprowadŸ dwie liczby i zatwierdŸ.")

def dodawanie(a, b):
  wynik = a + b
  return wynik
 
get_help()
zm1 = int(input("Podaj pierwsz¹ liczbê"))
zm2 = int(input("Podaj druga liczbê"))
print (dodawanie(zm1, zm2))
