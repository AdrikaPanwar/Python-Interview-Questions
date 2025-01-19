'''AutoCompleteSystem - trie search and insert '''

# Python3 program to demonstrate auto-complete
# feature using Trie data structure.
# Note: This is a basic implementation of Trie
# and not the most optimized one.


# 1st way

class TrieNode():
	def __init__(self):
		# Initialising one node for trie
		self.children = {}
		self.last = False


class Trie():
	def __init__(self):

		# Initialising the trie structure.
		self.root = TrieNode()

	def formTrie(self, keys):

		# Forms a trie structure with the given set of strings
		# if it does not exists already else it merges the key
		# into it by extending the structure as required
		for key in keys:
			self.insert(key) # inserting one key to the trie.

	def insert(self, key):

		# Inserts a key into trie if it does not exist already.
		# And if the key is a prefix of the trie node, just
		# marks it as leaf node.
		node = self.root

		for a in key:
			if not node.children.get(a):
				node.children[a] = TrieNode()

			node = node.children[a]

		node.last = True

	def suggestionsRec(self, node, word):

		# Method to recursively traverse the trie
		# and return a whole word.
		if node.last:
			print(word)

		for a, n in node.children.items():
			self.suggestionsRec(n, word + a)

	def printAutoSuggestions(self, key):

		# Returns all the words in the trie whose common
		# prefix is the given key thus listing out all
		# the suggestions for autocomplete.
		node = self.root

		for a in key:
			# no string in the Trie has this prefix
			if not node.children.get(a):
				return 0
			node = node.children[a]

		# If prefix is present as a word, but
		# there is no subtree below the last
		# matching node.
		if not node.children:
			return -1

		self.suggestionsRec(node, key)
		return 1


# Driver Code
keys = ["hello", "dog", "hell", "cat", "a",
		"hel", "help", "helps", "helping"] # keys to form the trie structure.
key = "h" # key for autocomplete suggestions.

# creating trie object
t = Trie()

# creating the trie structure with the
# given set of strings.
t.formTrie(keys)

# autocompleting the given key using
# our trie structure.
comp = t.printAutoSuggestions(key)

if comp == -1:
	print("No other strings found with this prefix\n")
elif comp == 0:
	print("No string found with this prefix\n")








# 2nd way

from collections import defaultdict

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.history = defaultdict(int)  # Dictionary to store sentence frequencies
        self.current_input = ""          # To store the current user input
        for i, sentence in enumerate(sentences):
            self.history[sentence] += times[i]  # Initialize the historical sentences

    def input(self, c):
        if c == '#':  # If the user ends the input
            self.history[self.current_input] += 1  # Save the current sentence to history
            self.current_input = ""  # Reset the current input
            return []  # Return empty list
        else:
            self.current_input += c  # Append the character to the current input
            prefix = self.current_input
            # Filter and sort sentences based on prefix and frequency
            results = sorted(
                (sentence for sentence in self.history if sentence.startswith(prefix)),
                key=lambda x: (-self.history[x], x)
            )
            return results[:3]  # Return the top 3 results

# Example usage
if __name__ == "__main__":
    sentences = ["i love you", "island", "ironman", "i love geeksforgeeks"]
    times = [5, 3, 2, 2]

    obj = AutoCompleteSystem(sentences, times)

    # Simulating the input process
    inputs = ['i', ' ', 'a', '#', 'i']
    for c in inputs:
        suggestions = obj.input(c)
        print(f"Typed : \"{c}\" , Suggestions:")
        for suggestion in suggestions:
            print(suggestion)
 
        
        
        
     
# 3rd way     
        
import heapq
from collections import defaultdict

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.trie = {}
        self.history = defaultdict(int)
        self.prefix = ""
        
        # Populate the trie with sentences and their corresponding times
        for i, sentence in enumerate(sentences):
            self.add_to_trie(sentence, times[i])

    def add_to_trie(self, sentence, time):
        node = self.trie
        for char in sentence:
            if char not in node:
                node[char] = {}
            node = node[char]
        # Store the frequency of the sentence at the end of the sentence
        if 'end' not in node:
            node['end'] = []
        node['end'].append((sentence, time))

    def input(self, c):
        if c == '#':
            # Save the current prefix as a new sentence and reset the prefix
            self.history[self.prefix] += 1
            self.prefix = ""
            return []

        # Update the current prefix
        self.prefix += c
        node = self.trie

        # Traverse the trie to find all possible completions with the current prefix
        for char in self.prefix:
            if char not in node:
                return []
            node = node[char]

        # Gather the possible completions
        if 'end' in node:
            sentences = node['end']
        else:
            sentences = []

        # Sort the sentences by frequency (descending), and then by lexicographical order (ascending)
        sentences.sort(key=lambda x: (-x[1], x[0]))

        # Return the top 3 sentences
        return [sentence for sentence, _ in sentences[:3]]






# Trie Data Structure:- 

class TrieNode:

    def __init__(self):
      
        # Array for child nodes of each node
        self.child = [None] * 26
        
        # for end of word
        self.word_end = False

# Method to insert a key into the Trie
def insert_key(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:

            # If node for current character does 
            # not exist then make a new node
            new_node = TrieNode()

            # Keep the reference for the newly
            # created node
            curr.child[index] = new_node

        # Move the curr pointer to the
        # newly created node
        curr = curr.child[index]

    # Mark the end of the word
    curr.word_end = True

# Method to search a key in the Trie
def search_key(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False

        # Move the curr pointer to the 
        # already existing node for the 
        # current character
        curr = curr.child[index]

    # Return true if the word exists 
    # and is marked as ending
    return curr.word_end

# Create an example Trie
root = TrieNode()
arr = ["and", "ant", "do", "geek", "dad", "ball"]
for s in arr:
    insert_key(root, s)

# One by one search strings
search_keys = ["do", "gee", "bat"]
for s in search_keys:
    print(f"Key : {s}")
    if search_key(root, s):
        print("Present")
    else:
        print("Not Present")