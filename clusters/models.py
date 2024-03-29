from django.db import models


class Cluster(models.Model):
    #Q43
    DISABILITY = (
        ('1', 'Has disability'),
        ('2', 'Has long term illness'),
        ('3', 'Has both disability and illness'),
        ('4', 'None'),
    )
    #Q45
    BENEFITS = (
        ('A', 'Pension from a former employer'),
        ('B', 'State pension'),
        ('C', 'Child benefit'),
        ('D', 'Income support or Job seekers allowance'),
        ('E', 'Housing benefit'),
        ('F', 'Council tax benefit'),
        ('G', 'Any other state benefits'),
    )
    #Q46
    ACTIVITY = (
        ('1', 'Employee in full-time job'),
        ('2', 'Employee in part-time job'),
        ('3', 'Self employed full-time'),
        ('4', 'Self employed part-time'),
        ('5', 'On government supported training programme'),
        ('6', 'Full-time education at school, college or university'),
        ('7', 'Unemployed and available for work'),
        ('8', 'Permanently sick/disabled'),
        ('9', 'Wholly retired from work'),
        ('10', 'Looking after the home'),
        ('95', 'Doing something else'),
        ('98', 'Refused'),
        ('97', 'Dont know'),
    )
    #Q47
    LLW = (
        ('1', 'Yes I am paid the London Living Wage or higher amount'),
        ('2', 'I am paid less than the London Living Wage'),
        ('3', 'Dont know'),
        ('4', 'Prefer not to say'),
    )
    #Q35
    HOUSING = (
        ('1', 'Owner occupier - Lambeth leaseholder'),
        ('2', 'Owner occupier - private'),
        ('3', 'Rented from Housing Association'),
        ('4', 'Rengint from Lambeth Council'),
        ('5', 'Rent from private landlord'),
        ('6', 'Shared ownership'),
        ('7', 'A residential home'),
        ('95', 'Other'),
        ('98', 'Refused'),
    )
    name = models.CharField(max_length=200)
    factor1 = models.CharField(max_length=1, choices=DISABILITY)
    factor2 = models.CharField(max_length=1, choices=BENEFITS)
    factor3 = models.CharField(max_length=1, choices=ACTIVITY)
    factor4 = models.CharField(max_length=1, choices=LLW)
    factor5 = models.CharField(max_length=1, choices=HOUSING)
