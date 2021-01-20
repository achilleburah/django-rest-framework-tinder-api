from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):

  def create_user(self, email, first_name, last_name, genre, bio, location, password=None):

    if not email:
      raise ValueError('Users must have an email address')
    if not first_name:
      raise ValueError('Users must have a first_name')
    if not last_name:
      raise ValueError('Users must have a last_name')
    if not genre:
      raise ValueError('Users must have a genre')
    if not bio:
      raise ValueError('Users must have a bio')

    user = self.model(
      email=self.normalize_email(email),
      first_name=first_name,
      last_name=last_name,
      genre=genre,
      bio=bio,
      location=location,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user


  def create_superuser(self, email, first_name, last_name, genre, password, location, bio):
    user = self.create_user(
      email=self.normalize_email(email),
      password=password,
      first_name=first_name,
      last_name=last_name,
      genre=genre,
      bio=bio,
      location=location,
    )
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


