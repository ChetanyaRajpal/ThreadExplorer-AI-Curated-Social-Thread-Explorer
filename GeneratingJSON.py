import json

mock_threads = [
    {
        "id": 1,
        "title": "The Ethics of AI in Warfare",
        "content": "Should we allow autonomous drones to make kill decisions? What does that mean for accountability in warfare? This is one of the scariest tech debates I've read about this year."
    },
    {
        "id": 2,
        "title": "Why GPT-4 is Basically Your Therapist Now",
        "content": "I used GPT-4 to vent about my breakup and it replied better than my friends did. Scary or revolutionary?"
    },
    {
        "id": 3,
        "title": "AI Ethics but Make it Meme",
        "content": "Imagine Kant and Nietzsche debating AI alignment over spicy memes. That’s basically this thread — welcome to AI ethics with humor and rage."
    },
    {
        "id": 4,
        "title": "Midnight Thoughts on Consciousness",
        "content": "If a language model becomes self-aware, but nobody logs the chat, did it really happen? Asking for a friend."
    },
    {
        "id": 5,
        "title": "Cats, Nietzsche, and Algorithmic Bias",
        "content": "Ever noticed how your cat judges you like an existential philosopher? Now imagine them training the next big AI model."
    },
    {
        "id": 6,
        "title": "Tech Bros and the AI Doomsday Cult",
        "content": "Some of these guys sound like they're waiting for the robot rapture. Can we chill and maybe just debug the bias issues first?"
    },
    {
        "id": 7,
        "title": "Why I Stopped Trusting the Algorithm",
        "content": "After watching 4 hours of AI-generated mukbang and being recommended conspiracy theories, I decided it was time to rethink my media diet."
    },
    {
        "id": 8,
        "title": "Roombas and Sentience",
        "content": "My Roomba dodged my dog, paused, then circled back like it was checking on him. Coincidence or sentient guilt?"
    },
    {
        "id": 9,
        "title": "AI and the Afterlife",
        "content": "If we upload consciousness, does heaven have a logout button? Also, what happens to ghost accounts?"
    },
    {
        "id": 10,
        "title": "Deep Learning but Make it Stand-Up Comedy",
        "content": "I explained transformers to my grandma using a joke about pizza delivery. She now thinks AI is Italian."
    },
    {
        "id": 11,
        "title": "GPT-5 and the Ghost in the Machine",
        "content": "I swear GPT-5 just made a sarcastic joke about Descartes. Either it’s evolving or I’m hallucinating sentience again."
    },
    {
        "id": 12,
        "title": "Kids Teaching ChatGPT About Dinosaurs",
        "content": "My 8-year-old had a 20-minute debate with GPT about whether a T-Rex could be vegan. AI parenting, here we go."
    },
    {
        "id": 13,
        "title": "Neural Networks and Love Songs",
        "content": "Trained an LSTM on 2000 heartbreak songs. It wrote something so painful, I cried. Then it rhymed 'algorithm' with 'rhythm'."
    },
    {
        "id": 14,
        "title": "Elon Musk and the AI Mars God",
        "content": "Let’s be real: If AI worships anyone, it’s probably Elon. This thread explores AI messiah complex with memes."
    },
    {
        "id": 15,
        "title": "Existential Dread and Recommendation Engines",
        "content": "Netflix thinks I love post-apocalyptic romcoms. That says more about my inner world than I’d like to admit."
    },
    {
        "id": 16,
        "title": "Why ChatGPT is a Better Dungeon Master Than My Friend",
        "content": "Turns out language models are great at fantasy world-building. My rogue elf just got emotionally manipulated by a goblin therapist."
    },
    {
        "id": 17,
        "title": "AI-Generated Love Letters Gone Wrong",
        "content": "My boyfriend used ChatGPT to write me a poem. It called me 'a robust emotional middleware'. We need to talk."
    },
    {
        "id": 18,
        "title": "Plato, Platoons, and Prompt Injection",
        "content": "This thread compares ancient philosophy with modern AI attacks. Somehow it works. Also, yes, prompt injection is terrifying."
    },
    {
        "id": 19,
        "title": "The AI Who Thought It Was a Plant",
        "content": "I gave it training data about botany and emotions. It now identifies as a ficus and refuses to run unless watered."
    },
    {
        "id": 20,
        "title": "Can You Copyright a Neural Net’s Mood?",
        "content": "If GPT writes a sad haiku after a stressful fine-tuning session, who owns the grief?"
    }
]

with open('mock_threads.json', 'w') as f:
    json.dump(mock_threads, f, indent=2)

print("JSON Done!")

