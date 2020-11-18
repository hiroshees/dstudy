from django import forms

class Work01Form (forms.Form):
    name = forms.CharField(label = "名前")
    mail = forms.EmailField(label = "メール")
    age = forms.IntegerField(label = "年齢")


class Work03Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    mail = forms.EmailField(label = "メール",
        widget=forms.EmailInput(attrs={"class" : "form-control"}))
    age = forms.IntegerField(label = "年齢",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))


class Work04Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    mail = forms.EmailField(label = "メール",
        widget=forms.EmailInput(attrs={"class" : "form-control"}))
    age = forms.IntegerField(label = "年齢",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))


class Work05Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    city = forms.ChoiceField(label = "行ってみたい都市",
        choices = (
            ('tokyo', '東京'),
            ('la', 'ロサンゼルス'),
            ('london', 'ロンドン'),
            ('paris', 'パリ'),
            ('madrid', 'マドリード')
        ),
        widget=forms.Select(attrs={"class" : "form-control"}))


class Work06Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    music = forms.ChoiceField(label="好きな音楽",
        choices = (
            ('pop', 'ポップ'),
            ('rock', 'ロック'),
            ('anime', 'アニソン'),
            ('idol', 'アイドル'),
        ),
        widget=forms.RadioSelect(attrs={"class" : "form-check-input"}))


class Work07Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    movie = forms.ChoiceField(label="好きな映画",
        choices = (
            ('sf', 'SF'),
            ('action', 'アクション'),
            ('comedy', 'コメディ'),
            ('suspence', 'サスペンス'),
        ),
        widget=forms.CheckboxSelectMultiple(attrs={"class" : "form-check-input"}))


class Work08Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    message = forms.CharField(label="メッセージ",
        widget=forms.Textarea(attrs={"class" : "form-control"}))


class Work09Form (forms.Form):
    name = forms.CharField(label = "名前", 
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    secret = forms.CharField(
        initial = "this is secret")

