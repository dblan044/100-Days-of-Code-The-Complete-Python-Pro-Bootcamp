def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    total_letters_true = 0
    total_letters_love = 0

    for letter in "true":
        count = lower_names.count(letter)
        total_letters_true += count

    for letter in "love":
        count = lower_names.count(letter)
        total_letters_love += count

    print(int(str(total_letters_true) + str(total_letters_love)))

calculate_love_score("Illidan Stormrage", "Tyranda Whisperwind")