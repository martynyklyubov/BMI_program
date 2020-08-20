def bmi(weight, height): ## formula to evaluate the Body Mass
    if height < 1.0 or height > 2.5 or \  
    weight < 20 or weight > 200: ## checking if the value is trustworthy.
        return None ## if value is not trustworthy return None
    
    return weight / height ** 2

print(bmi(352.5, 1.65))