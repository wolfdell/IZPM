# Imports for the class
from menus.menu import Menu
from util.flush import flush_screen 

class Comment():
    def __init__(self):
        self.username = None
        self.comment = None

    def form_comment():
        return f"[{self.username}] коментира: {self.comment}"

class CommentSectionMenu(Menu):

    # Self initialization
    def __init__(self):

        # Holder for the translation file
        self.translation_file = ""

    # Create the menu instance
    def spawn(self):
        
        # Clear the screen instance
        flush_screen()

        # Print the menu header
        print('\x1b[6;30;42m' + ' Меню за добавяне на коментари към превода ' + '\x1b[0m')
        print("За да добавиш нов коментар, изпълни командата \x1b[0;36;40mкоментирай\x1b[0m")
        print("За да спреш менюто, изпълни командата \x1b[0;36;40mq\x1b[0m")

        # Start the commenting instance
        with open(self.translation_file, "a") as f:
            
            # Print the comment header into the output file
            print("\n---------- КОМЕНТАРИ ----------", file=f)
            
            # Start the instance loop
            while True:

                # Get the input command
                command = input("> ")
                
                # Check for the quit command 
                if command == "q": break

                # Check for the create comment command
                if command == "коментирай": 
                    
                    # Create the comment
                    comment = self.create_comment()

                    # Print the comment into the file
                    print(comment, file=f)

                    # Show if everything is ok
                    print("\x1b[0;36;40m[+]\x1b[0m Коментара беше добавен успешно!\n")


    # Method for creating the comment instance
    def create_comment():
        
        # Create the comment instance
        current_comment = Comment()

        # Fill the instance info
        current_comment.username = input("Име на коментиращия: ")
        current_comment.comment = actual_comment = input("Коментар: ")

        # Return the formed comment
        return current_comment.form_comment()
