from enum import Enum

class Scholarship_Status(Enum):
    INELIGABLE = 1
    ELIGABLE = 2
    DEAN_CONSIDERATION = 3

# Takes infromation about the student and determines if they are eligable to recieve the scholarship 
# @param age - age of the applicant, lived - the amount of time the applicant has lived in california
# @param worked - amount of time the applicant has worked in CA, volunteered - true if the applicant has completed volunteer work false otherwise
# @param household_income - the anual household income of the applicant, parents_lived - how long the applicants parents lived in california
# @return true - if the applicant is eligible for the scholarship, false - if the applciant is ineligible for the scholarship
def scholarship_eligibility(age, lived, worked, parents_lived, volunteered, household_income):
    # checks if the applicant meets the age requirment for the scholarship
    # @param age - age of the applicant 
    # @return
    def age_req(age):
        min_age_req = 18
        max_age_req = 24
        return (min_age_req <= age and age <= max_age_req)
    
    # checks if the applicant meets at least one of the california residency requirements for the scholarship
    # @param lived - the amount of time the applicant has lived in california, worked - the amount of time the applicant has worked in california 
    # @param parent_lived - how long the applicants parents lived in california, volunteered - true if the applicant has competed voluteer work false otherwise
    # @return true - if any of the eligibility requirment are met, false - if none of the requirements are met
    def ca_residency(lived, worked, parents_lived, volunteered):
        min_years_lived = 2
        min_months_worked = 6
        min_year_parents_lived = 1
        
        if (lived >= min_years_lived): return True
        elif (worked >= min_months_worked): return True
        elif (parents_lived >= min_year_parents_lived): return True
        elif (volunteered): return True
        return False

    # determines if the applicant is eligible for the dean consideration 
    # @param household_income - the applicants anual household income 
    # @return true - if the household income is less than 5000
    def dean_consideration(household_income):
        min_household_income = 5000
        return (household_income < min_household_income)
    
    if not age_req(age):
        return Scholarship_Eligibility.INELIGABLE
    
    if not CA_Residency(lived, worked, parents_lived, volunteered):
        if not dean_consideration(house_hold_income):
            return Scholarship_Eligability.DEAN_CONSIDERATION
        else:
            return Scholarship_Eligability.INELIGABLE
    return Scholarship_Eligability.ELIGABLE
            
