# Generated by Django 3.1 on 2021-06-17 01:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('file_path', models.URLField(unique=True, verbose_name='link to the file')),
            ],
            options={
                'verbose_name': 'episode',
                'verbose_name_plural': 'episodes',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='plot')),
                ('creation_date', models.DateField(blank=True, verbose_name='release date')),
                ('certificate', models.TextField(blank=True, verbose_name='certificate')),
                ('age_classification', models.IntegerField(choices=[(0, '0+'), (6, '6+'), (12, '12+'), (16, '16+'), (18, '18+')], default=18, verbose_name='age rating system')),
                ('rating', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='rating')),
                ('file_path', models.URLField(unique=True, verbose_name='link to the file')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='MoviePersonRole',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.IntegerField(choices=[(0, 'actor'), (1, 'actor'), (2, 'screenwriter'), (3, 'producer')], verbose_name='role')),
            ],
            options={
                'verbose_name': 'creator',
                'verbose_name_plural': 'creators',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('birth_date', models.DateField(blank=True, verbose_name='date of birth')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='plot')),
                ('creation_date', models.DateField(blank=True, verbose_name='release date')),
                ('certificate', models.TextField(blank=True, verbose_name='certificate')),
                ('age_classification', models.IntegerField(choices=[(0, '0+'), (6, '6+'), (12, '12+'), (16, '16+'), (18, '18+')], default=18, verbose_name='age rating system')),
                ('rating', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='rating')),
                ('genres', models.ManyToManyField(to='movie.Genre')),
            ],
            options={
                'verbose_name': 'serial',
                'verbose_name_plural': 'serials',
            },
        ),
        migrations.CreateModel(
            name='SerialPersonRole',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.IntegerField(choices=[(0, 'actor'), (1, 'actor'), (2, 'screenwriter'), (3, 'producer')], verbose_name='role')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.person')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.serial')),
            ],
            options={
                'verbose_name': 'creator',
                'verbose_name_plural': 'creators',
            },
        ),
        migrations.AddField(
            model_name='serial',
            name='persons',
            field=models.ManyToManyField(through='movie.SerialPersonRole', to='movie.Person'),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('description', models.TextField(blank=True, verbose_name='plot')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.serial')),
            ],
            options={
                'verbose_name': 'season',
                'verbose_name_plural': 'seasons',
            },
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['last_name', 'first_name'], name='person_name_idx'),
        ),
        migrations.AddField(
            model_name='moviepersonrole',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.movie'),
        ),
        migrations.AddField(
            model_name='moviepersonrole',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='persons',
            field=models.ManyToManyField(through='movie.MoviePersonRole', to='movie.Person'),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.season'),
        ),
        migrations.AddIndex(
            model_name='serialpersonrole',
            index=models.Index(fields=['serial'], name='movie_seria_serial__8aab13_idx'),
        ),
        migrations.AddIndex(
            model_name='serialpersonrole',
            index=models.Index(fields=['person'], name='movie_seria_person__11eef9_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='serialpersonrole',
            unique_together={('serial', 'person', 'role')},
        ),
        migrations.AlterUniqueTogether(
            name='season',
            unique_together={('serial', 'number')},
        ),
        migrations.AddIndex(
            model_name='moviepersonrole',
            index=models.Index(fields=['movie'], name='movie_movie_movie_i_cd5733_idx'),
        ),
        migrations.AddIndex(
            model_name='moviepersonrole',
            index=models.Index(fields=['person'], name='movie_movie_person__9b040e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='moviepersonrole',
            unique_together={('movie', 'person', 'role')},
        ),
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together={('season', 'number')},
        ),
    ]
