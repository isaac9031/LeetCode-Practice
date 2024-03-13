def fizzbuzz(maximum):
   lista = []
   if maximum == 0:
       return lista
   if maximum !=0:
        for number in range(1,maximum+1):
            if number%3 == 0 and number%5 ==0:
                lista.append("fizzbuzz")
            elif number%3 == 0:
               lista.append("fizz")
            elif number%5 == 0:
                lista.append("buzz")
            else:
                lista.append(str(number))
        return lista

print(fizzbuzz(16))
