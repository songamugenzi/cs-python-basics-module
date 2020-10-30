"""
Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []

Notes:

Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.

[execution time limit] 4 seconds (py3)

[input] array.string chords

[output] array.string
"""

def csMakeItJazzy(chords):
    new_chord_list = []
    for c in chords:
        if c[-1] != "7":
            new_chord_list.append(f"{c}7")
        else:
            new_chord_list.append(c)
    # different method using List Comprehension
    # new_chord = [f"{c}{7}" for c in chords if c[-1] != 7 else c for c in chords]
    return new_chord_list

print(csMakeItJazzy(["G", "F", "C"]))
print(csMakeItJazzy(["Dm", "G", "E", "A"]))
print(csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(csMakeItJazzy([]))
print(csMakeItJazzy(["E", "C", "F", "A", "B"]))