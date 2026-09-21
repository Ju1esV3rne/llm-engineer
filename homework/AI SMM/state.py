from typing import TypedDict


class SMMState(TypedDict):
    user_task: str
    niche: str
    content_plan: str
    posts: str
    editor_feedback: str
    approved: bool
    revision_count: int
    final_content: str