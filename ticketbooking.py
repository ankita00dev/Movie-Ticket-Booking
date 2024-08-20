class movie_ticket:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.user_details = {}
       

    def show_seats(self):
        for i in range(self.row+1):      # step 4 to create pattern 
            for j in range(self.column+1):
                if i == 0:
                    if j == 0:
                        print(" ",end = ' ')
                    else:
                        print(j,end = ' ')
                elif j == 0:
                    print(i,end=' ')
                else:
                    if self.is_seat_booked(i,j):
                        print("B",end=" ")
                    else:
                        print("S",end=' ')
            print()


    def buy_ticket(self):
        row1 = int(input("Enter the row number : "))
        column1 = int(input("Enter the column number : "))

        total_seats = self.row * self.column 
        if total_seats <= 60:
            ticket_price = 10
        else:
            if row1 < (self.row//2):
                ticket_price = 10
            else:
                ticket_price = 8
             

        option = int(input(f"Your opt row is {row1} and column is {column1}, So the price for your ticket is {ticket_price}. If you wish to book the ticket Enter \n1 -> yes \n2 -> No \n")) 
        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = int(input("Enter your age : "))
            phone_number = int(input("Enter your phone number : "))
            seat_number = str(row1) + str(column1) 
            self.user_details[seat_number] = [name,gender,age,phone_number,ticket_price] 
            print("Booked Successfully!")
            
        else:
            print("No Problem, Thank you for connecting with us")

    def statistics(self):
        total_seats = self.row * self.column      #here we have purposely stored the (self.row * self.column) into the total number of seats because it is frequently used 
        no_of_tickets_booked = len(self.user_details)
        percentage_of_tickets_booked = no_of_tickets_booked/total_seats*100

        price_lst = []
        for k,v in self.user_details.items():
            price_lst.append(v[4])

        current_income = sum(price_lst)

        if total_seats <= 60:
            total_income = total_seats * 10    # this 10 is the ticket price
        else:
            front_price = 10
            back_price = 8
            front_seats = (self.row//2)*self.column
            total_income = front_seats * front_price + (total_seats - front_seats) * back_price

        print(f"Number of purchased tickets : {no_of_tickets_booked} \nPercentage of ticket booked : {percentage_of_tickets_booked}\nCurrent income : {current_income} \nTotal incomet : {total_income}")

    def user_info(self):
        row1 = int(input("Enter the row : "))
        column1 = int(input("Enter the column : "))
        seat_number = str(row1) + str(column1) 
        user_data = self.user_details.get(seat_number,None)       #here user_data is the list and user_details is dictionary
        if user_data:
            print(f"Name : {user_data[0]} \nGender : {user_data[1]} \nAge : {user_data[2]} \nTicket Price : {user_data[4]} \nPhone Number  : {user_data[3]}")
        else:
            print(f"No ticket Booked with respect to row : {row1} and column : {column1} ")


    def is_seat_booked(self,rows,columns):
        seat_no = str(rows) +str(columns)
        if seat_no in self.user_details.keys():   # here we are checking whether the seat_no is present inside the dictionary or not it will check whether these values are present in the keys or not 
            return True                           # if it is present it will return true else false 
        return False


    



        


  








#Explanation : Here consider everything as matrix now here we have space in the output (that is column = 0 and row = 0) 
# that is why in the code we first wrote the logic for space that is 
# here i value will also be zero and j value will also be zero that is why we are saying that when i==o and j==0 
# print space (print(" ",end=' '))  
# then in the else part (line number 6) we are printing j value 
 


#OUTPUT -->
#   1 2 3 4 5 6 7 8 
# 1 S S S S S S S S
# 2 S S S S S S S S
# 3 S S S S S S S S
# 4 S S S S S S S S
# 5 S S S S S S S S
# 6 S S S S S S S S
# 7 S S S S S S S S