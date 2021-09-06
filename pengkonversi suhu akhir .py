print()
print("--Pengkonversi Suhu--")
print("1. Celcius.")
print("2. Fahrenheit.")
print("3. Kelvin.")
print("4. Reamur.")
print()

pilihan = input("Silahkan pilih suhu yang akan dikonversi diatas: ")

if pilihan == "1":
    formatfah = " F"
    formatkel = " K"
    formatrea = " Re"
    nilaicel = int(input("Masukkan suhu dalam Celcius: "))
    nilaifah = (nilaicel * 9/5) + 32
    nilaikel = nilaicel + 273.15
    nilairea = nilaicel * 4/5

    print("Suhu dalam fahrenheit: " + str(nilaifah) + formatfah)
    print("Suhu dalam kelvin: " + str(nilaikel) + formatkel)
    print("Suhu dalam reamur: " + str(nilairea) + formatrea)

elif pilihan == "celcius":
    formatfah = " F"
    formatkel = " K"
    formatrea = " Re"
    nilaicel = int(input("Masukkan suhu dalam Celcius: "))
    nilaifah = (nilaicel * 9/5) + 32
    nilaikel = nilaicel + 273.15
    nilairea = nilaicel * 4/5

    print("Suhu dalam fahrenheit: " + str(nilaifah) + formatfah)
    print("Suhu dalam kelvin: " + str(nilaikel) + formatkel)
    print("Suhu dalam reamur: " + str(nilairea) + formatrea)

elif pilihan == "2":
    formatcel = " C"
    formatkel = " K"
    formatrea = " Re"
    nilaifah = int(input("Masukkan suhu dalam fahrenheit: "))
    nilaicel = (nilaifah - 32) * 5/9
    nilaikel = ((nilaifah + 459.67) * 5/9)
    nilairea = 4/9 * (nilaifah - 32)

    print("Suhu dalam celcius: " + str(nilaicel) + formatcel)
    print("Suhu dalam kelvin: " + str(nilaikel) + formatkel)
    print("Suhu dalam reamur: " + str(nilairea) + formatrea)

elif pilihan == "fahrenheit":
    formatcel = " C"
    formatkel = " K"
    formatrea = " Re"
    nilaifah = int(input("Masukkan suhu dalam fahrenheit: "))
    nilaicel = (nilaifah - 32) * 5/9
    nilaikel = ((nilaifah + 459.67) * 5/9)
    nilairea = 4/9 * (nilaifah - 32)

    print("Suhu dalam celcius: " + str(nilaicel) + formatcel)
    print("Suhu dalam kelvin: " + str(nilaikel) + formatkel)
    print("Suhu dalam reamur: " + str(nilairea) + formatrea)

elif pilihan == "3":
    formatcel = " C"
    formatfah = " F"
    formatrea = " Re"
    nilaikel = int(input("Masukkan suhu dalam kelvin: "))
    nilaicel = nilaikel - 273.15
    nilaifah = nilaikel * 9/5 - 459.67
    nilairea = (nilaikel - 273.15) * 0.80000

    print("Suhu dalam celcius: " + str(nilaicel) + formatcel)
    print("Suhu dalam fahrenheit: " + str(nilaifah) + formatfah)
    print("Suhu dalam reamur: " + str(nilairea) + formatrea)

elif pilihan == "kelvin":
    formatcel = " C"
    formatfah = " F"
    formatrea = " Re"
    nilaikel = int(input("Masukkan suhu dalam kelvin: "))
    nilaicel = nilaikel - 273.15
    nilaifah = nilaikel * 9/5 - 459.67
    nilairea = (nilaikel - 273.15) * 0.80000

    print("Suhu dalam celcius: " + str(nilaicel) + formatcel)
    print("Suhu dalam fahrenheit: " + str(nilaifah) + formatfah)
    print("Suhu dalam reamur: " + str(nilairea) + formatrea)

elif pilihan == "4":
    formatcel = " C"
    formatfah = " F"
    formatkel = " K"
    nilairea = int(input("Masukkan suhu dalam reamur: "))
    nilaicel = nilairea * 5/4
    nilaifah = (nilairea * 9/4) + 32
    nilaikel = (nilairea * 5/4) + 273.15

    print("Suhu dalam celcius: " + str(nilaicel) + formatcel)
    print("Suhu dalam fahrenheit: " + str(nilaifah) + formatfah)
    print("Suhu dalam kelvin: " + str(nilaikel) + formatkel)

elif pilihan == "reamur":
    formatcel = " C"
    formatfah = " F"
    formatkel = " K"
    nilairea = int(input("Masukkan suhu dalam reamur: "))
    nilaicel = nilairea * 5/4
    nilaifah = (nilairea * 9/4) + 32
    nilaikel = (nilairea * 5/4) + 273.15

    print("Suhu dalam celcius: " + str(nilaicel) + formatcel)
    print("Suhu dalam fahrenheit: " + str(nilaifah) + formatfah)
    print("Suhu dalam kelvin: " + str(nilaikel) + formatkel)

else:
    print("maaf yang kamu masukkan salah")
    print("ulangi lagi dari awal")