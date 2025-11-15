import asyncio
from agent import support_agent

async def main():
    """Main CLI loop for the support agent"""
    print("\n╔════════════════════════════════════════════════════════╗")
    print("║                    💝 FOR ASHU 💝                     ║")
    print("║         🏹 Cupid - A Gift From Ahsan's Heart 🏹       ║")
    print("║           An AI Companion Crafted With Love           ║")
    print("╚════════════════════════════════════════════════════════╝\n")
    
    if support_agent.conversation_history:
        print(f"✨ Welcome back! Cupid remembered our {len(support_agent.conversation_history)//2} previous conversations.\n")
    else:
        print("Hey Ashu! 😊 I'm Cupid, here to make your day brighter.\n")
    print("Type 'exit' to leave, or 'clear' to start fresh.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'exit':
                print("\nCatch you later, Ashu! Take care. 💕\n")
                break
            
            if user_input.lower() == 'clear':
                support_agent.clear_history()
                print("Conversation history cleared.\n")
                continue
            
            if not user_input:
                continue
            
            print("\nAgent: Thinking...\n")
            response = await support_agent.chat(user_input)
            print(f"Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nAgent session interrupted. Goodbye!\n")
            break
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())

