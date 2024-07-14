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
                          A student fell when playing basket ball.
                          he has a headache, feels nausea and dizzy.
                          He is also sensitive to light and sound and 
                          feel sluggish.
                          Do this step by step, 
                          give detailed step by step instruction to diagnose
                          as to whether the student have concussion and how 
                          severe it is. 
                          Then provide detailed, step by step treatment plan, 
                          and give detailed, step by step procedures on what 
                          to monitor each day and how to manage recovery
                          in this student's 
                          daily life and school activities. 
                          """)
print(output)
