import pandas as pd
from datetime import date
import os

# Exercises we're tracking
EXERCISES = ['bench', 'squat', 'deadlift', 'pull ups']
CSV_FILE = 'workouts.csv'

def log_workout():
    print("\n📝 LOG WORKOUT")
    print("=" * 30)
    
    # Show exercise options
    print("Exercises:")
    for i, ex in enumerate(EXERCISES, 1):
        print(f"{i}. {ex.title()}")
    
    # Pick exercise
    choice = input("\nSelect exercise (1-4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return
    exercise = EXERCISES[int(choice) - 1]
    
    # Get workout details
    sets = input("How many sets? ")
    reps = input("How many reps? ")
    weight = input("Weight (lbs)? ")
    
    # Save to CSV
    workout = {
        'date': date.today(),
        'exercise': exercise,
        'sets': sets,
        'reps': reps,
        'weight': weight
    }
    
    df_new = pd.DataFrame([workout])
    
    # Append to CSV if exists, create if not
    if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
        df_new.to_csv(CSV_FILE, mode='a', header=False, index=False)
    else:
        df_new.to_csv(CSV_FILE, mode='w', header=True, index=False)
    
    print(f"\n✅ Logged: {exercise.title()} — "
          f"{sets} sets x {reps} reps @ {weight}lbs")


def view_history():
    print("\n📋 VIEW HISTORY")
    print("=" * 30)
    
    # Check if file exists and has data
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        print("No workouts logged yet!")
        return
    
    # Load the CSV
    df = pd.read_csv(CSV_FILE)
    
    # Show filter options
    print("Filter by:")
    print("1. All workouts")
    print("2. Specific exercise")
    
    choice = input("\nEnter choice (1-2): ")
    
    if choice == '1':
        print(f"\n📋 All Workouts ({len(df)} total)")
        print("=" * 50)
        print(df.to_string(index=False))
        
    elif choice == '2':
        print("\nExercises:")
        for i, ex in enumerate(EXERCISES, 1):
            print(f"{i}. {ex.title()}")
        ex_choice = input("\nSelect exercise (1-4): ")
        if ex_choice not in ['1', '2', '3', '4']:
            print("Invalid choice")
            return
        exercise = EXERCISES[int(ex_choice) - 1]
        filtered = df[df['exercise'] == exercise]
        if filtered.empty:
            print(f"No {exercise} workouts logged yet!")
        else:
            print(f"\n📋 {exercise.title()} History "
                  f"({len(filtered)} sessions)")
            print("=" * 50)
            print(filtered.to_string(index=False))
    else:
        print("Invalid choice")


def personal_bests():
    print("\n🏆 PERSONAL BESTS")
    print("=" * 30)
    
    # Check if file exists
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        print("No workouts logged yet!")
        return
    
    df = pd.read_csv(CSV_FILE)
    
    # Find heaviest weight per exercise
    bests = df.groupby('exercise')['weight'].max()
    
    print("\n🏆 Your Heaviest Lifts:")
    print("=" * 30)
    for exercise, weight in bests.items():
        # Get the full row for that best lift
        best_row = df[(df['exercise'] == exercise) & 
                      (df['weight'] == weight)].iloc[0]
        print(f"\n{exercise.title()}")
        print(f"  Weight : {weight}lbs")
        print(f"  Sets   : {best_row['sets']}")
        print(f"  Reps   : {best_row['reps']}")
        print(f"  Date   : {best_row['date']}")        


def view_progress():
    print("\n📈 VIEW PROGRESS")
    print("=" * 30)
    
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        print("No workouts logged yet!")
        return
    
    df = pd.read_csv(CSV_FILE)
    
    # Show exercise options
    print("Select exercise:")
    for i, ex in enumerate(EXERCISES, 1):
        print(f"{i}. {ex.title()}")
    
    choice = input("\nEnter choice (1-4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return
    
    exercise = EXERCISES[int(choice) - 1]
    filtered = df[df['exercise'] == exercise].copy()
    
    if filtered.empty:
        print(f"No {exercise} workouts logged yet!")
        return
    
    print(f"\n📈 {exercise.title()} Progress")
    print("=" * 40)
    
    # Show each session
    for _, row in filtered.iterrows():
        print(f"{row['date']} → "
              f"{row['weight']}lbs "
              f"({row['sets']} sets x {row['reps']} reps)")
    
    # Show stats
    print("\n📊 Stats:")
    print(f"  Sessions  : {len(filtered)}")
    print(f"  Starting  : {filtered['weight'].iloc[0]}lbs")
    print(f"  Current   : {filtered['weight'].iloc[-1]}lbs")
    print(f"  Personal Best : {filtered['weight'].max()}lbs")
    
    # Progress indicator
    diff = filtered['weight'].iloc[-1] - filtered['weight'].iloc[0]
    if diff > 0:
        print(f"  Progress  : +{diff}lbs 📈 Keep going!")
    elif diff < 0:
        print(f"  Progress  : {diff}lbs 📉 Keep pushing!")
    else:
        print(f"  Progress  : Maintaining 💪")

def show_menu():
    print("\n🏋️ GYM PROGRESS TRACKER")
    print("=" * 30)
    print("1. Log Workout")
    print("2. View History")
    print("3. Personal Bests")
    print("4. View Progress")
    print("5. Quit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1-5): ")
        
        if choice == '1':
            log_workout()
        elif choice == '2':
            view_history()
        elif choice == '3':
            personal_bests()
        elif choice == '4':
            view_progress()
        elif choice == '5':
            print("\nGood work today! 💪")
            break
        else:
            print("\nInvalid choice, try again")

main()