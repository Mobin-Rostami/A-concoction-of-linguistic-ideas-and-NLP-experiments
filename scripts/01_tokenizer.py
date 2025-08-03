import re #re stands for regular expression. It rules out all the punctuation marks.

def tokenize(text):
    return re.findall(r'\b\w+\b', text)
  """ findall finds all the parts of the text given that match the folllowing pattern
  within the parenthesis) 
  """
  """ \b is for word boundary, \w+ means one or more word characters including letters, numbers, 
  and underscores). So, basically, it asks the computer to identify all the words surrounded by
  boundaries)"""


if __name__ == "__main__": 
  """the above code is also something I have recently learned about. It is 
  usually referred to as being 'The main guard' and it prevents interferring with your code
  if you happen to import this program into another program"""
    sample = "This is a sample sentence!"
    tokens = tokenize(sample)
    print(tokens)
