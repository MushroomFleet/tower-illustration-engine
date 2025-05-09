import re

def extract_background_descriptions(input_file):
    """
    Extract unique background descriptions from the prompt list.
    """
    # Read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        prompts = f.readlines()
    
    # Define our background sets
    backgrounds = set()
    
    # Define standard backgrounds for each location type
    backgrounds.add("plain white background with shadow, lit from above")
    backgrounds.add("inside a sorcerer's tower corridor with animated armor pieces scattered around")
    backgrounds.add("inside a sorcerer's tower library with chronometric devices and floating books")
    backgrounds.add("inside a sorcerer's tower maintenance tunnel with pipes and magical conduits")
    backgrounds.add("inside a sorcerer's tower chamber with animated armor pieces dissolving into rust")
    backgrounds.add("inside a sorcerer's tower room where reality bends and distorts")
    backgrounds.add("in the countryside of Spellwick with towers visible in background")
    backgrounds.add("in a dimly lit tavern with wooden tables and patrons in background")
    
    # Add special spotlight scene backgrounds
    backgrounds.add("in a chamber with rainbow energy and prismatic light effects")
    backgrounds.add("in a chronometric library with swirling temporal energy and floating timepieces")
    backgrounds.add("in a swirling vortex of dimensional distortion with reality bending and distorting")
    backgrounds.add("inside the United Sorcerers' Tower with a maintenance shaft visible")
    backgrounds.add("in a study room with floating mathematical equations and probability charts")
    
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
