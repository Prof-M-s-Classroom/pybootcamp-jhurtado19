from imghdr import tests



class CrewMember:

    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience  # Years of experience

    def __str__(self):
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"


"""Crew_List = []
Crew1 = CrewMember("Steve", "crew", 1)
Crew2 = CrewMember("Crew2", "crew", 2)
Crew3 = CrewMember("Crew3", "crew", 3)
Crew_List.append(Crew1)
Crew_List.append(Crew2)
Crew_List.append(Crew3)

New_Crew_List = [member for member in Crew_List if member.name != "Steve"] # list comprehension, for each object in the list, check each object.atr for some condition 


for crew in New_Crew_List:
    print(crew)
"""




class CrewRoster:

    def __init__(self):
        self.crew = []  # List of CrewMember objects

    def add_member(self, name, role, experience):
        """Creates a new crew member and adds to roster."""
        self.crew.append(CrewMember(name, role, experience)) # this method uses append method to add class object CrewMember to CrewRoster list

    def remove_member(self, name):
        """Removes a crew member by name."""
        self.crew = [member for member in self.crew if member.name != name] #  this method uses list comprehension to make a new list after filtering the name out of the old list
        print(f"Removed {name}") # added for output clarity

    def list_crew(self):
        """Prints all crew members."""
        for crew in self.crew: # iterates through all objects in the list and prints them
            print(crew)



# === TEST CODE ===

roster=CrewRoster() #Empty Crew roster created

    # TODO: Uncomment and implement methods
roster.add_member("Alice", "Engineer", 5)  # add Alice
roster.add_member("Bob", "Pilot", 10)      # add Bob
roster.list_crew()                                               # print crew list

roster.remove_member("Alice")              # remove Alice
roster.list_crew()                         # reprint crew list

