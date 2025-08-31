with open("C:/Users/sukit/OneDrive/Documents/test.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Word count:", len(words))
