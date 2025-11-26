"""
Database of dog breed visual characteristics and aesthetic qualities.
"""

BREED_DATABASE = {
    # SPORTING GROUP
    "golden_retriever": {
        "name": "Golden Retriever",
        "group": "Sporting",
        "proportions": {
            "body_ratio": "balanced, slightly longer than tall",
            "build": "medium, athletic, well-proportioned",
            "head": "broad skull, friendly expression",
            "legs": "moderate length, sturdy"
        },
        "coat": {
            "texture": "dense, water-repellent, wavy",
            "length": "medium to long",
            "qualities": "lustrous, flowing, feathering"
        },
        "movement": {
            "gait": "smooth, powerful, ground-covering",
            "energy": "moderate to high, fluid",
            "qualities": "effortless, balanced, purposeful"
        },
        "temperament_aesthetic": {
            "mood": "warm, friendly, approachable",
            "presence": "confident yet gentle, reliable",
            "character": "harmonious, inviting, soft power"
        },
        "color_palette": ["golden", "cream", "rich amber", "warm honey"],
        "scale": "medium-large",
        "visual_essence": "warm harmony, approachable elegance, soft flowing textures, reliable grace"
    },
    
    "pointer": {
        "name": "Pointer",
        "group": "Sporting",
        "proportions": {
            "body_ratio": "square to slightly longer, lean",
            "build": "athletic, clean lines, muscular without bulk",
            "head": "chiseled, alert expression",
            "legs": "long, straight, powerful"
        },
        "coat": {
            "texture": "short, smooth, dense",
            "length": "short",
            "qualities": "sleek, clean, minimal"
        },
        "movement": {
            "gait": "smooth, effortless, far-reaching",
            "energy": "high, focused, purposeful",
            "qualities": "suspended tension, directional emphasis, poised alertness"
        },
        "temperament_aesthetic": {
            "mood": "intense focus, eager alertness",
            "presence": "aristocratic, athletic, purposeful",
            "character": "pointed intention, suspended readiness"
        },
        "color_palette": ["white with liver", "white with lemon", "white with black", "tri-color"],
        "scale": "medium-large",
        "visual_essence": "suspended tension, directional emphasis, lean athletic lines, focused intensity"
    },
    
    "cocker_spaniel": {
        "name": "Cocker Spaniel",
        "group": "Sporting",
        "proportions": {
            "body_ratio": "compact, balanced",
            "build": "sturdy but refined, well-proportioned",
            "head": "rounded skull, gentle expression",
            "legs": "moderate length, sturdy"
        },
        "coat": {
            "texture": "silky, flat or wavy",
            "length": "medium, feathering on ears/chest/legs",
            "qualities": "flowing, luxurious, soft"
        },
        "movement": {
            "gait": "smooth, coordinated, effortless",
            "energy": "moderate, cheerful",
            "qualities": "flowing grace, gentle rhythm"
        },
        "temperament_aesthetic": {
            "mood": "merry, gentle, affectionate",
            "presence": "refined sweetness, approachable charm",
            "character": "soft elegance, cheerful grace"
        },
        "color_palette": ["black", "buff", "parti-color", "rich browns", "golden"],
        "scale": "small-medium",
        "visual_essence": "flowing curves, luxurious texture, compact grace, gentle refinement"
    },
    
    # HOUND GROUP
    "greyhound": {
        "name": "Greyhound",
        "group": "Hound",
        "proportions": {
            "body_ratio": "distinctly long, streamlined",
            "build": "lean, aerodynamic, deep-chested",
            "head": "long, narrow, refined",
            "legs": "very long, straight, elegant"
        },
        "coat": {
            "texture": "short, smooth, fine",
            "length": "very short",
            "qualities": "sleek, minimal, close-fitting"
        },
        "movement": {
            "gait": "low, free-swinging, enormous stride",
            "energy": "explosive speed capability, calm reserve",
            "qualities": "aerodynamic flow, effortless speed, liquid motion"
        },
        "temperament_aesthetic": {
            "mood": "gentle dignity, quiet presence",
            "presence": "aristocratic grace, elegant restraint",
            "character": "refined minimalism, serene power"
        },
        "color_palette": ["any color", "often brindle", "fawn", "white", "black"],
        "scale": "large",
        "visual_essence": "aerodynamic minimalism, extreme streamlining, elegant speed, liquid grace"
    },
    
    "basset_hound": {
        "name": "Basset Hound",
        "group": "Hound",
        "proportions": {
            "body_ratio": "very long, low-slung",
            "build": "heavy-boned, substantial, elongated",
            "head": "large, domed, long ears",
            "legs": "very short, heavy-boned, powerful"
        },
        "coat": {
            "texture": "smooth, short, dense",
            "length": "short",
            "qualities": "clean, easy-care, loose skin"
        },
        "movement": {
            "gait": "deliberate, powerful, ground-hugging",
            "energy": "low to moderate, unhurried",
            "qualities": "heavy-footed dignity, leisurely pace"
        },
        "temperament_aesthetic": {
            "mood": "mild, patient, melancholic charm",
            "presence": "clownish dignity, humble nobility",
            "character": "sorrowful sweetness, grounded wisdom"
        },
        "color_palette": ["tri-color", "red and white", "lemon and white"],
        "scale": "medium (but low)",
        "visual_essence": "elongated horizontals, grounded weight, melancholic warmth, patient dignity"
    },
    
    "afghan_hound": {
        "name": "Afghan Hound",
        "group": "Hound",
        "proportions": {
            "body_ratio": "square, tall, elegant",
            "build": "aristocratic, refined, powerful beneath coat",
            "head": "long, refined, proud expression",
            "legs": "very long, straight"
        },
        "coat": {
            "texture": "long, fine, silky",
            "length": "very long, flowing",
            "qualities": "luxurious, dramatic, high-maintenance"
        },
        "movement": {
            "gait": "elastic, powerful, smooth",
            "energy": "moderate, dignified",
            "qualities": "floating stride, majestic flow"
        },
        "temperament_aesthetic": {
            "mood": "aloof dignity, regal distance",
            "presence": "aristocratic, exotic, independent",
            "character": "dramatic elegance, mysterious refinement"
        },
        "color_palette": ["cream", "red", "black", "brindle", "often masked face"],
        "scale": "large",
        "visual_essence": "dramatic verticality, flowing luxury, exotic refinement, aristocratic aloofness"
    },
    
    # WORKING GROUP
    "siberian_husky": {
        "name": "Siberian Husky",
        "group": "Working",
        "proportions": {
            "body_ratio": "slightly longer than tall, balanced",
            "build": "medium, athletic, efficient",
            "head": "fox-like, alert expression",
            "legs": "moderate length, powerful"
        },
        "coat": {
            "texture": "double coat, medium length",
            "length": "medium",
            "qualities": "thick, plush, insulating, natural layers"
        },
        "movement": {
            "gait": "smooth, effortless, light on feet",
            "energy": "high, tireless, playful",
            "qualities": "efficient power, joyful athleticism"
        },
        "temperament_aesthetic": {
            "mood": "friendly mischief, alert playfulness",
            "presence": "pack-oriented, energetic, expressive",
            "character": "wild beauty, natural harmony"
        },
        "color_palette": ["gray and white", "black and white", "red and white", "blue eyes common"],
        "scale": "medium",
        "visual_essence": "layered complexity, natural gradients, alert intensity, wild elegance"
    },
    
    "great_dane": {
        "name": "Great Dane",
        "group": "Working",
        "proportions": {
            "body_ratio": "square, massive scale",
            "build": "giant, powerful, elegant despite size",
            "head": "large, rectangular, noble",
            "legs": "very long, straight, strong"
        },
        "coat": {
            "texture": "short, smooth, dense",
            "length": "short",
            "qualities": "sleek, glossy, minimal"
        },
        "movement": {
            "gait": "powerful, ground-covering, surprisingly graceful",
            "energy": "moderate, dignified",
            "qualities": "gentle giant, imposing yet elegant"
        },
        "temperament_aesthetic": {
            "mood": "gentle dignity, quiet confidence",
            "presence": "commanding, noble, approachable despite size",
            "character": "monumental grace, friendly power"
        },
        "color_palette": ["fawn", "brindle", "black", "blue", "harlequin", "mantle"],
        "scale": "giant",
        "visual_essence": "monumental scale, dignified restraint, vertical emphasis, gentle power"
    },
    
    "boxer": {
        "name": "Boxer",
        "group": "Working",
        "proportions": {
            "body_ratio": "square, compact",
            "build": "muscular, powerful, athletic",
            "head": "distinctive broad, blunt",
            "legs": "moderate length, sturdy"
        },
        "coat": {
            "texture": "short, smooth, tight-fitting",
            "length": "short",
            "qualities": "sleek, shiny, minimal"
        },
        "movement": {
            "gait": "springy, powerful, energetic",
            "energy": "high, playful, athletic",
            "qualities": "muscular grace, bouncing energy"
        },
        "temperament_aesthetic": {
            "mood": "playful intensity, alert curiosity",
            "presence": "confident, energetic, protective",
            "character": "clownish power, joyful strength"
        },
        "color_palette": ["fawn", "brindle", "white markings"],
        "scale": "medium-large",
        "visual_essence": "muscular geometry, compact power, dynamic readiness, playful strength"
    },
    
    # TERRIER GROUP
    "jack_russell_terrier": {
        "name": "Jack Russell Terrier",
        "group": "Terrier",
        "proportions": {
            "body_ratio": "slightly longer than tall, compact",
            "build": "small but athletic, sturdy",
            "head": "flat skull, keen expression",
            "legs": "moderate length, sturdy"
        },
        "coat": {
            "texture": "smooth or rough, dense",
            "length": "short to medium",
            "qualities": "weather-resistant, practical"
        },
        "movement": {
            "gait": "quick, agile, energetic",
            "energy": "very high, intense, tireless",
            "qualities": "explosive bursts, determined drive"
        },
        "temperament_aesthetic": {
            "mood": "fearless intensity, bold confidence",
            "presence": "feisty, determined, high-spirited",
            "character": "compact dynamite, relentless energy"
        },
        "color_palette": ["white with black", "white with tan", "tri-color"],
        "scale": "small",
        "visual_essence": "explosive intensity, chaotic energy, compact determination, fearless spirit"
    },
    
    "scottish_terrier": {
        "name": "Scottish Terrier",
        "group": "Terrier",
        "proportions": {
            "body_ratio": "short-legged, compact body",
            "build": "sturdy, thick-set, low to ground",
            "head": "long, rectangular, bearded",
            "legs": "short, heavy-boned"
        },
        "coat": {
            "texture": "hard, wiry, dense undercoat",
            "length": "medium, distinctive furnishings",
            "qualities": "textured, sculptural, dense"
        },
        "movement": {
            "gait": "smooth, deliberate, powerful",
            "energy": "moderate, determined",
            "qualities": "dignified march, purposeful stride"
        },
        "temperament_aesthetic": {
            "mood": "dignified independence, serious demeanor",
            "presence": "confident, aloof, self-assured",
            "character": "architectural solidity, scottish pride"
        },
        "color_palette": ["black", "wheaten", "brindle"],
        "scale": "small",
        "visual_essence": "architectural solidity, dignified angles, textured density, compact nobility"
    },
    
    "bull_terrier": {
        "name": "Bull Terrier",
        "group": "Terrier",
        "proportions": {
            "body_ratio": "square, sturdy, muscular",
            "build": "powerful, thick-set, athletic",
            "head": "distinctive egg-shaped, unique profile",
            "legs": "moderate length, sturdy, parallel"
        },
        "coat": {
            "texture": "short, smooth, harsh to touch",
            "length": "short",
            "qualities": "glossy, flat, minimal"
        },
        "movement": {
            "gait": "smooth, jaunty, powerful",
            "energy": "high, playful, determined",
            "qualities": "muscular flow, clownish confidence"
        },
        "temperament_aesthetic": {
            "mood": "playful mischief, good-natured determination",
            "presence": "unique character, confident individualism",
            "character": "quirky charm, powerful playfulness"
        },
        "color_palette": ["white", "colored (various)", "brindle"],
        "scale": "medium",
        "visual_essence": "egg-shaped uniqueness, muscular curves, playful geometry, distinctive character"
    },
    
    # TOY GROUP
    "pomeranian": {
        "name": "Pomeranian",
        "group": "Toy",
        "proportions": {
            "body_ratio": "compact, square, small",
            "build": "sturdy beneath coat, well-balanced",
            "head": "fox-like, alert expression",
            "legs": "short, fine-boned"
        },
        "coat": {
            "texture": "double coat, harsh outer, soft undercoat",
            "length": "long, abundant, standing off body",
            "qualities": "fluffy, cloud-like, profuse"
        },
        "movement": {
            "gait": "smooth, free, lively",
            "energy": "high, spirited, bold",
            "qualities": "bouncy confidence, animated spirit"
        },
        "temperament_aesthetic": {
            "mood": "extroverted boldness, vivacious charm",
            "presence": "confident despite size, commanding attention",
            "character": "fluffy exuberance, big personality"
        },
        "color_palette": ["orange", "red", "cream", "black", "brown", "many colors possible"],
        "scale": "toy",
        "visual_essence": "fluffy abundance, spherical form, bright exuberance, outsized personality"
    },
    
    "italian_greyhound": {
        "name": "Italian Greyhound",
        "group": "Toy",
        "proportions": {
            "body_ratio": "square to slightly longer, miniature",
            "build": "slender, elegant, refined bone structure",
            "head": "narrow, long, refined",
            "legs": "very long for size, slender"
        },
        "coat": {
            "texture": "short, smooth, soft",
            "length": "very short",
            "qualities": "satin-like, glossy, minimal"
        },
        "movement": {
            "gait": "high-stepping, free, elegant",
            "energy": "moderate, graceful",
            "qualities": "prancing delicacy, miniature elegance"
        },
        "temperament_aesthetic": {
            "mood": "gentle sensitivity, sweet affection",
            "presence": "delicate refinement, shy grace",
            "character": "miniature aristocracy, fragile elegance"
        },
        "color_palette": ["gray", "fawn", "red", "cream", "black", "blue"],
        "scale": "toy",
        "visual_essence": "delicate refinement, miniature elegance, fragile grace, satin smoothness"
    },
    
    "pug": {
        "name": "Pug",
        "group": "Toy",
        "proportions": {
            "body_ratio": "square, compact, cobby",
            "build": "sturdy, thick-set, solid",
            "head": "large, round, wrinkled",
            "legs": "short, strong, straight"
        },
        "coat": {
            "texture": "short, smooth, soft",
            "length": "short",
            "qualities": "fine, glossy, minimal"
        },
        "movement": {
            "gait": "slight roll, jaunty, confident",
            "energy": "moderate, playful",
            "qualities": "charming waddle, dignified swagger"
        },
        "temperament_aesthetic": {
            "mood": "charming mischief, even temperament",
            "presence": "comical dignity, lovable character",
            "character": "wrinkled wisdom, clownish charm"
        },
        "color_palette": ["fawn", "black", "silver fawn", "apricot fawn"],
        "scale": "toy",
        "visual_essence": "compressed features, wrinkled character, compact charm, dignified comedy"
    },
    
    # NON-SPORTING GROUP
    "poodle": {
        "name": "Poodle (Standard)",
        "group": "Non-Sporting",
        "proportions": {
            "body_ratio": "square, well-proportioned",
            "build": "elegant, athletic, refined",
            "head": "long, refined, intelligent expression",
            "legs": "long, straight, elegant"
        },
        "coat": {
            "texture": "dense, curly, harsh texture",
            "length": "medium to long, styled",
            "qualities": "sculptural, geometric when groomed, cloud-like"
        },
        "movement": {
            "gait": "light, springy, effortless",
            "energy": "high, animated, athletic",
            "qualities": "elegant bounce, refined athleticism"
        },
        "temperament_aesthetic": {
            "mood": "intelligent alertness, dignified playfulness",
            "presence": "aristocratic bearing, confident elegance",
            "character": "sculptural refinement, intellectual grace"
        },
        "color_palette": ["black", "white", "apricot", "gray", "brown", "solid colors"],
        "scale": "medium (Standard), also toy and miniature varieties",
        "visual_essence": "sculptural precision, geometric artifice, intelligent composition, refined elegance"
    },
    
    "bulldog": {
        "name": "Bulldog",
        "group": "Non-Sporting",
        "proportions": {
            "body_ratio": "low-slung, wide, compact",
            "build": "heavy, thick-set, muscular",
            "head": "massive, broad, short-faced",
            "legs": "short, very stout, wide-set"
        },
        "coat": {
            "texture": "short, smooth, fine",
            "length": "short",
            "qualities": "glossy, minimal, loose skin"
        },
        "movement": {
            "gait": "loose-jointed, shuffling, rolling",
            "energy": "low to moderate, deliberate",
            "qualities": "determined waddle, dignified shuffle"
        },
        "temperament_aesthetic": {
            "mood": "dignified stubbornness, gentle determination",
            "presence": "courageous despite appearance, kind demeanor",
            "character": "wrinkled wisdom, steadfast loyalty"
        },
        "color_palette": ["red brindle", "fawn", "white", "brindle", "piebald"],
        "scale": "medium",
        "visual_essence": "horizontal compression, sturdy grounding, dignified wrinkles, steadfast presence"
    },
    
    "dalmatian": {
        "name": "Dalmatian",
        "group": "Non-Sporting",
        "proportions": {
            "body_ratio": "square, balanced, athletic",
            "build": "medium, muscular, elegant",
            "head": "moderate length, alert expression",
            "legs": "moderate length, straight, powerful"
        },
        "coat": {
            "texture": "short, smooth, dense",
            "length": "short",
            "qualities": "sleek, glossy, distinctive spotted pattern"
        },
        "movement": {
            "gait": "smooth, powerful, effortless",
            "energy": "high, tireless, athletic",
            "qualities": "steady rhythm, endurance, balanced flow"
        },
        "temperament_aesthetic": {
            "mood": "outgoing energy, friendly alertness",
            "presence": "dignified poise, athletic confidence",
            "character": "graphic distinctiveness, rhythmic pattern"
        },
        "color_palette": ["white with black spots", "white with liver spots"],
        "scale": "medium-large",
        "visual_essence": "rhythmic pattern, athletic balance, graphic contrast, distinctive repetition"
    },
    
    # HERDING GROUP
    "border_collie": {
        "name": "Border Collie",
        "group": "Herding",
        "proportions": {
            "body_ratio": "slightly longer than tall, athletic",
            "build": "medium, athletic, agile",
            "head": "moderate width, keen expression",
            "legs": "moderate length, sturdy, agile"
        },
        "coat": {
            "texture": "double coat, moderately long",
            "length": "medium to moderately long",
            "qualities": "weather-resistant, may be rough or smooth"
        },
        "movement": {
            "gait": "smooth, free, tireless",
            "energy": "very high, intense, focused",
            "qualities": "effortless speed, agile precision"
        },
        "temperament_aesthetic": {
            "mood": "intense focus, intelligent alertness",
            "presence": "energetic determination, laser-like attention",
            "character": "workaholic intensity, brilliant concentration"
        },
        "color_palette": ["black and white", "red and white", "tricolor", "merle patterns"],
        "scale": "medium",
        "visual_essence": "intense focus, dynamic motion, high-contrast energy, intelligent alertness"
    },
    
    "german_shepherd": {
        "name": "German Shepherd",
        "group": "Herding",
        "proportions": {
            "body_ratio": "longer than tall, substantial",
            "build": "large, athletic, powerful",
            "head": "wedge-shaped, noble, intelligent",
            "legs": "moderate length, powerful, angulated"
        },
        "coat": {
            "texture": "double coat, medium length",
            "length": "medium",
            "qualities": "dense, straight, weather-resistant"
        },
        "movement": {
            "gait": "smooth, far-reaching, effortless trot",
            "energy": "high, controlled, purposeful",
            "qualities": "powerful efficiency, noble carriage"
        },
        "temperament_aesthetic": {
            "mood": "confident alertness, noble bearing",
            "presence": "commanding authority, intelligent presence",
            "character": "powerful grace, steadfast loyalty"
        },
        "color_palette": ["black and tan", "sable", "black", "bi-color"],
        "scale": "large",
        "visual_essence": "angular alertness, powerful diagonals, noble bearing, intelligent strength"
    },
    
    "corgi": {
        "name": "Pembroke Welsh Corgi",
        "group": "Herding",
        "proportions": {
            "body_ratio": "low-set, long body on short legs",
            "build": "sturdy, compact, powerful",
            "head": "fox-like, intelligent expression",
            "legs": "very short, strong, straight"
        },
        "coat": {
            "texture": "medium length, double coat",
            "length": "medium",
            "qualities": "weather-resistant, thick, straight"
        },
        "movement": {
            "gait": "smooth, free, active",
            "energy": "high, cheerful, determined",
            "qualities": "efficient despite short legs, jaunty confidence"
        },
        "temperament_aesthetic": {
            "mood": "bold friendliness, cheerful outlook",
            "presence": "confident despite size, intelligent charm",
            "character": "elongated cuteness, determined spirit"
        },
        "color_palette": ["red", "sable", "fawn", "black and tan", "with white markings"],
        "scale": "small-medium (but low)",
        "visual_essence": "low-slung perspective, cheerful determination, elongated compactness, fox-like charm"
    }
}

def get_breed_names():
    """Return list of all available breed names for display"""
    return sorted([breed_data["name"] for breed_data in BREED_DATABASE.values()])

def get_breed_data(breed_key):
    """Get breed data by key (snake_case name)"""
    return BREED_DATABASE.get(breed_key)

def normalize_breed_name(breed_name):
    """Convert user input breed name to database key"""
    # Convert to lowercase and replace spaces with underscores
    normalized = breed_name.lower().strip().replace(" ", "_").replace("-", "_")
    
    # Handle common variations
    variations = {
        "pembroke_welsh_corgi": "corgi",
        "welsh_corgi": "corgi",
        "standard_poodle": "poodle",
    }
    
    return variations.get(normalized, normalized)
