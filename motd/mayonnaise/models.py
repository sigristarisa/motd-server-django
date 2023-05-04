from django.db import models

class Mayonnaise(models.Model):
    name = models.CharField(max_length=20)
    ingredient = models.CharField(max_length=20)
    portion = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Dish(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class Combination(models.Model):
    mayonnaise = models.ForeignKey(Mayonnaise, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return "combination – mayonnaise: {mayonnaise}, dish: {dish}".format(mayonnaise=self.mayonnaise, dish=self.dish)
    
