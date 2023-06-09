from django.db import models

class ParisEtablissement(models.Model):
    
    variant_status = [('NLH', 'NLH'),('PLO-4', 'PLO-4'),]
    limit_status = [('1€-2€', '1€-2€'),('2€-4€', '2€-4€'),('5€-5€', '5€-5€'),('5€-10€', '5€-10€'),('10€-20€', '10€-20€'),('20€-40€', '20€-40€')]
    
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128, blank=True, null=True)
    adresse = models.CharField(max_length=128, blank=True, null=True)
    opening_time = models.CharField(max_length=128, blank=True, null=True)
    variant = models.CharField(max_length=128, choices=variant_status)
    limit = models.CharField(max_length=128,choices=limit_status)
    description = models.TextField(max_length=2048, blank=True)
    
    class Meta:
        verbose_name_plural = "Liste des Clubs"
    
    def __str__(self):
        return self.name
    