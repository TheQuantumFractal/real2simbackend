import openai

class AgentConversation:
    def __init__(self, system_prompt1, system_prompt2, model="gpt-4-turbo"):
        self.client = openai.OpenAI()
        self.model = model
        self.conversation1 = [{"role": "system", "content": system_prompt1}]
        self.conversation2 = [{"role": "system", "content": system_prompt2}]
    
    def chat(self, num_messages):
        for _ in range(num_messages):
            response1 = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation1
            )
            last_message1 = response1.choices[0].message.content
            self.conversation1.append({"role": "user", "content": last_message1})
            self.conversation2.append({"role": "assistant", "content": last_message1})

            response2 = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation2
            )
            last_message2 = response2.choices[0].message.content
            self.conversation2.append({"role": "user", "content": last_message2})
            self.conversation1.append({"role": "assistant", "content": last_message2})

    def get_conversation_history(self, agent_number):
        if agent_number == 1:
            return self.conversation1
        elif agent_number == 2:
            return self.conversation2
        else:
            raise ValueError("Invalid agent number, choose 1 or 2.")
    
    def interview_phase