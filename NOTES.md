# TOWER Character Illustration Plan

## Project Overview

This project involves creating detailed visual descriptions for each of the six main characters from the TOWER story. These descriptions will be used to commission character key art through image generation systems and will serve as the foundation for further refinement through Human-in-Loop (HiL) curation.

## Character Trigger System

Each character will have a unique 4-character trigger created by deforming their name using a pattern that substitutes vowels with similar-looking numbers:
- A → 4
- E → 3
- I → 1
- O → 0
- U → u

The triggers, clamped to 4 characters, are:
1. BR0D (Broderick Ironheart)
2. LYS4 (Lysandra Veil)
3. TH1M (Thimbletack Silverfingers)
4. M0RG (Morganthe Bloom)
5. GR0K (Grok Stonefist)
6. WH1S (Whisper)

These deformed names create micro-triggers that resist tokenization and can function as specific activation terms during fine-tuning.

## Prompt Template Structure

All prompts will follow this standardized template:

```
[trigger-phrase] [persona-phrase] [outfit-phrase] [scene-phrase]
```

Where:
- [trigger-phrase] = "depiction of T0W3R style, [character-trigger]"
- [persona-phrase] = "[character description],"
- [outfit-phrase] = "[clothing description],"
- [scene-phrase] = "[character pose], [background description]."

For example:
```
depiction of T0W3R style, BR0D, barrel-chested human with sunburned face and wild auburn hair, practical plate armor with numerous pouches and hooks, standing alert with hand on weapon, inside a dimly lit tower corridor with magical runes glowing on the walls.
```

## Background/Scene Variations

For each character, we will create descriptions for these standardized settings:

1. **Plain White Background**
   - Standing neutrally, plain white background with shadow, lit from above

2. **Inside a Tower Setting**
   - Inside a sorcerer's tower with location/elements relevant to the character

3. **Countryside Setting**
   - In the countryside of Spellwick with towers visible in background

4. **Tavern Setting**
   - In a dimly lit tavern with wooden tables and patrons in background

5. **Spotlight Scene**
   - One iconic moment from the story that captures the character's essence

## Character Consistency Approach

To ensure consistency across all depictions:
- Each character will have a single, definitive physical description
- Each character will have one specific outfit/clothing description
- These descriptions will remain identical across all prompts
- Only the pose and background descriptions will change

This approach prevents conceptual wandering and maintains a consistent visual identity for each character throughout the development process.

## Implementation Plan

1. Create NOTES.md (this document) outlining the overall approach
2. Create individual character description files for each of the six characters
3. For each character:
   - Extract key physical details from source materials
   - Identify distinctive clothing/equipment
   - Craft consistent description blocks
   - Create variations for each of the five scene types

## File Structure

```
/
├── NOTES.md
├── characters/
│   ├── broderick.md
│   ├── lysandra.md
│   ├── thimbletack.md
│   ├── morganthe.md
│   ├── grok.md
│   └── whisper.md
```

## Next Steps

1. Create the `characters` directory
2. Create detailed description files for each character
3. For each character, extract relevant information from:
   - TOWER-lorebook.md
   - characters.txt
   - story-supplement-001.md
   - story-supplement-002.md
   - world.txt
4. Compile standardized description blocks
5. Generate scene variations
6. Review for consistency and visual clarity
7. Prepare for HiL curation loops and iterative refinement

After completing these descriptions, we'll have a robust foundation for commissioning character artwork that accurately captures the essence of each character while maintaining consistency across all depictions.
