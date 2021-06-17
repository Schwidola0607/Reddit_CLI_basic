import os
import questionary
import praw
import click
import textwrap
from colorama import Fore
from dotenv import load_dotenv
load_dotenv()
ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('CLIENT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = ""

def init(subreddit_name: str, pwd: str) -> list:
    """ 
    create a reddit instance, 
    return a list contains 10 hot submissions from 'subreddit_name'
    """
    reddit = praw.Reddit(
        client_id = ID,
        client_secret = SECRET,
        username = REDDIT_USERNAME,
        password = pwd,
        user_agent = "praw_tutorial_04"
    )
    thread_list = []
    hot_threads = reddit.subreddit(subreddit_name).hot(limit = 10)
    for submission in hot_threads:
        thread_list.append(submission)
        
    return thread_list
def create_barrier() -> str:
    """
    create a yellow barrier 
    """
    return Fore.YELLOW + '-' * 110 + Fore.WHITE
def show_score(comment, level: int) -> str:
    """
    display a score, upvotes, and downvotes symbol of a comment
    """
    wrapper = textwrap.TextWrapper(
        initial_indent = "\t" * level + " " * 55, 
        width = 100, 
        subsequent_indent = "\t" * level + " " * 55,
    )
    upvotes = Fore.RED + 'ʌ ' + Fore.WHITE
    downvotes = Fore.BLUE + ' v' + Fore.WHITE
    message = upvotes + str(comment.score) + downvotes
    print(wrapper.fill(message))
     
def show_comment(comment, level: int):
    """
    display a comment according to its position on the comment forest 
    """
    wrapper = textwrap.TextWrapper(
        initial_indent = "\t" * level + Fore.RED + ">>> " + Fore.WHITE, 
        width = 100, 
        subsequent_indent = "\t" * level
    )
    message = comment.body
    print(wrapper.fill(message))
    show_score(comment, level)
    print(create_barrier())

def dfs(comment, level: int):
    """
    traverse a comment tree under a submission
    """
    show_comment(comment, level)
    if level == 5:
        return
    for reply in comment.replies:
        dfs(reply, level + 1)

def show_submission(submission):
    """ 
    display a full reddit submission 
    """
    print(
        Fore.MAGENTA + f'{submission.title}\n' 
        + Fore.WHITE + f'{submission.selftext}\n'
        + create_barrier()
    )
    for comment in submission.comments:
        dfs(comment, 0)

@click.command()
@click.password_option()
@click.option('--subreddit-name', '-sr', help = "What subreddit do you want to surf today")
def main(subreddit_name, password):
    """
    main function
    """
    global REDDIT_PASSWORD
    REDDIT_PASSWORD = password
    list_of_choices = init(subreddit_name, password)
    answer = questionary.select(
        "Choose your post",
        choices = [submission.title for submission in list_of_choices]
    ).ask()
    for submision in list_of_choices:
        if submision.title == answer:
            show_submission(submision)
            break

if __name__ == '__main__':
    main()

def test_init():
    """
    test for init function
    """
    temp_list = init('all', REDDIT_PASSWORD)
    assert len(temp_list) == 10, "There should be 10 hot submissions"
def test_create_barrier():
    """
    test the length of the barrier
    """
    barrier = create_barrier()
    assert len(barrier) != 110, "Barrier too short"
