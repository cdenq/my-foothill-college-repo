""" Module that can instantiate instances of an elementary school class.
Each instance is a ragged row of seats (2D array), with functionality to
edit the roster and assign students to teams. Included in this module is
an array shape generator under determine_seats(), which randomly creates
the roster while respecting the given parameters. - Chris Denq
"""
# Import Statements
import numpy as np
import random  # For randomly generating roster; see determine_seats().

# Global Parameters
max_class_size = 20  # Total number of students allowed in class.
random.seed(42)  # Fixing random seed for reproducibility.
num_of_seats = 30  # Chances to randomly generate a student; see auto_roster().


def evaluate_seats(roster):
    """
    Print out statistics of the randomly generated roster shape.
    """
    check_roster = [len(roster[i]) for i in range(len(roster))]
    print("Classroom Statistics:")
    print(f"{len(roster)} rows with {check_roster} seats in each row.")
    print(f"Arranged for {sum(check_roster)} seats, "
          f"{max_class_size - sum(check_roster)} seats under capacity of "
          f"{max_class_size}.")
    print("--")
    print("Classroom Roster:")
    for i in range(len(roster)):
        for j in range(len(roster[i])):
            print(roster[i][j], end="\t")
        print()


def get_random_seats(num, roster):
    """
    Randomly return NUM valid seats for the roster.
    """
    rows = len(roster)
    cols = [len(roster[i]) for i in range(rows)]
    all_seats = []

    for i in range(num):
        return_row = random.randint(0, rows - 1)
        return_col = random.randint(0, cols[return_row] - 1)
        all_seats.append((return_row, return_col))

    return all_seats


def determine_seats():
    """
    Randomly create shape of ragged array of seats, given parameters.
    """
    # Determining rows.
    min_rows = max_class_size // 6
    max_rows = max_class_size // 4
    row_count = random.randint(min_rows, max_rows)
    roster = np.empty(row_count, dtype=np.ndarray)

    # Determining seats per row.
    min_seats = 1
    max_seats = max_class_size

    reserved = row_count - 1
    remaining_seats = max_class_size - reserved
    seated_seats = 0
    for i in range(row_count):
        seat_count = random.randint(min_seats, max_seats)
        if seat_count > remaining_seats:
            seat_count = remaining_seats
        roster[i] = np.array(["N/A"] * seat_count, dtype=object)
        seated_seats += seat_count
        reserved -= 1
        remaining_seats = max_class_size - reserved - seated_seats

    # Evaluating seats.
    # evaluate_seats(roster)

    # Return result.
    return roster


class ElementarySchoolClass:
    """
    Represent an elementary school classroom with seats and students.
    """
    def __init__(self, classroom_name: str = "Gordon Ramsay Elementary"):
        """  Initialize the seats of the class in 2D array format. """
        self.classroom_name = classroom_name
        self.seats = determine_seats()
        self.teams = []

    def add_student(self, student_name, seat_row, seat_col):
        """  Add a student to a specified seat by (row, col). """
        try:
            self.seats[seat_row][seat_col] = student_name
        except IndexError:
            print(f"Seat ({seat_row}, {seat_col}) doesn't exist.")
        return

    def display_seating_chart(self):
        """  Display all the students in their assigned seats. """
        # Retrieves the max length of any student's name
        longest_name = max([len(max(self.seats[i], key=len))
                            for i in range(len(self.seats))])

        # Prints out in grid format.
        print("\n", end="")
        print(f"{self.classroom_name} Roster:")
        for i in range(len(self.seats)):
            for j in range(len(self.seats[i])):
                print(f"{self.seats[i][j]:<{longest_name}}", end="\t")
            print()
        return

    def assign_teams(self):
        """ Create a new 2D array of all students in their teams. """
        # Given the team-assignment metric, we know that the total number of
        # teams will be equal to the row with the most students.
        team_count = max([len(self.seats[i])
                          for i in range(len(self.seats))])
        team_roster = [[] for _ in range(team_count)]

        # Populating team_roster with students.
        for i in range(len(self.seats)):
            for j in range(len(self.seats[i])):
                if self.seats[i][j] != "N/A":
                    team_roster[j].append(self.seats[i][j])

        # Removing empty teams.
        team_roster = [i for i in team_roster if i]

        # Adding to self.teams.
        self.teams = np.array(team_roster, dtype=object)
        return

    def display_teams(self):
        """  Display all students by their assigned teams. """
        # Retrieves the max length of any student's name
        longest_name = max([len(max(self.teams[i], key=len))
                            for i in range(len(self.teams))])

        # Prints out in grid format.
        print("\n", end="")
        print(f"{self.classroom_name} Roster:")
        for i in range(len(self.teams)):
            print(f"Team {i+1}:", end="\t")
            for j in range(len(self.teams[i])):
                print(f"{self.teams[i][j]:<{longest_name}}", end="\t")
            print()
        return


