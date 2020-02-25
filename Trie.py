class Trie:
    head = {}

    def add(self, word):
        current = self.head
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['*'] = True

    def search(self, word):
        current = self.head
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if '*' in current:
            return True
        else:
            return False


dictionary = Trie()
dictionary.add("table")
dictionary.add("tab")
dictionary.add("tabulate")
print(dictionary.search("table"))
print(dictionary.search("tabs"))
