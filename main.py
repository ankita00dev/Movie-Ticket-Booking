from ticketbooking import movie_ticket      #importing the class
class Main:           #step2
    def excute(self,choice):
        if choice == 1:
            print("*********Show the seats**********")
            movie_ticket_obj.show_seats()       #calling the show_seats method
        if choice == 2:
            print("*********Buy Ticket**********")
            movie_ticket_obj.buy_ticket()
        if choice == 3:
            print("********Statistics**********")
            movie_ticket_obj.statistics()
        if choice == 4:
            print("********Show Booked Tickets User Info**********")
            movie_ticket_obj.user_info()
        if choice == 0:
            print("*************Exit***************")
            exit()
       

if __name__ == "__main__":   #step 1
    row = int(input("Enter the number of rows : "))
    column = int(input("Enter the number of seats in each row : "))

    movie_ticket_obj = movie_ticket(row, column)  

    obj = Main() 
  
    while True:    
        choice = int(input("Enter \n1. show the seats \n2. Buy a ticket \n3. statistics \n4. Show booked Tickets User Info \n0. Exit \n"))

        obj.excute(choice)
    


