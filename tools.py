class CalorieClaculator:
    # Tool: Calorie calculator

    def calculate(self,goal):
        if goal=="weight loss":
            return 1800
        elif goal=="muscle gain":
            return 2300
        else:
            return 2000