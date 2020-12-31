#Python Program to Append, Delete and Display Elements of a List Using Classes


# class of name list in that we have appending function to append element and delete function to delete element
class List_:
    def __init__(self,list_):
        self.list_=list_


    def append(self):
        x=input("Enter Number :   ")
        self.list_.append(x)
        print("Appending   :   ",self.list_)

    def delete(self):
        x=input("Delete from list  :   ")
        if x in self.list_:
            self.list_.pop(self.list_.index(x))
            print("Deleting from list :  ",list_)


#List and calling funtions
list_=[1,2,3,4,5]
obj=List_(list_)
obj.append()
obj.delete()

