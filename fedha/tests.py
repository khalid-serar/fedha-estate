from fedha.models import Business, Neighbourhood, Profile
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
# Set up method
    def setUp(self):
        self.user = User(username="khalid", password="jay123")
        self.user.save()
        self.neighbourhood= Neighbourhood(neighbourhood_name = "karen", neighbourhood_location= "Nairobi", admin = self.user, neighbourhood_description='hood of hoods')
        self.neighbourhood.save()
        self.profile = Profile(bio='my hood',email='email@gmail.com', id_number=37515889,user = self.user, neighbourhood = self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

    def test_get_profile(self):
        self.profile.save_profile()
        

    def test_delete_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)
    
class NeighbourhoodTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='jay')
        self.user.save()
        self.neighbourhood = Neighbourhood(neighbourhood_name='Karen',neighbourhood_location='Nairobi',neighbourhood_description="hood of hoods",neighbourhood_photo='photo.url',admin = self.user)
        self.neighbourhood.create_neighbourhood()


    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_create_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

class BusinessTestClass(TestCase):
    # Set up method

    def setUp(self):

        self.user = User(username="kay", password="pass123")
        self.user.save()
        self.neighbourhood = Neighbourhood(neighbourhood_name="route4", neighbourhood_location="Eastside", admin=self.user, neighbourhood_description='mtaa yetu')
        self.neighbourhood.save()
        self.business = Business(business_name='my hood', business_email='email@g.com',business_description='my business')
     

   