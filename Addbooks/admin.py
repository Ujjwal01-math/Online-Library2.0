from django.contrib import admin
from Addbooks.models import book,Programming,Mystery,history,Business,Electronics,Science,Story
class bookAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_des','book_pdf')
admin.site.register(book,bookAdmin)
class ProgrammingAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf')
admin.site.register(Programming,ProgrammingAdmin)
class MysteryAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf') 
admin.site.register(Mystery,MysteryAdmin) 
class historyAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf')
admin.site.register(history,historyAdmin)  
class businessAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf')
admin.site.register(Business,businessAdmin) 
class ElectronicsAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf') 
admin.site.register(Electronics,ElectronicsAdmin)
class ScienceAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf')
admin.site.register(Science,ScienceAdmin)    
class StoryAdmin(admin.ModelAdmin):
    list_display=('book_image','book_title','book_author','book_des','book_pdf')
admin.site.register(Story,StoryAdmin)

# Register your models here.
