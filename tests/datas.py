# * This evaluation dictionary has been generated by ChatGPT, the prompt was:
# *Request: "I am working on a Mastermind project, and I need to create a varied dataset
# *to test the evaluation function that compares a secret combination with a guessed combination.
# *The function should return a tuple with two values:
# *1. The number of colors in the correct position (good position).
# *2. The number of colors of the correct color but in the wrong position (wrong position).

# *I have a list of possible colors: COLORS = ["R", "V", "B", "J", "N", "M", "O", "G"].
# *I need you to generate a large dataset with various secret and guessed combinations,
# *and for each pair of combinations, provide the expected evaluation as a tuple (good_position, wrong_position).

# *The format for the generated data should be as follows:

# *[
# *    (secret_combination, guess_combination, (good_position, wrong_position)),
# *    ...
# *]
# *
evaluation_test = [
    ("RVBJ", "RVBJ", (4, 0)),
    ("RVBJ", "JBVR", (0, 4)),
    ("RVBJ", "RBJO", (1, 2)),
    ("GONM", "MNOG", (0, 4)),
    ("RRBB", "RBRB", (2, 2)),
    ("VBJN", "BJVO", (0, 3)),
    ("MOGR", "RGOM", (0, 4)),
    ("JNMO", "JNOM", (2, 2)),
    ("RVBJ", "RRRR", (1, 0)),
    ("VBJN", "VVVV", (1, 0)),
    ("GONM", "GGGG", (1, 0)),
    ("BJNM", "JBMN", (0, 4)),
    ("RVBJ", "BJMO", (0, 2)),
    ("RVBB", "BRVB", (1, 3)),
    ("VGBJ", "VGBJ", (4, 0)),
    ("VGBJ", "JBVG", (0, 4)),
    ("GGGG", "GGGG", (4, 0)),
    ("RRRR", "RRRR", (4, 0)),
    ("RRGG", "GGRR", (0, 4)),
    ("RVBG", "GRVB", (0, 4)),
    ("RVBJ", "RVBR", (3, 0)),
    ("RVBJ", "RVJB", (2, 2)),
    ("RRGB", "RGRB", (2, 2)),
    ("RRGB", "BRRG", (1, 3)),
    ("GGBB", "BGBG", (2, 2)),
    ("VNVN", "NVNV", (0, 4)),
    ("RBRB", "BRBR", (0, 4)),
    ("RGVB", "BRGV", (0, 4)),
    ("RBJG", "RBJG", (4, 0)),
    ("RBJG", "RBGJ", (2, 2)),
    ("NNMM", "MNMN", (2, 2)),
    ("OMGO", "OGOM", (1, 3)),
    ("GVBR", "RGVB", (0, 4)),
    ("RNVG", "RVNG", (2, 2)),
    ("GBRJ", "GRJB", (1, 3)),
    ("VGBR", "BGRV", (1, 3)),
    ("BRNV", "BVRN", (1, 3)),
    ("RVOJ", "RVJO", (2, 2)),
    ("OBRJ", "ORJB", (1, 3)),
    ("NGBR", "BRNG", (0, 4)),
    ("RGOV", "RGVO", (2, 2)),
    ("MJGV", "MJGV", (4, 0)),
    ("MJVG", "MJGV", (2, 2)),
    ("NRGV", "NRVG", (2, 2)),
    ("OBGV", "OVGB", (2, 2)),
    ("GBRV", "GVRB", (2, 2)),
    ("RJGV", "RJGV", (4, 0)),
    ("RVBG", "RVBJ", (3, 0)),
    ("BRGV", "BRVG", (2, 2)),
    ("NRBV", "NVBR", (2, 2)),
]
