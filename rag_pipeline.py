import re
import json
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

# Define threat intelligence queries
QUERIES = {
    "threat_actors": "Threat Actors, Adversary Groups, Cybercriminal Organizations, APT Groups, Cyber Espionage Groups",
    "ttps": "Attacks, Tactics, Techniques, and Procedures (TTPs), Attack Patterns, Exploitation Techniques",
    "malware": "Malware, Malicious Files, Ransomware, Trojans, Worms, Keyloggers, Botnets, Fileless Malware, Rootkits, Backdoors",
    "targeted_entities": "Targeted Entities (victims), Industries, Organizations, Government Agencies, Individuals, Geographic Regions"
}

# Define threat intelligence extraction prompts
PROMPTS = {
    "threat_actors": PromptTemplate(
        template="""You are a cybersecurity threat intelligence assistant. Extract structured threat intelligence data from the given report.

        **Rules:**
        - Only extract the name(s) of threat actors mentioned in the text.
        - Do **not** include any other JSON keys or additional data.

        **Report:** {text}

        **Strict JSON Response Format:**  
        {{
            "threat_actors": ["<Threat Actor Name>", "<Threat Actor Name>"]
        }}

        **Important:**  
        - If no threat actor is found, return an empty list (e.g., `"threat_actors": []`).
        - Do **not** use markdown or explanations, **only return JSON**.
        """, 
        input_variables=["text"]
    ),
    "ttps": PromptTemplate(
        template="""You are a cybersecurity threat intelligence assistant. Extract structured threat intelligence data from the given report.

        **Rules:**
        - Analyse and find the MITRE ATT&CK **Tactics and Techniques**.
        - Do **not** include any other JSON keys or additional data.

        **Report:** {text}

        **Strict JSON Response Format:**  
        {{
            "ttps": {{
                "Tactics": [
                    ["<Tactic Name>"],
                    ["<Tactic Name>"]
                ],
                "Techniques": [
                    ["<Technique Name>"],
                    ["<Technique Name>"]
                ]
            }}
        }}

        **Important:**  
        - If no TTPs are found, return an empty `"ttps": {{"Tactics": [], "Techniques": []}}` object.
        - Do **not** use markdown or explanations, **only return JSON**.
        """, 
        input_variables=["text"]
    ),
    "malware": PromptTemplate(
        template="""You are a cybersecurity threat intelligence assistant. Extract structured threat intelligence data from the given report.

        **Rules:**
        - Only extract the malware names.
        - Do **not** include any other JSON keys or additional data.

        **Report:** {text}

        **Strict JSON Response Format:**  
        {{
            "malware": [ 
                {{"Name": "<Malware Name>"}}
            ]
        }}

        **Important:**  
        - If no malware is found, return an empty list (e.g., `"malware": []`).
        - Do **not** use markdown or explanations, **only return JSON**.
        """, 
        input_variables=["text"]
    ),
    "targeted_entities": PromptTemplate(
        template="""Extract the names of **Targeted Entities** (industries, sectors, organizations) from the text.

        **Rules:**
        - Only extract the names of targeted industries/sectors.
        - Do **not** include any other JSON keys or additional data.

        **Report:** {text}

        **Strict JSON Response Format:**  
        {{
            "targeted_entities": ["<Entity Name>", "<Entity Name>"]
        }}

        **Important:**  
        - If no targeted entities are found, return an empty list (e.g., `"targeted_entities": []`).
        - Do **not** use markdown or explanations, **only return JSON**.
        """, 
        input_variables=["text"]
    ),
}

class RAGPipeline:
    def __init__(self, documents):
        """Initialize the RAG pipeline with documents."""
        self.embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
        self.vectorstore = Chroma.from_documents(documents, self.embeddings)
        self.retriever = self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 15})
        self.llm = ChatOllama(model="qwen2.5", base_url="http://192.168.12.221:11434/")

    def generate_threat_intelligence(self):
        """Generate structured threat intelligence from the report."""
        extracted_data = []

        for key, query in QUERIES.items():
            retrieved_docs = self.retriever.get_relevant_documents(query)
            retrieved_text = " ".join([doc.page_content for doc in retrieved_docs])

            qa_prompt = PROMPTS[key]
            question_generator_chain = LLMChain(llm=self.llm, prompt=qa_prompt)
            response = question_generator_chain.invoke({"text": retrieved_text})
            result = response['text'].strip()

            # Clean JSON response
            result = re.sub(r'^\s*```(?:python|json)?\s*|\s*```$', '', result, flags=re.MULTILINE).strip()
            
            try:
                extracted_data.append(json.loads(result))
                
            except json.JSONDecodeError:
                extracted_data.append({"error": "Invalid JSON response"})

        return extracted_data
