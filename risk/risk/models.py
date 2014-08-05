# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Agtagenttypes(models.Model):
    agenttypeid = models.IntegerField(db_column='agentTypeID', primary_key=True)  # Field name made lowercase.
    agenttype = models.CharField(db_column='agentType', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgentTypes'


class Agtagents(models.Model):
    agentid = models.IntegerField(db_column='agentID', primary_key=True)  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='divisionID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    agenttypeid = models.IntegerField(db_column='agentTypeID', blank=True, null=True)  # Field name made lowercase.
    islocator = models.IntegerField(db_column='isLocator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgents'


class Agtresearchagents(models.Model):
    agentid = models.IntegerField(db_column='agentID')  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtResearchAgents'
        unique_together = (('agentID', 'typeID'),)


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Certcerts(models.Model):
    certid = models.IntegerField(db_column='certID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    groupid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'certCerts'


class Certmasteries(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    masterylevel = models.IntegerField(db_column='masteryLevel', blank=True, null=True)  # Field name made lowercase.
    certid = models.IntegerField(db_column='certID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certMasteries'


class Certskills(models.Model):
    certid = models.IntegerField(db_column='certID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    certlevelint = models.IntegerField(db_column='certLevelInt', blank=True, null=True)  # Field name made lowercase.
    skilllevel = models.IntegerField(db_column='skillLevel', blank=True, null=True)  # Field name made lowercase.
    certleveltext = models.CharField(db_column='certLevelText', max_length=8, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certSkills'


class Chrancestries(models.Model):
    ancestryid = models.IntegerField(db_column='ancestryID', primary_key=True)  # Field name made lowercase.
    ancestryname = models.CharField(db_column='ancestryName', max_length=100, blank=True)  # Field name made lowercase.
    bloodlineid = models.IntegerField(db_column='bloodlineID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    perception = models.IntegerField(blank=True, null=True)
    willpower = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrAncestries'


class Chrattributes(models.Model):
    attributeid = models.IntegerField(db_column='attributeID', primary_key=True)  # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True)  # Field name made lowercase.
    notes = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'chrAttributes'


class Chrbloodlines(models.Model):
    bloodlineid = models.IntegerField(db_column='bloodlineID', primary_key=True)  # Field name made lowercase.
    bloodlinename = models.CharField(db_column='bloodlineName', max_length=100, blank=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    maledescription = models.CharField(db_column='maleDescription', max_length=1000, blank=True)  # Field name made lowercase.
    femaledescription = models.CharField(db_column='femaleDescription', max_length=1000, blank=True)  # Field name made lowercase.
    shiptypeid = models.IntegerField(db_column='shipTypeID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    perception = models.IntegerField(blank=True, null=True)
    willpower = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True)  # Field name made lowercase.
    shortmaledescription = models.CharField(db_column='shortMaleDescription', max_length=500, blank=True)  # Field name made lowercase.
    shortfemaledescription = models.CharField(db_column='shortFemaleDescription', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrBloodlines'


class Chrfactions(models.Model):
    factionid = models.IntegerField(db_column='factionID', primary_key=True)  # Field name made lowercase.
    factionname = models.CharField(db_column='factionName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    raceids = models.IntegerField(db_column='raceIDs', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    sizefactor = models.FloatField(db_column='sizeFactor', blank=True, null=True)  # Field name made lowercase.
    stationcount = models.IntegerField(db_column='stationCount', blank=True, null=True)  # Field name made lowercase.
    stationsystemcount = models.IntegerField(db_column='stationSystemCount', blank=True, null=True)  # Field name made lowercase.
    militiacorporationid = models.IntegerField(db_column='militiaCorporationID', blank=True, null=True)  # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrFactions'


class Chrraces(models.Model):
    raceid = models.IntegerField(db_column='raceID', primary_key=True)  # Field name made lowercase.
    racename = models.CharField(db_column='raceName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrRaces'


class Crpactivities(models.Model):
    activityid = models.IntegerField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'crpActivities'


class Crpnpccorporationdivisions(models.Model):
    corporationid = models.IntegerField(db_column='corporationID')  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='divisionID')  # Field name made lowercase.
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationDivisions'
        unique_together = (('corporationID', 'divisionID'),)


class Crpnpccorporationresearchfields(models.Model):
    skillid = models.IntegerField(db_column='skillID')  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationResearchFields'
        unique_together = (('skillID', 'corporationID'),)


class Crpnpccorporationtrades(models.Model):
    corporationid = models.IntegerField(db_column='corporationID')  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationTrades'
        unique_together = (('corporationID', 'typeID'),)


class Crpnpccorporations(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True)  # Field name made lowercase.
    size = models.CharField(max_length=1, blank=True)
    extent = models.CharField(max_length=1, blank=True)
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    investorid1 = models.IntegerField(db_column='investorID1', blank=True, null=True)  # Field name made lowercase.
    investorshares1 = models.IntegerField(db_column='investorShares1', blank=True, null=True)  # Field name made lowercase.
    investorid2 = models.IntegerField(db_column='investorID2', blank=True, null=True)  # Field name made lowercase.
    investorshares2 = models.IntegerField(db_column='investorShares2', blank=True, null=True)  # Field name made lowercase.
    investorid3 = models.IntegerField(db_column='investorID3', blank=True, null=True)  # Field name made lowercase.
    investorshares3 = models.IntegerField(db_column='investorShares3', blank=True, null=True)  # Field name made lowercase.
    investorid4 = models.IntegerField(db_column='investorID4', blank=True, null=True)  # Field name made lowercase.
    investorshares4 = models.IntegerField(db_column='investorShares4', blank=True, null=True)  # Field name made lowercase.
    friendid = models.IntegerField(db_column='friendID', blank=True, null=True)  # Field name made lowercase.
    enemyid = models.IntegerField(db_column='enemyID', blank=True, null=True)  # Field name made lowercase.
    publicshares = models.BigIntegerField(db_column='publicShares', blank=True, null=True)  # Field name made lowercase.
    initialprice = models.IntegerField(db_column='initialPrice', blank=True, null=True)  # Field name made lowercase.
    minsecurity = models.FloatField(db_column='minSecurity', blank=True, null=True)  # Field name made lowercase.
    scattered = models.IntegerField(blank=True, null=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    sizefactor = models.FloatField(db_column='sizeFactor', blank=True, null=True)  # Field name made lowercase.
    stationcount = models.IntegerField(db_column='stationCount', blank=True, null=True)  # Field name made lowercase.
    stationsystemcount = models.IntegerField(db_column='stationSystemCount', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=4000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporations'


class Crpnpcdivisions(models.Model):
    divisionid = models.IntegerField(db_column='divisionID', primary_key=True)  # Field name made lowercase.
    divisionname = models.CharField(db_column='divisionName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    leadertype = models.CharField(db_column='leaderType', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCDivisions'


class Dgmattributecategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=50, blank=True)  # Field name made lowercase.
    categorydescription = models.CharField(db_column='categoryDescription', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmAttributeCategories'


class Dgmattributetypes(models.Model):
    attributeid = models.IntegerField(db_column='attributeID', primary_key=True)  # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.FloatField(db_column='defaultValue', blank=True, null=True)  # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', max_length=100, blank=True)  # Field name made lowercase.
    unitid = models.IntegerField(db_column='unitID', blank=True, null=True)  # Field name made lowercase.
    stackable = models.IntegerField(blank=True, null=True)
    highisgood = models.IntegerField(db_column='highIsGood', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmAttributeTypes'


class Dgmeffects(models.Model):
    effectid = models.IntegerField(db_column='effectID', primary_key=True)  # Field name made lowercase.
    effectname = models.CharField(db_column='effectName', max_length=400, blank=True)  # Field name made lowercase.
    effectcategory = models.IntegerField(db_column='effectCategory', blank=True, null=True)  # Field name made lowercase.
    preexpression = models.IntegerField(db_column='preExpression', blank=True, null=True)  # Field name made lowercase.
    postexpression = models.IntegerField(db_column='postExpression', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    guid = models.CharField(max_length=60, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    isoffensive = models.IntegerField(db_column='isOffensive', blank=True, null=True)  # Field name made lowercase.
    isassistance = models.IntegerField(db_column='isAssistance', blank=True, null=True)  # Field name made lowercase.
    durationattributeid = models.IntegerField(db_column='durationAttributeID', blank=True, null=True)  # Field name made lowercase.
    trackingspeedattributeid = models.IntegerField(db_column='trackingSpeedAttributeID', blank=True, null=True)  # Field name made lowercase.
    dischargeattributeid = models.IntegerField(db_column='dischargeAttributeID', blank=True, null=True)  # Field name made lowercase.
    rangeattributeid = models.IntegerField(db_column='rangeAttributeID', blank=True, null=True)  # Field name made lowercase.
    falloffattributeid = models.IntegerField(db_column='falloffAttributeID', blank=True, null=True)  # Field name made lowercase.
    disallowautorepeat = models.IntegerField(db_column='disallowAutoRepeat', blank=True, null=True)  # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', max_length=100, blank=True)  # Field name made lowercase.
    iswarpsafe = models.IntegerField(db_column='isWarpSafe', blank=True, null=True)  # Field name made lowercase.
    rangechance = models.IntegerField(db_column='rangeChance', blank=True, null=True)  # Field name made lowercase.
    electronicchance = models.IntegerField(db_column='electronicChance', blank=True, null=True)  # Field name made lowercase.
    propulsionchance = models.IntegerField(db_column='propulsionChance', blank=True, null=True)  # Field name made lowercase.
    distribution = models.IntegerField(blank=True, null=True)
    sfxname = models.CharField(db_column='sfxName', max_length=20, blank=True)  # Field name made lowercase.
    npcusagechanceattributeid = models.IntegerField(db_column='npcUsageChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    npcactivationchanceattributeid = models.IntegerField(db_column='npcActivationChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    fittingusagechanceattributeid = models.IntegerField(db_column='fittingUsageChanceAttributeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmEffects'


class Dgmtypeattributes(models.Model):
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='attributeID')  # Field name made lowercase.
    valueint = models.IntegerField(db_column='valueInt', blank=True, null=True)  # Field name made lowercase.
    valuefloat = models.FloatField(db_column='valueFloat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmTypeAttributes'
        unique_together = (('typeID', 'attributeID'),)


class Dgmtypeeffects(models.Model):
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    effectid = models.IntegerField(db_column='effectID')  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmTypeEffects'
        unique_together = (('typeID', 'effectID'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Eveicons(models.Model):
    iconid = models.IntegerField(db_column='iconID', primary_key=True)  # Field name made lowercase.
    iconfile = models.CharField(db_column='iconFile', max_length=500)  # Field name made lowercase.
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'eveIcons'


class Eveunits(models.Model):
    unitid = models.IntegerField(db_column='unitID', primary_key=True)  # Field name made lowercase.
    unitname = models.CharField(db_column='unitName', max_length=100, blank=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', max_length=50, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'eveUnits'


class Industryactivity(models.Model):
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    time = models.IntegerField(blank=True, null=True)
    activityid = models.IntegerField(db_column='activityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'industryActivity'
        unique_together = (('typeID', 'activityID'),)


class Industryactivitymaterials(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    materialtypeid = models.IntegerField(db_column='materialTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    consume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivityMaterials'


class Industryactivityprobabilities(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    producttypeid = models.IntegerField(db_column='productTypeID', blank=True, null=True)  # Field name made lowercase.
    probability = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivityProbabilities'


class Industryactivityproducts(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    producttypeid = models.IntegerField(db_column='productTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivityProducts'


class Industryactivityskills(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivitySkills'


class Industryblueprints(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    maxproductionlimit = models.IntegerField(db_column='maxProductionLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'industryBlueprints'


class Invcategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invCategories'


class Invcontrabandtypes(models.Model):
    factionid = models.IntegerField(db_column='factionID')  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    standingloss = models.FloatField(db_column='standingLoss', blank=True, null=True)  # Field name made lowercase.
    confiscateminsec = models.FloatField(db_column='confiscateMinSec', blank=True, null=True)  # Field name made lowercase.
    finebyvalue = models.FloatField(db_column='fineByValue', blank=True, null=True)  # Field name made lowercase.
    attackminsec = models.FloatField(db_column='attackMinSec', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invContrabandTypes'
        unique_together = (('factionID', 'typeID'),)


class Invcontroltowerresourcepurposes(models.Model):
    purpose = models.IntegerField(primary_key=True)
    purposetext = models.CharField(db_column='purposeText', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invControlTowerResourcePurposes'


class Invcontroltowerresources(models.Model):
    controltowertypeid = models.IntegerField(db_column='controlTowerTypeID')  # Field name made lowercase.
    resourcetypeid = models.IntegerField(db_column='resourceTypeID')  # Field name made lowercase.
    purpose = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    minsecuritylevel = models.FloatField(db_column='minSecurityLevel', blank=True, null=True)  # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invControlTowerResources'
        unique_together = (('controlTowerTypeID', 'resourceTypeID'),)


class Invflags(models.Model):
    flagid = models.IntegerField(db_column='flagID', primary_key=True)  # Field name made lowercase.
    flagname = models.CharField(db_column='flagName', max_length=200, blank=True)  # Field name made lowercase.
    flagtext = models.CharField(db_column='flagText', max_length=100, blank=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invFlags'


class Invgroups(models.Model):
    groupid = models.IntegerField(db_column='groupID', primary_key=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    usebaseprice = models.IntegerField(db_column='useBasePrice', blank=True, null=True)  # Field name made lowercase.
    allowmanufacture = models.IntegerField(db_column='allowManufacture', blank=True, null=True)  # Field name made lowercase.
    allowrecycler = models.IntegerField(db_column='allowRecycler', blank=True, null=True)  # Field name made lowercase.
    anchored = models.IntegerField(blank=True, null=True)
    anchorable = models.IntegerField(blank=True, null=True)
    fittablenonsingleton = models.IntegerField(db_column='fittableNonSingleton', blank=True, null=True)  # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invGroups'


class Invitems(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID')  # Field name made lowercase.
    locationid = models.BigIntegerField(db_column='locationID')  # Field name made lowercase.
    flagid = models.IntegerField(db_column='flagID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invItems'


class Invmarketgroups(models.Model):
    marketgroupid = models.IntegerField(db_column='marketGroupID', primary_key=True)  # Field name made lowercase.
    parentgroupid = models.IntegerField(db_column='parentGroupID', blank=True, null=True)  # Field name made lowercase.
    marketgroupname = models.CharField(db_column='marketGroupName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    hastypes = models.IntegerField(db_column='hasTypes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMarketGroups'


class Invmetagroups(models.Model):
    metagroupid = models.IntegerField(db_column='metaGroupID', primary_key=True)  # Field name made lowercase.
    metagroupname = models.CharField(db_column='metaGroupName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMetaGroups'


class Invmetatypes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parentTypeID', blank=True, null=True)  # Field name made lowercase.
    metagroupid = models.IntegerField(db_column='metaGroupID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMetaTypes'


class Invnames(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invNames'


class Invpositions(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    yaw = models.FloatField(blank=True, null=True)
    pitch = models.FloatField(blank=True, null=True)
    roll = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invPositions'


class Invtraits(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    bonus = models.FloatField(blank=True, null=True)
    bonustext = models.TextField(db_column='bonusText', blank=True)  # Field name made lowercase.
    unitid = models.IntegerField(db_column='unitID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invTraits'


class Invtypematerials(models.Model):
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    materialtypeid = models.IntegerField(db_column='materialTypeID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invTypeMaterials'
        unique_together = (('typeID', 'materialTypeID'),)


class Invtypereactions(models.Model):
    reactiontypeid = models.IntegerField(db_column='reactionTypeID')  # Field name made lowercase.
    input = models.IntegerField()
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invTypeReactions'
        unique_together = (('reactionTypeID', 'input', 'typeID'),)


class Invtypes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    mass = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    portionsize = models.IntegerField(db_column='portionSize', blank=True, null=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    baseprice = models.DecimalField(db_column='basePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)
    marketgroupid = models.IntegerField(db_column='marketGroupID', blank=True, null=True)  # Field name made lowercase.
    chanceofduplicating = models.FloatField(db_column='chanceOfDuplicating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invTypes'


class Invuniquenames(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', unique=True, max_length=200)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invUniqueNames'


class Mapcelestialstatistics(models.Model):
    celestialid = models.IntegerField(db_column='celestialID', primary_key=True)  # Field name made lowercase.
    temperature = models.FloatField(blank=True, null=True)
    spectralclass = models.TextField(db_column='spectralClass', blank=True)  # Field name made lowercase.
    luminosity = models.FloatField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    life = models.FloatField(blank=True, null=True)
    orbitradius = models.FloatField(db_column='orbitRadius', blank=True, null=True)  # Field name made lowercase.
    eccentricity = models.FloatField(blank=True, null=True)
    massdust = models.FloatField(db_column='massDust', blank=True, null=True)  # Field name made lowercase.
    massgas = models.FloatField(db_column='massGas', blank=True, null=True)  # Field name made lowercase.
    fragmented = models.IntegerField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    surfacegravity = models.FloatField(db_column='surfaceGravity', blank=True, null=True)  # Field name made lowercase.
    escapevelocity = models.FloatField(db_column='escapeVelocity', blank=True, null=True)  # Field name made lowercase.
    orbitperiod = models.FloatField(db_column='orbitPeriod', blank=True, null=True)  # Field name made lowercase.
    rotationrate = models.FloatField(db_column='rotationRate', blank=True, null=True)  # Field name made lowercase.
    locked = models.IntegerField(blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    mass = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapCelestialStatistics'


class Mapconstellationjumps(models.Model):
    fromregionid = models.BigIntegerField(db_column='fromRegionID', blank=True, null=True)  # Field name made lowercase.
    fromconstellationid = models.BigIntegerField(db_column='fromConstellationID')  # Field name made lowercase.
    toconstellationid = models.BigIntegerField(db_column='toConstellationID')  # Field name made lowercase.
    toregionid = models.BigIntegerField(db_column='toRegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapConstellationJumps'
        unique_together = (('fromConstellationID', 'toConstellationID'),)


class Mapconstellations(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', primary_key=True)  # Field name made lowercase.
    constellationname = models.TextField(db_column='constellationName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapConstellations'


class Mapdenormalize(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    orbitid = models.IntegerField(db_column='orbitID', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    itemname = models.TextField(db_column='itemName', blank=True)  # Field name made lowercase.
    security = models.FloatField(blank=True, null=True)
    celestialindex = models.IntegerField(db_column='celestialIndex', blank=True, null=True)  # Field name made lowercase.
    orbitindex = models.IntegerField(db_column='orbitIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapDenormalize'


class Mapjumps(models.Model):
    stargateid = models.BigIntegerField(db_column='stargateID', primary_key=True)  # Field name made lowercase.
    destinationid = models.BigIntegerField(db_column='destinationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapJumps'


class Maplandmarks(models.Model):
    landmarkid = models.BigIntegerField(db_column='landmarkID', primary_key=True)  # Field name made lowercase.
    landmarkname = models.TextField(db_column='landmarkName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    locationid = models.BigIntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLandmarks'


class Maplocationscenes(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    graphicid = models.IntegerField(db_column='graphicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLocationScenes'


class Maplocationwormholeclasses(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    wormholeclassid = models.IntegerField(db_column='wormholeClassID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLocationWormholeClasses'


class Mapregionjumps(models.Model):
    fromregionid = models.BigIntegerField(db_column='fromRegionID')  # Field name made lowercase.
    toregionid = models.BigIntegerField(db_column='toRegionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapRegionJumps'
        unique_together = (('fromRegionID', 'toRegionID'),)


class Mapregions(models.Model):
    regionid = models.IntegerField(db_column='regionID', primary_key=True)  # Field name made lowercase.
    regionname = models.TextField(db_column='regionName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapRegions'


class Mapsolarsystemjumps(models.Model):
    fromregionid = models.BigIntegerField(db_column='fromRegionID', blank=True, null=True)  # Field name made lowercase.
    fromconstellationid = models.BigIntegerField(db_column='fromConstellationID', blank=True, null=True)  # Field name made lowercase.
    fromsolarsystemid = models.BigIntegerField(db_column='fromSolarSystemID')  # Field name made lowercase.
    tosolarsystemid = models.BigIntegerField(db_column='toSolarSystemID')  # Field name made lowercase.
    toconstellationid = models.BigIntegerField(db_column='toConstellationID', blank=True, null=True)  # Field name made lowercase.
    toregionid = models.BigIntegerField(db_column='toRegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapSolarSystemJumps'
        unique_together = (('fromSolarSystemID', 'toSolarSystemID'),)


class Mapsolarsystems(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', primary_key=True)  # Field name made lowercase.
    solarsystemname = models.TextField(db_column='solarSystemName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    luminosity = models.FloatField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    international = models.IntegerField(blank=True, null=True)
    regional = models.IntegerField(blank=True, null=True)
    constellation = models.IntegerField(blank=True, null=True)
    security = models.FloatField(blank=True, null=True)
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    suntypeid = models.IntegerField(db_column='sunTypeID', blank=True, null=True)  # Field name made lowercase.
    securityclass = models.TextField(db_column='securityClass', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapSolarSystems'


class Mapuniverse(models.Model):
    universeid = models.IntegerField(db_column='universeID', primary_key=True)  # Field name made lowercase.
    universename = models.CharField(db_column='universeName', max_length=100, blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapUniverse'


class Planetschematics(models.Model):
    schematicid = models.IntegerField(db_column='schematicID', primary_key=True)  # Field name made lowercase.
    schematicname = models.CharField(db_column='schematicName', max_length=255, blank=True)  # Field name made lowercase.
    cycletime = models.IntegerField(db_column='cycleTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematics'


class Planetschematicspinmap(models.Model):
    schematicid = models.IntegerField(db_column='schematicID')  # Field name made lowercase.
    pintypeid = models.IntegerField(db_column='pinTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematicsPinMap'
        unique_together = (('schematicID', 'pinTypeID'),)


class Planetschematicstypemap(models.Model):
    schematicid = models.IntegerField(db_column='schematicID')  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    isinput = models.IntegerField(db_column='isInput', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematicsTypeMap'
        unique_together = (('schematicID', 'typeID'),)


class Ramactivities(models.Model):
    activityid = models.IntegerField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=100, blank=True)  # Field name made lowercase.
    iconno = models.CharField(db_column='iconNo', max_length=5, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    published = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ramActivities'


class Ramassemblylinestations(models.Model):
    stationid = models.IntegerField(db_column='stationID')  # Field name made lowercase.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineStations'
        unique_together = (('stationID', 'assemblyLineTypeID'),)


class Ramassemblylinetypedetailpercategory(models.Model):
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.
    timemultiplier = models.FloatField(db_column='timeMultiplier', blank=True, null=True)  # Field name made lowercase.
    materialmultiplier = models.FloatField(db_column='materialMultiplier', blank=True, null=True)  # Field name made lowercase.
    costmultiplier = models.FloatField(db_column='costMultiplier', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerCategory'
        unique_together = (('assemblyLineTypeID', 'categoryID'),)


class Ramassemblylinetypedetailpergroup(models.Model):
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID')  # Field name made lowercase.
    timemultiplier = models.FloatField(db_column='timeMultiplier', blank=True, null=True)  # Field name made lowercase.
    materialmultiplier = models.FloatField(db_column='materialMultiplier', blank=True, null=True)  # Field name made lowercase.
    costmultiplier = models.FloatField(db_column='costMultiplier', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerGroup'
        unique_together = (('assemblyLineTypeID', 'groupID'),)


class Ramassemblylinetypes(models.Model):
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', primary_key=True)  # Field name made lowercase.
    assemblylinetypename = models.CharField(db_column='assemblyLineTypeName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    basetimemultiplier = models.FloatField(db_column='baseTimeMultiplier', blank=True, null=True)  # Field name made lowercase.
    basematerialmultiplier = models.FloatField(db_column='baseMaterialMultiplier', blank=True, null=True)  # Field name made lowercase.
    basecostmultiplier = models.FloatField(db_column='baseCostMultiplier', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(blank=True, null=True)
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    mincostperhour = models.FloatField(db_column='minCostPerHour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypes'


class Raminstallationtypecontents(models.Model):
    installationtypeid = models.IntegerField(db_column='installationTypeID')  # Field name made lowercase.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ramInstallationTypeContents'
        unique_together = (('installationTypeID', 'assemblyLineTypeID'),)


class Staoperationservices(models.Model):
    operationid = models.IntegerField(db_column='operationID')  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='serviceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staOperationServices'
        unique_together = (('operationID', 'serviceID'),)


class Staoperations(models.Model):
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    operationid = models.IntegerField(db_column='operationID', primary_key=True)  # Field name made lowercase.
    operationname = models.CharField(db_column='operationName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    caldaristationtypeid = models.IntegerField(db_column='caldariStationTypeID', blank=True, null=True)  # Field name made lowercase.
    minmatarstationtypeid = models.IntegerField(db_column='minmatarStationTypeID', blank=True, null=True)  # Field name made lowercase.
    amarrstationtypeid = models.IntegerField(db_column='amarrStationTypeID', blank=True, null=True)  # Field name made lowercase.
    gallentestationtypeid = models.IntegerField(db_column='gallenteStationTypeID', blank=True, null=True)  # Field name made lowercase.
    jovestationtypeid = models.IntegerField(db_column='joveStationTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staOperations'


class Staservices(models.Model):
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'staServices'


class Stastationtypes(models.Model):
    stationtypeid = models.IntegerField(db_column='stationTypeID', primary_key=True)  # Field name made lowercase.
    dockentryx = models.FloatField(db_column='dockEntryX', blank=True, null=True)  # Field name made lowercase.
    dockentryy = models.FloatField(db_column='dockEntryY', blank=True, null=True)  # Field name made lowercase.
    dockentryz = models.FloatField(db_column='dockEntryZ', blank=True, null=True)  # Field name made lowercase.
    dockorientationx = models.FloatField(db_column='dockOrientationX', blank=True, null=True)  # Field name made lowercase.
    dockorientationy = models.FloatField(db_column='dockOrientationY', blank=True, null=True)  # Field name made lowercase.
    dockorientationz = models.FloatField(db_column='dockOrientationZ', blank=True, null=True)  # Field name made lowercase.
    operationid = models.IntegerField(db_column='operationID', blank=True, null=True)  # Field name made lowercase.
    officeslots = models.IntegerField(db_column='officeSlots', blank=True, null=True)  # Field name made lowercase.
    reprocessingefficiency = models.FloatField(db_column='reprocessingEfficiency', blank=True, null=True)  # Field name made lowercase.
    conquerable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staStationTypes'


class Stastations(models.Model):
    stationid = models.IntegerField(db_column='stationID', primary_key=True)  # Field name made lowercase.
    security = models.IntegerField(blank=True, null=True)
    dockingcostpervolume = models.FloatField(db_column='dockingCostPerVolume', blank=True, null=True)  # Field name made lowercase.
    maxshipvolumedockable = models.FloatField(db_column='maxShipVolumeDockable', blank=True, null=True)  # Field name made lowercase.
    officerentalcost = models.IntegerField(db_column='officeRentalCost', blank=True, null=True)  # Field name made lowercase.
    operationid = models.IntegerField(db_column='operationID', blank=True, null=True)  # Field name made lowercase.
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    stationname = models.CharField(db_column='stationName', max_length=100, blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    reprocessingefficiency = models.FloatField(db_column='reprocessingEfficiency', blank=True, null=True)  # Field name made lowercase.
    reprocessingstationstake = models.FloatField(db_column='reprocessingStationsTake', blank=True, null=True)  # Field name made lowercase.
    reprocessinghangarflag = models.IntegerField(db_column='reprocessingHangarFlag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staStations'


class Translationtables(models.Model):
    sourcetable = models.CharField(db_column='sourceTable', max_length=200)  # Field name made lowercase.
    destinationtable = models.CharField(db_column='destinationTable', max_length=200, blank=True)  # Field name made lowercase.
    translatedkey = models.CharField(db_column='translatedKey', max_length=200)  # Field name made lowercase.
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'translationTables'
        unique_together = (('sourceTable', 'translatedKey'),)


class Trntranslationcolumns(models.Model):
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=256)  # Field name made lowercase.
    columnname = models.CharField(db_column='columnName', max_length=128)  # Field name made lowercase.
    masterid = models.CharField(db_column='masterID', max_length=128, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnTranslationColumns'


class Trntranslationlanguages(models.Model):
    numericlanguageid = models.IntegerField(db_column='numericLanguageID', primary_key=True)  # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', max_length=50, blank=True)  # Field name made lowercase.
    languagename = models.CharField(db_column='languageName', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnTranslationLanguages'


class Trntranslations(models.Model):
    tcid = models.IntegerField(db_column='tcID')  # Field name made lowercase.
    keyid = models.IntegerField(db_column='keyID')  # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', max_length=50)  # Field name made lowercase.
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'trnTranslations'
        unique_together = (('tcID', 'keyID', 'languageID'),)


class Warcombatzonesystems(models.Model):
    solarsystemid = models.IntegerField(db_column='solarSystemID', primary_key=True)  # Field name made lowercase.
    combatzoneid = models.IntegerField(db_column='combatZoneID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warCombatZoneSystems'


class Warcombatzones(models.Model):
    combatzoneid = models.IntegerField(db_column='combatZoneID', primary_key=True)  # Field name made lowercase.
    combatzonename = models.CharField(db_column='combatZoneName', max_length=100, blank=True)  # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    centersystemid = models.IntegerField(db_column='centerSystemID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'warCombatZones'
