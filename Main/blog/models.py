from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=50)
	class Meta:
		verbose_name="Category"
		verbose_name_plural="Categories"
	def __str__(self):
		return self.name

class Tag(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Post(models.Model):
	#Id=models.IntegerField(unique=True)
	title=models.CharField(max_length=100)
	date=models.DateField()
	content=models.TextField()
	category=models.ForeignKey(Category, on_delete=models.CASCADE )
	tags=models.ManyToManyField(Tag)
	author=models.CharField(
					verbose_name="Author Name",
					help_text="Enter Author Name",
					max_length=30,
					blank=True,
					null=True
				)
	def __str__(self):
		return self.title
