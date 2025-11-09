from typing import Any

import requests

from task.tools.base import BaseTool


class WebSearchTool(BaseTool):

    def __init__(self, open_ai_api_key: str):
        self.__api_key = f"Bearer {open_ai_api_key}"
        self.__endpoint = "https://api.openai.com/v1/chat/completions"

    # Sample of tool config:
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "web_search_tool",
    #         "description": "Tool for WEB searching.",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "request": {
    #                     "type": "string",
    #                     "description": "The search query or question to search for on the web"
    #                 }
    #             },
    #             "required": [
    #                 "request"
    #             ]
    #         }
    #     }
    # }

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `web_search_tool`
        raise NotImplementedError()

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        raise NotImplementedError()

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO: Provide tool params Schema (it applies `request` string to search by)
        raise NotImplementedError()

    def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat
        # 1. Make POST call to `gpt-4o-search-preview` with request argument
        # 4. Check if response status is 200 and if yes then return message content, otherwise return `f"Error: {response.status_code} {response.text}"`
        raise NotImplementedError()
