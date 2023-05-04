from django.db import models

class Mayonnaise(models.Model):
    id = models.AutoField()
    name = models.CharField()
    ingredient = models.CharField()
    portion = models.CharField()

    def __str__(self):
        return self.name
    
    
class Dish(models.Model):
    id = models.AutoField()
    name = models.CharField()
    image = models.CharField()

    def __str__(self):
        return self.name
    

class Combination(models.Model):
    id = models.AutoField()
    mayonnaise = models.ForeignKey(Mayonnaise, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return "combination – mayonnaise: {mayonnaise}, dish: {dish}".format(mayonnaise=self.mayonnaise, dish=self.dish)