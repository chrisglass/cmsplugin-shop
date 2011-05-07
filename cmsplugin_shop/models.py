
class TopProducts(CMSPlugin):
    number_of_products = models.IntegerField(help_text=_('How many products to show'))
    
