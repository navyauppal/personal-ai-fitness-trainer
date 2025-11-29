# Personal AI Fitness Trainer (Google Agent Capstone)

## Overview
This project is an intelligent multi-agent system that generates a personalized fitness plan using agents and tools.

### Features:
- Multi-Agent Architecture
- Loop Agent for weekly schedule
- Custom calorie calculation tool
- Session Memory
- Logging + Observability
- Nutrition + Workout Suggestions

---

## Agents Used

1. **Controller Agent**
   - Coordinates other agents and composes the final plan.

2. **Fitness Agent**
   - Generates daily exercises based on fitness goal.

3. **Nutrition Agent**
   - Uses a calorie calculation tool.
   - Outputs daily nutrition plan.

4. **Weekly Routine Agent (Loop Agent)**
   - Creates 7-day routine using looping logic.

---

## Tools
- Custom Calorie Calculator

---

## Memory
Used `InMemorySessionService` to store user profile.

---

## Output Example
============= PERSONAL TRAINER RESULT =============

Hello Navya!.Your goal is muscle gain.
You can workout 40 minutes per day.

 Your Workout Plan:
Workout for 40 minutes: 
-Push-ups
-Squats
-Lunges
-Plank hold

 Your Nutrition Plan
Daily calories 2300 kcal
- Breakfast: Oats + fruit
- Lunch: Dal + rice + veggies
- Dinner: Paneer/Eggs + salad

Weekly Routine
Day 1:Push-ups
Day 2:Squats
Day 3:Lunges
Day 4: Rest Day
Day 5:Push-ups
Day 6:Squats
Day 7: Rest Day


===================================================


---

## How to Run

1. Open terminal and navigate to the project folder:
   cd personal_trainer_ai

2. Run the application:
   python main.py


### Running the Project

1. Clone or download the project.

2. Open a terminal in the project directory:
cd personal_trainer_ai

3. Execute the app:
python main.py

4. Enter your name, goal, and workout time.

The AI Trainer will generate:
- Personalized workout plan
- Nutrition plan
- 7-day weekly schedule
