# Importing langdetect library
from langdetect import detect

# Function to detect the language of a sentence
def detect_language(text):
    return detect(text)

# The Sentence
text = input("Enter sentence in any language:")

# Dictionary of some famous Languages and their respective codes
codes={
    'ar': 'Arabic', 'et': 'Estonian', 'art': 'Artificial Language',
    'sq': 'Albanian', 'bn': 'Bengali', 'bh': 'Bhojpuri',
    'bg': 'Bulgarian', 'cai': 'Central American Indian Language',
    'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'eg': 'Egyptian', 'en': 'English',
    'fr': 'French', 'gon': 'Gondi', 'el': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
    'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'ks': 'Kashmiri', 'ka': 'Georgian', 'ko': 'Korean', 'la': 'Latin',
    'mr': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'nl': 'Dutch',
    'te': 'Telugu', 'ta': 'Tamil', 'cy': 'Welsh'}

print("The language of the text is:", codes[detect_language(text)])