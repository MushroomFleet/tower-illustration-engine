import re

def harvest_prompts(input_file, output_file):
    """
    Extract prompt lines from input_file and write them to output_file.
    Uses regex to find prompts regardless of formatting.
    """
    # Read the entire file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find all prompts
    # This pattern looks for text starting with "depiction of T0W3R style" and ending with a period
    pattern = r'depiction of T0W3R style.*?(?<=\.)'
    prompts = re.findall(pattern, content, re.DOTALL)
    
    # Clean up each prompt (remove extra whitespace, newlines, etc.)
    cleaned_prompts = []
    for prompt in prompts:
        # Remove newlines and normalize whitespace
        cleaned = re.sub(r'\s+', ' ', prompt).strip()
        cleaned_prompts.append(cleaned)
    
    # Write prompts to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for prompt in cleaned_prompts:
            f.write(prompt + '\n')
    
    print(f"Successfully extracted {len(cleaned_prompts)} prompts to {output_file}")

if __name__ == "__main__":
    input_file = 'prompt_output/all_character_prompts.txt'
    output_file = 'prompt_list.txt'
    harvest_prompts(input_file, output_file)
