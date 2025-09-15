import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool
)

from crewai_tools import CrewaiEnterpriseTools


@CrewBase
class SocialCapitalAgentCrew:
    """SocialCapitalAgent crew"""

    
    @agent
    def network_analyzer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["network_analyzer"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def meeting_coordinator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["meeting_coordinator"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def event_scout(self) -> Agent:
        
        return Agent(
            config=self.agents_config["event_scout"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def meeting_coordinator_2(self) -> Agent:
        
        return Agent(
            config=self.agents_config["meeting_coordinator_2"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def strategic_connection_advisor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["strategic_connection_advisor"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def conversation_starter_generator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["conversation_starter_generator"],
            
            
            tools=[
				ScrapeWebsiteTool(website_url="https://conversationstartersworld.com/250-conversation-starters/")
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def map_professional_network(self) -> Task:
        return Task(
            config=self.tasks_config["map_professional_network"],
            markdown=False,
        )
    
    @task
    def identify_networking_events(self) -> Task:
        return Task(
            config=self.tasks_config["identify_networking_events"],
            markdown=False,
        )
    
    @task
    def recommend_priority_connection(self) -> Task:
        return Task(
            config=self.tasks_config["recommend_priority_connection"],
            markdown=False,
        )
    
    @task
    def coordinate_initial_outreach(self) -> Task:
        return Task(
            config=self.tasks_config["coordinate_initial_outreach"],
            markdown=False,
        )
    
    @task
    def finalize_meeting_coordination(self) -> Task:
        return Task(
            config=self.tasks_config["finalize_meeting_coordination"],
            markdown=False,
        )
    
    @task
    def generate_meeting_conversation_starters(self) -> Task:
        return Task(
            config=self.tasks_config["generate_meeting_conversation_starters"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the SocialCapitalAgent crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
