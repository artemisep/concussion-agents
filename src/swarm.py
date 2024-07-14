from treatmentagent import treatment_agent
from diagnosisagent import diagnosis_agent
from monitoringagent import monitoring_agent
from recoveryagent import recovery_agent
from symptomagent import symptom_agent
from swarms import AgentRearrange

# Create a list of agents
agents = [symptom_agent, diagnosis_agent, treatment_agent, monitoring_agent, recovery_agent]
# Define the flow pattern
flow = "Symptom-Agent -> Diagnosis-Agent -> Treatment-Agent -> Monitoring-Agent, Recovery-Agent"

# Using AgentRearrange class
agent_system = AgentRearrange(agents=agents, flow=flow)
output = agent_system.run("""
                          Do this step by steo, list the symptom of a student 
                          whose head hit the wall
                          give instruction for diagnosis as to whether
                          the student have concussion and how severe it is. 
                          Then provide treatment plan, give instructions on 
                          what to monitor and how to manage recovery in this student's 
                          daily life
                          """)
print(output)
