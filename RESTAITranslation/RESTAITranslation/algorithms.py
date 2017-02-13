class Algorithms(object):
    
    def __init__(self):
        self.name = "Algorithm Example"

    def translate(self, algorithmName, algorithmId, text):          
        if algorithmName == "LSTM":
            return text + " translated by LSTM Server"
        elif algorithmName == "BBC":
            return text + " translated by BBC Server"
        else:
            return text + " translated by " + algorithmName + " Special Server"