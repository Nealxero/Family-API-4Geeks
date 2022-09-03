"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age":33,
                "lucky_numbers":[7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age":35,
                "lucky_numbers":[10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age":5,
                "lucky_numbers":[1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        print(member)        
        newMember={
            "id":member["id"],
            "first_name":member["first_name"],
            "last_name": self.last_name,
            "age":member["age"],
            "lucky_numbers":member["lucky_numbers"]
        }
        self._members.append(newMember)
        return newMember["id"]
        
    def update_member(self, id, member):
        newMember={
            "id":id,
            "first_name":member["first_name"],
            "last_name": self.last_name,
            "age":member["age"],
            "lucky_numbers":member["lucky_numbers"]
        }
        for i in range(0,self._members.__len__()):
            mem=self._members.__getitem__(i)
            print(mem["id"])
            if (int(mem["id"])==int(id)):
                self._members[i]=newMember
                return self._members[i]
        return False

    def delete_member(self, id):
        # fill this method and update the return
        for i in range(0,self._members.__len__()):
            mem=self._members.__getitem__(i)
            print(mem["id"])
            if (int(mem["id"])==int(id)):
                self._members.pop(i)
                return True                
        return False
        pass

    def get_member(self, id):
        # fill this method and update the return
        for i in range(0,self._members.__len__()):
            mem=self._members.__getitem__(i)
            if (int(mem["id"])==int(id)):
                return self._members[i]
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members