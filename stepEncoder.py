alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

encoded_shift = ""


def step_encoder(text)


array_text = text.split(" ")
shift = array_text[-1]
print(shift)
ar_shift = []
for i in shift:
    ar_shift += i
print(ar_shift)

for f in ar_shift:
    index_for_alph = int(f) - 1
    encoded_shift += alphabet[index_for_alph]
print(encoded_shift)
