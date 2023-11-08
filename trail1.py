name = input("Wpisz swoje imie: ")
print("Witaj, " + name + "!")
age = input(name+", "+"wpisz swoj wiek: ")
if int(age) >= 18:
    search = input("Co chcesz wyszukać? ")
    import webbrowser
    webbrowser.open('https://www.google.com/search?q='+search)
else:
    print("Jesteś za młody by korzystać z wyszukiwarki")