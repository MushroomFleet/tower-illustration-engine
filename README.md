# TOWER Character Illustration Prompts

A comprehensive toolkit for generating consistent, structured prompts for AI image generation of characters from the TOWER story. This system enables the creation of high-quality character illustrations with consistent styling across various environments and scenes.

It makes captions before you build a dataset ;) in this way we can create coherent and consistent illustrations for pre-existing narratives by extracting details from the story and using this information to plan out a pristine dataset structure promoting ideal alignment. This is permitted by HiL (Human in Loop) design, where a human curator is involved in this process using external tools. The resulting captions are used both as prompts and as training captions to build out the initial concept art dataset.

## What This Is

This project provides a complete pipeline for transforming detailed character descriptions into standardized prompts for AI image generation systems. It includes:

- Character description templates and files for the six main TOWER characters
- A flexible prompt generation system that maintains character consistency
- Tools for creating both character prompts and matching background scenes
- Utilities for formatting and organizing prompt collections

The system is designed for commissioning character key art with a consistent style using modern AI image generation platforms.

## What This Does

- Transforms markdown character descriptions into standardized image generation prompts
- Generates multiple scene variations for each character (plain background, tower, countryside, tavern, spotlight)
- Creates matching empty background prompts for composite illustrations
- Standardizes prompt formatting and fixes line wrapping issues
- Maintains a consistent style identifier and character triggers across all prompts

## Project Structure

