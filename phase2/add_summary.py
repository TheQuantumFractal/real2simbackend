import openai
import edge_lib
import os

if __name__ == "__main__":
  all_dates = edge_lib.get_couples()
  
  for date in all_dates:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
      How they met:
      {date["meet_cute"]}
      What {date["couple"][0]} thought:
      {date["perspective1"]}
      What {date["couple"][1]} thought:
      {date["perspective2"]}
      Make a concise one-line summary about the date between {date["couple"][0]} and {date["couple"][1]}.

      Example 1: Person A and Person B met at a cat cafe and hit it off immediately.
      Example 2: Person A and Person B had a date at a symphony orchestra and unfortunately did not have much in common.
    """
    
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[{
          "role": "system",
          "content": prompt
      }],
    ).choices[0].message.content
    edge_lib.update_couple(date["couple"][0], date["couple"][1], summary=response)
