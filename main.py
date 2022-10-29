from Tweets_generator.project_functions import click_funcs
from tkinter import *


unique_words_dict = {}
root = Tk()
root.title("Tweets Generator")

# information message and input field

opening_label = Label(root, text="Under here enter the path for which you want to open and use or browse for it: ")
user_input = Entry(root, width=50)


opening_label.grid(row=0, column=0, columnspan=2)
user_input.grid(row=1, column=0)

# The field where a single sentence will be generated
sentence_frame = LabelFrame(root, text="The tweet is: ", padx=5, pady=5)
sentence_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# information message and buttons for submitting a path, browsing for a file, using the default path, generate a
# sentence and input field for requesting a few tweets
info_label = Label(root, text="Press the Generate button to create a single sentence or enter a number\
 to create multiple: ")
browse_button = Button(root, text="Browse", command=lambda: click_funcs.browse(user_input))
submit_button = Button(root, text="Submit", command=lambda: click_funcs.submit_click(user_input, unique_words_dict,
                                                                                     generate_button, multi_input))
default_button = Button(root, text="Default path", command=lambda: click_funcs.default_click(unique_words_dict,
                                                                                             generate_button, multi_input))
generate_button = Button(root, text="Generate", state=DISABLED, command=lambda: click_funcs.generate_click(multi_input,
                                                                                                           unique_words_dict, sentence_frame,
                                                                                                           root))
multi_input = Entry(root, width=10, state=DISABLED)


browse_button.grid(row=1, column=1)
submit_button.grid(row=2, column=0, pady=10)
default_button.grid(row=2, column=1)
info_label.grid(row=3, column=0, columnspan=2)
generate_button.grid(row=4, column=0)
multi_input.grid(row=4, column=1)


root.mainloop()
