import boto3

def translator(text,sl,tl, region_name):
    translate = boto3.client(service_name='translate', region_name=region_name, use_ssl=True)

    ttext=[]
    for t in text:
        result = translate.translate_text(Text=t, SourceLanguageCode=sl, TargetLanguageCode=tl)
        ttext.append(result.get('TranslatedText'))

    print(ttext)

    return ttext