a = int (input("Enter marks :"))

if a>=90 :
  print("A+")
elif 80<=a<=89:
  if a%5 == 0:
    print("A(with bonus)")
  else:
    print("A")
elif 60<=a<=79:
  if a%2 == 0:
    print("B")
  else:
    print("C")
else:
  print("Fail !")