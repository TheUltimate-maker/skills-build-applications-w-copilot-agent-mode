from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', username='IronMan', team=marvel),
            User(email='captain@marvel.com', username='CaptainAmerica', team=marvel),
            User(email='spiderman@marvel.com', username='SpiderMan', team=marvel),
            User(email='batman@dc.com', username='Batman', team=dc),
            User(email='superman@dc.com', username='Superman', team=dc),
            User(email='wonderwoman@dc.com', username='WonderWoman', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        running = Workout.objects.create(name='Running', description='Cardio workout')
        pushups.suggested_for.add(marvel, dc)
        running.suggested_for.add(marvel, dc)

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-12-29')
        Activity.objects.create(user=users[3], type='Pushups', duration=20, date='2025-12-29')

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150, rank=1)
        Leaderboard.objects.create(team=dc, total_points=120, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
