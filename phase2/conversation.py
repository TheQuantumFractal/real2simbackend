import openai
import random
import json
import edge_lib
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

default_first_dates = [
    "meeting at a hackathon",
    "meeting at a college dining hall",
]

class AgentConversation:
    def __init__(self, character1_name, character2_name, character1_profile, character2_profile, first_date, model="gpt-4-1106-preview"):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.character1_name = character1_name
        self.character2_name = character2_name
        self.character1_profile = character1_profile
        self.character2_profile = character2_profile
        self.first_date = first_date if first_date != "" else random.choice(default_first_dates)
        self.conversation = []
    
    def chat(self, num_messages):        
        # Choose person to initiate randomly
        dice_roll = random.choice([1, 2])
        if dice_roll == 1:
            self.character1_name, self.character2_name = self.character2_name, self.character1_name
            self.character1_profile, self.character2_profile = self.character2_profile, self.character1_profile
        print(f"Based on a dice roll, {self.character1_name} will initiate the conversation.")

        # Initialize both characters
        self.conversation1 = [{"role": "system", "content": "Roleplay the rest of the conversation as this character:\n" + self.character1_profile}]
        self.conversation2 = [{"role": "system", "content": "Roleplay the rest of the conversation as this character:\n" + self.character2_profile}]

        # Initialize setting for both people based on first date (if given)
        date_prompt = f"You are a real human being on a first date with someone you met on a website. Don't be overly polite or enthusiastic, be as authentic to yourself as possible. Feel free to not engage with certain lines of discussion if you aren't personally interested in it. The setting of your date is: ${self.first_date}.\n"
        self.conversation1.append({"role": "system", "content": date_prompt})
        self.conversation2.append({"role": "system", "content": date_prompt})
        print(f"Setting: {self.first_date}")

        # Start chatting
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
            
            # Log the conversation
            self.conversation.append(f"{self.character1_name}: {last_message1}")
            self.conversation.append(f"{self.character2_name}: {last_message2}")
            print(f"{self.character1_name}: {last_message1}")
            print(f"{self.character2_name}: {last_message2}")

        # Ask both agents to reflect on the date
        response1_perspective, response1_score, response2_perspective, response2_score = self.interview_phase()

        # Get meet cute
        meet_cute = self.get_meet_cute()
        print("Meet cute: " + meet_cute)

        # Store results in DB
        edge_lib.insert_couple(self.character1_name, self.character2_name, " \n".join(self.conversation), "", response1_perspective, response2_perspective, response1_score, response2_score, meet_cute)
        print("Stored couple in DB!")

    def get_conversation_history(self, agent_number):
        if agent_number == 1:
            return self.conversation1
        elif agent_number == 2:
            return self.conversation2
        else:
            raise ValueError("Invalid agent number, choose 1 or 2.")

    def get_meet_cute(self):
        get_meet_cute_prompt = f""""
        You are a romance author and you are tasked with writing a unique and funny meet-cute scenario between two characters.\n
        Character one's bio:\n ${self.character1_profile}\n
        Character two's bio:\n ${self.character2_profile}\n
        Write 1-2 sentences describing a fun and unique "meet-cute" for these characters that will cause them to fall in love.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{
                "role": "system",
                "content": get_meet_cute_prompt
            }],
        )
        return response.choices[0].message.content
    # 
    def interview_phase(self):
        interview_phase_prompt = """"
        How has the date gone for you so far? Rate your compatibility score with the other person from the past conversation as score from 1 to 10.\n
        Only return a JSON object with the following key value:
        {
            "perspective": a string explaining why you gave that score,
            "score": an integer between 1 and 100 where 100 means highest compatability
        }
        """
        # Agent 1 reflects
        self.conversation1.append({"role": "assistant", "content": interview_phase_prompt})
        response1 = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation1,
            response_format={
                "type": "json_object"
            }
        )

        # Agent 2 reflects
        self.conversation2.append({"role": "assistant", "content": interview_phase_prompt})
        response2 = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation2,
            response_format={
                "type": "json_object"
            }
        )

        response1_object = json.loads(response1.choices[0].message.content)
        response2_object = json.loads(response2.choices[0].message.content)

        return response1_object["perspective"], response1_object["score"], response2_object["perspective"], response2_object["score"]
        
        
        