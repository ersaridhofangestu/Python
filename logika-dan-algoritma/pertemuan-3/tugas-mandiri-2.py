kelereng_aldi = 1

while True :
    kelereng_budi = kelereng_aldi - 15
    kelereng_anto = 2 * (kelereng_aldi + kelereng_budi)
    kelereng_agung = (kelereng_aldi + kelereng_budi + kelereng_anto) - 5

    if kelereng_aldi > 0 and kelereng_budi > 0 and kelereng_anto > 0 and kelereng_agung > 0 :
        print("Jumlah kelereng aldi adalah {}\nJumlah kelereng budi adalah {}\nJumlah kelereng anto adalah {}\nJumlah kelereng agung adalah {}".format(kelereng_aldi,kelereng_budi,kelereng_anto,kelereng_agung))
        break
    kelereng_aldi += 1