

def elect_next_budget_item(votes, balances, costs):
    
    # computes the number of votes for each item
    number_of_votes = {item: sum(1 for voter in votes if item in voter)
                       for item in costs}
    
    # computes the value should be added to each voter for each item to buy it
    value_to_add = {item: cost / number_of_votes[item] if number_of_votes[item] > 0 else float('inf')
                    for item, cost in costs.items()}
    
    # find the item with the lowest value to add for each voter
    lowest_item, lowest_budget_per_voter = min(value_to_add.items(), key=lambda x: x[1])
    print(f"After adding {lowest_budget_per_voter:.2f} to each voter, \"{lowest_item}\" is chosen.")

    # add virtual money to each voter
    for i, voters in enumerate(votes):
        balances[i] += lowest_budget_per_voter
        if lowest_item in voters:
            balances[i] -= lowest_budget_per_voter
            
    # print the remaining balance for each voter
    for i, balance in enumerate(balances):
        print(f"Citizen {i + 1} has {balance:.2f} remaining balance.")

    
    

# Example of using the modified algorithm
if __name__ == "__main__":
    # Define votes, balances, and costs
    votes = []
    for i in range(51):
        votes.append(["A", "B", "C", "D", "E"])
        
    for i in range(49):
        votes.append(["V", "W", "X", "Y", "Z"])
        
    balances = [0.0] * 100  # Set initial budget to 0 for each citizen
    costs = {"A": 100, "B": 100, "C": 100, "D": 100, "E": 100, "V": 100, "W": 100, "X": 100, "Y": 100, "Z": 100}

    # Call the function
    elect_next_budget_item(votes, balances, costs)

    