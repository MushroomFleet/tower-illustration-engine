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
    
    # Track scene types for more detailed extraction
    plain_backgrounds = set()
    tower_scenes = set()
    countryside_scenes = set()
    tavern_scenes = set()
    special_scenes = set()
    
    for prompt in prompts:
        prompt = prompt.strip()
        
        # Skip incomplete prompts
        if not prompt or prompt.count(',') < 3:
            continue
        
        # Pattern matching for different scene types
        if "plain white background" in prompt:
            plain_backgrounds.add("plain white background with shadow, lit from above")
        
        elif "inside a sorcerer's tower" in prompt or "inside a sorcerer's tower" in prompt:
            # Extract tower scene descriptions
            match = re.search(r'inside a sorcerer\'s tower\s[^,]+(.*?)\.', prompt)
            if match:
                full_scene = f"inside a sorcerer's tower{match.group(0)}"
                tower_scenes.add(full_scene.strip())
            else:
                # Try a simpler approach
                parts = prompt.split("inside a sorcerer's tower")
                if len(parts) > 1:
                    scene_desc = parts[1].split(',')[0].strip()
                    tower_scenes.add(f"inside a sorcerer's tower {scene_desc}")
                
        elif "in the countryside of Spellwick" in prompt:
            countryside_scenes.add("in the countryside of Spellwick with towers visible in background")
            
        elif "in a dimly lit tavern" in prompt:
            tavern_scenes.add("in a dimly lit tavern with wooden tables and patrons in background")
        
        # Special spotlight scenes
        elif any(spotlight in prompt for spotlight in ["Lady Prismatica", "Pendleton Chronos", "Sir Puffington", "dimensional distortion"]):
            # Extract the contextual environment for spotlight scenes
            if "Lady Prismatica" in prompt:
                special_scenes.add("in a chamber with rainbow energy and prismatic light effects")
            elif "Pendleton Chronos" in prompt:
                special_scenes.add("in a chronometric library with swirling temporal energy and floating timepieces")
            elif "Sir Puffington" in prompt or "dimensional distortion" in prompt:
                special_scenes.add("in a swirling vortex of dimensional distortion with reality bending and distorting")
            elif "animated armor" in prompt and "#37-B" in prompt:
                special_scenes.add("in a chamber with animated armor pieces dissolving into rust and oxidizing metal")
            elif "United Sorcerers' Tower" in prompt:
                special_scenes.add("inside the United Sorcerers' Tower with a maintenance shaft visible")
            elif "calculating the 27" in prompt:
                special_scenes.add("in a study room with floating mathematical equations and probability charts glowing with faint magical energy")
    
    # Combine all unique backgrounds
    backgrounds.update(plain_backgrounds)
    backgrounds.update(tower_scenes)
    backgrounds.update(countryside_scenes)
    backgrounds.update(tavern_scenes)
    backgrounds.update(special_scenes)
    
    # Add some additional standard backgrounds that might be useful
    backgrounds.add("inside a sorcerer's tower corridor with animated armor pieces scattered around")
    backgrounds.add("inside a sorcerer's tower library with chronometric devices and floating books")
    backgrounds.add("inside a sorcerer's tower maintenance tunnel with pipes and magical conduits")
    backgrounds.add("inside a sorcerer's tower chamber with animated armor pieces dissolving into rust")
    backgrounds.add("inside a sorcerer's tower room where reality bends and distorts")
    
    return backgrounds

def generate_background_prompts(backgrounds, output_file):
    """
    Generate background-only prompts and write them to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for background in sorted(backgrounds):
            # Ensure we have proper formatting and ending punctuation
            background = background.strip()
            if not background.endswith('.'):
                background += '.'
                
            prompt = f"depiction of T0W3R style, in the background {background}\n"
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
