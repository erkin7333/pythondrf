from django.db import models




# Kitob Kategoriyalari
class BookCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()



# Kitoblar
class Books(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Kutupxona Foydalanuvchilari
class LibUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Ijaraga berilgan Kitoblar modeli
class RentBook(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentData = models.DateTimeField(auto_now_add=True)
    returnDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} {self.user} {self.rentData} {self.returnDate}"
