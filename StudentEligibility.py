
def scholarship_eligibility(age, lived, worked, parents_lived, volunteered, household_income):
    def age_req(age):
        min_age_req = 18
        max_age_req = 24
        return (min_age_req <= age and age <= max_age_req)

    def CA_Residency(lived, worked, parents_lived, volunteered):
        min_years_lived = 2
        min_months_worked = 6
        min_year_parents_lived = 1
        
        if (lived >= min_years_lived): return True
        elif (worked >= min_months_worked): return True
        elif (parents_lived >= min_year_parents_lived): return True
        elif (volunteered): return True
        return False

    def Dean_Consideration(household_income):
        min_household_income = 5000
        return (household_income < min_household_income)
    
    return (age_req(age) and (CA_Residency(lived, worked, parents_lived, volunteered) or Dean_Consideration(household_income)))