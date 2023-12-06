## matériel de référence #2 par .casca 

class Translate:
    def __init__(self):
        self.mapping = {i: {} for i in range(1, 5)}
        
    def add_syllables(self, syllables, translation):
        self.mapping[len(syllables.split())][syllables] = translation
        
    def get_syllables(self, syllables):
        return self.mapping[len(syllables.split())][syllables]
    
    def _extract_syllables(self, text):
        if len(text.split()) == 1:
            return text.strip()
        
        for i in range(4, 0, -1):
            for j in range(len(text.split()) - 1):
                span = ' '.join(text.split()[j:j + i])
                if span in self.mapping[i] and text.index(span) == 0:
                    return span
    
    def get_chains(self, text):
        chains = []
        
        while text:
            chain = self._extract_syllables(text)
            
            if chain:
                text = text.replace(chain, '', 1).strip()
                chains.append(chain)
            
        return chains
    
    def translate_chains(self, chains):
        new = []
        
        for chain in chains:
            new.append(self.get_syllables(chain))
            
        return ' '.join(new)
    
    def translate(self, text):
        chains = self.get_chains(text)
        
        return self.translate_chains(chains)
            
translator = Translate()
translator.add_syllables('ga', 'cu')
translator.add_syllables('li', 'ry')
translator.add_syllables('ka', 'ca')
translator.add_syllables('lu', 'lo')
translator.add_syllables('lu li', 'lo rie')