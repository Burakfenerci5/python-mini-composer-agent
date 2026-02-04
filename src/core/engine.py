import os
from openai import OpenAI
from src.core.file_ops import read_file, write_file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are 'Mini-Composer', an AI coding agent.
Your goal is to fulfill the user's request by rewriting code files.

You will receive:
1. The User's Instruction.
2. The Current File Content.

You must return:
The COMPLETE, updated code for the file. Do not use diffs or placeholders.
"""

def run_composer_agent(user_prompt, target_file):
    print(f"🤖 Mini-Composer is thinking about {target_file}...")
    
    # 1. Read the current state
    current_code = read_file(target_file)
    if not current_code:
        return "Error: File not found."

    # 2. Construct the context (simulating Cursor's Context Window)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"USER REQUEST: {user_prompt}\n\nTARGET FILE ({target_file}):\n```python\n{current_code}\n```"}
    ]

    # 3. Call the Model (GPT-4o or o1-mini works best for coding)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    new_code = response.choices[0].message.content
    
    # Clean up Markdown tags if the LLM adds them
    new_code = new_code.replace("```python", "").replace("```", "").strip()

    # 4. Apply the Edit
    write_file(target_file, new_code)
    return "Edit Complete."