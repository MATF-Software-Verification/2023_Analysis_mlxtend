import os
from mlxtend.text import tokenizer_words_and_emoticons, tokenizer_emoticons


def save_results_tokenizer(test_name, text, result, expected_result, iteration):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open(f"log/{test_name}_results.log", "a") as f:
        f.write(f"Test: {test_name}, Iteration: {iteration}\n")
        f.write(f"Input text:\n{text}\n")
        f.write(f"Tokenizer result:\n{result}\n")
        f.write(f"Expected result:\n{expected_result}\n")
        f.write("-" * 50 + "\n")


def test_tokenizer_words_and_emoticons():
    text = 'In the land of Mordor :) where the shadows lie :-D, a ring was forged :-P <html>You cannot pass!</html>'
    expected_result = ['in', 'the', 'land', 'of', 'mordor', 'where', 'the', 'shadows', 'lie', 'a', 'ring', 'was', 'forged', 'you', 'cannot', 'pass', ':)', ':-D', ':-P']

    result = tokenizer_words_and_emoticons(text)
    save_results_tokenizer("test_tokenizer_words_and_emoticons", text, result, expected_result, 0)
    
    assert result == expected_result, "Rezultat funkcije tokenizer_words_and_emoticons nije ispravan!"


def test_tokenizer_emoticons():
    text = 'In the land of Mordor :) where the shadows lie :-D, a ring was forged :-P <html>You cannot pass!</html>'
    expected_result = [':)', ':-D', ':-P']

    result = tokenizer_emoticons(text)
    save_results_tokenizer("test_tokenizer_emoticons", text, result, expected_result, 0)
    
    assert result == expected_result, "Rezultat funkcije tokenizer_emoticons nije ispravan!"
