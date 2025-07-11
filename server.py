from mcp.server.fastmcp import FastMCP
from manager import Manager
from typing import Any

mcp = FastMCP("FacebookMCP")
manager = Manager()

@mcp.tool()
def post_to_facebook(message: str) -> dict[str, Any]:
    """Create a new Facebook Page post with a text message.
    Input: message (str)
    Output: dict with post ID and creation status
    """
    return manager.post_to_facebook(message)

@mcp.tool()
def reply_to_comment(post_id: str, comment_id: str, message: str) -> dict[str, Any]:
    """Reply to a specific comment on a Facebook post.
    Input: post_id (str), comment_id (str), message (str)
    Output: dict with reply creation status
    """
    return manager.reply_to_comment(post_id, comment_id, message)

@mcp.tool()
def get_page_posts() -> dict[str, Any]:
    """Fetch the most recent posts on the Page.
    Input: None
    Output: dict with list of post objects and metadata
    """
    return manager.get_page_posts()

@mcp.tool()
def get_post_comments(post_id: str) -> dict[str, Any]:
    """Retrieve all comments for a given post.
    Input: post_id (str)
    Output: dict with comment objects
    """
    return manager.get_post_comments(post_id)

@mcp.tool()
def delete_post(post_id: str) -> dict[str, Any]:
    """Delete a specific post from the Facebook Page.
    Input: post_id (str)
    Output: dict with deletion result
    """
    return manager.delete_post(post_id)

@mcp.tool()
def delete_comment(comment_id: str) -> dict[str, Any]:
    """Delete a specific comment from the Page.
    Input: comment_id (str)
    Output: dict with deletion result
    """
    return manager.delete_comment(comment_id)


@mcp.tool()
def hide_comment(comment_id: str) -> dict[str, Any]:
    """Hide a comment from public view."""
    return manager.hide_comment(comment_id)


@mcp.tool()
def unhide_comment(comment_id: str) -> dict[str, Any]:
    """Unhide a previously hidden comment."""
    return manager.unhide_comment(comment_id)

@mcp.tool()
def delete_comment_from_post(post_id: str, comment_id: str) -> dict[str, Any]:
    """Alias to delete a comment on a post.
    Input: post_id (str), comment_id (str)
    Output: dict with deletion result
    """
    return manager.delete_comment_from_post(post_id, comment_id)

@mcp.tool()
def filter_negative_comments(comments: dict[str, Any]) -> list[dict[str, Any]]:
    """Filter comments for basic negative sentiment.
    Input: comments (dict)
    Output: list of flagged negative comments
    """
    return manager.filter_negative_comments(comments)

@mcp.tool()
def get_number_of_comments(post_id: str) -> int:
    """Count the number of comments on a given post.
    Input: post_id (str)
    Output: integer count of comments
    """
    return manager.get_number_of_comments(post_id)

@mcp.tool()
def get_number_of_likes(post_id: str) -> int:
    """Return the number of likes on a post.
    Input: post_id (str)
    Output: integer count of likes
    """
    return manager.get_number_of_likes(post_id)

@mcp.tool()
def get_post_insights(post_id: str) -> dict[str, Any]:
    """Fetch all insights metrics (impressions, reactions, clicks, etc).
    Input: post_id (str)
    Output: dict with multiple metrics and their values
    """
    return manager.get_post_insights(post_id)

@mcp.tool()
def get_post_impressions(post_id: str) -> dict[str, Any]:
    """Fetch total impressions of a post.
    Input: post_id (str)
    Output: dict with total impression count
    """
    return manager.get_post_impressions(post_id)

@mcp.tool()
def get_post_impressions_unique(post_id: str) -> dict[str, Any]:
    """Fetch unique impressions of a post.
    Input: post_id (str)
    Output: dict with unique impression count
    """
    return manager.get_post_impressions_unique(post_id)

@mcp.tool()
def get_post_impressions_paid(post_id: str) -> dict[str, Any]:
    """Fetch paid impressions of a post.
    Input: post_id (str)
    Output: dict with paid impression count
    """
    return manager.get_post_impressions_paid(post_id)

@mcp.tool()
def get_post_impressions_organic(post_id: str) -> dict[str, Any]:
    """Fetch organic impressions of a post.
    Input: post_id (str)
    Output: dict with organic impression count
    """
    return manager.get_post_impressions_organic(post_id)

