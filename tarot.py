import random
tarot_cards = {
    "The Fool": "innocence, new beginning, idealism, youth, lack of commitment",
    "The Magician": "manifestation, resourcefulness, skill, creation",
    "The High Priestess": "intuition, mystery, sensuality, subconscious, allure",
    "The Empress": "prosperity, nuture, motherhood, fertility, femininity",
    "The Emperor": "fatherhood, dependability, authority, practicality, rules",
    "The Hierophant": "tradition, knowledge, religion, beliefs, marriage",
    "The Lovers": "love, harmony, choices, wants, decision, fate",
    "The Chariot": "willpower, victory, determination, bravery, effort",
    "Strength": "compassion, patience, inner strength, resilience, triumph",
    "The Hermit": "solitude, inner wisdom, introspection, pondering, self-reflection",
    "Wheel of Fortune": "destiny, luck, cycles of fate, karma, fortune",
    "Justice": "truth, justice, consequences, fairness, balance",
    "The Hanged Man": "confinement, lack of direction, letting go, surrenduring, new perspectives",
    "Death": "transformation, endings, new beginnings, change, rebirth",
    "Temperance": "balance, moderation, harmony, peace, protection",
    "The Devil": "addictions, boundings, attachment, shadow self, materialism",
    "The Tower": "sudden change,  chaos, awakening, bankruptcy, tragedy",
    "The Star": "hope, inspiration, faith, creativity, positive direction",
    "The Moon": "insecurity, emotions, illusion, confusion, intuition",
    "The Sun": "success, joy, optimism, celebration, self expression, confidence",
    "Judgement": "awakening , reflection, evaluation, judgement, revealation",
    "The World": "completion, wholeness, fulfillment, accomplishment, freedom",

    "Ace of Wands": "New beginnings, inspiration, potential, creative spark, enthusiasm, spiritual energy, divine inspiration",
    "Two of Wands": "Planning, decisions, discovery, future vision, personal power, dominion, patience before action",
    "Three of Wands": "Expansion, foresight, overseas opportunities, commerce, ships coming in, leadership, exploration",
    "Four of Wands": "Celebration, homecoming, community, foundation, stability, marriage, harmonious relationships",
    "Five of Wands": "Competition, conflict, rivalry, challenges, tension, disagreements, growing pains",
    "Six of Wands": "Victory, success, public recognition, progress, self-confidence, triumph after struggle",
    "Seven of Wands": "Defense, perseverance, maintaining position, courage, standing your ground, conviction",
    "Eight of Wands": "Swift action, movement, air travel, quick developments, messages, arrows of love",
    "Nine of Wands": "Resilience, persistence, last stand, boundaries, defensive position, preparedness",
    "Ten of Wands": "Burden, responsibility, hard work, stress, achievement at a cost, obligation",
    "Page of Wands": "Enthusiasm, exploration, discovery, free spirit, messenger, exciting news, new ideas",
    "Knight of Wands": "Action, adventure, fearlessness, impulsiveness, travel, passionate pursuit",
    "Queen of Wands": "Confidence, determination, social butterfly, vivacious, warmth, courage, independence",
    "King of Wands": "Natural leader, vision, entrepreneur, honor, charisma, bold action, inspiration",
    
    "Ace of Cups": "New feelings, intuition, spirituality, love, emotional fulfillment, divine love",
    "Two of Cups": "Partnership, attraction, romance, harmony, unity, mutual understanding",
    "Three of Cups": "Celebration, friendship, community, joy, gatherings, social events, creative collaboration",
    "Four of Cups": "Contemplation, meditation, apathy, reevaluation, discontent, turning inward",
    "Five of Cups": "Loss, grief, disappointment, regret, focusing on the negative, learning from loss",
    "Six of Cups": "Nostalgia, childhood memories, innocence, reunion, past influences, gifts",
    "Seven of Cups": "Choices, fantasy, illusion, possibilities, dreams, scattered focus, wishful thinking",
    "Eight of Cups": "Walking away, seeking more, abandonment, withdrawal, spiritual journey",
    "Nine of Cups": "Contentment, satisfaction, emotional fulfillment, wishes granted, abundance",
    "Ten of Cups": "Happy family, lasting happiness, emotional fulfillment, harmony, perfect love",
    "Page of Cups": "Creative beginnings, intuitive messages, gentle soul, inner child, dreamer",
    "Knight of Cups": "Romance, charm, imagination, beauty, refined feelings, artistic pursuit",
    "Queen of Cups": "Intuition, empathy, nurturing, compassion, emotional stability, inner wisdom",
    "King of Cups": "Emotional balance, diplomacy, wisdom, counselor, master of feelings",

    "Ace of Swords": "Mental clarity, breakthrough, new ideas, truth, justice, intellectual power",
    "Two of Swords": "Decision, stalemate, blocked emotions, avoidance, difficult choices",
    "Three of Swords": "Heartbreak, emotional pain, sorrow, grief, rejection, betrayal",
    "Four of Swords": "Rest, recuperation, meditation, retreat, solitude, mental recharge",
    "Five of Swords": "Conflict, defeat, win at all costs, hostility, discord, dishonor",
    "Six of Swords": "Transition, leaving behind, moving on, gradual change, journey over water",
    "Seven of Swords": "Deception, stealth, strategy, sneaking away, running away, theft",
    "Eight of Swords": "Restriction, imprisonment, victim mentality, isolation, self-imposed bounds",
    "Nine of Swords": "Anxiety, worry, fear, depression, nightmares, mental anguish",
    "Ten of Swords": "Painful endings, rock bottom, victim, crisis, ultimate defeat, letting go",
    "Page of Swords": "New ideas, curiosity, communication, vigilance, seeking truth",
    "Knight of Swords": "Ambitious, direct, intellectual, truth-seeker, harsh, aggressive action",
    "Queen of Swords": "Clear thinking, intellectual, independent, direct communication, wisdom",
    "King of Swords": "Authority, truth, intellectual power, clear thinking, justice, leadership",

    "Ace of Pentacles": "New financial opportunity, prosperity, abundance, manifestation, potential",
    "Two of Pentacles": "Balance, adaptability, time management, prioritization, juggling resources",
    "Three of Pentacles": "Teamwork, collaboration, learning, mastery, skill development",
    "Four of Pentacles": "Security, conservation, frugality, possessiveness, material concerns",
    "Five of Pentacles": "Hardship, loss, poverty, isolation, spiritual poverty, health issues",
    "Six of Pentacles": "Generosity, charity, giving, receiving, sharing wealth, gratitude",
    "Seven of Pentacles": "Assessment, evaluation, hard work, patience, investment, waiting",
    "Eight of Pentacles": "Apprenticeship, skill development, craftsmanship, quality work",
    "Nine of Pentacles": "Luxury, self-reliance, financial independence, refinement, rewards",
    "Ten of Pentacles": "Wealth, family, inheritance, establishment, tradition, legacy",
    "Page of Pentacles": "New opportunity, study, scholarship, new job, manifestation",
    "Knight of Pentacles": "Hard work, routine, conservatism, methodical, reliability",
    "Queen of Pentacles": "Nurturing, practical, abundance, down-to-earth, financial security",
    "King of Pentacles": "Wealth, business, leadership, security, discipline, abundance"
}
def draw_card(tarot_cards):
    card = random.choice(list(tarot_cards.keys()))
    meaning = tarot_cards[card]
    return {
        "card": card,
        "meaning": meaning
    }
