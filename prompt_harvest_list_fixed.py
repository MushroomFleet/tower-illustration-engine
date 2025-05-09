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
    # Look for lines starting with "depiction of T0W3R style" and capture the full prompt
    # This approach ensures we get the complete prompt even with line breaks
    prompt_sections = []
    lines = content.split('\n')
    current_prompt = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('depiction of T0W3R style'):
            # If we were collecting a previous prompt, save it
            if current_prompt is not None:
                prompt_sections.append(current_prompt)
            # Start a new prompt
            current_prompt = line
        elif current_prompt is not None and line and not line.startswith('#') and not line.startswith('---'):
            # Continue collecting the current prompt if the line isn't a header or separator
            current_prompt += ' ' + line
    
    # Don't forget to add the last prompt if we were collecting one
    if current_prompt is not None:
        prompt_sections.append(current_prompt)
    
    # Clean up each prompt (remove extra whitespace, normalize spacing)
    cleaned_prompts = []
    for prompt in prompt_sections:
        # Normalize whitespace (replace multiple spaces with a single space)
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
