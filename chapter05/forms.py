from django import forms

class Work01Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    mail = forms.EmailField(label = "メール",
            widget=forms.TextInput(attrs={"class" : "form-control"}))
    movie = forms.ChoiceField(label="好きな映画",
        choices = (
            ('sf', 'SF'),
            ('action', 'アクション'),
            ('comedy', 'コメディ'),
            ('suspence', 'サスペンス'),
        ),
        widget=forms.CheckboxSelectMultiple(attrs={"class" : "form-check-input"}))


class Work02Form(forms.Form):
    name = forms.CharField(label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    subject = forms.ChoiceField(label="好き科目",
        choices = (
            ('Japanese', '国語'),
            ('Math', '数学'),
            ('English', '英語'),
            ('Science', '理科'),
            ('Social Study', '社会'),
        ),
        widget=forms.Select(attrs={"class" : "form-control"}))

