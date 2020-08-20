def bmi(weight, height): ## formula to evaluate the Body Mass
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200: ## checking if the value is trustworthy.
        return None ## if value is not trustworthy return None
    
    return weight / height ** 2 ## convert imperial units to metric ones.
def ftintom(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

