class FoodItem:
    def __init__(self,i,name,category,price):
        self.item_id = i
        self.item_name = name
        self.item_category = category
        self.item_price = price

    def provideDiscount(self,p):
        if p>0:
            self.item_price-=(self.item_price*p/100)

class Restaurant:
    def __init__(self, name, list):
        self.restaurant_name = name
        self.fooditem_list = list

    def retrieveUpdatedPrice(self,i,p):
        for food in self.fooditem_list:
            if(food.item_id == i):
                food.provideDiscount(p)
                return food
        return None

if __name__=='__main__':
    number=int(input())
    fooditem_list=[]
    for _ in range(number):
        item_id=int(input())
        item_name=input()
        item_category=input()
        item_price=int(input())
        fooditem_list.append(FoodItem(item_id,item_name,item_category,item_price))
    Rest=Restaurant("name",fooditem_list)
    item_id=int(input())
    percentage=int(input())
    result=Rest.retrieveUpdatedPrice(item_id,percentage)
    if result==None:
        print("No Food item exists which matches the search criteria")
    else:
        print(result.item_name,result.item_price,sep=" - ")