- **characters/** - Individual character description markdown files
- **prompt_output/** - Generated character prompts organized by character/scene
- **config.json** - Configuration settings for the prompt generator
- **final_prompt_generator.py** - Main script to generate character prompts
- **prompt_harvest_list.py** - Extracts and consolidates prompts into a single file
- **background_prompt_generator.py** - Creates matching background-only prompts
- **fix_line_wrapping.py** - Fixes formatting and line break issues in prompt files

### Output Files

- **prompt_list.txt** - Consolidated list of all character prompts
- **fixed_prompt_list.txt** - Line-wrapped fixed version of consolidated prompts
- **background_list.txt** - Empty scene background prompts matching character environments
- **fixed_background_list.txt** - Line-wrapped fixed version of background prompts

## Installation

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

### Setup

1. Clone or download this repository:
   ```
   git clone https://github.com/MushroomFleet/tower-illustration-engine
   cd tower-illustration
   ```

2. Ensure the project structure is maintained with character files in the `characters/` directory.

3. No additional installation steps required - all scripts use standard Python libraries.

## Characters

Each character has a dedicated markdown file with structured sections:

1. **Character Description File** (`characters/[name].md`)
   - Detailed description of physical appearance
   - Clothing and equipment details
   - Scene variations
   - Spotlight scene from their story
   - Notes on character essence

The six main TOWER characters are:

1. **Broderick Ironheart** (BR0D) - Barrel-chested human warrior with glitter-speckled beard
2. **Lysandra Veil** (LYS4) - Elven mage with silver hair that moves to magical currents
3. **Thimbletack Silverfingers** (TH1M) - Halfling rogue with shadow-blending cloak
4. **Morganthe Bloom** (M0RG) - Human healer with wildflowers in her hair
5. **Grok Stonefist** (GR0K) - Orc mathematician with formula tattoos
6. **Whisper** (WH1S) - Tiefling bard/warlock with solid black, starlight-reflecting eyes

Each character has a unique 4-character trigger with intentionally deformed spelling to help AI systems recognize the character consistently.

## How To Use

### Step 1: Generate Character Prompts

To generate all character prompts from the character markdown files:

```bash
python final_prompt_generator.py
```

This processes each character file in the `characters/` directory and creates:
- Individual prompt files in `prompt_output/[character]/`
- A consolidated `prompt_output/all_character_prompts.txt` file

### Step 2: Create Consolidated Prompt List

To extract all prompts into a single usable list:

```bash
python prompt_harvest_list.py
```

This creates `prompt_list.txt` containing all character prompts, one per line, without headers or metadata.

### Step 3: Generate Background Prompts

To create matching background-only prompts for empty scenes:

```bash
python final_background_generator.py
```

This generates `background_list.txt` with prompts for empty scenes that match the character environments.

### Step 4: Fix Line Wrapping Issues

To ensure all prompts are properly formatted on single lines:

```bash
python fix_line_wrapping.py
```

This creates `fixed_prompt_list.txt` and `fixed_background_list.txt` with properly formatted prompts.

## Step-by-Step Guide

### Creating a New Character

1. Create a new character markdown file in `characters/` directory following the template:
   ```md
   # Character Name
   
   ## Physical Description
   [Description text]
   
   ## Clothing and Equipment
   [Description text]
   
   ## Scene Variations
   
   ### Plain Background
   [Description text]
   
   ### Tower Setting
   [Description text]
   
   ### Countryside Setting
   [Description text]
   
   ### Tavern Setting
   [Description text]
   
   ## Spotlight Scene
   [Description text]
   
   ## Character Essence
   [Notes on character personality/essence]
   ```

2. Update `config.json` to include the new character with their trigger code.

3. Run the full pipeline:
   ```bash
   python final_prompt_generator.py
   python prompt_harvest_list.py
   python final_background_generator.py
   python fix_line_wrapping.py
   ```

4. Find your complete prompt files in `fixed_prompt_list.txt` and `fixed_background_list.txt`.

### Modifying Prompt Templates

To change the prompt format:

1. Edit the template strings in `final_prompt_generator.py`.
2. Regenerate all prompts with the updated format.

## Examples

### Example Character Description File

```md
# Broderick

## Physical Description
Barrel-chested human with a perpetually sunburned face, wild auburn hair, and a beard containing various small objects he's forgotten about—now including trace amounts of glitter that refuse to be removed.

## Clothing and Equipment
Practical plate armor modified with numerous pouches, hooks, and questionable "improvements."

## Scene Variations

### Plain Background
Standing neutrally, plain white background with shadow, lit from above.

### Tower Setting
Performing his elaborate pre-battle stretching routine, inside a sorcerer's tower corridor with animated armor pieces scattered around.

### Countryside Setting
Striding purposefully forward with hand on weapon, in the countryside of Spellwick with towers visible in background.

### Tavern Setting
Seated at a wooden table examining a small mechanical puzzle, in a dimly lit tavern with wooden tables and patrons in background.

## Spotlight Scene
Transformed into a mobile disco ball with glittering reflective surface covering his entire body, delivering a decisive blow against Lady Prismatica with Skullcrusher raised high.

## Character Essence
Courageous to the point of absurdity but not without tactical sense. Believes most situations can be resolved through direct communication and precisely applied violence.
```

### Example Generated Prompt

```
depiction of T0W3R style, BR0D, barrel-chested human with a perpetually sunburned face, wild auburn hair, and a glitter-speckled beard, practical plate armor modified with numerous pouches and hooks, performing his elaborate pre-battle stretching routine, inside a sorcerer's tower corridor with animated armor pieces scattered around.
```

### Example Background Prompt

```
depiction of T0W3R style, in the background inside a sorcerer's tower corridor with animated armor pieces scattered around.
```

### Example Command Sequence

```bash
# Generate all character prompts
python final_prompt_generator.py

# Extract prompts to a consolidated list
python prompt_harvest_list.py

# Create background-only prompts
python final_background_generator.py

# Fix line wrapping issues
python fix_line_wrapping.py
```

## Advanced Usage

### Human-in-Loop Curation

For best results, use these prompts as a starting point for AI image generation, then:

1. Generate initial images using the prompts from `fixed_prompt_list.txt`
2. Evaluate results and make targeted adjustments to specific aspects
3. Keep the character trigger (e.g., BR0D) and core description consistent
4. Iterate to refine the style and details while maintaining character consistency

### Creating Custom Scenes

To add new scene variations:

1. Update the character markdown files with new scene descriptions
2. Regenerate the prompts using the pipeline
3. Update `final_background_generator.py` to include any new scene types

### Using Background and Character Composites

To create composite illustrations:

1. Generate empty backgrounds using prompts from `fixed_background_list.txt`
2. Generate characters using prompts from `fixed_prompt_list.txt`
3. Use the matching backgrounds and characters for consistent scene composition
