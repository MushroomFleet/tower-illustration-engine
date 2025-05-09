import re

def extract_background_descriptions(input_file):
    """
    Extract unique background descriptions from the prompt list.
    """
    # Read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        prompts = f.readlines()
    
    # Extract background descriptions
    backgrounds = set()
    
    for prompt in prompts:
        # Split the prompt to extract the description part
        parts = prompt.split(', ')
        
        # We need at least 4 parts (style, character, character desc, outfit/clothing, scene)
        if len(parts) >= 4:
            # Extract everything after the third comma (scene description)
            # This is a bit tricky because of variable number of commas in the prompt
            scene_start_index = prompt.find(', ', prompt.find(', ', prompt.find(', ') + 1) + 1) + 2
            scene_description = prompt[scene_start_index:].strip()
            
            # For plain background, we want the entire description
            if "plain white background" in scene_description:
                backgrounds.add(scene_description)
            # For other scenes, find the part that starts with "in" or "inside"
            elif "in " in scene_description or "inside " in scene_description:
                # Find where the actual scene description starts
                if "inside " in scene_description:
                    match = re.search(r'inside [^,]+', scene_description)
                    if match:
                        scene_part = match.group(0)
                    else:
                        # Fallback - take everything after "inside"
                        scene_part = scene_description[scene_description.find("inside "):]
                else:
                    match = re.search(r'in [^,]+', scene_description)
                    if match:
                        scene_part = match.group(0)
                    else:
                        # Fallback - take everything after "in"
                        scene_part = scene_description[scene_description.find("in "):]
                
                # Add to our set of backgrounds
                backgrounds.add(scene_part)
    
    return backgrounds

def generate_background_prompts(backgrounds, output_file):
    """
    Generate background-only prompts and write them to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for background in sorted(backgrounds):
            prompt = f"depiction of T0W3R style, in the background {background}.\n"
            f.write(prompt)
    
    print(f"Successfully generated {len(backgrounds)} background prompts in {output_file}")

def main():
    input_file = 'prompt_list.txt'
    output_file = 'background_list.txt'
    
    # Extract background descriptions
    backgrounds = extract_background_descriptions(input_file)
    
    # Generate and save background prompts
    generate_background_prompts(backgrounds, output_file)

if __name__ == "__main__":
    main()
