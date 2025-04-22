# 🧵 ThreadExplorer – AI-Curated Social Thread Search
ThreadExplorer is an intelligent local-first search engine that lets you explore semantically relevant social media threads using natural language queries. It uses SentenceTransformers for embedding queries and threads, and LLaMA (via Ollama) to generate natural language explanations of why each result was retrieved.

# 🔍 Example Use Case
Query: "why people burn out after going viral"
Match:

“After my post went viral last year, I couldn’t write again for months…”
💡 Why this? This thread was matched because it describes emotional exhaustion and creative block after virality, which aligns thematically with burnout after exposure.

# 🧠 Features
🔎 Semantic Search powered by all-MiniLM-L6-v2
🧠 LLaMA via Ollama explains relevance in plain language
🧩 Based on embedded_threads.json file (precomputed)
💻 Entirely offline/local capable (no cloud dependencies)
🛠️ Simple Python CLI tool — easy to customize and extend

# 🧠 Thought Process & Tech Stack
This project was part of an assignment, not an original idea — but I decided to approach it with the mindset of building something genuinely useful, scalable, and conceptually interesting. Here's how I thought through and tackled each stage:

🗺️ Initial Understanding
The brief was to create a semantic search interface for exploring threads. I immediately recognized the need for two core parts:

A way to encode and compare threads semantically, so users could search beyond just keywords.

An explanation mechanism — to justify why each result showed up, bridging the gap between model reasoning and user intuition.

⚙️ Stack Choices
📦 Sentence Embedding: sentence-transformers (MiniLM) was used for its speed and quality balance.

🔍 Similarity Matching: cosine_similarity from scikit-learn let us keep it simple but powerful.

🧠 Explanation Generator: I used ollama with a local LLaMA 2 model to generate lightweight, natural language explanations. This gave the project a “smart assistant” vibe.

🖥️ UI: Streamlit was the natural choice for prototyping a clean, interactive UI.

📁 Data Handling: Everything was stored in JSON for simplicity and readability.

🚀 How I Approached It (Step by Step)
Started with data – created or collected deep, funny, and ethical AI-related threads that felt meaningful and quirky.

Embedded the threads – used the MiniLM model to encode each thread into vector form.

Built the search logic – compared user queries to thread embeddings and sorted by similarity.

Added explanation generation – integrated LLaMA 2 via ollama to explain semantic matches.

Wrapped it up in Streamlit – built a frontend to test, demo, and eventually deploy the system.

Iterated with deployment – attempted cloud options, ran into library/model compatibility issues (Ollama and PyTorch especially), and settled on local deployment for stability.

# 📁 Project Structure
├── app.py                     # Main CLI search + explanation tool
├── embedded_threads.json      # Your pre-embedded thread data
├── requirements.txt           # Python deps (does NOT include Ollama)
└── README.md

# 🚀 Getting Started (Local)
1. Clone the Repo
git clone https://github.com/ChetanyaRajpal/ThreadExplorer-AI-Curated-Social-Thread-Explorer.git
cd ThreadExplorer-AI-Curated-Social-Thread-Explorer

2. Install Python Dependencies
pip install -r requirements.txt

3. Install & Set Up Ollama
Follow Ollama's install guide for your platform (macOS, Windows, or Linux)

4. Once installed, run search_threads.py
5. Once ollama has downloaded the llama model and it is running successfully in the terminal after you have passed your first query, you can now run the app in the local server using streamlit.
6. 🔧 Configuration
Make sure the embedded_threads.json file is in the root directory. Each thread should have:
7. Run the App
   In terminal, type
   streamlit run app.py
8. Then you'll be prompted to enter a search query.
9. After searching, You'll then see the top matches and the AI's Explaination

# 🛠 How It Works
SentenceTransformer (all-MiniLM-L6-v2) embeds your search query
Compares it to the precomputed thread embeddings via cosine similarity
Top-k matches are passed into a prompt for LLaMA via Ollama
LLaMA explains why each thread is relevant — concisely and contextually

# 🧠 Model Customization
Want to use a different Ollama model?
Change this line in app.py:

generate_explanation_ollama(query, content, model_name="llama2")

#💡 Note on Models & Hosting
Sure, you could swap out the local LLaMA for OpenAI’s API and host this on the cloud like a normal person. And yeah, it works beautifully with gpt-4 or gpt-3.5-turbo, especially if you’ve got that sweet API key and don’t mind OpenAI reading your spicy AI takes.

