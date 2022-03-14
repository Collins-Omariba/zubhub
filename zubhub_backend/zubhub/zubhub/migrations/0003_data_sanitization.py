# Generated by Django 3.2 on 2022-03-14 05:54

from django.db import migrations
from lxml.html.clean import Cleaner
from lxml.html import document_fromstring

def clean_summernote_html(string):
    cleaner = Cleaner()
    return cleaner.clean_html(string)

def apply(apps, schema_editor):
    """
    Sanitize Summernote text fields in models.
    """

    Privacy = apps.get_model("zubhub", "Privacy")
    Help = apps.get_model("zubhub", "Help")
    FAQ = apps.get_model("zubhub", "FAQ")

    for each in Privacy.objects.all():
        if each.privacy_policy:
            each.privacy_policy = clean_summernote_html(each.privacy_policy)
        if each.terms_of_use:
            each.terms_of_use = clean_summernote_html(each.terms_of_use)
        each.save()

    for each in Help.objects.all():
        if each.about:
            each.about = clean_summernote_html(each.about)
        each.save()

    for each in FAQ.objects.all():
        if each.question:
            each.question = clean_summernote_html(each.question)
        if each.answer:
            each.answer = clean_summernote_html(each.answer)
        each.save()



def revert(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('zubhub', '0002_auto_20220215_0329_squashed_0004_alter_hero_image_url'),
    ]

    operations = [
        migrations.RunPython(apply, revert),
    ]