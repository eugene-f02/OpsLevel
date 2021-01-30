
# I'm using LinkedList as the main data structure

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, node):
        self.length += 1
        if self.head == None:
            self.head = node
            return 
        if self.head.priority >= node.priority:
            node.next=self.head
            self.head = node
            for i in range(1, self.head.next.priority - self.head.priority):
                missing_priorities.add(i + self.head.priority)
        else:
            copy_head=self.head
            while(copy_head != None and copy_head.priority < node.priority):
                previous_node = copy_head
                copy_head=copy_head.next
            if (copy_head != None):
                copy_head.data, node.data = node.data, copy_head.data
                copy_head.priority, node.priority = node.priority, copy_head.priority
                node.next = copy_head.next
                copy_head.next = node
                if copy_head.priority in missing_priorities:
                    missing_priorities.remove(copy_head.priority)
            else:
                previous_node.next = node
                for i in range(1, node.priority - previous_node.priority):
                    missing_priorities.add(i + previous_node.priority)
        
    def remove(self, num):
        self.length -= 1
        copy_head=self.head
        counter = 1
        while counter != num:
            previous_node = copy_head
            copy_head=copy_head.next
            counter+=1
        if counter == 1:
            if self.length == 0:
                self.head = None
                return
            for i in range(1, self.head.next.priority - self.head.priority):
                missing_priorities.remove(i + self.head.priority)
            self.head = self.head.next
        elif copy_head.next != None:
            previous_node.next = copy_head.next
            if previous_node.priority != copy_head.priority and copy_head.next.priority != copy_head.priority:
                missing_priorities.add(copy_head.priority)
        else:
            for i in range(1, copy_head.priority - previous_node.priority):
                missing_priorities.remove(i + previous_node.priority)
            previous_node.next = None

    def __repr__(self):
        node = self.head
        nodes = []
        counter = 1
        while node is not None:
            nodes.append(str(counter)+ ". "+node.data + " ("+str(node.priority)+")")
            node = node.next
            counter+=1
        return "\n"+"\n".join(nodes)

todo_list = LinkedList() 
missing_priorities=set()

def main():
    print("Welcome to the simple TODO list application!")
    while(True):
        print("\nPlease, select one of the following options by entering the corresponding number:\n   ")
        print("1. List all of my current items to do.")
        print("2. Create a new item.")
        print("3. Delete existing item.")
        print("4. Exit.")
        option = get_option()
        if option == 1:
            print(todo_list)
        elif option == 2:
            create_new_item()
        elif option == 3:
            delete_item()
        elif option == 4:
            exit()

def get_option():
    while(True):
        option = input(">>> ")
        if option in {"1","2","3","4"}:
            return int(option)
        print("Invalid option. The only valid options are 1, 2, 3, or 4. Try again.")

def create_new_item():
    print("\nPlease, specify the name of the item:\n")
    item = input(">>> ")
    print("\nPlease, specify the priority of the item:\n")
    if missing_priorities !=set():
        sorted_missing_prior = list(missing_priorities)
        sorted_missing_prior.sort()
        print("Priorities " + ', '.join(str(p) for p in sorted_missing_prior) + " are missing.")
    priority = get_priority()
    todo_list.insert(Node(item,priority))
    print("\n Item '" + item + "' has been successfully created and added to the list!")

def get_priority():
    while(True):
        priority = input(">>> ")
        try:
            priority = int(priority)
        except:
            print("Invalid priority! Please enter a positive integer")
            continue
        if priority <= 0:
            print("Invalid priority! Please enter a positive integer")
            continue
        return priority

def add_item_to_the_list(item):
    for i in todo_list:
        if i[0] <= item[0]:
            continue

def delete_item():
    if todo_list.length == 0:
        print("\nThe TODO list is empty\n")
        return
    print("\nPlease, specify the number of the item you want to delete:\n")
    number = get_number()
    todo_list.remove(number)
    print("\n Item '" + str(number) + "' has been successfully deleted from the list!")

def get_number():
    while(True):
        number = input(">>> ")
        try:
            number = int(number)
        except:
            print("Invalid number! Please, enter a positive integer")
            continue
        if number <= 0:
            print("Invalid number! Please, enter a positive integer")
            continue
        if number > todo_list.length:
            print("Invalid input! There are only "+str(todo_list.length)+" item(s) in the list")
            continue
        return number

if __name__ == "__main__":
    main()

