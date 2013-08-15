from django.db import models

# Create your models here.

class Appfamily(models.Model):
    appid = models.IntegerField(db_column='appId', primary_key=True) # Field name made lowercase.
    appname = models.CharField(max_length=300, db_column='appName') # Field name made lowercase.
    vendorid = models.IntegerField(db_column='vendorId') # Field name made lowercase.
    description = models.TextField(blank=True)
    webpage = models.CharField(max_length=300, db_column='webPage', blank=True) # Field name made lowercase.
    catid = models.IntegerField(null=True, db_column='catId', blank=True) # Field name made lowercase.
    submittime = models.DateTimeField(db_column='submitTime') # Field name made lowercase.
    submitterid = models.IntegerField(db_column='submitterId') # Field name made lowercase.
    state = models.CharField(max_length=24)

    class Meta:
        db_table = u'appFamily'


class Appversion(models.Model):
    versionid = models.IntegerField(db_column='versionId', primary_key=True) # Field name made lowercase.
    appid = models.IntegerField(db_column='appId') # Field name made lowercase.
    versionname = models.CharField(max_length=300, db_column='versionName') # Field name made lowercase.
    description = models.TextField(blank=True)
    rating = models.TextField(blank=True)
    ratingrelease = models.TextField(db_column='ratingRelease', blank=True) # Field name made lowercase.
    license = models.CharField(max_length=63, blank=True)
    state = models.CharField(max_length=24)
    class Meta:
        db_table = u'appVersion'

class Appcategory(models.Model):
    catid = models.IntegerField(db_column='catId', primary_key=True) # Field name made lowercase.
    catname = models.CharField(max_length=192, db_column='catName') # Field name made lowercase.
    catdescription = models.TextField(db_column='catDescription', blank=True) # Field name made lowercase.
    catparent = models.IntegerField(null=True, db_column='catParent', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'appCategory'

class Distributions(models.Model):
    distributionid = models.IntegerField(db_column='distributionId', primary_key=True) # Field name made lowercase.
    name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'distributions'

class Testresults(models.Model):
    testingid = models.IntegerField(db_column='testingId', primary_key=True) # Field name made lowercase.
    versionid = models.IntegerField(db_column='versionId') # Field name made lowercase.
    whatworks = models.TextField(db_column='whatWorks', blank=True) # Field name made lowercase.
    whatdoesnt = models.TextField(db_column='whatDoesnt', blank=True) # Field name made lowercase.
    whatnottested = models.TextField(db_column='whatNotTested', blank=True) # Field name made lowercase.
    testeddate = models.DateTimeField(db_column='testedDate') # Field name made lowercase.
    distributionid = models.IntegerField(db_column='distributionId') # Field name made lowercase.
    testedrelease = models.TextField(db_column='testedRelease', blank=True) # Field name made lowercase.
    installs = models.CharField(max_length=66)
    runs = models.CharField(max_length=45)
    testedrating = models.CharField(max_length=24, db_column='testedRating') # Field name made lowercase.
    comments = models.TextField(blank=True)
    submittime = models.DateTimeField(db_column='submitTime') # Field name made lowercase.
    state = models.CharField(max_length=24)
    class Meta:
        db_table = u'testResults'


class Buglinks(models.Model):
    linkid = models.IntegerField(db_column='linkId', primary_key=True) # Field name made lowercase.
    bug_id = models.IntegerField()
    versionid = models.IntegerField(db_column='versionId') # Field name made lowercase.
    state = models.CharField(max_length=24)
    class Meta:
        db_table = u'buglinks'

class Bugs(models.Model):
    bug_id = models.IntegerField(primary_key=True)
    bug_status = models.CharField(max_length=192)
    resolution = models.CharField(max_length=192)
    short_desc = models.CharField(max_length=765)
    class Meta:
        db_table = u'bugs'

class Appnotes(models.Model):
    noteid = models.IntegerField(db_column='noteId',primary_key=True) # Field name made lowercase.
    notetitle = models.CharField(max_length=765, db_column='noteTitle', blank=True) # Field name made lowercase.
    notedesc = models.TextField(db_column='noteDesc', blank=True) # Field name made lowercase.
    versionid = models.IntegerField(db_column='versionId') # Field name made lowercase.
    appid = models.IntegerField(db_column='appId') # Field name made lowercase.
    submittime = models.DateTimeField(db_column='submitTime') # Field name made lowercase.
    class Meta:
        db_table = u'appNotes'

class Appcomments(models.Model):
    time = models.DateTimeField(null=True, blank=True)
    commentid = models.IntegerField(db_column='commentId',primary_key=True) # Field name made lowercase.
    parentid = models.IntegerField(null=True, db_column='parentId', blank=True) # Field name made lowercase.
    versionid = models.IntegerField(null=True, db_column='versionId', blank=True) # Field name made lowercase.
    subject = models.CharField(max_length=384, blank=True)
    body = models.TextField(blank=True)
    class Meta:
        db_table = u'appComments'