@mcp.tool()
def get_post_engaged_users(post_id: str) -> dict[str, Any]:
    """Fetch number of engaged users.
    Input: post_id (str)
    Output: dict with engagement count
    """
    return manager.get_post_engaged_users(post_id)

@mcp.tool()
def get_post_clicks(post_id: str) -> dict[str, Any]:
    """Fetch number of post clicks.
    Input: post_id (str)
    Output: dict with click count
    """
    return manager.get_post_clicks(post_id)

@mcp.tool()
def get_post_reactions_like_total(post_id: str) -> dict[str, Any]:
    """Fetch number of 'Like' reactions.
    Input: post_id (str)
    Output: dict with like count
    """
    return manager.get_post_reactions_like_total(post_id)

@mcp.tool()
def get_post_reactions_love_total(post_id: str) -> dict[str, Any]:
    """Fetch number of 'Love' reactions.
    Input: post_id (str)
    Output: dict with love count
    """
    return manager.get_post_reactions_love_total(post_id)

@mcp.tool()
def get_post_reactions_wow_total(post_id: str) -> dict[str, Any]:
    """Fetch number of 'Wow' reactions.
    Input: post_id (str)
    Output: dict with wow count
    """
    return manager.get_post_reactions_wow_total(post_id)

@mcp.tool()
def get_post_reactions_haha_total(post_id: str) -> dict[str, Any]:
    """Fetch number of 'Haha' reactions.
    Input: post_id (str)
    Output: dict with haha count
    """
    return manager.get_post_reactions_haha_total(post_id)

@mcp.tool()
def get_post_reactions_sorry_total(post_id: str) -> dict[str, Any]:
    """Fetch number of 'Sorry' reactions.
    Input: post_id (str)
    Output: dict with sorry count
    """
    return manager.get_post_reactions_sorry_total(post_id)

@mcp.tool()
def get_post_reactions_anger_total(post_id: str) -> dict[str, Any]:
    """Fetch number of 'Anger' reactions.
    Input: post_id (str)
    Output: dict with anger count
    """
    return manager.get_post_reactions_anger_total(post_id)

@mcp.tool()
def get_post_top_commenters(post_id: str) -> list[dict[str, Any]]:
    """Get the top commenters on a post.
    Input: post_id (str)
    Output: list of user IDs with comment counts
    """
    return manager.get_post_top_commenters(post_id)

@mcp.tool()
def post_image_to_facebook(image_url: str, caption: str) -> dict[str, Any]:
    """Post an image with a caption to the Facebook page.
    Input: image_url (str), caption (str)
    Output: dict of post result
    """
    return manager.post_image_to_facebook(image_url, caption)

@mcp.tool()
def send_dm_to_user(user_id: str, message: str) -> dict[str, Any]:
    """Send a direct message to a user.
    Input: user_id (str), message (str)
    Output: dict of result from Messenger API
    """
    return manager.send_dm_to_user(user_id, message)

@mcp.tool()
def update_post(post_id: str, new_message: str) -> dict[str, Any]:
    """Updates an existing post's message.
    Input: post_id (str), new_message (str)
    Output: dict of update result
    """
    return manager.update_post(post_id, new_message)
@mcp.tool()
def schedule_post(message: str, publish_time: int) -> dict[str, Any]:
    """Schedule a new post for future publishing.
    Input: message (str), publish_time (Unix timestamp)
    Output: dict with scheduled post info
    """
    return manager.schedule_post(message, publish_time)

@mcp.tool()
def get_page_fan_count() -> int:
    """Get the Page's total fan/like count.
    Input: None
    Output: integer fan count
    """
    return manager.get_page_fan_count()

@mcp.tool()
def get_post_share_count(post_id: str) -> int:
    """Get the number of shares for a post.
    Input: post_id (str)
    Output: integer share count
    """
    return manager.get_post_share_count(post_id)


@mcp.tool()
def get_post_reactions_breakdown(post_id: str) -> dict[str, Any]:
    """Get counts for all reaction types on a post."""
    return manager.get_post_reactions_breakdown(post_id)


@mcp.tool()
def bulk_delete_comments(comment_ids: list[str]) -> list[dict[str, Any]]:
    """Delete multiple comments by ID."""
    return manager.bulk_delete_comments(comment_ids)


@mcp.tool()
def bulk_hide_comments(comment_ids: list[str]) -> list[dict[str, Any]]:
    """Hide multiple comments by ID."""
    return manager.bulk_hide_comments(comment_ids)

