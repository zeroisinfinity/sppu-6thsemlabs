# ============================================================
# QUESTION:
# Implement Expert System for Help Desk Management.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Expert System simulates decision-making of a human expert.
#
# This program:
#
# - Stores problems
# - Matches user input
# - Provides solution
#
# It uses:
# - Dictionary
# - Condition checking
# - Loop
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# User Input:
# Printer not working
#
# Output:
# Check printer connection.
#
# User Input:
# exit
#
# Output:
# Goodbye
# ============================================================


# ======================
# EXPERT SYSTEM PROGRAM
# ======================

problem_dict = {

    "Printer not working":
    "Check printer power and connection",

    "Can't log in":
    "Check username and password",

    "Software not installing":
    "Check system requirements",

    "Internet connection not working":
    "Restart modem or router",

    "Email not sending":
    "Check email settings"

}


def handle_request(user_input):

    if user_input.lower() == "exit":

        return "Goodbye!"

    elif user_input in problem_dict:

        return problem_dict[user_input]

    else:

        return "Problem not found."


while True:

    user_input = input(
        "Enter problem (type exit to quit): ")

    response = handle_request(user_input)

    print(response)

    if user_input.lower() == "exit":

        break