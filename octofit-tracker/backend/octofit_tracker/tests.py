from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(email="ironman@marvel.com", username="IronMan", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Upper body workout")
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, date="2025-12-29")
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboards/')
        self.assertEqual(response.status_code, 200)
