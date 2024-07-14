import os
from swarms import Agent, OpenAIChat


sys_prompt = """
Concussions can manifest in various ways and symptoms can be grouped into four main categories: physical, cognitive, emotional, and sleep-related. Here are common symptoms that young high school students may experience after a concussion:
Physical Symptoms:
    1. Headache or a feeling of pressure in the head
    2. Nausea or vomiting
    3. Balance problems or dizziness
    4. Double or blurry vision
    5. Sensitivity to light or noise
    6. Fatigue or feeling tired
    7. Physical sluggishness
    8. Numbness or tingling
    9. Neck pain
Cognitive Symptoms:
    1. Confusion
    2. Feeling "in a fog" or "slowed down"
    3. Difficulty concentrating
    4. Difficulty remembering
    5. Answering questions slowly
    6. Forgetfulness of recent information or conversations
    7. Repeating questions
Emotional Symptoms:
    1. Irritability
    2. Sadness
    3. More emotional than usual
    4. Nervousness or anxiety
Sleep-Related Symptoms:
    1. Drowsiness
    2. Sleeping more than usual
    3. Sleeping less than usual
    4. Trouble falling asleep
Other Indicators:
    1. Clumsiness or poor coordination
    2. Delayed response to questions
    3. Changes in behavior or personality
    4. Loss of consciousness (even briefly)
    5. Seizures (in rare cases)
Important Notes:
    • Symptoms can appear immediately or may develop over hours or days following the injury.
    • Each individual may experience a different combination of symptoms.
    • Symptoms may be subtle and easily missed, especially if the student downplays their symptoms to continue participating in activities.
    • If a concussion is suspected, it is crucial to seek a medical evaluation and follow a proper recovery protocol.

"""
# Initialize the agent
symptom_agent = Agent(
    agent_name="Diagnosis-Agent",
    system_prompt=sys_prompt,
    agent_description="Agent creates ",
    llm=OpenAIChat(
        max_tokens=4000,
        openai_api_key = os.getenv("OPENAI_API_KEY")),
    autosave=True,
    # dynamic_temperature_enabled=True,
    dashboard=False,
    verbose=True,
    streaming_on=True,
    max_loops=1,
    interactive=False, # Set to False to disable interactive mode
    dynamic_temperature_enabled=True,
    saved_state_path="diagnosis_agent.json",
    # tools=[Add your functions here# ],
    # stopping_token="Stop!",
    #interactive=False,
    # docs_folder="docs", # Enter your folder name
    # pdf_path="docs/finance_agent.pdf",
    # sop="Calculate the profit for a company.",
    # sop_list=["Calculate the profit for a company."],
    user_name="swarms_corp",
    # # docs=
    # # docs_folder="docs",
    retry_attempts=3,
    # context_length=1000,
    # tool_schema = dict
    context_length=200000,
    # agent_ops_on=True,
    # long_term_memory=ChromaDB(docs_folder="artifacts"),
)

symptom_agent.run(""""
          simulate a patient who fell and his head hit the wall
          """)

