
#REF https://docs.djangoproject.com/en/1.7/topics/http/file-uploads/
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination: #UPDATE
        for chunk in f.chunks():
            destination.write(chunk)