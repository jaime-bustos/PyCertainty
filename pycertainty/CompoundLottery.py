import pandas as pd

class CompoundLottery():

    name = str()
    outcomes = list()
    lottery = pd.DataFrame()

    def __init__(self, name: str, outcomes: list, probabilities: list, layers: int):

        self.name = name

        # Check if outcomes and probabilities are correctly set (balanced)
        if len(outcomes) == len(probabilities):
            
            if (sum(probabilities) == 1):

                self.outcomes = outcomes
                self.weights = probabilities
                self.layers = layers

                temp_columns = self.outcomes
                temp_columns.insert(0, self.name)
                self.lottery = pd.DataFrame(index=temp_columns, columns=temp_columns)



            else:
                raise ValueError("Probabilities must sum to 1.")


        else:
            raise ValueError("Outcomes and weights must be balanced.")

    