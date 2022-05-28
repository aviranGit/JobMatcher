from django.test import TestCase
from jobmatcher.models import Skill, Candidate, Job

class SkillTestCase(TestCase):
    def setUp(self):
        Skill.objects.create(name="Django")
        Skill.objects.create(name="React")
    def check_existence(self):
        """ Testing that each name in skills is unique"""
        self.assertTrue(Skill.objects.filter(name="Django"), True)
        self.assertTrue(Skill.objects.filter(name="Django"), True)
        self.assertTrue(Skill.objects.create(name="MongoDB"), True)

