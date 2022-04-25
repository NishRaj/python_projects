class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, group):
        self_member_list = self.get_members()
        passed_member_list = group.get_members()
        self_member_list.extend(passed_member_list)
        merged_group = Group("Merged Group",sorted(self_member_list))
        return merged_group

group6 = Group("group6", ["A", "D"])
group7 = Group("group7", ["B", "C"])
merged_group = group6.merge(group7)
print(merged_group.get_members())