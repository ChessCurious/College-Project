import random

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why don’t programmers like nature? Too many bugs.",
    "Why did the computer go to the doctor? Because it caught a virus.",
    "Why was the JavaScript developer sad? Because he didn’t know how to ‘null’ his feelings."
]

def get_random_joke():
    return random.choice(jokes)

if __name__ == "__main__":
    print("😂 Here's a random joke for you:")
    print(get_random_joke())
