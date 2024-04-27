# -*- coding: utf-8 -*-
from conversation import AgentConversation
import edge_lib
import json

class Simulation():
    def __init__(self, candidate_file, emojis_file):
        self.candidates = self.load_json(candidate_file)
        self.emojis = self.load_json(emojis_file)

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def run(self):
        print("Simulation is running...")
        for i in range(len(self.candidates)):
            candidate1 = list(self.candidates.keys())[i]
            if not edge_lib.get_user(candidate1):
                edge_lib.insert_user(candidate1, self.candidates[candidate1], self.emojis[candidate1])
            for j in range(i+1, len(self.candidates)):
                candidate2 = list(self.candidates.keys())[j]
                self.simulate_conversation(candidate1, self.candidates[candidate1], candidate2, self.candidates[candidate2])
    
    def simulate_conversation(self, name1, profile1, name2, profile2):
        first_date = ""
        prompt_prefix = " is going on their first date. Here are some personality questions and their responses to each. "
        character1_profile = name1 + prompt_prefix + profile1
        character2_profile = name2 + prompt_prefix + profile2
        AgentConversation(name1, name2, character1_profile, character2_profile, first_date, model="gpt-4-turbo").chat(3)


    # def run(self):
    #     print("Simulation is running...")
    #     character1_name = "Ali"
    #     character2_name = "J"
    #     character1_profile = character1_name + """
    #        is going on their first date. Here are some personality questions and their responses to each. What do you do for fun? 🤩 (hobbies, activities, etc)Hitting the golf course—love the game and the quiet it brings.What are your favorite cuisines? \U0001fac4🤰Big fan of Persian Pizza. It’s a game changer.What music do you like? 🎶🎸🥁Totally into soundtracks. They make every day feel epic.What's your biggest RED flag? ❌😵Diplomatically left blank to keep things lightWhat are your biggest pet peeves / icks? 🤢Diplomatically left blank to keep things lightWhat are your favorite movies / TV shows? 🎥🍿📺Not into moviesNot huge into movies, but I’m always down for something that’s a crowd-pleaser.Policy on drugs / alcohol? 💊🥂🥃NeverIs crypto a scam? 🪙🤑my net worth is in $Jeo BodenDo you like to travel? ✈️🚗🚌My own bed is comfyWhat are you doing on a Friday night? 👀😈It's only 5AM? The night is still young!What's your best friend's best quality? 🥰🫂They're real—can’t beat genuine people.What kind of people are you looking to meet? 😉Looking to meet some smart, driven folks who are all about good vibes.Are you e/acc or de/acc ⁉️I was patient 0 for NeuralinkDo you have any pets? 🐶Yes, I love animalsWhat's your ideal first date? 🌹Good food, great chat—what’s better than that?What's your favorite emoji? 🤣👻😝🤡👅🤓🤡 - Because who doesn’t love a good laugh
    #     """
    #     character2_profile = character2_name + """
    #        is going on their first date. Here are some personality questions and their responses to each. What do you do for fun? \ud83e\udd29 (hobbies, activities, etc)Concerts / Festivals, Play bass guitar & cello\nGym / outdoor activites\nWatch old movies / watch animeWhat are your favorite cuisines? \ud83e\udec4\ud83e\udd30Japanese & Korean (asian in general)What music do you like? \ud83c\udfb6\ud83c\udfb8\ud83e\udd41RnBWhat's your biggest RED flag? \u274c\ud83d\ude35Lack of ambition in lifeWhat are your biggest pet peeves / icks? \ud83e\udd22Body odor/smelling bad and bad skin (lowkey)What are your favorite movies / TV shows? \ud83c\udfa5\ud83c\udf7f\ud83d\udcfaPulp Fiction, Chunking Express, Truman Show, InterstellarPolicy on drugs / alcohol? \ud83d\udc8a\ud83e\udd42\ud83e\udd43OftenIs crypto a scam? \ud83e\ude99\ud83e\udd11of courseDo you like to travel? \u2708\ufe0f\ud83d\ude97\ud83d\ude8cI'm rarely homeWhat are you doing on a Friday night? \ud83d\udc40\ud83d\ude08It's only 5AM? The night is still young!What's your best friend's best quality? \ud83e\udd70\ud83e\udec2Genuine & super down to earth\nFun person to be around; social and love meeting people\nActive / athletic so we can go do stuff together\nGood leadership in clubs and orgs (important bc we often work tgt)What kind of people are you looking to meet? \ud83d\ude09Rather introverted / down to earth\nOpen to dating or just friends\nAge 19-21\nAmbitious in lifeAre you e/acc or de/acc \u2049\ufe0fI was patient 0 for NeuralinkDo you have any pets? \ud83d\udc36Yes, I love animalsWhat's your ideal first date? \ud83c\udf39Movie Marathon Night / Late Night Drive / Nice dinner with wine / Lowkey an anime run lolWhat's your favorite emoji? \ud83e\udd23\ud83d\udc7b\ud83d\ude1d\ud83e\udd21\ud83d\udc45\ud83e\udd13\ud83e\uddc3
    #     """
    #     first_date = ""
    #     AgentConversation(character1_name, character2_name, character1_profile, character2_profile, first_date, model="gpt-4-turbo").chat(1)
        


if __name__ == "__main__":
    simulation = Simulation('../phase1/characters.json', '../phase1/emojis.json')
    # simulation = Simulation()
    simulation.run()