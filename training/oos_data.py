"""Hand-written out-of-scope (OTHER) messages. Used so the classifier can say 'this is not a support ticket'
instead of forcing every input into one of the 11 support categories."""
import random

OOS_CORE = [
 "what is the weather like today", "write me a poem about cats", "who won the cricket match last night",
 "how do I bake sourdough bread", "tell me a joke", "what is the capital of france", "recommend a good movie to watch",
 "explain how photosynthesis works", "can you help me with my python homework", "what is the price of bitcoin",
 "translate good morning into spanish", "how far is the moon from earth", "suggest a name for my puppy",
 "what time does the football game start", "how do I lose weight fast", "give me a recipe for chicken biryani",
 "which phone is better iphone or android", "who is the prime minister of india", "tell me about the history of rome",
 "how do I fix my wifi router", "what are good places to visit in goa", "what is machine learning",
 "can you write a cover letter for me", "how many calories are in a banana", "what is the meaning of life",
 "recommend a good biryani place near me", "how do I learn to play guitar", "is it going to rain tomorrow",
 "solve this equation 2x + 3 = 11", "what is the best way to invest in stocks", "tell me a bedtime story",
 "who painted the mona lisa", "how do airplanes fly", "I am feeling bored", "what should I cook for dinner",
 "sing me a song", "what is the score of the match", "how do I meditate", "what is the speed of light",
 "help me plan a birthday party", "asdfgh jkl", "hello", "hi there how are you", "good morning",
 "can you play some music", "what year did world war two end", "is pluto a planet",
]
PREFIX = ["", "", "hey, ", "hi, ", "quick question: ", "pls tell me ", "hello, ", "just curious, "]
SUFFIX = ["", "", "?", " please", " thanks", "!!", " lol"]


def build_oos(n: int, seed: int = 42, cores=None):
    rng = random.Random(seed)
    cores = cores or OOS_CORE
    return [rng.choice(PREFIX) + rng.choice(cores) + rng.choice(SUFFIX) for _ in range(n)]


def split_oos_cores(seed: int = 42):
    """Hold out WHOLE out-of-scope sentences for validation/test so the OTHER score is not inflated by leakage."""
    rng = random.Random(seed)
    cores = OOS_CORE[:]
    rng.shuffle(cores)
    a, b = int(len(cores) * 0.70), int(len(cores) * 0.85)
    return {"train": cores[:a], "val": cores[a:b], "test": cores[b:]}
