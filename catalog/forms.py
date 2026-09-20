from django import forms

class FeedbackForm(forms.Form):
    """Класс для формы обратной связи"""
    name = forms.CharField(max_length=100, label="Имя", required=True)
    phone = forms.CharField(max_length=50, label="Телефон", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Сообщение", required=True)
