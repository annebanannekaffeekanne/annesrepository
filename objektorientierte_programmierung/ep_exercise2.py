#import pip
#import pylint
import pytest

def vowels(text: str) -> int:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in text:
        if i in vowels:
            count += 1
    return count


text = "Hallo"
print("Anzahl der Vokale:", vowels(text))

if __name__ == '__ep_exercise2__':
    pytest.ep_exercise2()