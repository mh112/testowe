def get_help():
	print("To jest prosty program kalkulatora. Wprowad� dwie liczby i zatwierd�.")

def dodawanie(a, b):
  wynik = a + b
  return wynik
 
get_help()
zm1 = int(input("Podaj pierwsz� liczb�"))
zm2 = int(input("Podaj druga liczb�"))
print (dodawanie(zm1, zm2))
