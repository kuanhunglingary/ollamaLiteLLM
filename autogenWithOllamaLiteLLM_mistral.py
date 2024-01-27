import autogen

config_list_mistral = [
    {
        'base_url': "http://0.0.0.0:8000",  # itellm --model ollama/mistral
        'api_key': "NULL"
    }
]

llm_config_mistral={
    "config_list": config_list_mistral,
}

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config_mistral
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task="""
Tell me a ghost story
"""

groupchat = autogen.GroupChat(agents=[user_proxy, assistant], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_mistral)
user_proxy.initiate_chat(manager, message=task)