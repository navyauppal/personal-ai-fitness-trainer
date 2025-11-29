from utils import logger

class ControllerAgent:
    def __init__(self,session):
        self.session=session

    def create_plan(self):
        logger.info("ControllerAgent: Starting Plan Creation ")
        profile=self.session.get_session_profile()

        name=profile.get("Name")
        goal=profile.get("Goal")
        duration=profile.get("Duration")

        plan=f"Hello {name}!.Your goal is {goal}.\n"
        plan += f"You can workout {duration} minutes per day.\n"
        
        fitness_agent= FitnessAgent(self.session)
        logger.info("FitnessAgent: generating workout")
        workout=fitness_agent.generate_workout()

        plan+="\n Your Workout Plan:\n"
        plan+=workout

        nutrition_agent=NutritionAgent(self.session)
        
        logger.info("NutritionAgent: generating food plan")
        nutrition=nutrition_agent.generate_nutrition_plan()
        
        plan+="\n Your Nutrition Plan\n"
        plan+=nutrition

        weekly_agent=WeeklyRoutineAgent(self.session)
        logger.info("WeeklyRoutineAgent: generating weekly routine")
        weekly_routine=weekly_agent.generate_weekly_routine()

        plan+="\n"+ weekly_routine
        logger.info("Plan successfully generated!")


        return plan
    
class FitnessAgent:
    def __init__(self,session):
        self.session=session

    def generate_workout(self):
        profile=self.session.get_session_profile()
        goal=profile.get("Goal")
        duration=int(profile.get("Duration"))    

        if goal=="weight loss":
            exercises=["Jumping jacks", "Burpees", "Mountain climbers", "High knees"]
        if goal=="muscle gain":
            exercises=["Push-ups", "Squats", "Lunges", "Plank hold"]
        if goal=="general":
            exercises=["Squats", "Plank", "Jumping jacks", "Arm circles"]

        workout_plan=f"Workout for {duration} minutes: \n"
        for ex in exercises:
            workout_plan+=f"-{ex}\n"
        return workout_plan                

from tools import CalorieClaculator  

class NutritionAgent: 
    def __init__(self,session):
        self.session=session
        self.calorie_calculator=CalorieClaculator()   

    def generate_nutrition_plan(self):
        profile=self.session.get_session_profile()
        goal=profile.get("Goal")

        calories=self.calorie_calculator.calculate(goal)

        plan=f"Daily calories {calories} kcal\n"
        plan += "- Breakfast: Oats + fruit\n"
        plan += "- Lunch: Dal + rice + veggies\n"
        plan += "- Dinner: Paneer/Eggs + salad\n"

        return plan
    
class WeeklyRoutineAgent:
    # Create weekly routine using loop agent
    def __init__(self,session):
        self.session=session 

    def generate_weekly_routine(self,):
        profile=self.session.get_session_profile()
        goal=profile.get("Goal")

        if goal == "weight loss":
            exercises = ["Jumping jacks", "Burpees", "Mountain climbers", "High knees"]
        elif goal == "muscle gain":
            exercises = ["Push-ups", "Squats", "Lunges", "Plank"]
        else:
            exercises = ["Squats", "Plank", "Jumping jacks", "Arm circles"] 

        routine="Weekly Routine\n"    

        for day in range(1,8):
            if day==4 or day==7:
                  routine+=f"Day {day}: Rest Day\n"
            else:
                routine+=f"Day {day}:{exercises[(day-1)%len(exercises)]}\n"

        return routine                 