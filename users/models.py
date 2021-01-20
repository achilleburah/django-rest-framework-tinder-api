from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.gis.geos import Point

from users.managers import CustomUserManager


paris_location = Point(float(2.351462), float(48.856697))


GENRE_CHOICES =(
                ("M", "Male"),
                ("F", "Female"),
                ("U", "Undefined"),
                )

def user_directory_path(instance, filename):
	return 'images/{0}/'.format(filename)



class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	genre = models.CharField(choices=GENRE_CHOICES, max_length=10)
	bio = models.TextField(max_length=500)
	picture = models.ImageField(upload_to=user_directory_path, default='images/default.jpg')
	location = models.PointField(max_length=40, null=True, default=paris_location, blank=True)


	# Other required Fields
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'genre', 'bio', 'location']

	objects = CustomUserManager()


	def __str__(self):
		return self.first_name + " " + self.last_name


	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
				return True





class MatchRequest(models.Model):

	sender = models.ForeignKey('users.CustomUser', related_name='request_asker', on_delete=models.CASCADE, null=True)
	receiver = models.ForeignKey('users.CustomUser', related_name='request_receiver', on_delete=models.CASCADE, null=True)


	def __str__(self):
		return str(self.sender) + " x " + str(self.receiver)

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


class MatchedUser(models.Model):

	user1 = models.IntegerField(null = True)
	user2 = models.IntegerField(null = True)

	def __str__(self):
		return str(self.user1) + " x " + str(self.user2)

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True




