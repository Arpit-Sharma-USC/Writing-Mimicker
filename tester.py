
# load ascii text and covert to lowercase
filename = "input.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()
print raw_text
# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print "Total Characters: ", n_chars
print "Total Vocab: ", n_vocab
# prepare the dataset of input to output pairs encoded as integers
seq_length = 00
dataX_test = []
data_test = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX_test.append([char_to_int[char] for char in seq_in])
	data_test.append(char_to_int[seq_out])
n_patterns = len(data_test)
print data_test