But I built this using Ollama because:

I like running models locally, like it’s 1999 and the GPU is my best friend.

I like owning the stack, even if it means fighting Torch errors at 3am.

And most of all, I like not paying every time I generate a sarcastic LLaMA explanation.

That said, the code is modular — want to plug in OpenAI instead? Change the generate_explanation function to call OpenAI’s ChatCompletion API and you're golden. Host it on Streamlit, Hugging Face Spaces, or wherever vibes take you.

# 🧗 Challenges I Faced (and Lived to Tell)
Torch went full Torch.
PyTorch occasionally decided to throw existential errors (RuntimeError: Tried to instantiate class '__path__._path'...) that felt like messages from a haunted compiler. Turns out, torch.classes is a little too spicy for some setups. Lots of fun.

Ollama doesn’t hold your hand.
Running LLaMA models locally is a power move, but getting it to talk nicely with subprocess and returning clean output took some googling professional debugging. Pro tip: line breaks are your enemy.

Streamlit doesn’t like being run like a regular script.
When running outside of streamlit run, it throws "missing ScriptRunContext" warnings like candy. Mostly ignorable, but still mildly alarming at 2 AM.

Cloud hosting? Nah, we’re local rebels.
Tried setting it up on the cloud. Got yelled at by Torch, missed my GPU, and came crawling back to localhost like a hero in an indie rom-com.

Semantic similarity ≠ good UX out of the box.
Sentence transformers are magical, but picking the right thread match needs more than just cosine similarity. Had to tweak the explanation layer to avoid outputs like "This thread is relevant because it mentions AI."

The “missing module” whack-a-mole.
ModuleNotFoundError: No module named 'sentence_transformers' — ah, yes. The inevitable moment when Python reminds you that virtual environments are not optional, they’re survival gear.

Subprocess is not your friend (until it is).
Wrapping LLaMA calls in subprocess.run sounded simple in theory. In practice? Let's just say stderr was my second monitor.

Embedding JSONs are large, mysterious creatures.
You don’t realize how big and nested your thread data is until you try to pretty-print it and crash your terminal. Learned to embrace the minimal view.

Explaining the explainer.
Writing prompts for LLaMA to explain why a thread matched the search is harder than writing the search function itself. Prompt engineering is half poetry, half StackOverflow.

Trying to stay funny when debugging.
Debugging is a humbling journey. Staying witty while sifting through Python stack traces? That’s an art form. Send snacks.

# Steps to RUN

![1](https://github.com/user-attachments/assets/7d568cb8-c31e-4a45-afe3-067b5013ff86)

After cloning the repo, it will look something like this, ignore the open-ai file in the screenshot, its not in the repo.

![2](https://github.com/user-attachments/assets/553504f5-8b77-438e-9591-29f15992fcaa)


Once you’ve installed Ollama, you're all set to run the searchthreads script. This script will automatically fetch the required LLaMA model (if not already available) and serves as the core interface for semantic search. You can then run your queries directly from the terminal and receive both the top matching threads and insightful, AI-generated explanations.


![3](https://github.com/user-attachments/assets/cc681be2-c749-4eca-b336-ca872b549a63)

Here you are prompted to search your first query!


![4](https://github.com/user-attachments/assets/de631c5f-ab01-45b2-bba5-edfbb4f203cd)

Type in your query and smash that ENTER!


![5](https://github.com/user-attachments/assets/04ba08a0-523b-49a7-b6db-51045706619a)

And voila! Your system is ready to go and now you have the results!!
Now, lets run it locally!


![6](https://github.com/user-attachments/assets/bb7223a9-d40e-4735-990c-59d748a1cb71)

Navigate to app.py



![7](https://github.com/user-attachments/assets/88fe7409-3418-4814-8fe8-2324575c1ab7)

Type in this code to run the app.py

![8](https://github.com/user-attachments/assets/54d89ca0-655e-4a77-815f-a82481151567)

And here we are at the local server, you can change the number of responses you want from 1-10, and just type in your query and SEARCH!

![9](https://github.com/user-attachments/assets/2c310986-b01d-4b96-b7d7-9bfdf2b5a8c6)



![10](https://github.com/user-attachments/assets/87e8c588-dfe6-49f3-8d57-db31cc11340b)


Here we GO!








