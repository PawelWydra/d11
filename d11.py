envelope_small = (10, 15)
envelope_medium = (20, 30)
envelope_big = (30, 30)

prepare_gifts = {("Parfum", 12, 30),
                 ("Socks", 10, 10),
                 ("Book", 30, 25),
                 ("Clock", 15, 15),
                 ("Wallet", 5, 10)}

for gift in prepare_gifts:
    if gift[1] <= envelope_small[0] and gift[2] <= envelope_small[1]:
        print(f"for {gift[0]} best choice is small envelope.")
    elif gift[1] <= envelope_medium[0] and gift[2] <= envelope_medium[1]:
        print(f"for {gift[0]} best choice is medium envelope.")
    else:
        print(f"for {gift[0]} best choice is big envelope.")