def teamify(roster):
    """  Complete auto_roster() or manual_roster(); this is a helper
    function that sets up the team for the either choice.
    """
    print("--")
    print("Now assigning students to teams.")
    roster.assign_teams()
    print(f"Done! We have {len(roster.teams)} teams.")
    print("--")
    print(f"Here's our classroom now, divided up into teams.")
    roster.display_teams()
    print("--")
    print(f"Teams are good to go.")
    return


def auto_roster():
    """  Inputs pre-define list of students and seats. """
    print("--")
    print("Randomly generating our classroom's seat roster...")
    my_cls = ElementarySchoolClass()
    print("Here's our classroom's shape--currently empty!")
    my_cls.display_seating_chart()
    print("--")
    print(f"Now generating {num_of_seats} random seats, with repeats.")
    ls_of_seats = get_random_seats(num_of_seats, my_cls.seats)
    for seat in ls_of_seats:
        my_cls.add_student(f"(Kid {seat[0]},{seat[1]})", seat[0], seat[1])
    print(f"Done!")
    print("--")
    print(f"Out of {num_of_seats} random seats, we got {len(set(ls_of_seats))}"
          f" unique seats! Let's add students to these.")
    my_cls.display_seating_chart()
    teamify(my_cls)
    return


def manual_roster():
    """  Allows user to input his/her own student names and seats. """
    print("--")
    print("Randomly generating our classroom's seat roster...")
    my_cls = ElementarySchoolClass()
    while True:
        # Get name.
        name = input("Full name of student?")

        # Get row.
        row = 0
        while True:
            try:
                row = int(input(f"Which row? (1 - {len(my_cls.seats)})"))
                if (row >= 1) and (row <= len(my_cls.seats)):
                    break
                else:
                    print("Please input a valid row number.")
            except ValueError:
                print("Please input a number.")
        row -= 1  # adjusting row to account for index starting at 0

        # Get col.
        col = 0
        while True:
            try:
                col = int(input(f"Which seat number? (1 - "
                                f"{len(my_cls.seats[row])})"))
                if (col >= 1) and (col <= len(my_cls.seats[row])):
                    break
                else:
                    print("Please input a valid seat number.")
            except ValueError:
                print("Please input a number.")
        col -= 1  # adjusting col to account for index starting at 0

        # Adding student.
        print("Adding that student!")
        my_cls.add_student(name, row, col)
        my_cls.display_seating_chart()

        # Checking if user wants to add another student.
        done = False
        while True:
            ans = input("Want to add another student? (y/n)")
            if ans == "y":
                break
            elif ans == "n":
                done = True
                break
            else:
                print("Please put 'y' or 'n' exactly (it's lowercase).")

        if done:
            print("Done adding students!")
            break
    teamify(my_cls)


def main():
    print("Welcome to the school's roster program!")
    while True:
        ans = input("Would you want the program to do it automatically (0) or "
                    "would you like to manually enter names and seats (1)?")
        if ans == "0":
            auto_roster()
            break
        elif ans == "1":
            manual_roster()
            break
        else:
            print("Please enter 0 or 1.")
    print("Thank you for using the roster program!")
    return


if __name__ == "__main__":
    main()


