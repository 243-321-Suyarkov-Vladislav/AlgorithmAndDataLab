def reverse_words(s):
    words = s.split()

    def helper(i):
        if i == len(words):          # базовый случай
            return []
        return helper(i + 1) + [words[i]]  # сначала обрабатываем конец

    return " ".join(helper(0))

text = input("Введите строку: ")
print(reverse_words(text))