
# Question:
# Kullanıcı tarafından girilecek bir kelimenin tersten okunuşu ile düz okunuşunun aynı olup
# olmadığını kontrol eden ve okunuşları aynı ise ekrana True değilse False çıktısı veren bir program
# yazmak

# Approach:
# This question can be solved by determining whether the text entered by the user is a
# Palindrome or not


def is_palindrome():
    txt = input("Please enter a text: ")
    txt = txt.lower()   # python is 'case sensitive'
    txt_copy = []
    for ch in txt:
        if ch == ' ':   # remove space character in text
            continue
        txt_copy.append(ch)
    reversed_txt = ''.join(reversed(txt_copy))  # the reversed method returns the string passed to it in a reversed form
    reversed_txt = list(reversed_txt)

    if txt_copy != reversed_txt:  # tests to see if the content of both variables are the same or not
        print("False")
    else:
        print("True")


# This is a driver program to test this  program.
if __name__ == "__main__":
    is_palindrome()