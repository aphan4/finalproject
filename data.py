FOODS = [
    #noodles
    {"name": "Ramen", "taste": "savory", "type": "noodles", "cuisine": "east_asian", "search": "ramen"},
    {"name": "Pad Thai", "taste": "savory", "type": "noodles", "cuisine": "southeast_asian", "search": "pad thai"},
    {"name": "Pho", "taste": "savory", "type": "noodles", "cuisine": "southeast_asian", "search": "pho"},
    {"name": "Pasta", "taste": "savory", "type": "noodles", "cuisine": "mediterranean", "search": "italian pasta"},
    
    #handhelds
    {"name": "Tacos", "taste": "savory", "type": "handheld", "cuisine": "latin", "search": "tacos"},
    {"name": "Burrito", "taste": "savory", "type": "handheld", "cuisine": "latin", "search": "burrito"},
    {"name": "Burger", "taste": "savory", "type": "handheld", "cuisine": "american", "search": "burger"},
    {"name": "Banh Mi", "taste": "savory", "type": "handheld", "cuisine": "southeast_asian", "search": "banh mi"},
    {"name": "Shawarma", "taste": "savory", "type": "handheld", "cuisine": "mediterranean", "search": "shawarma"},
    {"name": "Pizza", "taste": "savory", "type": "handheld", "cuisine": "european", "search": "pizza"},

    #bowls
    {"name": "Poke Bowl", "taste": "savory", "type": "bowl", "cuisine": "east_asian", "search": "poke bowl"},
    {"name": "Bibimbap", "taste": "savory", "type": "bowl", "cuisine": "east_asian", "search": "bibimbap"},
    {"name": "Burrito Bowl", "taste": "savory", "type": "bowl", "cuisine": "latin", "search": "burrito bowl"},
    {"name": "Butter Chicken", "taste": "savory", "type": "bowl", "cuisine": "indian", "search": "butter chicken"},
    {"name": "Biryani", "taste": "savory", "type": "bowl", "cuisine": "indian", "search": "biryani"},
    
    #grilled
    {"name": "Korean BBQ", "taste": "savory", "type": "grilled", "cuisine": "east_asian", "search": "korean bbq"},
    {"name": "BBQ Ribs", "taste": "savory", "type": "grilled", "cuisine": "american", "search": "bbq ribs"},
    {"name": "Kebabs", "taste": "savory", "type": "grilled", "cuisine": "mediterranean", "search": "kebab"},
   
   #shareable
    {"name": "Dumplings", "taste": "savory", "type": "shareable", "cuisine": "east_asian", "search": "dumplings"},
    {"name": "Falafel", "taste": "savory", "type": "shareable", "cuisine": "mediterranean", "search": "falafel"},
    {"name": "Samosas", "taste": "savory", "type": "shareable", "cuisine": "indian", "search": "samosas"},
    {"name": "Nachos", "taste": "savory", "type": "shareable", "cuisine": "latin", "search": "nachos"},
    
    #soup
    {"name": "Tom Yum", "taste": "savory", "type": "soup", "cuisine": "southeast_asian", "search": "tom yum soup"},
    {"name": "Hot Pot", "taste": "savory", "type": "soup", "cuisine": "east_asian", "search": "hot pot"},
    
    #fried
    {"name": "Fried Chicken", "taste": "savory", "type": "fried", "cuisine": "american", "search": "fried chicken"},
    {"name": "Chicken Wings", "taste": "savory", "type": "fried", "cuisine": "american", "search": "chicken wings"},
    {"name": "Tempura", "taste": "savory", "type": "fried", "cuisine": "east_asian", "search": "tempura"},
    {"name": "Fish & Chips", "taste": "savory", "type": "fried", "cuisine": "european", "search": "fish and chips"},

    #sweets
    {"name": "Pancakes", "taste": "sweet",  "type": "sweet", "cuisine": "american", "search": "pancakes breakfast"},
    {"name": "Ice Cream", "taste": "sweet",  "type": "sweet", "cuisine": "american", "search": "ice cream"},
    {"name": "Açaí Bowl", "taste": "sweet",  "type": "bowl", "cuisine": "american", "search": "acai bowl"},
    {"name": "Crepes", "taste": "sweet",  "type": "sweet", "cuisine": "european", "search": "crepes"},
    {"name": "Churros", "taste": "sweet",  "type": "sweet", "cuisine": "latin", "search": "churros"},
]

QUESTIONS = [
    {
        "key": "taste",
        "prompt": "First up: sweet or savory?",
        "answers": [
            ("savory", "Savory"),
            ("sweet", "Sweet"),
            ("any", "Either is fine"),
        ],
    },
    {
        "key": "type",
        "prompt": "What kind of dish sounds good?",
        "answers": [
            ("noodles", "Noodles & pasta"),
            ("handheld", "Handheld (tacos, burgers, wraps)"),
            ("bowl", "Rice & bowls"),
            ("grilled", "Grilled & BBQ"),
            ("shareable", "Small plates to share"),
            ("soup", "Soup & broth"),
            ("fried", "Fried & crispy"),
            ("sweet", "Something sweet"),
            ("any", "No preference"),
        ],
    },
    {
        "key": "cuisine",
        "prompt": "Which flavors are you feeling?",
        "answers": [
            ("east_asian", "East Asian"),
            ("southeast_asian", "Southeast Asian"),
            ("latin", "Latin American"),
            ("american", "American"),
            ("mediterranean", "Mediterranean"),
            ("indian", "Indian"),
            ("european", "European"),
            ("any", "Surprise me"),
        ],
    },
]


def answer_label(question_key, value):
    for q in QUESTIONS:
        if q["key"] == question_key:
            for v, label in q["answers"]:
                if v == value:
                    return label
    return value