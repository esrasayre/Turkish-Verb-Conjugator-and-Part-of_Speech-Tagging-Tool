#         OOP VERB CONJUGATOR AND PART OF SPEECH TAGGING TOOL IN TURKISH
from encodings import utf_8
encoding = utf_8


class Word:
    def __init__(self, root, pos):
        self.root = root
        self.pos = pos

class Verb(Word):
    def conjugate(self, subject, tense):
        # apply phonetic rules to the verb's root to generate the correct conjugation
        conjugated_form = apply_phonetic_rules(self.root, subject, tense)
        return conjugated_form

class PhoneticRules:
    def apply_rules(self, root, subject, tense):
        # apply the appropriate phonetic rules to the root to generate the correct conjugation
        conjugated_form = root
        return conjugated_form

    def apply_vowel_harmony(self, root, subject_pronoun):
        last_vowel = root[-1]
        subject_vowel = subject_pronoun[-1]
        if last_vowel == "a" and subject_vowel == "i":
            root = root[:-1] + "i"
        elif last_vowel == "e" and subject_vowel == "i":
            root = root[:-1] + "i"
        elif last_vowel == "a" and subject_vowel == "u":
            root = root[:-1] + "u"
        elif last_vowel == "e" and subject_vowel == "u":
            root = root[:-1] + "u"
        return root

    def apply_consonant_mutation(self, root, tense):
        last_consonant = root[-1]
        if tense == "past" and last_consonant == "m":
            root = root[:-1] + "t"
        return root

    def add_suffix(self, root, tense):
        if tense == "present_continuous":
            root += "iyor"
        elif tense == "past":
            root += "ti"
        return root

phonetic_rules = PhoneticRules()

# Example usage:
root = "gitmek"
subject_pronoun = "ben"
tense = "present_continuous"

# Apply vowel

# Example usage:
phonetic_rules = PhoneticRules()
verb = Verb("gitmek", "verb")

# Get user input for the subject and tense
subject = input("Enter the subject: ")
tense = input("Enter the tense: ")

conjugated_form = verb.conjugate(subject, tense)
print(conjugated_form)
