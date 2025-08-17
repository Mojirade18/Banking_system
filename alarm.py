import time
from datetime import datetime, timedelta

# Ask for user details
name = input("Enter your name: ").strip()
subject = input("What subject do you want to study? ").strip()
study_minutes = int(input("How many minutes do you plan to study for? "))

# Calculate end time
end_time = datetime.now() + timedelta(minutes=study_minutes)

# Display start message
print(f"\nHello {name}! 📚")
print(f"You are studying {subject} for {study_minutes} minutes.")
print(f"Your session will end at {end_time.strftime('%H:%M:%S')}.\n")

# Countdown loops
for remaining in range(study_minutes, 0, -1):
    print(f"{remaining} minute(s) left... Keep going! 💪")
    time.sleep(60)  # Wait for 1 minute

# Session complete
print("\n⏰ Time's up")
print(f"Great work, {name}! Take a break now before your next study session. ")
