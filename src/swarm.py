from treatmentagent import treatment_agent
from diagnosisagent import diagnosis_agent
from monitoringagent import monitoring_agent
from recoveryagent import recovery_agent
from swarms import AgentRearrange

# Create a list of agents
agents = [diagnosis_agent, treatment_agent, monitoring_agent, recovery_agent]
# Define the flow pattern
flow = "Diagnosis-Agent -> Treatment-Agent -> Monitoring-Agent, Recovery-Agent"

# Using AgentRearrange class
agent_system = AgentRearrange(agents=agents, flow=flow)
output = agent_system.run("give instruction for diagnosis of concussion then provide treatment plan and then provide monitoring and recovery instructions")
print(output)
