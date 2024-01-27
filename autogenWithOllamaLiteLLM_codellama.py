import autogen

config_list_codellama = [
    {
        'base_url': "http://0.0.0.0:10906",  # litellm --model ollama/codellama
        'api_key': "NULL"
    }
]

llm_config_codellama={
    "config_list": config_list_codellama,
}

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_codellama
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_codellama,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task="""
Write a python script to output numbers 1 to 100 and then the user_proxy agent should run the script
"""

groupchat = autogen.GroupChat(agents=[user_proxy, coder], messages=[], max_round=12)
coder = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_codellama)
user_proxy.initiate_chat(coder, message=task)