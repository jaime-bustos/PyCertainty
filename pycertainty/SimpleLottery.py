class SimpleLottery():

    name = ""
    outcomes = []
    probabilities = []


    def __init__(self, name: str, outcomes: list, probabilities: list):
        self.name = name

        if len(outcomes) == len(probabilities):
            
            if (sum(probabilities) == 1):

                self.outcomes = outcomes
                self.weights = probabilities

            else:
                raise ValueError("Probabilities must sum to 1.")


        else:
            raise ValueError("Outcomes and weights must be balanced.")
        

    def __str__(self):
        return f"LotteryObject(name: {self.name}, outcomes: {self.outcomes}, probabilities: {self.weights})"
    
    def setOutcomes(self, outcomes: list):

        if len(outcomes) == len(probabilities):
            self.outcomes = outcomes
        else:
           
            raise ValueError("Outcomes and weights must be balanced.")
        
    def setName(self, name: str):
        self.name = name


probabilities = [1/3,1/3,1/3]
outcomes = ["Paris", "London", "Tokyo"]



P = SimpleLottery("P", outcomes, probabilities)

print(P)

P.setOutcomes(["NYC", "Washington", "California"])
P.setName("Q")

print(P)



