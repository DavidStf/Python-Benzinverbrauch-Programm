

Antw=False
Nicht_Erkenntbar =0


while Antw == False:
  user_eingabeL= float(input('Bitte geben Sie ein wie viel Liter haben Sie getankt:  '))
  user_eingabeK= float(input('Wie viel Km sind Sie gefahren: '))
  if user_eingabeK !=Nicht_Erkenntbar:
    Rechnung= user_eingabeL/user_eingabeK *100*12
    print(round(Rechnung,2),'liter','Pro 100km im Jahr')
    Antw= True
  elif user_eingabeL != Nicht_Erkenntbar:
    Rechnung= user_eingabeL/user_eingabeK *100*12
    print(round(Rechnung,2),'liter' ,'Pro 100km im Jahr')
  else:
    print('Falsche eingabe !')

Rechnung= user_eingabeL/user_eingabeK *100*12


