from transformers import AutoModelForCausalLM, AutoTokenizer
import openai

# Set up the GPT-3 model and tokenizer
model_name = "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Main loop for chatbot interaction
print("Chatbot: Hello! I'm here to assist with grammar. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    corrected_text = generate_response(user_input)
    print("Chatbot:", corrected_text)