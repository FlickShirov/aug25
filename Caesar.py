massive = []
alphabet = 'аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхЧцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ' * 2

def launch():
    if input('Введите желаемое действие (Расшифровать/Зашифровать): ') == 'Расшифровать':
        text = input()
        operation_text(text, decrypt)
    else:
        text = input()
        operation_text(text, encrypt)
def encrypt(letter):
    return letter-4
def decrypt(letter):
    return letter+4

def operation_text(text, operation):
    for i in range(len(text)):
        if text[i] in alphabet:
            letter = alphabet.find(text[i])
            massive.append(alphabet[operation(letter)])
        else:
            massive.append(text[i])
    print(''.join(massive))


launch()


