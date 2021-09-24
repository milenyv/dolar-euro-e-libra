real = float(input("Quanto você tem na carteira? R$"))
dolar = real / 5.34
euro = real / 6.26
libra = real / 7.31
print("Com R${:.2f} reais, você pode comprar US${:.2f} dolares, EUR${:.2f} euros e £${:.2f} libras".format(real, dolar, euro, libra))
