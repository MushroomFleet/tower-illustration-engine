"""
Script to fix line wrapping in the prompt files.
"""

def fix_line_wrapping(input_file, output_file):
    """
    Fix line wrapping issues in the prompt files.
    Ensures each prompt is on a single line without mid-word breaks.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any instances where a line break occurs in the middle of a word
    fixed_content = content.replace('\n', ' ').replace('  ', ' ')
    
    # Split by periods to identify individual prompts
    prompts = fixed_content.split('.')
    
    # Clean up and reformat each prompt
    clean_prompts = []
    for prompt in prompts:
        if 'depiction of T0W3R style' in prompt:
            # Clean up the prompt and add the period back
            clean_prompt = prompt.strip() + '.'
            clean_prompts.append(clean_prompt)
    
    # Write the clean prompts to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for prompt in clean_prompts:
            f.write(prompt + '\n')
    
    print(f"Fixed line wrapping in {len(clean_prompts)} prompts in {output_file}")

if __name__ == "__main__":
    # Fix the character prompts
    fix_line_wrapping('prompt_list.txt', 'fixed_prompt_list.txt')
    
    # Fix the background prompts
    fix_line_wrapping('background_list.txt', 'fixed_background_list.txt')
