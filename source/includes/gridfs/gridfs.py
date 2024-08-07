    # start create bucket
    client = MongoClient("<connection string>")
    db = client["db"]
    bucket = gridfs.GridFSBucket(db)
    # end create bucket

    # start create custom bucket
    custom_bucket = gridfs.GridFSBucket(db, bucket_name='myCustomBucket')
    # end create custom bucket

    # start upload files
    source_path = './file_to_upload'
    filename = 'my_file'

    with open(source_path, 'rb') as source:
        bucket.upload_from_stream(filename, source)
    # end upload files

    # start retrieve file info
    for file_doc in bucket.find({}):
        print(file_doc)
    # end retrieve file info

    # start download files name
    destination = open('output_file','wb')
    bucket.download_to_stream_by_name('my_file', destination)
    # end download files name

    # start download files id
    destination = open('output_file','wb+')
    bucket.download_to_stream(ObjectId('66b3c86e672a17b6c8a4a4a9'), destination)
    # end download files id

    # start rename files
    bucket.rename(ObjectId('66b3c86e672a17b6c8a4a4a9'), "new_file_name")
    # end rename files

    # start delete files
    bucket.delete(ObjectId('66b3c86e672a17b6c8a4a4a9'))
    # end delete files