import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer

class WordInfo(object):
  def __init__(self, text):
    _text = nltk.word_tokenize(text)
    self._tagged_text = nltk.pos_tag(_text, tagset='universal')

  def __repr__(self):
    return '<WordInfo>'

  def get_tagged_text(self):
    return self._tagged_text

# convert to wordnet pos
def get_wordnet_pos(tag):
  if tag.startswith('J'):
    return wordnet.ADJ
  elif tag.startswith('V'):
    return wordnet.VERB
  elif tag.startswith('N'):
    return wordnet.NOUN
  elif tag.startswith('R'):
    return wordnet.ADV
  else:
    return wordnet.NOUN

# convert universal pos to pos from class lectures
def get_custom_pos(tag):
  tag_map = {
    'ADJ': 'Adjective',
    'ADP': 'Preposition',
    'ADV': 'Adverb',
    'CONJ': 'Conjunction',
    'DET': 'Determiner',
    'NOUN': 'Noun',
    'NUM': 'Noun',
    'PRT': 'Preposition',
    'PRON': 'Pronoun',
    'VERB': 'Verb',
    '.': 'Noun',
    'X': 'Noun'
  }
  return tag_map[tag]

# convert universal pos to oed pos
def get_oed_pos(tag):
  tag_map = {
    'ADJ': 'adj.',
    'ADP': 'prep.',
    'ADV': 'adv.',
    'CONJ': 'conj.',
    'DET': 'pron.',
    'NOUN': 'n.',
    'NUM': 'n.',
    'PRT': 'prep.',
    'PRON': 'pron.',
    'VERB': 'v.',
    '.': 'n.',
    'X': 'n.'
  }
  return tag_map[tag]