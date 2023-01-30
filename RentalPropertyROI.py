class ROICalculator():

    def cashFlow(self):
        income = int(input("What is your total monthly rental property income? "))
        expenses = int(input("What are your total monthly expenses? "))
        total_cash = income - expenses
        return total_cash
    
    def investment(self):
        down_payment = int(input("What is your down payment? "))
        closing_costs = int(input("What are your closing costs? "))
        rehab_budget = int(input("What is your total rehab budget? "))
        misc = int(input("Enter any other miscellaneous investment costs "))

        total = down_payment + closing_costs + rehab_budget + misc

        return total
    
    def main(self):
       annual_cash = self.cashFlow() * 12
       total_investment = self.investment()

       roi = annual_cash / total_investment

       print("Your ROI on your rental property is", "{:.2%}".format(roi))


def calculateROI():
    newCalculator = ROICalculator()

    newCalculator.main()

calculateROI()