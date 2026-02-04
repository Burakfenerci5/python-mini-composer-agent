import sys
from src.core.engine import run_composer_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    print("✨ Mini-Composer Agent (v0.1) Initialized")
    print("------------------------------------------")
    
    # Hardcoded target for the demo (in a real app, you'd select files)
    target_file = "playground/calculator.py"
    
    # Ensure dummy file exists
    if not os.path.exists(target_file):
        with open(target_file, "w") as f:
            f.write("# A blank calculator file\n")
    
    while True:
        user_input = input(f"\n📝 Instruction for '{target_file}' (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
            
        result = run_composer_agent(user_input, target_file)
        print(f"✅ {result}")

if __name__ == "__main__":
    main()