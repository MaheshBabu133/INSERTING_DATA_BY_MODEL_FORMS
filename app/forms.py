from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['name','url']     #it will display only name and url  at front end
        #fields=['name']           #it will display only name 
        #exclude=['name','url']    #it will display except name and url  at front end
        #exclude=['name']          #it will display except name   at front end

        #labels={'topic_name':'TN','name':'N','email':'mail_id'} #it will replace the previous label name with new label name
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea} 
        #above widget make url field as password and name is as like as text area
        #help_texts={'topic_name':'should not be interger','name':'Alphabets only ','email':'must ends with the @gmail.com/in/org ','url':'it must starts with http://'}
        #above help_texts are used to provide additional content at the end of the input element
        #It helps to user understanding


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'