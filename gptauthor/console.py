import typer

# Global variable to keep track of drafts
Drafts = []


def save_story(final_draft):
    print(f"Final story saved: {final_draft}")
    # Placeholder for storing in vector and relational databases
    print("Story data forwarded to Character Creator App and Screenplay application.")


def display_drafts():
    if not Drafts:
        print("No drafts have been saved yet.")
    else:
        print("--- Saved Drafts ---")
        for index, draft in enumerate(Drafts):
            print(f"Draft {index + 1}:
{draft}
")


def save_draft(draft):
    Drafts.append(draft)
    print("Draft saved successfully!")


def request_user_feedback():
    while True:
        feedback = input("Do you want to request changes? (yes/no): ").lower()
        if feedback == 'yes':
            change_request = input("What changes would you like? ")
            print(f"Processing your request: '{change_request}'...")
        elif feedback == 'no':
            break
        else:
            print("Please answer 'yes' or 'no'.")


def finalize_story():
    final_draft = "Finalized draft of the story: A brave hero embarks on a quest to save the world."  # Simulated final draft
    save_story(final_draft)


def create_new_story():
    print('--- Creating a New Story ---')
    runtime = input("Please choose a runtime: ")
    genre = input("Please choose a genre: ")
    details = input("Please enter detailed descriptions for the story: ")
    prompt_inspiration = request_prompt_inspiration()
    print(f"Prompt Inspiration: {prompt_inspiration}")
    display_initial_draft(runtime, genre, details)
    request_character_details()
    request_location_details()  # New function call for location details
    refine_story()
    add_remove_scenes()
    deepen_character_backstories()


def main(story: str):
    print('Starting gptauthor...')
    prompt_user_for_file()
    finalize_story()  # Finalizing the story at the end

if __name__ == '__main__':
    typer.run(main)