# start create bucket
db = MongoClient().test
bucket = gridfs.GridFSBucket(db)
# end create bucket

# start create custom bucket
bucket = gridfs.GridFSBucket(db, bucket_name='myCustomBucket')
# end create custom bucket

# start upload files
with open("my_file", "rb") as f:
    file_id = fs.put(f, filename="my_file")
# end upload files

# start retrieve file info
for file in bucket.find({}):
    data = file.read()
# end retrieve file info

# start download files name
destination = open('output_file','wb')
bucket.download_to_stream_by_name("my_file", destination)
# end download files name

# start download files id
destination = open('output_file','wb+')
bucket.download_to_stream(file_id, destination)
# end download files id

# start rename files
fs.rename(file_id, "new_file_name")
# end rename files

# start delete files
bucket.delete(file_id)
# end delete files