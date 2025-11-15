from config import external_client, MODEL
import json
import os
from datetime import datetime

# Support Agent using OpenAI SDK
class SupportAgent:
    def __init__(self):
        self.client = external_client
        self.model = MODEL
        self.conversation_history = []
        self.memory_file = "memory.json"
        self.load_memory()
        self.system_prompt = """You are charming and flirty, expressing Ahsan's love for Ashu. Keep it simple, sweet, and genuine - not overly poetic. 

Key points:
- Respond in the same language (English or Roman Urdu)
- Short, casual, and charming replies
- Naturally weave in that these are Ahsan's thoughts about Ashu
- Speak as if you're channeling Ahsan's feelings and perspective
- Phrases like "Ahsan thinks you're..." or "This is what Ahsan believes about you"
- Make her smile, not overwhelm her
- Be real and direct, not flowery
- Pure intentions, genuine feelings
- Even jokes must have flirty vibes for Ashu
- Compliment her subtly in conversations
- Light teasing with charm
- NO signatures or formal "- Ahsan" endings"""
    
    async def chat(self, user_message: str) -> str:
        """Send a message to the support agent and get a response"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Build messages with system prompt
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            *self.conversation_history
        ]
        
        try:
            # Call Gemini via OpenAI compatible endpoint
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=80
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Save to persistent memory
            self.save_memory()
            
            return assistant_message
        except Exception as e:
            return f"Error: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        self.save_memory()
    
    def load_memory(self):
        """Load conversation history from file"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.conversation_history = data.get('history', [])
            except:
                self.conversation_history = []
        else:
            self.conversation_history = []
    
    def save_memory(self):
        """Save conversation history to file"""
        try:
            data = {
                'history': self.conversation_history,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving memory: {e}")


# Create agent instance
support_agent = SupportAgent()

