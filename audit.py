import openai
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

df = pd.read_csv('company_data.csv')

def analyze_claim(claim, company_name):

    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    

    truth_row = df[df['company'] == company_name].iloc[0]
    prompt = f"Company: {company_name}\nClaim: {claim}\nActual Data: {truth_row.to_dict()}"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


print(analyze_claim("GreenEnergyCo has reduced emissions by 30%.", "GreenEnergyCo"))