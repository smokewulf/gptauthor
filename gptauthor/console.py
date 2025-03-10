import typer

# Global variable to keep track of drafts
Drafts = []


def save_story(final_draft):
    print(f"Final story saved: {final_draft}")
    print("Story data forwarded to Character Creator App and Screenplay application.")


def display_drafts():
    if not Drafts:
        print("No drafts have been saved yet.")
    else:
        print("--- Saved Drafts ---")
        for index, draft in enumerate(Drafts):
            print(f"Draft {index + 1}: {draft}")


def save_draft(draft):
    Drafts.append(draft)
    print("Draft saved successfully!")


def request_character_details():
    number_of_characters = int(input("How many characters do you want to create? "))
    for i in range(number_of_characters):
        character_name = input("Enter the character's name: ")
        display_character_description(character_name)


def request_location_details():
    number_of_locations = int(input("How many locations do you want to create? "))
    for i in range(number_of_locations):
        location_name = input("Enter the location name: ")
        display_location_description(location_name)


def display_character_description(character_name):                                                                                                                                          
       print(f'--- Character Description for {character_name} ---')                                                                                                                            
       appearance = input("Enter character appearance details: ")                                                                                                                              
       attire = input("Enter character attire details: ")                                                                                                                                      
       personality = input("Enter character personality details: ")                                                                                                                            
       environment = input("Enter character's environment details: ")                                                                                                                          
       print(f"Character '{character_name}':\n Appearance: {appearance}\n Attire: {attire}\n Personality: {personality}\n Environment: {environment}")                                         
       dialogue_enhancement(character_name) 


def dialogue_enhancement(character_name):
    dialogue = input(f"Enter the dialogue for {character_name}: ")
    emotions = input(f"Enter emotional states and facial expressions for {character_name} (format: [happy, smiling softly]): ")
    ssml_dialogue = f'<prosody rate="medium" pitch="medium">({character_name}): [{{emotions}}] {{dialogue}}</prosody>'
    print(f"SSML Annotated Dialogue for {character_name}: {ssml_dialogue}")


def prompt_user_for_file():
    upload = input("Do you want to upload a file to work on? (yes/no): ").lower()
    if upload == 'yes':
        print("File upload functionality not implemented yet.")
    elif upload == 'no':
        create_new_story()


def create_new_story():
    print('--- Creating a New Story ---')
    runtime = input("Please choose a runtime: ")
    genre = input("Please choose a genre: ")
    details = input("Please enter detailed descriptions for the story: ")
    prompt_inspiration = request_prompt_inspiration()
    print(f"Prompt Inspiration: {prompt_inspiration}")
    display_initial_draft(runtime, genre, details)
    request_character_details()  # Call for character details
    request_location_details()  # Call for location details
    refine_story()
    add_remove_scenes()
    deepen_character_backstories()


def main(story: str = typer.Argument(...)):                           
       print('Starting gptauthor...')                                    
       prompt_user_for_file()                                            
       finalize_story()  # Finalizing the story at the end

if __name__ == '__main__':
    typer.run(main)
