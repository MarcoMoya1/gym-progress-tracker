import pandas as pd
from datetime import date

#Exercises we're tracking 
EXERCISES = ['bench', 'squat', 'deadlift', 'pull ups']

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
            print("\n📝 Log Workout — coming soon")
        elif choice == '2':
            print("\n📋 View History — coming soon")
        elif choice == '3':
            print("\n🏆 Personal Bests — coming soon")
        elif choice == '4':
            print("\n📈 View Progress — coming soon")
        elif choice == '5':
            print("\nGood work today! 💪")
            break
        else:
            print("\nInvalid choice, try again")

main()