r"""
--- sample run #1 ---
Welcome to the school's roster program!
Would you want the program to do it automatically (0) or would you like to manually enter names and seats (1)?999
Please enter 0 or 1.
Would you want the program to do it automatically (0) or would you like to manually enter names and seats (1)?text
Please enter 0 or 1.
Would you want the program to do it automatically (0) or would you like to manually enter names and seats (1)?
Please enter 0 or 1.
Would you want the program to do it automatically (0) or would you like to manually enter names and seats (1)?0
--
Randomly generating our classroom's seat roster...
Here's our classroom's shape--currently empty!

Gordon Ramsay Elementary Roster:
N/A	N/A	N/A	N/A	
N/A	
N/A	N/A	N/A	N/A	N/A	N/A	N/A	N/A	N/A	
N/A	N/A	N/A	N/A	N/A	
N/A	
--
Now generating 30 random seats, with repeats.
Done!
--
Out of 30 random seats, we got 10 unique seats! Let's add students to these.

Gordon Ramsay Elementary Roster:
(Kid 0,0)	(Kid 0,1)	N/A      	(Kid 0,3)	
(Kid 1,0)	
N/A      	N/A      	(Kid 2,2)	N/A      	N/A      	(Kid 2,5)	N/A      	(Kid 2,7)	N/A      	
(Kid 3,0)	N/A      	(Kid 3,2)	N/A      	N/A      	
(Kid 4,0)	
--
Now assigning students to teams.
Done! We have 6 teams.
--
Here's our classroom now, divided up into teams!

Gordon Ramsay Elementary Roster:
Team 1:	(Kid 0,0)	(Kid 1,0)	(Kid 3,0)	(Kid 4,0)	
Team 2:	(Kid 0,1)	
Team 3:	(Kid 2,2)	(Kid 3,2)	
Team 4:	(Kid 0,3)	
Team 5:	(Kid 2,5)	
Team 6:	(Kid 2,7)	
--
Now leaving auto-roster...
Thank you for using the roster program!

--- sample run #2 ---
Welcome to the school's roster program!
Would you want the program to do it automatically (0) or would you like to manually enter names and seats (1)?1
--
Randomly generating our classroom's seat roster...
Full name of student?John Smith
Which row? (1 - 5)999
Please input a valid row number.
Which row? (1 - 5)text
Please input a number.
Which row? (1 - 5)
Please input a number.
Which row? (1 - 5)3
Which seat number? (1 - 9)999
Please input a valid seat number.
Which seat number? (1 - 9)text
Please input a number.
Which seat number? (1 - 9)
Please input a number.
Which seat number? (1 - 9)3
Adding that student!

Gordon Ramsay Elementary Roster:
N/A       	N/A       	N/A       	N/A       	
N/A       	
N/A       	N/A       	John Smith	N/A       	N/A       	N/A       	N/A       	N/A       	N/A       	
N/A       	N/A       	N/A       	N/A       	N/A       	
N/A       	
Want to add another student? (y/n)999
Please put 'y' or 'n' exactly (it's lowercase).
Want to add another student? (y/n)text
Please put 'y' or 'n' exactly (it's lowercase).
Want to add another student? (y/n)
Please put 'y' or 'n' exactly (it's lowercase).
Want to add another student? (y/n)y
Full name of student?Susan Yam
Which row? (1 - 5)3
Which seat number? (1 - 9)2
Adding that student!

Gordon Ramsay Elementary Roster:
N/A       	N/A       	N/A       	N/A       	
N/A       	
N/A       	Susan Yam 	John Smith	N/A       	N/A       	N/A       	N/A       	N/A       	N/A       	
N/A       	N/A       	N/A       	N/A       	N/A       	
N/A       	
Want to add another student? (y/n)y
Full name of student?Billy Jones
Which row? (1 - 5)1
Which seat number? (1 - 4)4
Adding that student!

Gordon Ramsay Elementary Roster:
N/A        	N/A        	N/A        	Billy Jones	
N/A        	
N/A        	Susan Yam  	John Smith 	N/A        	N/A        	N/A        	N/A        	N/A        	N/A        	
N/A        	N/A        	N/A        	N/A        	N/A        	
N/A        	
Want to add another student? (y/n)y
Full name of student?Phillip Longlastname
Which row? (1 - 5)1
Which seat number? (1 - 4)2
Adding that student!

Gordon Ramsay Elementary Roster:
N/A                 	Phillip Longlastname	N/A                 	Billy Jones         	
N/A                 	
N/A                 	Susan Yam           	John Smith          	N/A                 	N/A                 	N/A                 	N/A                 	N/A                 	N/A                 	
N/A                 	N/A                 	N/A                 	N/A                 	N/A                 	
N/A                 	
Want to add another student? (y/n)y
Full name of student?Felipe Last
Which row? (1 - 5)4
Which seat number? (1 - 5)5
Adding that student!

Gordon Ramsay Elementary Roster:
N/A                 	Phillip Longlastname	N/A                 	Billy Jones         	
N/A                 	
N/A                 	Susan Yam           	John Smith          	N/A                 	N/A                 	N/A                 	N/A                 	N/A                 	N/A                 	
N/A                 	N/A                 	N/A                 	N/A                 	Felipe Last         	
N/A                 	
Want to add another student? (y/n)n
Done adding students!
--
Now assigning students to teams.
Done! We have 4 teams.
--
Here's our classroom now, divided up into teams.

Gordon Ramsay Elementary Roster:
Team 1:	Phillip Longlastname	Susan Yam           	
Team 2:	John Smith          	
Team 3:	Billy Jones         	
Team 4:	Felipe Last         	
--
Teams are good to go.
Thank you for using the roster program!
"""