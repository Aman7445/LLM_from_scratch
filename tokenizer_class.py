import re

class SimpleTokenizer:
    def __init__(self,vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    
    def encode(self,text):
        preprocessed = re.split(r'([,.;?\'()_!":]|--|\s)',raw_text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        all_words = set(sorted(preprocessed))
        ids = [self.str_to_int[s] for s in all_words]
        return ids
    
    def decode(self,ids):
        text= " ".join(self.int_to_str[i] for i in ids)
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text 


raw_text= "Hello, world. Is this-- a test?"
preprocessed = re.split(r'([,.;?\'()_!":]|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# print(preprocessed[:30])

all_words = set(sorted(preprocessed))

vocab = {token:integer for integer, token in enumerate(all_words)}


tokenizer = SimpleTokenizer(vocab)

text = """"It's the last he painted, you know," 
        Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)

print(ids)

text=tokenizer.decode(ids)

print(text)

        


