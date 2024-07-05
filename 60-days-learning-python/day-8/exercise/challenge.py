total_flips = 0
heads_count = 0

while True:

    coin_flip = input("Enter head or tail: ").strip().lower()

    with open('heads.txt', 'a') as file:
        if coin_flip == 'head' or coin_flip == 'tail':
            total_flips += 1
            if coin_flip == 'head':
                heads_count += 1

            if total_flips > 0:
                percentage_heads = (heads_count / total_flips) * 100
            else:
                percentage_heads = 0.00

            file.write(f"{coin_flip} + {percentage_heads}\n")
            print(f"{percentage_heads}" + "%")
