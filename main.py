
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def main():
    print("=" * 50)
    print("   AI MARKETING STRATEGY MANAGER")
    print("=" * 50)
    print("\nWelcome! Let's create your marketing strategy.")

    business_name = input("\nEnter your business name: ")
    product = input("What product or service do you offer? ")
    audience = input("Who is your target audience? ")
    goal = input("What is your main marketing goal? ")

    print("\n--- YOUR BUSINESS DETAILS ---")
    print("Business:", business_name)
    print("Product/Service:", product)
    print("Target Audience:", audience)
    print("Marketing Goal:", goal)

    print("\nYour project setup is working!")
    print("Next, we will connect the AI marketing agents.")

if __name__ == "__main__":
    main()
