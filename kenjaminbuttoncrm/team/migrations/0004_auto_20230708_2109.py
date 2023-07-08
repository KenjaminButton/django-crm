from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        # Replace <previous_migration> with the previous migration file name for the 'team' app
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE team_team ADD COLUMN plan_id INTEGER",
            "ALTER TABLE team_team DROP COLUMN plan_id"
        ),
    ]
