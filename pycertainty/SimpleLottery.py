import pandas as pd

class SimpleLottery():

    name = str()
    outcomes = list()
    lottery = pd.DataFrame()

    def __init__(self, name: str, outcomes: list, probabilities: list):
        
        self.name = name

        # Check if outcomes and probabilities are correctly set (balanced)
        if len(outcomes) == len(probabilities):
            
            if (sum(probabilities) == 1):

                self.outcomes = outcomes
                self.weights = probabilities

                temp_columns = self.outcomes
                temp_columns.insert(0, self.name)
                self.lottery = pd.DataFrame(index=temp_columns, columns=temp_columns)



            else:
                raise ValueError("Probabilities must sum to 1.")


        else:
            raise ValueError("Outcomes and weights must be balanced.")
        

    """
    Print statement overloader
    """
    def __str__(self):
        return f"LotteryObject(name: {self.name}, outcomes: {self.outcomes}, probabilities: {self.weights})"
    
    def __setOutcomes(self, outcomes: list):
        self.outcomes = outcomes
        
    def __setProbabilities(self, probabilities: list):
        self.probabilities = probabilities

        
    def setName(self, name: str):
        self.name = name

    def addOutcome(self, new_outcome, new_probability):

        # set the temporary outcomes to add later
        temp = self.outcomes
        temp.append(new_outcome)

        # call probability balancer
        new_probabilities = self.p_balancer(self.weights, new_probability) # returns a new probability list that is balanced


        self.__setOutcomes(temp)
        self.__setProbabilities(new_probabilities)

    def p_balancer(self, probabilities, new_probability):
        
        temp = probabilities

        """
        old = [1/3,1/3,1/3]

        new = [1/3, 1/3, 1/,3, 1/2]


        """

        remaining = 1 - new_probability # 1/2 left

        remaining /= len(temp)
        
        for i in range(len(temp)):
            temp[i] = remaining

        temp.append(new_probability)

        return temp

    def displayLottery(self):

        print(self.lottery)

probabilities1 = [1/3,1/3,1/3]
outcomes1 = ["Paris", "London", "Tokyo"]


probabilities2 = [1/2,1/4,1/4]
outcomes2 = ["Paris", "Seoul", "Rome"]

P = SimpleLottery("P", outcomes1, probabilities1)
Q = SimpleLottery("Q", outcomes2, probabilities2)

print(P)

P.addOutcome("Test", 0.9)

P.displayLottery()





