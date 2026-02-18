def to_do_list(): 
    tasks=[]

    while True:
       print("1.Add Task:")
       print("2.Remove Task:")
       print("3.View task:")
       print("4.Quit")
       wish=input("What do you want:")

       if wish== "1":
         task=input("Enter your task shoud to do:")
         tasks.append(task)
         print("Task successfullly added")
       elif wish=="2":
            task=input("Enter which task you want to remove:")
            if task in tasks: 
                tasks.remove(task)
                print("Task is removed Succed Fully")
            else:
                print("Task not found")   
       elif wish=="3":
            print("Your Task List is:")
            print(tasks)
       elif wish=="4":
            print("Quiting the program")
            break
       else:
            print("Enter valid choice")
to_do_list()   