def format_card_message(card_info, position=None):
    message = f"\n💌 You drew the {card_info['card']}!"
    if position:
        message += f"\nThis card represents your {position.lower()}"
    message += f"\nLet's explore what it means: {card_info['meaning']}\n"
    return message    
# User chooses spread
print("💖 Hi there! Ready to explore some tarot insights together? 💖")
print("\nI can do a few different types of readings for you:")
print("1. One Card - Perfect for daily guidance or a quick check-in")
print("2. Three Cards - Great for understanding how a situation is developing")
print("3. Five Cards - Ideal for a deeper dive into a specific question")

choice = input("\nWhat kind of reading would you like? (Enter 1, 2, or 3): ")
question = input("What brings you here today?: ")

if choice == "1":
    print("-" * 40)  
    print("\nA one-card reading is perfect for daily guidance or a specific question.")
    print("It gives us a clear snapshot of the energies around your situation.")
    print(f"You're question is: {question}")
    card = draw_card(tarot_cards)
    print(format_card_message(card))
elif choice == "2":
    print("-"*40)
    print("A three-card reading helps us understand how your situation develops over time.")
    print("We'll look at how past events have shaped your present,")
    print("and what possibilities lie ahead!")
    print(f"You're question is: {question}")
    positions = ["Past","Present","Future"]
    for i, position in enumerate(positions):
        card = draw_card(tarot_cards)
        print(format_card_message(card, position))
elif choice == "3":
    print("-" * 40)
    print("A five-card reading gives us a deeper look at your situation.")
    print("It helps us understand the various factors at play")
    print("and suggests practical steps forward.")
    print(f"You're question is: {question}")
    positions = [
        "Current Situation",
        "Past Influences",
        "Potential Future",
        "Hidden Factors",
        "Advice"
    ]
    for i, position in enumerate(positions):
        card = draw_card(tarot_cards)
        print(format_card_message(card, position))
else:
    print("-" * 40)  
    print("\n💝 Oops! Let's start with a simple one-card reading...")    
    print("\nA one-card reading is perfect for daily guidance or a specific question.")
    print("It gives us a clear snapshot of the energies around your situation.")
    print(f"You're question is: {question}")
    card = draw_card(tarot_cards)
    print(format_card_message(card))
        
print("\n💝 I hope these insights are helpful! Remember, you know your situation best -")
print("take what resonates with you and trust your inner wisdom! 💗")
print("-" * 50)